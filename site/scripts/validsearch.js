// Function to stream the explanation results from the backend using Server-Sent Events (SSE)
async function streamExplainResults(query) {
    const explainUrl = 'http://localhost:3333/explain-results';

    try {
        const response = await fetch(explainUrl, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ userQuery: query })
        });

        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }

        // Create a reader to handle the stream
        const reader = response.body.getReader();
        const decoder = new TextDecoder("utf-8");
        let result = '';

        // Read the stream chunk by chunk
        while (true) {
            const { done, value } = await reader.read();
            if (done) break;

            // Decode the chunk and process "data: " lines
            const chunk = decoder.decode(value, { stream: true });
            const lines = chunk.split('\n').filter(line => line.startsWith('data: '));
            lines.forEach(line => {
                const content = line.replace(/^data: /, '').trim();  // Remove 'data: ' prefix and trim
                if (content !== '[DONE]') {
                    result += content + ' ';  // Append each chunk to the result
                }
            });

            // Update the UI incrementally
            document.getElementById('explain').innerText = result.trim();  // Display the result
        }

    } catch (error) {
        console.error("Error with SSE:", error);
    }
}


// Fetch the local Algolia search index
const SEARCH_INDEX_URL = 'search.json';

// Function to load search.json file and return it as a JavaScript object
async function loadSearchIndex() {
    const response = await fetch(SEARCH_INDEX_URL);
    const searchData = await response.json();
    return searchData;
}

// Function to test pinging the documentation backend
async function testPing() {
    const pingUrl = 'http://localhost:3333/ping';

    try {
        const response = await fetch(pingUrl);
        const data = await response.json();

        // Log the response to the console
        console.log("Ping response from backend:", data);
    } catch (error) {
        console.error("Error pinging backend:", error);
    }
}

// Function to initialize Lunr.js and index your documents for searching
async function setupLunr() {
    const searchData = await loadSearchIndex();

    // Create Lunr.js index
    const idx = lunr(function () {
        this.ref('href');
        this.field('title');
        this.field('text');
        this.field('section');
        this.field('crumbs');  // Make sure crumbs is also indexed

        searchData.forEach(function (doc) {
            const modifiedDoc = {
                ...doc,
                crumbs: Array.isArray(doc.crumbs) ? doc.crumbs.join(' ') : doc.crumbs
            };
            this.add(modifiedDoc);  // Add the modified document
        }, this);
    });

    return { idx, searchData };
}

// Set up Lunr.js and add search functionality
setupLunr().then(({ idx, searchData }) => {
    document.getElementById('searchbox').addEventListener('input', function (event) {
        const query = event.target.value.trim();
        const hitsContainer = document.getElementById('hits');
        hitsContainer.innerHTML = '';  // Clear previous results

        if (query === '') {
            hitsContainer.style.display = 'none';
            return;
        }

        // Perform a search with Lunr.js
        let lunrResults = idx.search(query);

        // Limit the results to 20
        lunrResults = lunrResults.slice(0, 20);

        // If there are results, display them with an "Explain this" button
        if (lunrResults.length > 0) {
            hitsContainer.style.display = 'block';

            lunrResults.forEach((result) => {
                const doc = searchData.find(d => d.href === result.ref);

                if (doc) {
                    const resultElement = document.createElement('div');

                    const crumbs = Array.isArray(doc.crumbs) ? doc.crumbs.join(' > ') : doc.crumbs;

                    resultElement.innerHTML = `
                        <div>
                            <a href="${doc.href}">
                                <strong>${doc.title}</strong><br>
                                <em>${doc.section}</em><br>
                                <small>${crumbs}</small><br>
                                ${doc.text.substring(0, 100)}...
                            </a>
                            <button class="explain-button" data-query="${doc.title}">Explain this</button>
                        </div>
                    `;

                    hitsContainer.appendChild(resultElement);
                }
            });

            // Add click event listener to all "Explain this" buttons
            document.querySelectorAll('.explain-button').forEach(button => {
                button.addEventListener('click', async (e) => {
                    const query = e.target.getAttribute('data-query');  // Get the query from the button's data attribute
                    streamExplainResults(query);  // Stream the explanation
                });
            });
        } else {
            hitsContainer.style.display = 'none';
        }
    });
});

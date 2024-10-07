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

// Function to test the /test-openai endpoint
async function testOpenAI() {
    const openaiUrl = 'http://localhost:3333/test-openai';  // Replace with your backend's actual URL

    try {
        const response = await fetch(openaiUrl);
        const data = await response.json();

        // Log the response to the console
        console.log("OpenAI test response from backend:", data);
    } catch (error) {
        console.error("Error fetching OpenAI test result:", error);
    }
}

// Function to initialize Lunr.js and index your documents for searching
async function setupLunr() {
    const searchData = await loadSearchIndex();

    // Create Lunr.js index
    const idx = lunr(function () {
        // Define the fields to index
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

// Function to call the explain-results endpoint from our backend server
async function fetchExplainResults(query) {
    const explainUrl = 'http://localhost:3333/explain-results';

    try {
        const response = await fetch(explainUrl, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ userQuery: query })  // Send the query to the backend
        });

        if (response.ok) {
            const data = await response.json();
            return {
                success: true,
                result: data.explanation,  // This contains the explanation from the backend
                message: "Successfully connected to the backend and retrieved the explanation."
            };
        } else {
            return {
                success: false,
                result: "Sorry, I couldn't generate a result at this time.",
                message: `Failed to connect to the backend. Status code: ${response.status}`
            };
        }
    } catch (error) {
        console.error("Error fetching explanation from backend:", error);
        return {
            success: false,
            result: "An error occurred while trying to generate a result.",
            message: "Failed to connect to the backend due to a network or server error."
        };
    }
}

// Clear the search input when the page loads
window.onload = function() {
    document.getElementById('searchbox').value = '';  // Clear the search box input

    // Call the testPing function
    // testPing();

    // Call the testOpenAI function
    // testOpenAI();
};

// Set up Lunr.js and add search functionality
setupLunr().then(({ idx, searchData }) => {
    document.getElementById('searchbox').addEventListener('input', function (event) {
        const query = event.target.value.trim();
        const hitsContainer = document.getElementById('hits');
        hitsContainer.innerHTML = '';  // Clear previous results

        // Check if the input is empty
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
                    const explainContainer = document.getElementById('explain');  // Container for explanation results
                    explainContainer.innerHTML = '';  // Clear previous explanation

                    const query = e.target.getAttribute('data-query');  // Get the query from the button's data attribute
                    const explanationResult = await fetchExplainResults(query);  // Fetch the explanation

                    const explainElement = document.createElement('div');
                    explainElement.innerHTML = `
                        <div style="margin-top: 10px; background-color: #f9f9f9; padding: 10px; border-radius: 4px; color: #333;">
                            <strong style="color: #000;">AI Generated Suggestion:</strong><br>
                            <p style="color: #000;">${explanationResult.result}</p>
                            <small style="color: #666;">${explanationResult.message}</small> <!-- Display connection info -->
                        </div>
                    `;

                    explainContainer.style.display = 'block';  // Show the 'explain' div
                    explainContainer.appendChild(explainElement);
                });
            });
        } else {
            hitsContainer.style.display = 'none';
        }
    });
});
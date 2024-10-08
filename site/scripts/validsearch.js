// Fetch the local Algolia search index
const SEARCH_INDEX_URL = 'search.json';

// Function to load search.json file and return it as a JavaScript object
async function loadSearchIndex() {
    const response = await fetch(SEARCH_INDEX_URL);
    const searchData = await response.json();
    return searchData;
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
        this.field('crumbs');

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

// Function to fetch the explanation from the backend
async function fetchExplainResults(query) {
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

        const reader = response.body.getReader();
        const decoder = new TextDecoder("utf-8");
        let result = '';

        while (true) {
            const { done, value } = await reader.read();
            if (done) break;

            const chunk = decoder.decode(value, { stream: true });
            const lines = chunk.split('\n').filter(line => line.startsWith('data: '));

            lines.forEach(line => {
                let content = line.replace(/^data: /, '').trim();

                // Fix spaces before punctuation
                content = content.replace(/\s+([.,'()])/g, '$1');

                if (content !== '[DONE]') {
                    result += content + ' ';
                }
            });

            document.getElementById('explain').innerText = result.trim();
        }

    } catch (error) {
        console.error("Error with fetching explanation:", error);
    }
}


// Clear the search input when the page loads
window.onload = function() {
    document.getElementById('searchbox').value = '';  // Clear the search box input
};

// Function to handle the search and display results
setupLunr().then(({ idx, searchData }) => {
    document.getElementById('searchbox').addEventListener('input', async function (event) {
        const query = event.target.value.trim();
        const hitsContainer = document.getElementById('hits');
        const explainContainer = document.getElementById('explain');

        hitsContainer.innerHTML = '';
        explainContainer.innerHTML = '';

        if (query === '') {
            hitsContainer.style.display = 'none';
            explainContainer.style.display = 'none';
            return;
        }

        // Perform a search with Lunr.js
        let lunrResults = idx.search(query);
        lunrResults = lunrResults.slice(0, 20);

        if (lunrResults.length > 0) {
            hitsContainer.style.display = 'block';

            lunrResults.forEach((result) => {
                const doc = searchData.find(d => d.href === result.ref);

                if (doc) {
                    const resultElement = document.createElement('div');
                    const crumbs = Array.isArray(doc.crumbs) ? doc.crumbs.join(' > ') : doc.crumbs;

                    resultElement.innerHTML = `
                        <a href="${doc.href}">
                            <strong>${doc.title}</strong><br>
                            <em>${doc.section}</em><br>
                            <small>${crumbs}</small><br>
                            ${doc.text.substring(0, 100)}...
                        </a>
                    `;
                    hitsContainer.appendChild(resultElement);
                }
            });
        } else {
            hitsContainer.style.display = 'none';
        }
    });
});

// Add the Explain button just below the search box
const explainButton = document.createElement('button');
explainButton.innerText = 'Explain';
explainButton.style.marginTop = '10px';  // Add some margin
document.getElementById('searchbox').insertAdjacentElement('afterend', explainButton);

// Add event listener to the Explain button
explainButton.addEventListener('click', async () => {
    const query = document.getElementById('searchbox').value.trim();
    if (query) {
        await fetchExplainResults(query);
    }
});

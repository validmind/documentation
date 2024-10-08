// Copyright © 2024 ValidMind Inc. All rights reserved.
// See the LICENSE file in the root of this repository for details.
// SPDX-License-Identifier: AGPL-3.0 AND ValidMind Commercial

// Fetch the local Algolia search index
const SEARCH_INDEX_URL = 'search.json';

// Set to 'true' to disable cleaning up the streaming text — should be disabled by default
let disableCleanText = true;  

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

// Clean out the text to make sure that words are actually, you know, words
function cleanText(text) {
    // Remove spaces before punctuation, fix hyphenation, and clean up parentheses
    return text
        .replace(/\s+([,.;!?()])/g, '$1')  // Remove space before punctuation
        .replace(/\(\s+/g, '(')  // Remove space after opening parenthesis
        .replace(/\s+\)/g, ')')  // Remove space before closing parenthesis
        .replace(/\s+-\s+/g, '-')  // Remove spaces around hyphens
        .replace(/\s+/g, ' ')  // Replace multiple spaces with a single space
        .trim();  // Trim any extra spaces
}

// Prompt the user to hit Enter for more info
function showToast() {
    // console.log('Toast shown');
    const toast = document.getElementById('toast');
    const searchbox = document.getElementById('searchbox');
    
    // Listen to input events on the searchbox
    searchbox.addEventListener('input', function () {
        if (searchbox.value.trim() !== '') {
            toast.classList.add('show');  // Show the toast when there is input
        } else {
            toast.classList.remove('show');  // Hide the toast if input is cleared
        }
    });
}

// Function to fetch and render streaming explanation
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
        let result = '';  // Initialize an empty string to store the final result
        let buffer = '';  // Buffer to handle incomplete words

        while (true) {
            const { done, value } = await reader.read();
            if (done) break;

            const chunk = decoder.decode(value, { stream: true });
            const lines = chunk.split('\n').filter(line => line.startsWith('data: '));

            lines.forEach(line => {
                const content = line.replace(/^data: /, '').trim();
                if (content !== '[DONE]') {
                    buffer += content;

                    // Clean up the buffer text if cleanText is enabled
                    if (!disableCleanText) {
                        result += cleanText(buffer) + ' ';
                    } else {
                        result += buffer + ' ';  // Skip cleanText if disabled
                    }

                    // Update the explain div with the new content
                    document.getElementById('explain').innerText = result.trim();

                    // Clear the buffer after processing
                    buffer = '';
                }
            });
        }

    } catch (error) {
        console.error("Error fetching explanation:", error);
    }
}

// Clear the search input when the page loads
window.onload = function() {
    document.getElementById('searchbox').value = ''; 
    showToast();
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

    // Add event listener for hitting Enter to start explanation
    document.getElementById('searchbox').addEventListener('keydown', async function (event) {
        if (event.key === 'Enter') {
            const query = document.getElementById('searchbox').value.trim();
            if (query) {
                await fetchExplainResults(query);  // Trigger the explanation on Enter
            }
        }
    });
});

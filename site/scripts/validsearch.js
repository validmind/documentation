// Copyright © 2024 ValidMind Inc. All rights reserved.
// See the LICENSE file in the root of this repository for details.
// SPDX-License-Identifier: AGPL-3.0 AND ValidMind Commercial

// Fetch the local Algolia search index
const SEARCH_INDEX_URL = 'search.json';

// Set to 'true' to disable cleaning up the streaming text (editing is done on the backend)
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
    const searchIndex = lunr(function () {
        this.ref('href');
        this.field('title', { boost: 10 });
        this.field('text', { boost: 5 });
        this.field('section', { boost: 0.5 });
        this.field('crumbs', { boost: 0.2 });

        searchData.forEach(function (doc) {
            const modifiedDoc = {
                ...doc,
                crumbs: Array.isArray(doc.crumbs) ? doc.crumbs.join(' ') : doc.crumbs
            };
            this.add(modifiedDoc);  // Add the modified document
        }, this);
    });

    return { searchIndex, searchData };
}

// Strip out text that can cause poor search ranking
function sanitizeInput(input) {
    let sanitized = input.toLowerCase(); // Convert to lowercase for consistent matching
    sanitized = sanitized.replace(/^how do i\s+/, ''); // Remove common phrases like "how do I"

    sanitized = sanitized.replace(/[?.!]/g, '');  // Remove punctuation marks like ? or !
    sanitized = sanitized.trim(); // Trim any leading or trailing spaces

    return sanitized;
}

// Clean up response text for minor tweaks, disabled by default (and major changes should be done on the backend)
function cleanText(text) {
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
    const toast = document.getElementById('toast');
    const searchbox = document.getElementById('searchbox');
    
    // Listen to input events on the searchbox
    searchbox.addEventListener('input', function () {
        if (searchbox.value.trim() !== '') {
            toast.classList.add('show');
        } else {
            toast.classList.remove('show');
        }
    });
}

// Function to fetch and render streaming explanation
async function fetchExplainResults(query) {
    const explainUrl = 'http://localhost:3333/explain-results';
    const explainContainer = document.getElementById('explain');
    
    let buffer = '';  // Buffer to accumulate incoming HTML chunks

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

        while (true) {
            const { done, value } = await reader.read();
            if (done) break;

            let chunk = decoder.decode(value, { stream: true });
            
            // Remove "data: " and "data: [DONE]"
            chunk = chunk.replace(/data: /g, '').replace(/\[DONE\]/g, '');

            // Add the cleaned chunk to the buffer
            buffer += chunk;

            // Append the cleaned HTML directly to the explainContainer
            explainContainer.innerHTML += buffer;

            // Clear the buffer after appending
            buffer = '';
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
setupLunr().then(({ searchIndex, searchData }) => {
    document.getElementById('searchbox').addEventListener('input', async function (event) {
        let query = event.target.value.trim();
        
        // Sanitize the query
        query = sanitizeInput(query);  // Call the sanitizeInput function here

        const hitsContainer = document.getElementById('hits');
        const explainContainer = document.getElementById('explain');

        hitsContainer.innerHTML = '';

        // Clear the explain div when the input is empty
        if (query === '') {
            hitsContainer.style.display = 'none';
            explainContainer.innerHTML = '';
            explainContainer.style.display = 'none';
            return;
        }

        // Perform an exact match search first
        let lunrResults = searchIndex.search(`"${query}"`);

        // If no exact matches found, fall back to a regular search
        if (lunrResults.length === 0) {
            lunrResults = searchIndex.search(query);
        }

        // Ensure that you limit the results to the top 20 in both cases
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
            let query = document.getElementById('searchbox').value.trim();

            // Sanitize the query before fetching the explanation
            query = sanitizeInput(query);

            const explainContainer = document.getElementById('explain');

            if (query) {
                explainContainer.style.display = 'block';
                await fetchExplainResults(query);
            }
        }
    });
});

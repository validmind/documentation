// Copyright © 2024 ValidMind Inc. All rights reserved.
// See the LICENSE file in the root of this repository for details.
// SPDX-License-Identifier: AGPL-3.0 AND ValidMind Commercial

// Fetch the generated Algolia search index
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
        // Define the fields to index
        this.ref('href');
        this.field('title');
        this.field('text');
        this.field('section');
        this.field('crumbs');  // Make sure crumbs is also indexed

        // Index crumbs as a space-separated string
        searchData.forEach(function (doc) {
            const modifiedDoc = {
                ...doc,
                crumbs: Array.isArray(doc.crumbs) ? doc.crumbs.join(' ') : doc.crumbs  // Convert crumbs array to string
            };
            this.add(modifiedDoc);  // Add the modified document with stringified crumbs
        }, this);
    });

    return { idx, searchData };
}

// Clear the search input when the page loads
window.onload = function() {
    document.getElementById('searchbox').value = '';  // Clear the search box input
};

setupLunr().then(({ idx, searchData }) => {
    document.getElementById('searchbox').addEventListener('input', function (event) {
        const query = event.target.value.trim();
        const hitsContainer = document.getElementById('hits');
        hitsContainer.innerHTML = '';  // Clear previous results

        // Hide the hits container if the search box is empty
        if (query === '') {
            hitsContainer.style.display = 'none';
            return;
        }

        const exactResults = idx.search(`"${query}"`);
        let results = exactResults.length > 0 ? exactResults : idx.search(query);

        // Show the hits container if there are results, otherwise hide it
        if (results.length > 0) {
            hitsContainer.style.display = 'block';  // Show the container
            results.forEach((result) => {
                const doc = searchData.find(d => d.href === result.ref);
                if (doc) {
                    const resultElement = document.createElement('div');
                    const crumbs = Array.isArray(doc.crumbs) ? doc.crumbs.join(' > ') : doc.crumbs;

                    resultElement.innerHTML = `
                        <a href="${doc.href}">
                            <strong>${doc.title}</strong><br>
                            <em>${doc.section}</em><br>
                            <small>${doc.text.substring(0, 100)}...</small><br>
                            <div class="crumbs" style="margin-top: 10px; font-size: small; color: grey;">
                                ${crumbs}
                            </div>
                        </a>
                    `;
                    hitsContainer.appendChild(resultElement);
                }
            });
        } else {
            hitsContainer.style.display = 'none';  // Hide the container if no results
        }
    });
});
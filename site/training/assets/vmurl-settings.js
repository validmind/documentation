// Copyright © 2023-2026 ValidMind Inc. All rights reserved.
// Custom ValidMind URL settings for training slides
// Allows users to specify a custom ValidMind URL via localStorage

(function() {
  'use strict';

  const STORAGE_KEY = 'validmind-url';
  const DEFAULT_URL = 'https://app.prod.validmind.ai';
  const URL_PATTERN = /https:\/\/app\.prod\.validmind\.ai/g;

  // Get custom URL from localStorage
  function getCustomUrl() {
    return localStorage.getItem(STORAGE_KEY) || null;
  }

  // Save custom URL to localStorage
  function setCustomUrl(url) {
    if (url && url.trim()) {
      localStorage.setItem(STORAGE_KEY, url.trim());
    } else {
      localStorage.removeItem(STORAGE_KEY);
    }
  }

  // Validate URL format
  function isValidUrl(string) {
    try {
      const url = new URL(string);
      return url.protocol === 'https:' || url.protocol === 'http:';
    } catch {
      return false;
    }
  }

  // Rewrite all ValidMind URLs in the document
  // Must run before Reveal.js initializes
  function rewriteUrls() {
    const customUrl = getCustomUrl();
    if (!customUrl) return;

    // Rewrite data-background-iframe attributes on section elements
    document.querySelectorAll('section[data-background-iframe]').forEach(function(section) {
      const iframe = section.getAttribute('data-background-iframe');
      if (iframe && URL_PATTERN.test(iframe)) {
        section.setAttribute('data-background-iframe', iframe.replace(URL_PATTERN, customUrl));
      }
    });

    // Rewrite href attributes on links
    document.querySelectorAll('a[href*="app.prod.validmind.ai"]').forEach(function(link) {
      const href = link.getAttribute('href');
      if (href) {
        link.setAttribute('href', href.replace(URL_PATTERN, customUrl));
      }
    });
  }

  // Create and show the settings modal
  function showSettingsModal() {
    // Remove existing modal if present
    const existing = document.getElementById('vmurl-settings-modal');
    if (existing) existing.remove();

    const customUrl = getCustomUrl();
    const currentUrl = customUrl || DEFAULT_URL;

    const modal = document.createElement('div');
    modal.id = 'vmurl-settings-modal';
    modal.className = 'vmurl-modal-overlay';
    modal.innerHTML = `
      <div class="vmurl-modal">
        <div class="vmurl-modal-header">
          <h3>ValidMind URL settings</h3>
          <button class="vmurl-close-btn" aria-label="Close">&times;</button>
        </div>
        <div class="vmurl-modal-body">
          <p class="vmurl-current">Current: <code>${currentUrl}</code>${customUrl ? ' (custom)' : ' (default)'}</p>
          <label for="vmurl-input">Custom ValidMind URL:</label>
          <input type="url" id="vmurl-input" class="vmurl-input" 
                 placeholder="https://app.staging.validmind.ai" 
                 value="${customUrl || ''}">
          <p class="vmurl-hint">Enter the base URL for the ValidMind platform. Leave empty to use the default.</p>
        </div>
        <div class="vmurl-modal-footer">
          <button class="vmurl-btn vmurl-btn-secondary" id="vmurl-reset">Reset to default</button>
          <button class="vmurl-btn vmurl-btn-primary" id="vmurl-save">Save &amp; reload</button>
        </div>
      </div>
    `;

    document.body.appendChild(modal);

    // Event handlers
    const closeBtn = modal.querySelector('.vmurl-close-btn');
    const saveBtn = modal.querySelector('#vmurl-save');
    const resetBtn = modal.querySelector('#vmurl-reset');
    const input = modal.querySelector('#vmurl-input');

    function closeModal() {
      modal.remove();
    }

    closeBtn.addEventListener('click', closeModal);
    modal.addEventListener('click', function(e) {
      if (e.target === modal) closeModal();
    });

    saveBtn.addEventListener('click', function() {
      const newUrl = input.value.trim();
      if (newUrl && !isValidUrl(newUrl)) {
        alert('Please enter a valid URL (e.g., https://app.staging.validmind.ai)');
        return;
      }
      setCustomUrl(newUrl);
      window.location.reload();
    });

    resetBtn.addEventListener('click', function() {
      setCustomUrl(null);
      window.location.reload();
    });

    // Focus input
    input.focus();

    // Close on Escape
    document.addEventListener('keydown', function handler(e) {
      if (e.key === 'Escape') {
        closeModal();
        document.removeEventListener('keydown', handler);
      }
    });
  }

  // Inject gear icon next to login links
  function injectSettingsButton() {
    document.querySelectorAll('a[href*="app.prod.validmind.ai"], a[href*="' + (getCustomUrl() || '') + '"]').forEach(function(link) {
      // Skip if already has a settings button
      if (link.parentElement.querySelector('.vmurl-settings-btn')) return;
      
      // Only add to links that look like login buttons
      if (!link.classList.contains('button')) return;

      const btn = document.createElement('button');
      btn.className = 'vmurl-settings-btn';
      btn.setAttribute('aria-label', 'Configure ValidMind URL');
      btn.setAttribute('title', 'Configure ValidMind URL');
      btn.innerHTML = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" width="16" height="16"><path fill="currentColor" d="M495.9 166.6c3.2 8.7 .5 18.4-6.4 24.6l-43.3 39.4c1.1 8.3 1.7 16.8 1.7 25.4s-.6 17.1-1.7 25.4l43.3 39.4c6.9 6.2 9.6 15.9 6.4 24.6c-4.4 11.9-9.7 23.3-15.8 34.3l-4.7 8.1c-6.6 11-14 21.4-22.1 31.2c-5.9 7.2-15.7 9.6-24.5 6.8l-55.7-17.7c-13.4 10.3-28.2 18.9-44 25.4l-12.5 57.1c-2 9.1-9 16.3-18.2 17.8c-13.8 2.3-28 3.5-42.5 3.5s-28.7-1.2-42.5-3.5c-9.2-1.5-16.2-8.7-18.2-17.8l-12.5-57.1c-15.8-6.5-30.6-15.1-44-25.4L83.1 425.9c-8.8 2.8-18.6 .3-24.5-6.8c-8.1-9.8-15.5-20.2-22.1-31.2l-4.7-8.1c-6.1-11-11.4-22.4-15.8-34.3c-3.2-8.7-.5-18.4 6.4-24.6l43.3-39.4C64.6 273.1 64 264.6 64 256s.6-17.1 1.7-25.4L22.4 191.2c-6.9-6.2-9.6-15.9-6.4-24.6c4.4-11.9 9.7-23.3 15.8-34.3l4.7-8.1c6.6-11 14-21.4 22.1-31.2c5.9-7.2 15.7-9.6 24.5-6.8l55.7 17.7c13.4-10.3 28.2-18.9 44-25.4l12.5-57.1c2-9.1 9-16.3 18.2-17.8C227.3 1.2 241.5 0 256 0s28.7 1.2 42.5 3.5c9.2 1.5 16.2 8.7 18.2 17.8l12.5 57.1c15.8 6.5 30.6 15.1 44 25.4l55.7-17.7c8.8-2.8 18.6-.3 24.5 6.8c8.1 9.8 15.5 20.2 22.1 31.2l4.7 8.1c6.1 11 11.4 22.4 15.8 34.3zM256 336a80 80 0 1 0 0-160 80 80 0 1 0 0 160z"/></svg>';
      
      btn.addEventListener('click', function(e) {
        e.preventDefault();
        e.stopPropagation();
        showSettingsModal();
      });

      // Insert after the link
      link.parentElement.insertBefore(btn, link.nextSibling);
    });
  }

  // Run URL rewriting immediately (before Reveal.js initializes)
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', rewriteUrls);
  } else {
    rewriteUrls();
  }

  // Inject settings button after DOM is ready
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', injectSettingsButton);
  } else {
    injectSettingsButton();
  }

  // Also run after Reveal.js is ready (for dynamically loaded content)
  if (typeof Reveal !== 'undefined') {
    Reveal.on('ready', function() {
      rewriteUrls();
      injectSettingsButton();
    });
  } else {
    // Wait for Reveal to be defined
    document.addEventListener('DOMContentLoaded', function() {
      if (typeof Reveal !== 'undefined') {
        Reveal.on('ready', function() {
          rewriteUrls();
          injectSettingsButton();
        });
      }
    });
  }
})();

(function () {
  'use strict';

  var SCOPE = '.template-schema-docs';

  function getRoot() {
    return document.querySelector(SCOPE);
  }

  function showCollapse(el) {
    el.classList.add('show');
  }

  function hideCollapse(el) {
    el.classList.remove('show');
  }

  function toggleCollapse(el) {
    el.classList.toggle('show');
  }

  function resolveTargets(root, selector) {
    if (!selector) {
      return [];
    }

    selector = selector.trim();
    if (selector.charAt(0) === '#') {
      var byId = document.getElementById(selector.slice(1));
      return byId ? [byId] : [];
    }

    var scoped = selector;
    if (scoped.indexOf('.template-schema-docs') === 0) {
      scoped = scoped.slice('.template-schema-docs'.length).trim();
    }

    try {
      return Array.from(root.querySelectorAll(scoped));
    } catch (error) {
      return [];
    }
  }

  function handleCollapseButton(button, root) {
    var target = button.getAttribute('data-target');
    if (!target) {
      return;
    }

    if (target.indexOf(':not(.show)') !== -1) {
      root.querySelectorAll('.collapse:not(.show)').forEach(showCollapse);
      return;
    }

    if (target.indexOf('.collapse.show') !== -1) {
      root.querySelectorAll('.collapse.show').forEach(hideCollapse);
      return;
    }

    resolveTargets(root, target).forEach(toggleCollapse);
  }

  function flashElement(elementId) {
    var el = document.getElementById(elementId);
    if (!el) {
      return;
    }
    el.classList.add('jsfh-animated-property');
    window.setTimeout(function () {
      el.classList.remove('jsfh-animated-property');
    }, 1000);
  }

  function setAnchor(anchorLinkDestination) {
    history.pushState({}, '', anchorLinkDestination);
  }

  function expandAncestors(targetEl, root) {
    var el = targetEl;
    while (el && el !== root) {
      if (el.classList && el.classList.contains('collapse')) {
        showCollapse(el);
      }
      el = el.parentElement;
    }
  }

  function anchorLink(linkTarget) {
    var root = getRoot();
    if (!root) {
      return;
    }

    var id = String(linkTarget).replace(/^#/, '');
    var targetEl = document.getElementById(id);
    if (!targetEl || !root.contains(targetEl)) {
      return;
    }

    expandAncestors(targetEl, root);

    window.setTimeout(function () {
      targetEl.scrollIntoView({ block: 'center', behavior: 'smooth' });
      window.setTimeout(function () {
        flashElement(id);
      }, 500);
    }, 100);
  }

  function anchorOnLoad() {
    var hash = decodeURIComponent(window.location.hash.split('?')[0].split('&')[0]);
    if (!hash || hash === '#') {
      return;
    }

    var root = getRoot();
    var id = hash.replace(/^#/, '');
    var targetEl = document.getElementById(id);
    if (root && targetEl && root.contains(targetEl)) {
      anchorLink(id);
    }
  }

  function refreshLayout(root) {
    root.querySelectorAll('.collapse').forEach(function (el) {
      void el.offsetHeight;
    });
  }

  function observeCalloutExpand(root) {
    var calloutBody = root.closest('.callout');
    calloutBody = calloutBody ? calloutBody.querySelector('.callout-body') : null;
    if (!calloutBody) {
      return;
    }

    var observer = new MutationObserver(function () {
      if (calloutBody.classList.contains('show')) {
        refreshLayout(root);
      }
    });
    observer.observe(calloutBody, { attributes: true, attributeFilter: ['class'] });

    root.addEventListener('click', function () {
      refreshLayout(root);
    }, { once: true });
  }

  function bindEvents(root) {
    root.addEventListener('click', function (event) {
      var button = event.target.closest('[data-toggle="collapse"]');
      if (button && root.contains(button)) {
        event.preventDefault();
        handleCollapseButton(button, root);
        return;
      }

      var link = event.target.closest('a[href^="#"]');
      if (link && root.contains(link) && !link.getAttribute('onclick')) {
        event.preventDefault();
        var href = link.getAttribute('href');
        history.pushState({}, '', href);
        anchorLink(href.replace(/^#/, ''));
      }
    });
  }

  function init() {
    var root = getRoot();
    if (!root) {
      return;
    }

    window.setAnchor = setAnchor;
    window.anchorLink = anchorLink;
    window.anchorOnLoad = anchorOnLoad;

    bindEvents(root);
    observeCalloutExpand(root);
    anchorOnLoad();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();

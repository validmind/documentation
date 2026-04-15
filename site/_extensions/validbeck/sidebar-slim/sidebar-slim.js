(function () {
  "use strict";

  var STORAGE_KEY = "validbeck:quarto:sidebar-slim-collapsed";
  var MQ = "(min-width: 992px)";

  function readCollapsed() {
    try {
      return window.sessionStorage.getItem(STORAGE_KEY) === "1";
    } catch (_e) {
      return false;
    }
  }

  function writeCollapsed(collapsed) {
    try {
      if (collapsed) {
        window.sessionStorage.setItem(STORAGE_KEY, "1");
      } else {
        window.sessionStorage.removeItem(STORAGE_KEY);
      }
    } catch (_e) {
      /* ignore */
    }
  }

  function applyCollapsed(body, collapsed) {
    if (collapsed) {
      body.classList.add("quarto-sidebar-slim-collapsed");
    } else {
      body.classList.remove("quarto-sidebar-slim-collapsed");
    }
  }

  function setIcon(btn, collapsed) {
    var span = btn.querySelector(".quarto-sidebar-slim-icon");
    if (!span) return;
    span.textContent = collapsed ? "\u00bb" : "\u00ab";
    btn.setAttribute(
      "aria-label",
      collapsed ? "Expand site sidebar" : "Collapse site sidebar"
    );
    btn.setAttribute("title", collapsed ? "Expand sidebar" : "Collapse sidebar");
  }

  function init() {
    var mq = window.matchMedia(MQ);
    var sidebar = document.getElementById("quarto-sidebar");
    if (!sidebar || !sidebar.classList.contains("sidebar")) {
      return;
    }

    function teardown() {
      document.body.classList.remove(
        "quarto-sidebar-slim-enabled",
        "quarto-sidebar-slim-collapsed"
      );
      var existing = sidebar.querySelector(".quarto-sidebar-slim-toolbar");
      if (existing) {
        existing.remove();
      }
    }

    function setupDesktop() {
      teardown();
      document.body.classList.add("quarto-sidebar-slim-enabled");
      var collapsed = readCollapsed();
      applyCollapsed(document.body, collapsed);

      var toolbar = document.createElement("div");
      toolbar.className =
        "sidebar-header quarto-sidebar-slim-toolbar";
      toolbar.setAttribute("role", "group");

      var btn = document.createElement("button");
      btn.type = "button";
      btn.className = "quarto-sidebar-slim-toggle";
      btn.setAttribute("type", "button");

      var icon = document.createElement("span");
      icon.className = "quarto-sidebar-slim-icon";
      icon.setAttribute("aria-hidden", "true");
      btn.appendChild(icon);

      setIcon(btn, collapsed);

      btn.addEventListener("click", function () {
        var next = !document.body.classList.contains(
          "quarto-sidebar-slim-collapsed"
        );
        applyCollapsed(document.body, next);
        setIcon(btn, next);
        writeCollapsed(next);
      });

      toolbar.appendChild(btn);
      sidebar.insertBefore(toolbar, sidebar.firstChild);
    }

    function onMqChange() {
      if (mq.matches) {
        setupDesktop();
      } else {
        teardown();
      }
    }

    if (mq.addEventListener) {
      mq.addEventListener("change", onMqChange);
    } else {
      mq.addListener(onMqChange);
    }

    onMqChange();
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();

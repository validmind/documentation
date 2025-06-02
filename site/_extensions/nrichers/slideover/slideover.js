window.slideover = {};

var Plugin = {
    id: 'slideover',
    init: function(reveal) {
        var holders = { presentation: undefined, slideover: undefined };

        function loadStylesheet() {
            var path = undefined;
            [].slice.call(document.getElementsByTagName('script')).forEach(function(script) {
                if (script.src.indexOf('slideover.js') > -1) {
                    path = script.src.split('/').slice(0, -1).join('/') + '/';
                }
            });
            var link = document.createElement('link');
            link.rel = 'stylesheet';
            link.href = path + 'slideover.css';
            document.head.appendChild(link);
        }

        function setup() {
            loadStylesheet();
            holders.presentation = document.querySelector('.reveal');
            if (!holders.presentation) return false;
            holders.presentation.classList.add('slideover__presentation');

            var slideover = document.createElement('div');
            slideover.classList.add('slideover__container');
            holders.presentation.parentNode.insertBefore(slideover, holders.presentation.nextElementSibling);
            holders.slideover = slideover;
            return true;
        }

        function processMarkdownContent(content) {
            const tempDiv = document.createElement('div');
            tempDiv.innerHTML = content;
            return tempDiv.innerHTML;
        }

        function handleOverlays() {
            if (!holders.slideover) return;
            holders.slideover.innerHTML = '';
            const currentSlide = reveal.getCurrentSlide();
            if (!currentSlide) return;
            const overlays = currentSlide.querySelectorAll('.slideover--r, .slideover--b, .slideover--l, .slideover--t');

            overlays.forEach((overlay) => {
                const originalContent = overlay.innerHTML;
                const content = document.createElement('div');
                content.classList.add('slideover__content');
                ['slideover--b', 'slideover--r', 'slideover--l', 'slideover--t'].forEach(dir => {
                    if (overlay.classList.contains(dir)) content.classList.add(dir);
                });

                // Add any additional modifier classes
                overlay.classList.forEach(cls => {
                    if (!['slideover--r', 'slideover--b', 'slideover--l', 'slideover--t'].includes(cls)) {
                        content.classList.add(cls);
                    }
                });

                const header = document.createElement('div');
                header.classList.add('slideover__header');
                const toggle = document.createElement('div');
                toggle.classList.add('slideover__toggle');
                toggle.innerHTML = (overlay.classList.contains('slideover--r') || overlay.classList.contains('slideover--l')) 
                    ? '<svg viewBox="0 0 24 24"><path fill="currentColor" d="M4.84 7.41L9.42 12l-4.58 4.59L6.25 18l6-6-6-6z M15.84 7.41L20.42 12l-4.58 4.59L17.25 18l6-6-6-6z"/></svg>'
                    : '<svg viewBox="0 0 24 24"><path fill="currentColor" d="M7.41 4.84L12 9.42l4.59-4.58L18 6.25l-6 6-6-6z M7.41 15.84L12 20.42l4.59-4.58L18 17.25l-6 6-6-6z"/></svg>';
                content.appendChild(toggle);
                content.appendChild(header);
                const contentArea = document.createElement('div');
                contentArea.classList.add('slideover__content-area');
                contentArea.innerHTML = processMarkdownContent(originalContent);
                content.appendChild(contentArea);
                holders.slideover.appendChild(content);

                // Start open, with toggle matching open state
                content.classList.add('slideover__content--active');
                toggle.classList.add('slideover__toggle--active');
                content.dataset.slideoverState = 'open';

                // Toggle click
                toggle.addEventListener('click', (e) => {
                    e.stopPropagation();
                    const isActive = content.classList.toggle('slideover__content--active');
                    toggle.classList.toggle('slideover__toggle--active', isActive);
                    content.dataset.slideoverState = isActive ? 'open' : 'closed';
                });

                // Auto-collapse
                if (overlay.classList.contains('auto-collapse') || [...overlay.classList].some(cls => cls.startsWith('auto-collapse-'))) {
                    let autoCollapseTimer;
                    let userExpanded = false;
                    const delay = [...overlay.classList].find(cls => cls.startsWith('auto-collapse-')) ? 
                        parseInt([...overlay.classList].find(cls => cls.startsWith('auto-collapse-')).replace('auto-collapse-', '')) * 1000 : 5000;
                    function resetAutoCollapseTimer(element) {
                        clearTimeout(autoCollapseTimer);
                        autoCollapseTimer = setTimeout(() => {
                            if (element.classList.contains('slideover__content--active') && !userExpanded) {
                                element.classList.remove('slideover__content--active');
                                const toggle = element.querySelector('.slideover__toggle');
                                if (toggle) {
                                    toggle.classList.remove('slideover__toggle--active');
                                    element.dataset.slideoverState = 'closed';
                                }
                            }
                        }, delay);
                    }
                    resetAutoCollapseTimer(content);
                    content.addEventListener('mouseenter', () => resetAutoCollapseTimer(content));
                    content.addEventListener('click', () => resetAutoCollapseTimer(content));
                    content.addEventListener('keydown', () => resetAutoCollapseTimer(content));
                    toggle.addEventListener('click', () => { if (content.classList.contains('slideover__content--active')) userExpanded = true; });
                }

                overlay.style.display = 'none';
            });
        }

        reveal.addEventListener('ready', () => setup() && handleOverlays());
        reveal.addEventListener('slidechanged', handleOverlays);
        reveal.addEventListener('fragmentshown', handleOverlays);
        reveal.addEventListener('fragmenthidden', handleOverlays);
        window.slideover = { setup, handleOverlays };
    }
};

if (typeof window.Reveal === 'undefined') throw new Error('Reveal.js slideover plugin requires Reveal.js');
Reveal.registerPlugin('slideover', Plugin);
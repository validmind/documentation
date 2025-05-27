// Create global namespace for the plugin
window.slideover = {};

var Plugin = {
    id: 'slideover',
    init: function(reveal) {
        console.log('Slideover plugin loading...');
        
        var holders = {
            presentation: undefined,
            slideover: undefined
        };

        function loadStylesheet() {
            var path = undefined;
            [].slice.call(document.getElementsByTagName('script')).forEach(function(script){
                if(script.src.indexOf('slideover.js') > - 1) {
                    path = script.src.split('/').slice(0, -1).join('/')+'/';
                }
            });

            var link = window.document.createElement('link');
            link.rel = 'stylesheet';
            link.href = path + 'slideover.css';
            window.document.getElementsByTagName('head')[0].appendChild(link);
            console.log('Stylesheet loaded:', link.href);
        }

        function setup() {
            loadStylesheet();
            holders.presentation = document.querySelector('.reveal');
            if (!holders.presentation) {
                console.error('Could not find .reveal element');
                return false;
            }
            holders.presentation.classList.add('slideover__presentation');

            var slideover = document.createElement('div');
            slideover.classList.add('slideover__container');
            holders.presentation.parentNode.insertBefore(slideover, holders.presentation.nextElementSibling);
            holders.slideover = slideover;
            console.log('Setup complete, slideover container created');
            return true;
        }

        function processMarkdownContent(content) {
            const tempDiv = document.createElement('div');
            tempDiv.innerHTML = content;
            return tempDiv.innerHTML;
        }

        function handleOverlays() {
            if (!holders.slideover) {
                console.error('Slideover container not initialized');
                return;
            }

            // Clear existing overlays
            holders.slideover.innerHTML = '';

            // Only process overlays in the current slide
            const currentSlide = reveal.getCurrentSlide();
            if (!currentSlide) return;

            const overlays = currentSlide.querySelectorAll('.slideover--r, .slideover--b, .slideover--l, .slideover--t');
            console.log('Found overlays in current slide:', overlays.length);
            
            overlays.forEach((overlay, index) => {
                console.log(`Processing overlay ${index}:`, overlay);
                
                // Store original content before we modify anything
                const originalContent = overlay.innerHTML;
                console.log('[Slideover] originalContent:', originalContent);
                
                // Create slideover content
                const content = document.createElement('div');
                content.classList.add('slideover__content');
                if (overlay.classList.contains('slideover--b')) {
                    content.classList.add('slideover--b');
                }
                if (overlay.classList.contains('slideover--r')) {
                    content.classList.add('slideover--r');
                }
                if (overlay.classList.contains('slideover--l')) {
                    content.classList.add('slideover--l');
                }
                if (overlay.classList.contains('slideover--t')) {
                    content.classList.add('slideover--t');
                }

                // Add any additional modifier classes
                overlay.classList.forEach(cls => {
                    if (!['slideover--r', 'slideover--b', 'slideover--l', 'slideover--t'].includes(cls)) {
                        content.classList.add(cls);
                    }
                });
                
                // Create header
                const header = document.createElement('div');
                header.classList.add('slideover__header');
                
                // Create toggle 
                const toggle = document.createElement('div');
                toggle.classList.add('slideover__toggle');
                if (overlay.classList.contains('slideover--r') || overlay.classList.contains('slideover--l')) {
                    // Left/right double chevron
                    toggle.innerHTML = '<svg viewBox="0 0 24 24" width="24" height="24"><path fill="currentColor" d="M4.84 7.41L9.42 12l-4.58 4.59L6.25 18l6-6-6-6z M15.84 7.41L20.42 12l-4.58 4.59L17.25 18l6-6-6-6z" stroke="currentColor"></path></svg>';
                } else {
                    // Up/down double chevron
                    toggle.innerHTML = '<svg viewBox="0 0 24 24" width="24" height="24"><path fill="currentColor" d="M7.41 4.84L12 9.42l4.59-4.58L18 6.25l-6 6-6-6z M7.41 15.84L12 20.42l4.59-4.58L18 17.25l-6 6-6-6z" stroke="currentColor"></path></svg>';
                }
                
                // Add toggle 
                content.appendChild(toggle);
                content.appendChild(header);
                
                // Create content area
                const contentArea = document.createElement('div');
                contentArea.classList.add('slideover__content-area');
                
                // Process the content to handle Markdown headings
                const processedContent = processMarkdownContent(originalContent);
                contentArea.innerHTML = processedContent;
                
                content.appendChild(contentArea);
                
                // Add to slideover container
                holders.slideover.appendChild(content);
                
                // Start with content expanded
                content.classList.add('slideover__content--active');
                
                // Add click handler to toggle
                toggle.addEventListener('click', (e) => {
                    e.stopPropagation(); // Prevent event from bubbling
                    content.classList.toggle('slideover__content--active');
                    toggle.classList.toggle('slideover__toggle--active');
                    // Reset auto-collapse timer when user interacts (only if defined)
                    if (typeof resetAutoCollapseTimer === 'function') {
                        resetAutoCollapseTimer(content);
                    }
                });
                
                // Add auto-collapse functionality if the overlay has the auto-collapse class
                if (overlay.classList.contains('auto-collapse') || Array.from(overlay.classList).some(cls => cls.startsWith('auto-collapse-'))) {
                    let autoCollapseTimer;
                    let userExpanded = false;
                    
                    // Get delay from auto-collapse-{s} class or use default 5s
                    const delayClass = Array.from(overlay.classList).find(cls => cls.startsWith('auto-collapse-'));
                    const delay = delayClass ? parseInt(delayClass.replace('auto-collapse-', '')) * 1000 : 5000;
                    
                    // Function to reset the timer
                    function resetAutoCollapseTimer(element) {
                        clearTimeout(autoCollapseTimer);
                        autoCollapseTimer = setTimeout(() => {
                            if (element.classList.contains('slideover__content--active') && !userExpanded) {
                                element.classList.remove('slideover__content--active');
                                element.querySelector('.slideover__toggle').classList.remove('slideover__toggle--active');
                            }
                        }, delay);
                    }
                    
                    // Start the timer
                    resetAutoCollapseTimer(content);
                    
                    // Add event listeners to reset the timer on user interaction
                    content.addEventListener('mouseenter', () => resetAutoCollapseTimer(content));
                    content.addEventListener('click', () => resetAutoCollapseTimer(content));
                    content.addEventListener('keydown', () => resetAutoCollapseTimer(content));
                    
                    // Track when you manually expand the slideover
                    toggle.addEventListener('click', (e) => {
                        if (content.classList.contains('slideover__content--active')) {
                            userExpanded = true;
                        }
                    });
                }
                
                // Instead of removing the original overlay, hide it
                overlay.style.display = 'none';
            });
        }

        reveal.addEventListener('ready', function(event) {
            console.log('Reveal ready event fired');
            if (setup()) {
                handleOverlays();
            }
        });

        // Also listen for slidechanged event to update overlays
        reveal.addEventListener('slidechanged', function(event) {
            console.log('Slide changed event fired');
            if (holders.slideover) {
                handleOverlays();
            }
        });

        // Handle backward navigation
        reveal.addEventListener('slidechanged-backward', function(event) {
            console.log('Slide changed backward event fired');
            if (holders.slideover) {
                handleOverlays();
            }
        });

        // Handle fragment shown/hidden events
        reveal.addEventListener('fragmentshown', function(event) {
            console.log('Fragment shown event fired');
            if (holders.slideover) {
                handleOverlays();
            }
        });

        reveal.addEventListener('fragmenthidden', function(event) {
            console.log('Fragment hidden event fired');
            if (holders.slideover) {
                handleOverlays();
            }
        });

        // Expose plugin methods to global scope
        window.slideover = {
            setup: setup,
            handleOverlays: handleOverlays
        };
    }
};

if (typeof window.Reveal === 'undefined') {
    throw new Error('The Reveal.js slideover plugin requires Reveal.js');
}

Reveal.registerPlugin('slideover', Plugin); 
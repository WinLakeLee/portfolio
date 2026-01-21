$(document).ready(function () {

    // ==========================================
    // 1. Navigation Logic
    // ==========================================
    const $navToggle = $('#navToggle');
    const $navLinks = $('#navLinks');
    const $navIcon = $navToggle.find('i');

    $navToggle.on('click', function () {
        $navLinks.toggleClass('active');
        if ($navLinks.hasClass('active')) {
            $navIcon.removeClass('fa-bars').addClass('fa-xmark');
        } else {
            $navIcon.removeClass('fa-xmark').addClass('fa-bars');
        }
    });

    // ==========================================
    // 2. Scroll Spy (Active Nav Link)
    // ==========================================
    // Using IntersectionObserver is still cleaner and more performant than scroll events
    const $sections = $('section, .category-section, .hero');
    const $navItems = {
        home: $('#nav-home'),
        projects: $('#nav-projects')
    };

    const observerOptions = {
        root: null,
        rootMargin: '-20% 0px -70% 0px',
        threshold: 0
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const id = entry.target.id;

                // Remove active class from all
                Object.values($navItems).forEach($item => {
                    if ($item.length) $item.removeClass('active');
                });

                // Add active class to current
                if (id === 'home' && $navItems.home.length) {
                    $navItems.home.addClass('active');
                } else if (id === 'projects' && $navItems.projects.length) {
                    $navItems.projects.addClass('active');
                }
            }
        });
    }, observerOptions);

    $sections.each(function () {
        if (this.id) observer.observe(this);
    });

    // ==========================================
    // 3. Carousel Logic
    // ==========================================
    $('.carousel-container').each(function () {
        const $container = $(this);
        const $wrapper = $container.find('.scrolling-wrapper');
        const $progressBar = $container.find('.scroll-progress-bar');
        const $prevBtn = $container.find('.prev');
        const $nextBtn = $container.find('.next');

        if (!$wrapper.length) return; // Skip if element missing

        const updateProgress = () => {
            const scrollLeft = $wrapper.scrollLeft();
            const scrollWidth = $wrapper[0].scrollWidth;
            const clientWidth = $wrapper[0].clientWidth;
            const maxScroll = scrollWidth - clientWidth;

            if (maxScroll > 0) {
                const widthPercentage = (scrollLeft / maxScroll) * 100;
                $progressBar.css('width', `${Math.min(100, Math.max(0, widthPercentage))}%`);
            }
        };

        $wrapper.on('scroll', updateProgress);
        $(window).on('resize', updateProgress);
        updateProgress(); // Initial

        const scrollAmount = 350 + 32; // card width + gap

        $nextBtn.on('click', function () {
            const wrapperEl = $wrapper[0];
            const maxScroll = wrapperEl.scrollWidth - wrapperEl.clientWidth;

            if (wrapperEl.scrollLeft >= maxScroll - 5) {
                wrapperEl.scrollTo({ left: 0, behavior: 'smooth' });
            } else {
                wrapperEl.scrollBy({ left: scrollAmount, behavior: 'smooth' });
            }
        });

        $prevBtn.on('click', function () {
            const wrapperEl = $wrapper[0];
            if (wrapperEl.scrollLeft <= 5) {
                wrapperEl.scrollTo({ left: wrapperEl.scrollWidth, behavior: 'smooth' });
            } else {
                wrapperEl.scrollBy({ left: -scrollAmount, behavior: 'smooth' });
            }
        });
    });

    // ==========================================
    // 4. View Toggle Logic
    // ==========================================
    $('.view-toggle-btn').on('click', function () {
        const targetId = $(this).data('target');
        const $targetContainer = $('#' + targetId);

        if ($targetContainer.length) {
            if ($targetContainer.hasClass('view-grid')) {
                $targetContainer.removeClass('view-grid').addClass('view-carousel');
            } else {
                $targetContainer.removeClass('view-carousel').addClass('view-grid');
            }
            // Re-trigger progress bar update in case layout change affects scroll
            $targetContainer.find('.scrolling-wrapper').trigger('scroll');
        }
    });

    // ==========================================
    // 5. Floating Action Buttons (FAB) logic
    // ==========================================
    const $fabContainer = $('#fabContainer');
    const $scrollTopBtn = $('#scrollToTop');
    const $scrollBottomBtn = $('#scrollToBottom');

    if ($fabContainer.length) {
        // Ensure container is visible
        $fabContainer.addClass('visible');

        const updateFabVisibility = () => {
            const scrollTop = $(window).scrollTop();
            const windowHeight = $(window).height();
            const docHeight = $(document).height();

            // Hide Up button if at top (< 100px)
            if (scrollTop < 100) {
                $scrollTopBtn.addClass('hidden');
            } else {
                $scrollTopBtn.removeClass('hidden');
            }

            // Hide Down button if at bottom (within 50px)
            if (scrollTop + windowHeight >= docHeight - 50) {
                $scrollBottomBtn.addClass('hidden');
            } else {
                $scrollBottomBtn.removeClass('hidden');
            }
        };

        $(window).on('scroll', updateFabVisibility);
        updateFabVisibility(); // Initial check

        $scrollTopBtn.on('click', function () {
            window.scrollTo({ top: 0, behavior: 'smooth' });
        });

        $scrollBottomBtn.on('click', function () {
            window.scrollTo({ top: document.body.scrollHeight, behavior: 'smooth' });
        });
    }

    // ==========================================
    // 6. Scroll Animations
    // ==========================================
    const $fadeElements = $('.fade-wrap');

    if ($fadeElements.length) {
        // Observer is generally better than scroll event for many elements
        const fadeObserver = new IntersectionObserver((entries, observer) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    $(entry.target).addClass('is-visible');
                    observer.unobserve(entry.target);
                }
            });
        }, { threshold: 0.1, rootMargin: "0px 0px -50px 0px" });

        $fadeElements.each(function () {
            fadeObserver.observe(this);
        });
    }
});

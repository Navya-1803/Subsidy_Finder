// SubsidySeva - Main JavaScript File

document.addEventListener('DOMContentLoaded', function() {
    
    // Initialize page animations
    initPageAnimations();
    
    // Initialize form enhancements
    initFormEnhancements();
    
    // Initialize search functionality
    initSearchEnhancements();
    
    // Initialize accessibility features
    initAccessibilityFeatures();
    
    // Initialize performance optimizations
    initPerformanceOptimizations();
    
});

/**
 * Initialize page animations and transitions
 */
function initPageAnimations() {
    // Add fade-in animation to main content
    const mainContent = document.querySelector('main');
    if (mainContent) {
        mainContent.classList.add('fade-in');
    }
    
    // Animate cards on scroll
    const cards = document.querySelectorAll('.card');
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };
    
    const cardObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = '0';
                entry.target.style.transform = 'translateY(20px)';
                entry.target.style.transition = 'all 0.6s ease-out';
                
                setTimeout(() => {
                    entry.target.style.opacity = '1';
                    entry.target.style.transform = 'translateY(0)';
                }, 100);
                
                cardObserver.unobserve(entry.target);
            }
        });
    }, observerOptions);
    
    cards.forEach(card => {
        cardObserver.observe(card);
    });
}

/**
 * Enhanced form functionality
 */
function initFormEnhancements() {
    // Real-time form validation
    const forms = document.querySelectorAll('form');
    forms.forEach(form => {
        const inputs = form.querySelectorAll('input[required], textarea[required], select[required]');
        
        inputs.forEach(input => {
            input.addEventListener('blur', validateField);
            input.addEventListener('input', clearValidationOnInput);
        });
        
        // Enhanced form submission
        form.addEventListener('submit', handleFormSubmission);
    });
    
    // Auto-resize textareas
    const textareas = document.querySelectorAll('textarea');
    textareas.forEach(textarea => {
        textarea.addEventListener('input', autoResizeTextarea);
        // Initial resize
        autoResizeTextarea.call(textarea);
    });
}

/**
 * Validate form field
 * @param {Event} event - The blur event
 */
function validateField(event) {
    const field = event.target;
    const value = field.value.trim();
    
    if (field.hasAttribute('required') && !value) {
        showFieldError(field, 'This field is required.');
        return false;
    }
    
    // Email validation
    if (field.type === 'email' && value) {
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (!emailRegex.test(value)) {
            showFieldError(field, 'Please enter a valid email address.');
            return false;
        }
    }
    
    // Phone validation
    if (field.type === 'tel' && value) {
        const phoneRegex = /^[\+]?[1-9][\d]{9,14}$/;
        if (!phoneRegex.test(value.replace(/[\s\-\(\)]/g, ''))) {
            showFieldError(field, 'Please enter a valid phone number.');
            return false;
        }
    }
    
    clearFieldError(field);
    return true;
}

/**
 * Show field validation error
 * @param {HTMLElement} field - The form field
 * @param {string} message - Error message
 */
function showFieldError(field, message) {
    field.classList.add('is-invalid');
    
    // Remove existing error message
    const existingError = field.parentNode.querySelector('.invalid-feedback');
    if (existingError) {
        existingError.remove();
    }
    
    // Add new error message
    const errorDiv = document.createElement('div');
    errorDiv.className = 'invalid-feedback';
    errorDiv.textContent = message;
    field.parentNode.appendChild(errorDiv);
}

/**
 * Clear field validation error
 * @param {HTMLElement} field - The form field
 */
function clearFieldError(field) {
    field.classList.remove('is-invalid');
    const errorDiv = field.parentNode.querySelector('.invalid-feedback');
    if (errorDiv) {
        errorDiv.remove();
    }
}

/**
 * Clear validation on input
 * @param {Event} event - The input event
 */
function clearValidationOnInput(event) {
    const field = event.target;
    if (field.classList.contains('is-invalid') && field.value.trim()) {
        clearFieldError(field);
    }
}

/**
 * Handle form submission with loading state
 * @param {Event} event - The submit event
 */
function handleFormSubmission(event) {
    const form = event.target;
    const submitButton = form.querySelector('button[type="submit"]');
    
    if (submitButton) {
        submitButton.classList.add('loading');
        submitButton.disabled = true;
        
        // Re-enable button after 3 seconds (fallback)
        setTimeout(() => {
            submitButton.classList.remove('loading');
            submitButton.disabled = false;
        }, 3000);
    }
}

/**
 * Auto-resize textarea based on content
 */
function autoResizeTextarea() {
    this.style.height = 'auto';
    this.style.height = (this.scrollHeight) + 'px';
}

/**
 * Enhanced search functionality
 */
function initSearchEnhancements() {
    const searchInputs = document.querySelectorAll('input[name="search"]');
    
    searchInputs.forEach(input => {
        // Add search icon if not present
        if (!input.parentNode.querySelector('.search-icon')) {
            addSearchIcon(input);
        }
        
        // Add clear button
        addClearButton(input);
        
        // Add search suggestions (if needed)
        // initSearchSuggestions(input);
    });
}

/**
 * Add search icon to input
 * @param {HTMLElement} input - Search input element
 */
function addSearchIcon(input) {
    if (input.parentNode.classList.contains('input-group')) {
        return; // Already has input group styling
    }
    
    const wrapper = document.createElement('div');
    wrapper.className = 'position-relative';
    
    const icon = document.createElement('i');
    icon.className = 'fas fa-search position-absolute search-icon';
    icon.style.cssText = 'top: 50%; left: 12px; transform: translateY(-50%); color: #6c757d; z-index: 10;';
    
    input.parentNode.insertBefore(wrapper, input);
    wrapper.appendChild(icon);
    wrapper.appendChild(input);
    
    input.style.paddingLeft = '40px';
}

/**
 * Add clear button to search input
 * @param {HTMLElement} input - Search input element
 */
function addClearButton(input) {
    if (input.parentNode.querySelector('.clear-search')) {
        return; // Already has clear button
    }
    
    const clearButton = document.createElement('button');
    clearButton.type = 'button';
    clearButton.className = 'btn btn-link position-absolute clear-search d-none';
    clearButton.style.cssText = 'top: 50%; right: 8px; transform: translateY(-50%); z-index: 10; padding: 0; border: none; color: #6c757d;';
    clearButton.innerHTML = '<i class="fas fa-times"></i>';
    
    // Position the wrapper relatively if needed
    if (!input.parentNode.classList.contains('position-relative')) {
        input.parentNode.classList.add('position-relative');
    }
    
    input.parentNode.appendChild(clearButton);
    
    // Show/hide clear button based on input value
    function toggleClearButton() {
        if (input.value.trim()) {
            clearButton.classList.remove('d-none');
        } else {
            clearButton.classList.add('d-none');
        }
    }
    
    input.addEventListener('input', toggleClearButton);
    input.addEventListener('keyup', toggleClearButton);
    
    // Clear input when button is clicked
    clearButton.addEventListener('click', () => {
        input.value = '';
        input.focus();
        toggleClearButton();
        
        // Trigger form submission or update if needed
        const form = input.closest('form');
        if (form) {
            form.submit();
        }
    });
    
    // Initial check
    toggleClearButton();
}

/**
 * Initialize accessibility features
 */
function initAccessibilityFeatures() {
    // Add skip navigation link
    addSkipNavigation();
    
    // Enhance keyboard navigation
    enhanceKeyboardNavigation();
    
    // Add ARIA labels and descriptions
    enhanceAriaLabels();
    
    // Improve focus indicators
    improveFocusIndicators();
}

/**
 * Add skip navigation link
 */
function addSkipNavigation() {
    const skipLink = document.createElement('a');
    skipLink.href = '#main-content';
    skipLink.className = 'visually-hidden-focusable btn btn-primary position-absolute';
    skipLink.style.cssText = 'top: 10px; left: 10px; z-index: 9999;';
    skipLink.textContent = 'Skip to main content';
    
    document.body.insertBefore(skipLink, document.body.firstChild);
    
    // Add main content ID if not present
    const main = document.querySelector('main');
    if (main && !main.id) {
        main.id = 'main-content';
    }
}

/**
 * Enhance keyboard navigation
 */
function enhanceKeyboardNavigation() {
    // Add keyboard support for card interactions
    const cards = document.querySelectorAll('.category-card, .subsidy-card');
    cards.forEach(card => {
        const link = card.querySelector('a');
        if (link) {
            card.setAttribute('tabindex', '0');
            card.setAttribute('role', 'button');
            card.addEventListener('keydown', (event) => {
                if (event.key === 'Enter' || event.key === ' ') {
                    event.preventDefault();
                    link.click();
                }
            });
        }
    });
}

/**
 * Enhance ARIA labels and descriptions
 */
function enhanceAriaLabels() {
    // Add ARIA labels to form controls
    const inputs = document.querySelectorAll('input, textarea, select');
    inputs.forEach(input => {
        const label = document.querySelector(`label[for="${input.id}"]`);
        if (label && !input.getAttribute('aria-label')) {
            input.setAttribute('aria-label', label.textContent.trim());
        }
    });
    
    // Add ARIA labels to buttons without text
    const iconButtons = document.querySelectorAll('button:not([aria-label])');
    iconButtons.forEach(button => {
        const icon = button.querySelector('i');
        if (icon && !button.textContent.trim()) {
            // Determine button purpose from icon class
            if (icon.classList.contains('fa-search')) {
                button.setAttribute('aria-label', 'Search');
            } else if (icon.classList.contains('fa-times')) {
                button.setAttribute('aria-label', 'Clear');
            } else if (icon.classList.contains('fa-external-link-alt')) {
                button.setAttribute('aria-label', 'Open in new tab');
            }
        }
    });
}

/**
 * Improve focus indicators
 */
function improveFocusIndicators() {
    // Add custom focus styles for better visibility
    const focusableElements = document.querySelectorAll('a, button, input, textarea, select, [tabindex]:not([tabindex="-1"])');
    
    focusableElements.forEach(element => {
        element.addEventListener('focus', function() {
            this.classList.add('custom-focus');
        });
        
        element.addEventListener('blur', function() {
            this.classList.remove('custom-focus');
        });
    });
}

/**
 * Initialize performance optimizations
 */
function initPerformanceOptimizations() {
    // Lazy load images (if any are added later)
    initLazyLoading();
    
    // Debounce search input
    debounceSearchInputs();
    
    // Optimize scroll events
    optimizeScrollEvents();
}

/**
 * Initialize lazy loading for images
 */
function initLazyLoading() {
    if ('IntersectionObserver' in window) {
        const imageObserver = new IntersectionObserver((entries, observer) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    const img = entry.target;
                    img.src = img.dataset.src;
                    img.classList.remove('lazy');
                    imageObserver.unobserve(img);
                }
            });
        });
        
        const lazyImages = document.querySelectorAll('img[data-src]');
        lazyImages.forEach(img => imageObserver.observe(img));
    }
}

/**
 * Debounce search inputs for better performance
 */
function debounceSearchInputs() {
    const searchInputs = document.querySelectorAll('input[name="search"]');
    
    searchInputs.forEach(input => {
        let timeoutId;
        
        input.addEventListener('input', function() {
            clearTimeout(timeoutId);
            
            timeoutId = setTimeout(() => {
                // Auto-submit search form after user stops typing
                const form = this.closest('form');
                if (form && this.value.length >= 3) {
                    // Only auto-submit if user has typed at least 3 characters
                    // form.submit(); // Uncomment if auto-submit is desired
                }
            }, 500);
        });
    });
}

/**
 * Optimize scroll events
 */
function optimizeScrollEvents() {
    let ticking = false;
    
    function updateScrollElements() {
        // Add scroll-based effects here if needed
        ticking = false;
    }
    
    function requestScrollUpdate() {
        if (!ticking) {
            requestAnimationFrame(updateScrollElements);
            ticking = true;
        }
    }
    
    window.addEventListener('scroll', requestScrollUpdate, { passive: true });
}

/**
 * Utility function to show toast notifications
 * @param {string} message - The message to display
 * @param {string} type - Type of toast (success, error, info)
 */
function showToast(message, type = 'info') {
    // Create toast container if it doesn't exist
    let toastContainer = document.querySelector('.toast-container');
    if (!toastContainer) {
        toastContainer = document.createElement('div');
        toastContainer.className = 'toast-container position-fixed top-0 end-0 p-3';
        toastContainer.style.zIndex = '9999';
        document.body.appendChild(toastContainer);
    }
    
    // Create toast element
    const toast = document.createElement('div');
    toast.className = `toast align-items-center text-white bg-${type === 'error' ? 'danger' : type === 'success' ? 'success' : 'primary'} border-0`;
    toast.setAttribute('role', 'alert');
    toast.setAttribute('aria-live', 'assertive');
    toast.setAttribute('aria-atomic', 'true');
    
    toast.innerHTML = `
        <div class="d-flex">
            <div class="toast-body">
                ${message}
            </div>
            <button type="button" class="btn-close btn-close-white me-2 m-auto" data-bs-dismiss="toast" aria-label="Close"></button>
        </div>
    `;
    
    toastContainer.appendChild(toast);
    
    // Initialize and show toast
    const bsToast = new bootstrap.Toast(toast, {
        autohide: true,
        delay: 5000
    });
    bsToast.show();
    
    // Remove toast element after it's hidden
    toast.addEventListener('hidden.bs.toast', () => {
        toast.remove();
    });
}

/**
 * Utility function to format currency (Indian Rupees)
 * @param {number} amount - Amount to format
 * @returns {string} Formatted currency string
 */
function formatCurrency(amount) {
    return new Intl.NumberFormat('en-IN', {
        style: 'currency',
        currency: 'INR',
        minimumFractionDigits: 0,
        maximumFractionDigits: 0
    }).format(amount);
}

/**
 * Utility function to truncate text
 * @param {string} text - Text to truncate
 * @param {number} length - Maximum length
 * @returns {string} Truncated text
 */
function truncateText(text, length = 100) {
    if (text.length <= length) return text;
    return text.substr(0, length) + '...';
}

// Export functions for use in other scripts
window.SubsidySeva = {
    showToast,
    formatCurrency,
    truncateText
};

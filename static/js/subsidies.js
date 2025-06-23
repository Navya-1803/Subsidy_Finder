// SubsidySeva - Subsidies Page JavaScript
// Handles filtering, searching, and display of subsidies

let currentFilters = {
    search: '',
    category: ''
};

// Initialize the page
document.addEventListener('DOMContentLoaded', function() {
    initializePage();
    loadFiltersFromURL();
    applyFilters();
});

function initializePage() {
    // Populate category dropdown
    const categorySelect = document.getElementById('category');
    const categories = getAllCategories();
    
    categories.forEach(category => {
        const option = document.createElement('option');
        option.value = category;
        option.textContent = category;
        categorySelect.appendChild(option);
    });

    // Add event listeners
    document.getElementById('search').addEventListener('input', debounce(handleSearchInput, 300));
    document.getElementById('category').addEventListener('change', handleCategoryChange);
    
    // Handle enter key in search
    document.getElementById('search').addEventListener('keypress', function(e) {
        if (e.key === 'Enter') {
            applyFilters();
        }
    });
}

function loadFiltersFromURL() {
    const urlParams = new URLSearchParams(window.location.search);
    
    // Load category from URL
    const categoryFromURL = urlParams.get('category');
    if (categoryFromURL) {
        currentFilters.category = categoryFromURL;
        document.getElementById('category').value = categoryFromURL;
    }
    
    // Load search from URL
    const searchFromURL = urlParams.get('search');
    if (searchFromURL) {
        currentFilters.search = searchFromURL;
        document.getElementById('search').value = searchFromURL;
    }
}

function handleSearchInput(e) {
    currentFilters.search = e.target.value.trim();
}

function handleCategoryChange(e) {
    currentFilters.category = e.target.value;
    applyFilters();
}

function applyFilters() {
    let filteredSubsidies = getActiveSubsidies();
    
    // Apply category filter
    if (currentFilters.category) {
        filteredSubsidies = filterByCategory(filteredSubsidies, currentFilters.category);
    }
    
    // Apply search filter
    if (currentFilters.search) {
        filteredSubsidies = searchSubsidies(filteredSubsidies, currentFilters.search);
    }
    
    displaySubsidies(filteredSubsidies);
    updateActiveFilters();
    updateURL();
}

function clearFilters() {
    currentFilters = { search: '', category: '' };
    document.getElementById('search').value = '';
    document.getElementById('category').value = '';
    
    const filteredSubsidies = getActiveSubsidies();
    displaySubsidies(filteredSubsidies);
    updateActiveFilters();
    updateURL();
}

function displaySubsidies(subsidies) {
    const container = document.getElementById('subsidiesContainer');
    const noResults = document.getElementById('noResults');
    const resultsCount = document.getElementById('resultsCount');
    
    // Update results count
    resultsCount.textContent = `${subsidies.length} found`;
    
    if (subsidies.length === 0) {
        container.innerHTML = '';
        noResults.classList.remove('d-none');
        return;
    }
    
    noResults.classList.add('d-none');
    
    // Generate HTML for subsidies
    container.innerHTML = subsidies.map(subsidy => createSubsidyCard(subsidy)).join('');
}

function createSubsidyCard(subsidy) {
    const categoryBadges = subsidy.categories.map(category => 
        `<span class="badge bg-success me-1 mb-1">${category}</span>`
    ).join('');
    
    return `
        <div class="col-lg-6 col-xl-4">
            <div class="card h-100 subsidy-card shadow-sm">
                <div class="card-header bg-primary text-white">
                    <h5 class="card-title mb-0">
                        <i class="fas fa-university me-2"></i>${subsidy.title}
                    </h5>
                </div>
                <div class="card-body d-flex flex-column">
                    <p class="card-text flex-grow-1">${subsidy.description}</p>
                    
                    <!-- Eligibility -->
                    <div class="mb-3">
                        <h6 class="text-secondary mb-2">
                            <i class="fas fa-check-circle me-1"></i>Eligibility:
                        </h6>
                        <p class="small text-muted mb-0">${subsidy.eligibility}</p>
                    </div>
                    
                    <!-- Categories -->
                    <div class="mb-3">
                        ${categoryBadges}
                    </div>
                    
                    <!-- Amount -->
                    <div class="mb-3">
                        <strong class="text-accent h6">
                            <i class="fas fa-rupee-sign me-1"></i>${subsidy.amount}
                        </strong>
                    </div>
                    
                    <!-- Department -->
                    <div class="mb-3 small text-muted">
                        <i class="fas fa-building me-1"></i>${subsidy.department}
                    </div>
                </div>
                <div class="card-footer bg-transparent">
                    <div class="d-grid">
                        <a href="${subsidy.application_link}" 
                           target="_blank" 
                           class="btn btn-primary"
                           rel="noopener noreferrer">
                            <i class="fas fa-external-link-alt me-2"></i>Apply Now
                        </a>
                    </div>
                </div>
            </div>
        </div>
    `;
}

function updateActiveFilters() {
    const activeFiltersDiv = document.getElementById('activeFilters');
    const filterTags = document.getElementById('filterTags');
    
    const hasFilters = currentFilters.search || currentFilters.category;
    
    if (!hasFilters) {
        activeFiltersDiv.classList.add('d-none');
        return;
    }
    
    activeFiltersDiv.classList.remove('d-none');
    
    let tags = [];
    
    if (currentFilters.search) {
        tags.push(`<span class="badge bg-info me-2">Search: "${currentFilters.search}"</span>`);
    }
    
    if (currentFilters.category) {
        tags.push(`<span class="badge bg-success me-2">Category: ${currentFilters.category}</span>`);
    }
    
    filterTags.innerHTML = tags.join('');
}

function updateURL() {
    const params = new URLSearchParams();
    
    if (currentFilters.search) {
        params.set('search', currentFilters.search);
    }
    
    if (currentFilters.category) {
        params.set('category', currentFilters.category);
    }
    
    const newURL = params.toString() ? 
        `${window.location.pathname}?${params.toString()}` : 
        window.location.pathname;
    
    // Update URL without reloading the page
    window.history.replaceState({}, '', newURL);
}

// Utility function for debouncing
function debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            clearTimeout(timeout);
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
}
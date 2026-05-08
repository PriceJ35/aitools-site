// Mobile nav toggle
function toggleNav() {
    document.getElementById('navLinks').classList.toggle('active');
}

// Search / filter tools
function filterTools() {
    const query = document.getElementById('searchInput').value.toLowerCase();
    const cards = document.querySelectorAll('.tool-card');

    cards.forEach(card => {
        const name = card.querySelector('.tool-name').textContent.toLowerCase();
        const desc = card.querySelector('.tool-desc').textContent.toLowerCase();
        const categories = card.dataset.categories || '';
        const match = name.includes(query) || desc.includes(query) || categories.includes(query);
        card.style.display = match ? '' : 'none';
    });
}

// Category filter on click
document.querySelectorAll('.category-card').forEach(card => {
    card.addEventListener('click', (e) => {
        e.preventDefault();
        const cat = card.dataset.category;
        document.getElementById('searchInput').value = cat;
        filterTools();
        document.getElementById('top-picks').scrollIntoView({ behavior: 'smooth' });
    });
});

// Navbar scroll effect
const navbar = document.querySelector('.navbar');
let lastScroll = 0;
window.addEventListener('scroll', () => {
    const scrollY = window.scrollY;
    if (scrollY > 20) {
        navbar.classList.add('scrolled');
    } else {
        navbar.classList.remove('scrolled');
    }
    lastScroll = scrollY;
}, { passive: true });

// Scroll-triggered animations (IntersectionObserver)
const animateElements = document.querySelectorAll('.animate-in');
if ('IntersectionObserver' in window) {
    const observer = new IntersectionObserver((entries) => {
        entries.forEach((entry, index) => {
            if (entry.isIntersecting) {
                // Stagger animation for grid items
                const parent = entry.target.parentElement;
                const siblings = parent ? Array.from(parent.querySelectorAll('.animate-in')) : [];
                const siblingIndex = siblings.indexOf(entry.target);

                const delay = siblingIndex >= 0 ? siblingIndex * 60 : 0;

                setTimeout(() => {
                    entry.target.classList.add('visible');
                }, delay);

                observer.unobserve(entry.target);
            }
        });
    }, {
        threshold: 0.08,
        rootMargin: '0px 0px -40px 0px'
    });

    animateElements.forEach(el => observer.observe(el));
} else {
    // Fallback: show all immediately
    animateElements.forEach(el => el.classList.add('visible'));
}

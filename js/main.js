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

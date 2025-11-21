// script.js
// Simple behavior:
// - Mobile nav toggle
// - Highlight active nav link on scroll
// - Tiny contact form handler (prevents real submission)
document.addEventListener('DOMContentLoaded', function(){
    const nav = document.getElementById('nav');
    const navToggle = document.getElementById('navToggle');
    const navLinks = document.querySelectorAll('.nav-link');

    navToggle && navToggle.addEventListener('click', function(){
        if (!nav) return;
        if (nav.style.display === 'flex') {
            nav.style.display = '';
        } else {
            nav.style.display = 'flex';
            nav.style.flexDirection = 'column';
            nav.style.gap = '0.5rem';
        }
    });

    // Active link on scroll
    const sections = document.querySelectorAll('main .section[id]');
    const observer = new IntersectionObserver(entries=>{
        entries.forEach(entry=>{
            const id = entry.target.id;
            const link = document.querySelector('.nav-link[href="#'+id+'"]');
            if (link) link.classList.toggle('active', entry.isIntersecting);
        });
    }, {root:null, threshold: 0.45});
    sections.forEach(s=>observer.observe(s));

    // Contact form demo handler
    const form = document.getElementById('contactForm');
    if (form){
        form.addEventListener('submit', function(e){
            e.preventDefault();
            alert('Thanks! This demo prevents real submission. Implement backend or email service to receive messages.');
            form.reset();
        });
    }
});

import os
from pathlib import Path
from datetime import datetime

# task1.py
# GitHub Copilot
# Generates a simple responsive portfolio website (index.html, styles.css, script.js, README.md)
# Features:
# - Sections: About Me, Projects, Contact
# - AI-suggested color palettes & typography included in README and CSS variables
# - Responsive layout using CSS Grid + Flexbox
# - Smooth-scrolling navigation (CSS + small JS to set active link)


BASE_DIR = Path(__file__).resolve().parent

INDEX_HTML = """<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width,initial-scale=1" />
    <title>Portfolio - Your Name</title>

    <!-- Google Fonts (suggested) -->
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&family=Merriweather:wght@300;400;700&display=swap" rel="stylesheet">

    <link rel="stylesheet" href="styles.css" />
</head>
<body>
    <header class="site-header">
        <div class="container header-inner">
            <a class="logo" href="#">YourName</a>
            <nav class="nav" id="nav">
                <a href="#about" class="nav-link">About</a>
                <a href="#projects" class="nav-link">Projects</a>
                <a href="#contact" class="nav-link">Contact</a>
            </nav>
            <button class="nav-toggle" id="navToggle" aria-label="Toggle navigation">☰</button>
        </div>
    </header>

    <main class="container site-main">
        <section id="about" class="section about">
            <div class="about-grid">
                <div class="about-text">
                    <h1>About Me</h1>
                    <p>Brief intro: describe who you are, key skills, and passions. Keep it concise and human-readable.</p>
                    <ul>
                        <li>Role: Frontend / Full-stack Developer</li>
                        <li>Tech: HTML, CSS, JavaScript, Python</li>
                        <li>Interests: UI/UX, accessibility, performance</li>
                    </ul>
                </div>
                <div class="about-photo">
                    <div class="avatar">YN</div>
                </div>
            </div>
        </section>

        <section id="projects" class="section projects">
            <h2>Projects</h2>
            <div class="projects-grid">
                <article class="card">
                    <div class="card-media" style="background-image:url('https://via.placeholder.com/800x450?text=Project+1');"></div>
                    <div class="card-body">
                        <h3>Project One</h3>
                        <p>Short description explaining the project's goal, tech stack and your role.</p>
                        <div class="card-actions">
                            <a href="#" class="btn">View</a>
                            <a href="#" class="link">Source</a>
                        </div>
                    </div>
                </article>

                <article class="card">
                    <div class="card-media" style="background-image:url('https://via.placeholder.com/800x450?text=Project+2');"></div>
                    <div class="card-body">
                        <h3>Project Two</h3>
                        <p>Short description. Use badges or small icons to note tech used.</p>
                        <div class="card-actions">
                            <a href="#" class="btn">View</a>
                            <a href="#" class="link">Source</a>
                        </div>
                    </div>
                </article>

                <article class="card">
                    <div class="card-media" style="background-image:url('https://via.placeholder.com/800x450?text=Project+3');"></div>
                    <div class="card-body">
                        <h3>Project Three</h3>
                        <p>Short description. Link to demo or repository.</p>
                        <div class="card-actions">
                            <a href="#" class="btn">View</a>
                            <a href="#" class="link">Source</a>
                        </div>
                    </div>
                </article>
            </div>
        </section>

        <section id="contact" class="section contact">
            <h2>Contact</h2>
            <div class="contact-grid">
                <form class="contact-form" id="contactForm">
                    <label>
                        <span>Name</span>
                        <input type="text" name="name" required />
                    </label>
                    <label>
                        <span>Email</span>
                        <input type="email" name="email" required />
                    </label>
                    <label>
                        <span>Message</span>
                        <textarea name="message" rows="6" required></textarea>
                    </label>
                    <div class="form-actions">
                        <button type="submit" class="btn primary">Send</button>
                        <button type="reset" class="btn">Reset</button>
                    </div>
                </form>

                <aside class="contact-info">
                    <h3>Get in touch</h3>
                    <p>Email: <a href="mailto:you@example.com">you@example.com</a></p>
                    <p>Location: City, Country</p>
                    <div class="social">
                        <a href="#" aria-label="GitHub">GitHub</a>
                        <a href="#" aria-label="LinkedIn">LinkedIn</a>
                    </div>
                </aside>
            </div>
        </section>
    </main>

    <footer class="site-footer">
        <div class="container">
            <p>© {year} Your Name — Built with a responsive Grid/Flexbox layout</p>
        </div>
    </footer>

    <script src="script.js"></script>
</body>
</html>
""".replace("{year}", str(Path().stat().st_mtime)[:4])  # harmless placeholder, will be replaced below if desired

STYLES_CSS = """/* styles.css
AI-suggested color palette & typography:
- Palette (Calm Professional):
    --color-primary: #0F172A (Rich Indigo)
    --color-accent:  #0066FF (Bright Blue)
    --color-muted:   #6B7280 (Cool Gray)
    --color-bg:      #F8FAFC (Off-white)
    --color-card:    #FFFFFF (Card background)
Typography:
- Sans for UI: Inter (400/600)
- Serif for headings: Merriweather (400/700)
*/

/* CSS variables */
:root{
    --color-primary: #0F172A;
    --color-accent:  #0066FF;
    --color-muted:   #6B7280;
    --color-bg:      #F8FAFC;
    --color-card:    #FFFFFF;
    --radius: 12px;
    --gap: 1.25rem;
    --max-width: 1100px;
    --elev: 0 6px 18px rgba(15,23,42,0.08);
    --text: #0b1220;
    --muted: #475569;
    --accent-contrast: #fff;
    font-family: "Inter", system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial;
    color-scheme: light;
    scroll-behavior: smooth;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
}

*{box-sizing:border-box}
html,body{height:100%}
body{
    margin:0;
    background:var(--color-bg);
    color:var(--text);
    line-height:1.5;
    -webkit-font-smoothing:antialiased;
}

/* Layout container */
.container{
    max-width: var(--max-width);
    margin: 0 auto;
    padding: 1rem;
}

/* Header */
.site-header{
    background: linear-gradient(180deg, rgba(255,255,255,0.6), rgba(255,255,255,0.4));
    position: sticky;
    top:0;
    z-index: 40;
    backdrop-filter: blur(6px);
    border-bottom: 1px solid rgba(15,23,42,0.04);
}
.header-inner{
    display:flex;
    align-items:center;
    gap:1rem;
    padding:0.75rem 0;
}
.logo{
    font-weight:700;
    color:var(--color-primary);
    text-decoration:none;
    font-size:1.125rem;
}
.nav{
    margin-left:auto;
    display:flex;
    gap:0.75rem;
    align-items:center;
}
.nav-link{
    color:var(--muted);
    text-decoration:none;
    padding:0.45rem 0.6rem;
    border-radius:8px;
}
.nav-link:hover, .nav-link.active{
    background:rgba(0,102,255,0.08);
    color:var(--color-primary);
}

/* Mobile nav toggle */
.nav-toggle{
    display:none;
    background:transparent;
    border:0;
    font-size:1.25rem;
}

/* Sections */
.section{
    padding:2.25rem 0;
}

/* About */
.about-grid{
    display:grid;
    gap:var(--gap);
    align-items:center;
    grid-template-columns: 1fr;
}
.about-photo{display:flex;justify-content:center}
.avatar{
    width:160px;height:160px;border-radius:50%;
    background:linear-gradient(135deg,var(--color-accent),#8b5cf6);
    display:flex;align-items:center;justify-content:center;font-weight:700;color:var(--accent-contrast);
    box-shadow:var(--elev);
    font-size:2rem;
}

/* Projects Grid using CSS Grid */
.projects-grid{
    display:grid;
    gap:1rem;
    grid-template-columns: 1fr;
}
/* Card */
.card{
    background:var(--color-card);
    border-radius:var(--radius);
    overflow:hidden;
    box-shadow:var(--elev);
    display:flex;
    flex-direction:column;
}
.card-media{
    height:160px;
    background-size:cover;
    background-position:center;
}
.card-body{padding:1rem}
.card-actions{display:flex;gap:0.5rem;align-items:center;margin-top:0.75rem}
.btn{
    display:inline-block;padding:0.45rem 0.8rem;border-radius:8px;background:transparent;border:1px solid rgba(15,23,42,0.06);text-decoration:none;color:var(--color-primary);font-weight:600;
}
.btn.primary{background:var(--color-accent);color:var(--accent-contrast);border:0}

/* Contact */
.contact-grid{
    display:grid;
    gap:1rem;
    grid-template-columns: 1fr;
}
.contact-form{display:flex;flex-direction:column;gap:0.75rem}
.contact-form label{display:flex;flex-direction:column;gap:0.35rem;font-size:0.95rem;color:var(--muted)}
.contact-form input, .contact-form textarea{
    padding:0.6rem;border-radius:8px;border:1px solid rgba(15,23,42,0.06);background:white;
}

/* Footer */
.site-footer{padding:1.25rem 0;color:var(--muted);font-size:0.9rem;border-top:1px solid rgba(15,23,42,0.04);background:transparent}
.site-footer a{color:var(--color-accent);text-decoration:none}

/* Responsive rules */
@media (min-width: 720px){
    .about-grid{grid-template-columns: 1fr 300px}
    .projects-grid{grid-template-columns: repeat(2, 1fr)}
    .contact-grid{grid-template-columns: 1fr 300px}
    .nav-toggle{display:none}
}

@media (min-width: 1100px){
    .projects-grid{grid-template-columns: repeat(3, 1fr)}
    .nav{display:flex}
}

/* small screens */
@media (max-width:719px){
    .nav{display:none}
    .nav-toggle{display:block;margin-left:auto}
}
"""

SCRIPT_JS = """// script.js
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
"""

README_MD = """# Portfolio Website (Generated)
This folder contains a simple responsive portfolio site (index.html, styles.css, script.js).

AI suggestions included:
- Color palette (Calm Professional):
    - Primary: #0F172A (deep indigo)
    - Accent:  #0066FF (bright blue)
    - Muted:   #6B7280 (cool gray)
    - Background: #F8FAFC (off-white)
- Typography:
    - UI: Inter (sans)
    - Headings: Merriweather (serif)
- Layout:
    - Responsive layout using CSS Grid for content cards and Flexbox for header/actions.
    - Projects shown in a grid that adjusts from 1 -> 2 -> 3 columns by viewport width.
- Smooth scrolling:
    - Implemented with CSS scroll-behavior: smooth and a small JS IntersectionObserver to mark the active nav link.

How to use:
1. Run this script: python task1.py
2. Open index.html in your browser (double-click or serve with a static server).
3. Edit content, replace placeholder images, and connect a real contact backend as needed.
"""

def write_file(path: Path, content: str):
        path.write_text(content, encoding="utf-8")
        print(f"Wrote {path.name}")

def main():
        # Ensure base dir exists (file will write into same folder)
        index_path = BASE_DIR / "index.html"
        css_path = BASE_DIR / "styles.css"
        js_path = BASE_DIR / "script.js"
        readme_path = BASE_DIR / "README.md"

        # Replace the placeholder year with current year
        html = INDEX_HTML.replace("{year}", str(datetime.now().year))

        write_file(index_path, html)
        write_file(css_path, STYLES_CSS)
        write_file(js_path, SCRIPT_JS)
        write_file(readme_path, README_MD)
        print("Done. Open index.html in a browser to preview the portfolio site.")

if __name__ == "__main__":
        main()
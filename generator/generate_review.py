#!/usr/bin/env python3
"""
AI Tool Review Page Generator
Usage:
    1. Edit the tool data in TOOLS list below
    2. Run: python3 generate_review.py
    3. Generated HTML files will be in /reviews/
"""

import os
import json

# ============================================================
# Tool Data - Add/edit tools here, then run the script
# ============================================================
TOOLS = [
    {
        "slug": "chatgpt-review",
        "name": "ChatGPT (OpenAI)",
        "rating": "4.6",
        "stars": "★★★★½",
        "badge": "Most Popular",
        "badge_class": "trending",
        "updated": "May 3, 2026",
        "read_time": "11 min",
        "summary": "ChatGPT by OpenAI remains the most widely-used AI chatbot in 2026. With GPT-4o, DALL-E 4 integration, web browsing, and a massive plugin ecosystem, it's the most versatile AI assistant for everyday users.",
        "category": "AI Writing & Chatbot",
        "price_range": "Free - $20/mo",
        "what_is": "ChatGPT is OpenAI's flagship AI assistant, powered by the GPT-4o model. It combines text generation, image creation (via DALL-E 4), web browsing, code execution, and file analysis in a single interface. With over 500 million weekly users, it's the most popular AI tool globally.",
        "features": [
            "GPT-4o Model — Fast, multimodal model with text, image, audio, and video understanding",
            "DALL-E 4 Integration — Generate and edit images directly in chat",
            "Web Browsing — Real-time web search and information retrieval",
            "Code Interpreter — Run Python code, analyze data, create charts",
            "Custom GPTs — Create and share custom AI assistants",
            "File Upload — Analyze PDFs, spreadsheets, images, and more",
        ],
        "test_results": [
            ("General Knowledge", "9.0/10", "Broad and accurate across most topics"),
            ("Creative Writing", "8.8/10", "Good versatility, sometimes generic output"),
            ("Code Generation", "8.5/10", "Solid but can struggle with complex architectures"),
            ("Math & Logic", "8.5/10", "Improved with o3 reasoning integration"),
            ("Image Generation", "8.7/10", "DALL-E 4 produces good results, great editing"),
        ],
        "pros": [
            "Most versatile all-in-one AI assistant",
            "Excellent image generation built-in",
            "Massive plugin and GPT ecosystem",
            "Strong mobile and desktop apps",
            "Voice conversation mode",
            "Free tier is genuinely useful",
        ],
        "cons": [
            "Can be verbose and generic in responses",
            "Context window smaller than Claude (128K vs 200K)",
            "Rate limits on free tier",
            "Occasional hallucinations in factual responses",
            "Privacy concerns with training data usage",
        ],
        "pricing": [
            ("Free", "$0/mo", "Limited GPT-4o access, standard features"),
            ("Plus", "$20/mo", "Full GPT-4o, DALL-E, browsing, Code Interpreter"),
            ("Team", "$25/user/mo", "Plus features + admin tools, shared workspace"),
            ("Pro", "$200/mo", "Unlimited access, o3 reasoning model, advanced features"),
        ],
        "comparison": {
            "title": "ChatGPT vs Claude",
            "rows": [
                ("Context Window", "128K tokens", "200K tokens"),
                ("Image Generation", "✅ DALL-E 4", "❌"),
                ("Reasoning Quality", "⭐⭐⭐⭐", "⭐⭐⭐⭐⭐"),
                ("Writing Quality", "⭐⭐⭐⭐", "⭐⭐⭐⭐⭐"),
                ("Code Quality", "⭐⭐⭐⭐", "⭐⭐⭐⭐½"),
                ("Plugin Ecosystem", "✅ Massive", "❌ Limited"),
                ("Web Browsing", "✅", "✅ (Pro)"),
                ("Price (Pro)", "$20/mo", "$20/mo"),
            ],
        },
        "verdict": "ChatGPT remains the best AI assistant for most people thanks to its versatility, image generation, and massive ecosystem. If you need an all-in-one tool with the most features, ChatGPT is the way to go. For pure text quality and reasoning, Claude edges ahead.",
        "cta_url": "https://chat.openai.com",
        "cta_text": "Try ChatGPT Free",
    },
    {
        "slug": "midjourney-review",
        "name": "Midjourney v7",
        "rating": "4.7",
        "stars": "★★★★★",
        "badge": "Best Value",
        "badge_class": "best-value",
        "updated": "May 1, 2026",
        "read_time": "10 min",
        "summary": "Midjourney v7 is the undisputed king of AI image generation. With stunning photorealistic quality, consistent character generation, and real-time editing, it's the top choice for designers, marketers, and creators.",
        "category": "AI Image Generation",
        "price_range": "$10 - $120/mo",
        "what_is": "Midjourney is an AI image generation tool that creates stunning visuals from text descriptions. Version 7 introduces real-time editing, character consistency across multiple images, and significantly improved photorealism. It runs through Discord and its web interface.",
        "features": [
            "Photorealistic Generation — Industry-leading image quality with accurate lighting, textures, and details",
            "Character Consistency — Generate the same character across multiple scenes and poses",
            "Real-time Editing — Modify images interactively with instant visual feedback",
            "Style Tuning — Fine-tune the aesthetic style to match your brand or preference",
            "Pan & Zoom — Extend images beyond their original boundaries seamlessly",
            "Variation Modes — Choose between subtle and strong variations for precise control",
        ],
        "test_results": [
            ("Photorealism", "9.7/10", "Best-in-class, nearly indistinguishable from photos"),
            ("Artistic Styles", "9.5/10", "Exceptional range from oil paintings to anime"),
            ("Text on Images", "7.5/10", "Improved but still struggles with longer text"),
            ("Prompt Following", "9.0/10", "Great adherence to complex multi-element prompts"),
            ("Speed", "8.0/10", "~60 seconds for high quality; turbo mode available"),
        ],
        "pros": [
            "Best image quality available",
            "Excellent character consistency",
            "Strong community and shared prompts",
            "Web interface now available (not just Discord)",
            "Commercial usage rights included",
        ],
        "cons": [
            "No free tier available",
            "Still primarily Discord-based",
            "Learning curve for optimal prompting",
            "Can't edit specific parts precisely",
            "Generation speed could be faster",
        ],
        "pricing": [
            ("Basic", "$10/mo", "~200 fast generations, 3 concurrent jobs"),
            ("Standard", "$30/mo", "15h fast generations, unlimited relaxed"),
            ("Pro", "$60/mo", "30h fast, stealth mode, 12 concurrent jobs"),
            ("Mega", "$120/mo", "60h fast, everything in Pro, max capacity"),
        ],
        "comparison": {
            "title": "Midjourney vs DALL-E 4",
            "rows": [
                ("Image Quality", "⭐⭐⭐⭐⭐", "⭐⭐⭐⭐"),
                ("Ease of Use", "⭐⭐⭐", "⭐⭐⭐⭐⭐"),
                ("Text on Images", "⭐⭐⭐", "⭐⭐⭐⭐"),
                ("Editing Tools", "⭐⭐⭐⭐", "⭐⭐⭐⭐⭐"),
                ("Speed", "⭐⭐⭐⭐", "⭐⭐⭐⭐⭐"),
                ("Pricing", "From $10/mo", "Included in $20/mo ChatGPT"),
                ("Free Tier", "❌", "✅ (limited)"),
                ("API", "❌", "✅"),
            ],
        },
        "verdict": "Midjourney v7 produces the most beautiful AI-generated images available. If image quality is your top priority, there's no competition. For casual users who want simplicity and editing tools, DALL-E 4 is a solid alternative.",
        "cta_url": "https://midjourney.com",
        "cta_text": "Try Midjourney",
    },
]

# ============================================================
# Template - Generates review HTML pages
# ============================================================

def generate_features(features):
    items = "\n".join(f'<li><strong>{f.split(" — ")[0]}</strong> — {f.split(" — ")[1]}</li>' for f in features)
    return f'<ul>{items}</ul>'

def generate_test_table(results):
    rows = "\n".join(f'<tr><td>{r[0]}</td><td>{r[1]}</td><td>{r[2]}</td></tr>' for r in results)
    return f'''<table class="pricing-table"><thead><tr><th>Test Category</th><th>Score</th><th>Notes</th></tr></thead><tbody>{rows}</tbody></table>'''

def generate_pros_cons(pros, cons):
    pros_items = "\n".join(f"<li>{p}</li>" for p in pros)
    cons_items = "\n".join(f"<li>{c}</li>" for c in cons)
    return f'''<div class="pros-cons"><div class="pros"><h3>✅ Pros</h3><ul>{pros_items}</ul></div><div class="cons"><h3>❌ Cons</h3><ul>{cons_items}</ul></div></div>'''

def generate_pricing(pricing):
    rows = "\n".join(f'<tr><td>{p[0]}</td><td>{p[1]}</td><td>{p[2]}</td></tr>' for p in pricing)
    return f'''<table class="pricing-table"><thead><tr><th>Plan</th><th>Price</th><th>Features</th></tr></thead><tbody>{rows}</tbody></table>'''

def generate_comparison(comp):
    rows = "\n".join(f'<tr><td>{r[0]}</td><td>{r[1]}</td><td>{r[2]}</td></tr>' for r in comp["rows"])
    return f'''<h2>{comp["title"]}: Quick Comparison</h2><table class="pricing-table"><thead><tr><th>Feature</th><th>{comp["title"].split(" vs ")[0]}</th><th>{comp["title"].split(" vs ")[1]}</th></tr></thead><tbody>{rows}</tbody></table>'''

def generate_review_html(tool):
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{tool["name"]} Review 2026 - AI Tool Scout</title>
    <meta name="description" content="{tool["summary"][:160]}">
    <link rel="canonical" href="https://yourusername.github.io/aitools-site/reviews/{tool["slug"]}.html">
    <meta property="og:title" content="{tool["name"]} Review 2026">
    <meta property="og:description" content="{tool["summary"][:160]}">
    <meta property="og:type" content="article">
    <link rel="stylesheet" href="../css/style.css">
    <style>
        .review-hero {{ padding: 60px 0 40px; background: linear-gradient(180deg, #f0f0ff 0%, #fff 100%); }}
        .review-hero h1 {{ font-size: 40px; font-weight: 800; margin-bottom: 8px; }}
        .review-meta {{ display: flex; gap: 16px; align-items: center; color: var(--text-light); font-size: 14px; margin-bottom: 24px; flex-wrap: wrap; }}
        .review-rating {{ font-size: 24px; color: #f59e0b; }}
        .review-rating span {{ font-size: 18px; color: var(--text); font-weight: 700; }}
        .review-summary {{ background: var(--bg-alt); border-radius: var(--radius); padding: 24px; margin-bottom: 40px; border-left: 4px solid var(--primary); }}
        .review-summary h2 {{ font-size: 18px; margin-bottom: 8px; }}
        .review-content {{ max-width: 800px; margin: 0 auto; }}
        .review-content h2 {{ font-size: 24px; margin: 40px 0 16px; padding-top: 20px; border-top: 1px solid var(--border); }}
        .review-content p {{ margin-bottom: 16px; font-size: 16px; line-height: 1.8; color: #334155; }}
        .review-content ul, .review-content ol {{ margin: 0 0 16px 24px; }}
        .review-content li {{ margin-bottom: 8px; font-size: 16px; line-height: 1.7; color: #334155; }}
        .pros-cons {{ display: grid; grid-template-columns: 1fr 1fr; gap: 24px; margin: 30px 0; }}
        .pros, .cons {{ border-radius: var(--radius); padding: 20px; }}
        .pros {{ background: #f0fdf4; border: 1px solid #bbf7d0; }}
        .cons {{ background: #fef2f2; border: 1px solid #fecaca; }}
        .pros h3 {{ color: #16a34a; margin-bottom: 12px; }}
        .cons h3 {{ color: #dc2626; margin-bottom: 12px; }}
        .pricing-table {{ width: 100%; border-collapse: collapse; margin: 20px 0; }}
        .pricing-table th, .pricing-table td {{ padding: 12px 16px; text-align: left; border-bottom: 1px solid var(--border); }}
        .pricing-table th {{ background: var(--bg-alt); font-weight: 600; font-size: 14px; }}
        .verdict-box {{ background: linear-gradient(135deg, #eef2ff, #faf5ff); border: 2px solid #c7d2fe; border-radius: var(--radius); padding: 32px; margin: 40px 0; text-align: center; }}
        .verdict-box h3 {{ font-size: 22px; margin-bottom: 12px; }}
        .verdict-box p {{ max-width: 600px; margin: 0 auto; }}
        .cta-btn {{ display: inline-block; background: var(--gradient); color: #fff; padding: 14px 32px; border-radius: 8px; font-weight: 700; font-size: 16px; margin-top: 16px; }}
        .cta-btn:hover {{ opacity: 0.9; color: #fff; }}
        .inline-ad {{ background: var(--bg-alt); border: 2px dashed var(--border); border-radius: var(--radius); padding: 20px; text-align: center; color: var(--text-light); font-size: 14px; margin: 30px 0; }}
        @media (max-width: 768px) {{ .pros-cons {{ grid-template-columns: 1fr; }} }}
    </style>
    <script type="application/ld+json">
    {{
        "@context": "https://schema.org",
        "@type": "Review",
        "itemReviewed": {{
            "@type": "SoftwareApplication",
            "name": "{tool["name"]}",
            "applicationCategory": "{tool["category"]}"
        }},
        "reviewRating": {{
            "@type": "Rating",
            "ratingValue": "{tool["rating"]}",
            "bestRating": "5"
        }},
        "author": {{ "@type": "Organization", "name": "AI Tool Scout" }},
        "datePublished": "2026-05-01"
    }}
    </script>
</head>
<body>
    <nav class="navbar">
        <div class="container nav-container">
            <a href="/" class="logo"><span class="logo-icon">⚡</span><span class="logo-text">AI Tool Scout</span></a>
            <ul class="nav-links">
                <li><a href="/">Home</a></li>
                <li><a href="/#categories">Categories</a></li>
                <li><a href="/#comparisons">Comparisons</a></li>
            </ul>
        </div>
    </nav>

    <header class="review-hero">
        <div class="container">
            <a href="/" style="font-size:14px; color:var(--text-light);">← Back to Home</a>
            <h1>{tool["name"]} Review (2026)</h1>
            <div class="review-meta">
                <span class="review-rating">{tool["stars"]} <span>{tool["rating"]}/5</span></span>
                <span>|</span>
                <span>Updated: {tool["updated"]}</span>
                <span>|</span>
                <span>{tool["read_time"]} read</span>
            </div>
            <div class="review-summary">
                <h2>Quick Summary</h2>
                <p>{tool["summary"]}</p>
            </div>
        </div>
    </header>

    <div class="ad-container"><div class="container"><div class="ad-slot">Ad Space - 728x90</div></div></div>

    <main class="section">
        <div class="container">
            <article class="review-content">
                <h2>What Is {tool["name"]}?</h2>
                <p>{tool["what_is"]}</p>

                <div class="inline-ad">In-Article Ad - 336x280</div>

                <h2>Key Features</h2>
                {generate_features(tool["features"])}

                <h2>Performance Testing Results</h2>
                <p>We tested {tool["name"]} across multiple real-world scenarios. Here are the results:</p>
                {generate_test_table(tool["test_results"])}

                <h2>Pros & Cons</h2>
                {generate_pros_cons(tool["pros"], tool["cons"])}

                <h2>Pricing</h2>
                {generate_pricing(tool["pricing"])}

                <div class="inline-ad">In-Article Ad - 336x280</div>

                {generate_comparison(tool["comparison"])}

                <div class="verdict-box">
                    <h3>Our Verdict: {tool["rating"]}/5 — {tool["badge"]}</h3>
                    <p>{tool["verdict"]}</p>
                    <a href="{tool["cta_url"]}" class="cta-btn" target="_blank" rel="noopener">{tool["cta_text"]} →</a>
                </div>
            </article>
        </div>
    </main>

    <div class="ad-container"><div class="container"><div class="ad-slot">Ad Space - 728x90</div></div></div>

    <footer class="footer">
        <div class="container">
            <div class="footer-bottom">
                <p>&copy; 2026 AI Tool Scout. All rights reserved. | <a href="/">Home</a> | <a href="#">Privacy Policy</a></p>
            </div>
        </div>
    </footer>
</body>
</html>'''


def main():
    output_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'reviews')
    os.makedirs(output_dir, exist_ok=True)

    for tool in TOOLS:
        html = generate_review_html(tool)
        filepath = os.path.join(output_dir, f'{tool["slug"]}.html')
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f'✅ Generated: reviews/{tool["slug"]}.html')

    # Save tool data as JSON for reference
    json_path = os.path.join(output_dir, '..', 'generator', 'tools_data.json')
    os.makedirs(os.path.dirname(json_path), exist_ok=True)
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(TOOLS, f, indent=2, ensure_ascii=False)
    print(f'\n✅ Tool data saved to generator/tools_data.json')
    print(f'Total tools: {len(TOOLS)}')


if __name__ == '__main__':
    main()

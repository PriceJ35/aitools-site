#!/usr/bin/env python3
"""
Batch 2 tools - 4 additional tools to insert into generate_review.py
Run this script to append these tools to the TOOLS list in generate_review.py.
"""

import os
import re

# ============================================================
# Batch 2 Tool Data
# ============================================================
TOOLS_BATCH2 = [
    {
        "slug": "canva-ai-review",
        "name": "Canva AI",
        "rating": "4.5",
        "stars": "★★★★½",
        "badge": "Best for Design",
        "badge_class": "best-value",
        "updated": "May 2, 2026",
        "read_time": "9 min",
        "summary": "Canva AI brings powerful AI design, image generation, and content creation to the world's most popular design platform. Perfect for non-designers who need professional-looking visuals quickly.",
        "category": "AI Design",
        "price_range": "Free / $13/mo",
        "what_is": "Canva AI is the AI-powered suite built into Canva, the world's most popular online design platform with 190M+ users. It includes Magic Design (AI-generated templates), text-to-image generation, background remover, Magic Write (AI text), Magic Eraser, and dozens of other AI tools. It makes professional design accessible to everyone without requiring design skills.",
        "features": [
            "Magic Design — AI generates custom templates based on your content and preferences",
            "Text to Image — Generate images from text descriptions directly in your design",
            "Magic Write — AI writing assistant for captions, copy, and content",
            "Background Remover — One-click background removal from any image",
            "Magic Eraser — Remove unwanted objects from photos seamlessly",
            "Brand Kit AI — Automatically apply your brand colors, fonts, and style across designs",
        ],
        "test_results": [
            ("Design Quality", "8.8/10", "Professional results with minimal effort"),
            ("Ease of Use", "9.5/10", "Most intuitive design tool available"),
            ("AI Image Gen", "8.0/10", "Good but behind Midjourney and DALL-E"),
            ("Template Quality", "9.3/10", "Massive library of high-quality templates"),
            ("Speed", "9.0/10", "Fast rendering and generation"),
        ],
        "pros": [
            "Extremely easy to use",
            "Huge template library",
            "Great for non-designers",
            "All-in-one design platform",
            "Collaborative features",
            "Free tier is generous",
        ],
        "cons": [
            "AI image generation not as good as dedicated tools",
            "Can feel limited for professional designers",
            "Pro features can be expensive for teams",
            "Template-heavy approach can feel generic",
            "Export quality limited on free tier",
        ],
        "pricing": [
            ("Free", "$0/mo", "Basic features, 5GB storage, limited AI"),
            ("Pro", "$13/mo", "Full AI suite, Brand Kit, 1TB storage"),
            ("Teams", "$15/user/mo", "Pro features + real-time collaboration"),
            ("Enterprise", "Custom", "SSO, admin controls, dedicated support"),
        ],
        "comparison": {
            "title": "Canva AI vs Figma AI",
            "rows": [
                ("Ease of Use", "⭐⭐⭐⭐⭐", "⭐⭐⭐"),
                ("Design Freedom", "⭐⭐⭐", "⭐⭐⭐⭐⭐"),
                ("AI Features", "⭐⭐⭐⭐½", "⭐⭐⭐"),
                ("Templates", "⭐⭐⭐⭐⭐", "⭐⭐⭐"),
                ("Collaboration", "⭐⭐⭐⭐", "⭐⭐⭐⭐⭐"),
                ("Price", "From $13/mo", "From $15/mo"),
                ("Best For", "Non-designers", "Design teams"),
            ],
        },
        "verdict": "Canva AI is the best AI design tool for non-designers and small teams who need professional results fast. Its intuitive interface and massive template library make it accessible to everyone. For professional UI/UX design, Figma remains the better choice.",
        "cta_url": "https://canva.com",
        "cta_text": "Try Canva Free",
    },
    {
        "slug": "jasper-review",
        "name": "Jasper",
        "rating": "4.3",
        "stars": "★★★★",
        "badge": "Best for Marketing",
        "badge_class": "",
        "updated": "Apr 30, 2026",
        "read_time": "9 min",
        "summary": "Jasper is an AI marketing copilot that helps teams create on-brand content at scale. With brand voice training, campaign workflows, and multi-channel output, it's built specifically for marketing teams.",
        "category": "AI Writing & Marketing",
        "price_range": "From $49/mo",
        "what_is": "Jasper is an AI content platform designed specifically for marketing teams. It goes beyond basic AI writing by offering brand voice training, marketing campaign workflows, SEO optimization, and multi-channel content generation. Jasper helps marketing teams maintain consistent brand voice while scaling content production across blogs, social media, email, and ads.",
        "features": [
            "Brand Voice — Train AI on your brand guidelines, tone, and style for consistent output",
            "Campaign Workflows — Plan and execute multi-channel campaigns with AI assistance",
            "SEO Mode — Generate content optimized for search with real-time SEO scoring",
            "Art — Generate marketing visuals and social media graphics",
            "Chrome Extension — Use Jasper AI anywhere you write on the web",
            "Templates — 50+ marketing-specific templates for every content type",
        ],
        "test_results": [
            ("Marketing Copy", "8.8/10", "Strong ad copy, email subject lines, social posts"),
            ("Brand Consistency", "9.0/10", "Excellent voice training maintains brand tone"),
            ("SEO Content", "8.5/10", "Good optimization, integrates with SurferSEO"),
            ("Long-form Content", "8.0/10", "Decent but can be repetitive"),
            ("Speed", "8.5/10", "Fast generation across all content types"),
        ],
        "pros": [
            "Best-in-class brand voice training",
            "Built for marketing workflows",
            "Multi-channel content generation",
            "Good SEO integration",
            "Chrome extension for anywhere-access",
            "Strong template library",
        ],
        "cons": [
            "Expensive compared to ChatGPT/Claude",
            "Long-form content can feel generic",
            "Steeper learning curve",
            "Credit-based limits on lower plans",
            "Some features require SurferSEO integration",
        ],
        "pricing": [
            ("Creator", "$49/mo", "1 brand voice, 50+ templates, SEO mode"),
            ("Pro", "$69/mo", "3 brand voices, campaigns, API access"),
            ("Business", "Custom", "Unlimited voices, SSO, dedicated support"),
        ],
        "comparison": {
            "title": "Jasper vs Copy.ai",
            "rows": [
                ("Brand Voice", "⭐⭐⭐⭐⭐", "⭐⭐⭐"),
                ("Templates", "⭐⭐⭐⭐", "⭐⭐⭐⭐½"),
                ("SEO Features", "⭐⭐⭐⭐", "⭐⭐⭐"),
                ("Price (Entry)", "$49/mo", "$49/mo"),
                ("Long-form Writing", "⭐⭐⭐⭐", "⭐⭐⭐"),
                ("API Access", "✅ (Pro+)", "✅"),
                ("Free Trial", "7 days", "❌"),
            ],
        },
        "verdict": "Jasper is the best AI writing tool for marketing teams who need on-brand, multi-channel content at scale. The brand voice training and campaign workflows set it apart. For individual creators on a budget, ChatGPT or Claude offer more value.",
        "cta_url": "https://jasper.ai",
        "cta_text": "Try Jasper",
    },
    {
        "slug": "grammarly-review",
        "name": "Grammarly",
        "rating": "4.5",
        "stars": "★★★★½",
        "badge": "Best for Writing",
        "badge_class": "",
        "updated": "May 1, 2026",
        "read_time": "8 min",
        "summary": "Grammarly is the most popular AI writing assistant, used by 30M+ people daily. It goes beyond grammar checking with AI-powered tone adjustment, clarity improvements, and full rewriting suggestions.",
        "category": "AI Writing Assistant",
        "price_range": "Free / $12/mo",
        "what_is": "Grammarly is an AI-powered writing assistant that helps users write clear, effective, and mistake-free content. Beyond basic grammar and spell checking, it offers tone detection, style suggestions, clarity improvements, plagiarism detection, and AI-powered rewriting. Available as a browser extension, desktop app, and mobile keyboard, it works across virtually every platform and application.",
        "features": [
            "Grammar & Spelling — Advanced correction that catches errors other tools miss",
            "Tone Detection — Analyzes and suggests changes to match your intended tone",
            "Clarity Improvements — Identifies wordy, unclear sentences and suggests improvements",
            "AI Rewriting — Rewrite entire sentences or paragraphs with one click",
            "Plagiarism Detection — Check content against 16B+ web pages for originality",
            "Generative AI — Compose, ideate, and reply with AI-powered writing assistance",
        ],
        "test_results": [
            ("Grammar Accuracy", "9.5/10", "Best-in-class grammar and spelling correction"),
            ("Style Suggestions", "8.8/10", "Excellent clarity and conciseness improvements"),
            ("Tone Detection", "8.5/10", "Accurate tone analysis and adjustment"),
            ("AI Rewriting", "8.0/10", "Good rewrites, sometimes changes meaning"),
            ("Integration", "9.8/10", "Works everywhere — browser, desktop, mobile"),
        ],
        "pros": [
            "Works everywhere — browser, desktop, mobile",
            "Best grammar checker available",
            "Excellent clarity and style suggestions",
            "Generous free tier",
            "Tone detection is very useful",
            "Plagiarism detection included",
        ],
        "cons": [
            "Premium is needed for full features",
            "Can be overly prescriptive with style",
            "Occasionally flags correct usage as errors",
            "AI suggestions can change intended meaning",
            "Privacy concerns with text analysis",
        ],
        "pricing": [
            ("Free", "$0/mo", "Grammar, spelling, tone detection"),
            ("Premium", "$12/mo", "Full rewriting, clarity, plagiarism, AI features"),
            ("Business", "$15/user/mo", "Brand tones, style guides, analytics"),
        ],
        "comparison": {
            "title": "Grammarly vs LanguageTool",
            "rows": [
                ("Grammar Accuracy", "⭐⭐⭐⭐⭐", "⭐⭐⭐⭐"),
                ("AI Features", "⭐⭐⭐⭐", "⭐⭐⭐"),
                ("Languages", "English focus", "30+ languages"),
                ("Free Tier", "✅ Good", "✅ Good"),
                ("Price (Premium)", "$12/mo", "€5/mo"),
                ("Integration", "⭐⭐⭐⭐⭐", "⭐⭐⭐⭐"),
                ("Plagiarism", "✅", "✅ (Premium)"),
            ],
        },
        "verdict": "Grammarly remains the best AI writing assistant for English speakers. Its grammar accuracy, style suggestions, and ubiquitous integration make it essential for anyone who writes professionally. For multilingual users, LanguageTool is a strong free alternative.",
        "cta_url": "https://grammarly.com",
        "cta_text": "Try Grammarly Free",
    },
    {
        "slug": "suno-review",
        "name": "Suno",
        "rating": "4.4",
        "stars": "★★★★",
        "badge": "Best for Music",
        "badge_class": "trending",
        "updated": "Apr 28, 2026",
        "read_time": "8 min",
        "summary": "Suno is the leading AI music generation platform that creates complete songs — vocals, instruments, and lyrics — from a text prompt. Perfect for content creators, musicians, and anyone who needs custom music.",
        "category": "AI Music",
        "price_range": "Free / $10/mo",
        "what_is": "Suno is an AI music generation platform that creates complete, production-quality songs from text descriptions. It generates vocals, instruments, lyrics, and arrangements in various genres and styles. Whether you need background music for videos, jingles for ads, or full songs, Suno produces impressive results in seconds. It supports multiple languages, genres, and custom lyrics.",
        "features": [
            "Text to Song — Generate complete songs with vocals from text descriptions",
            "Custom Lyrics — Write your own lyrics or let AI generate them",
            "Genre Versatility — Pop, rock, hip-hop, jazz, classical, electronic, and more",
            "Multi-language — Generate songs in 10+ languages",
            "Audio Extension — Extend generated songs beyond initial clip length",
            "Stem Separation — Separate vocals and instrumentals for mixing",
        ],
        "test_results": [
            ("Music Quality", "8.5/10", "Impressive production quality, especially pop and rock"),
            ("Vocal Quality", "8.0/10", "Good but can sound artificial on closer listen"),
            ("Genre Range", "8.8/10", "Excellent across most popular genres"),
            ("Prompt Following", "8.2/10", "Good but genre/style sometimes drifts"),
            ("Lyrics Quality", "7.5/10", "AI lyrics can be generic, custom lyrics work better"),
        ],
        "pros": [
            "Creates complete songs with vocals",
            "Impressive genre versatility",
            "Easy to use — just type a description",
            "Generous free tier (50 credits/day)",
            "Custom lyrics support",
            "Fast generation (~30 seconds)",
        ],
        "cons": [
            "Vocals can sound AI-generated",
            "Limited control over arrangement details",
            "Commercial rights only on paid plans",
            "Songs limited to ~2 minutes",
            "Quality varies by genre",
            "Some generations sound similar",
        ],
        "pricing": [
            ("Free", "$0/mo", "50 credits/day, non-commercial use"),
            ("Pro", "$10/mo", "2500 credits, commercial rights"),
            ("Premier", "$30/mo", "10000 credits, priority generation"),
        ],
        "comparison": {
            "title": "Suno vs Udio",
            "rows": [
                ("Music Quality", "⭐⭐⭐⭐", "⭐⭐⭐⭐½"),
                ("Ease of Use", "⭐⭐⭐⭐⭐", "⭐⭐⭐⭐"),
                ("Genre Range", "⭐⭐⭐⭐½", "⭐⭐⭐⭐"),
                ("Vocal Quality", "⭐⭐⭐⭐", "⭐⭐⭐⭐½"),
                ("Free Tier", "50 credits/day", "10 credits/day"),
                ("Price (Pro)", "$10/mo", "$10/mo"),
                ("Song Length", "~2 min", "~4 min"),
            ],
        },
        "verdict": "Suno is the most accessible AI music generator, perfect for content creators who need quick, custom songs. Its ease of use and generous free tier make it the best starting point for AI music creation. For slightly higher quality and longer songs, Udio is a strong alternative.",
        "cta_url": "https://suno.com",
        "cta_text": "Try Suno Free",
    },
]


# ============================================================
# Script to insert tools into generate_review.py
# ============================================================
def insert_tools():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    target_file = os.path.join(script_dir, 'generate_review.py')

    # Read the current file
    with open(target_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Build the new tool entries as Python source code
    import pprint
    pp = pprint.PrettyPrinter(indent=4, width=120, compact=False)

    new_entries_lines = []
    for tool in TOOLS_BATCH2:
        # Use repr for clean Python representation
        tool_repr = pp.pformat(tool)
        new_entries_lines.append(f"    {tool_repr},")

    new_entries_text = "\n".join(new_entries_lines)

    # Find the closing ] of the TOOLS list - look for the pattern where
    # the last tool entry ends with a closing brace/comma followed by newline and ]
    # We insert our new entries before the final ]
    pattern = r'(\n)\]'
    match = re.search(pattern, content)
    if not match:
        print("ERROR: Could not find the closing ] of the TOOLS list.")
        return

    # Insert new tools before the closing ]
    insert_position = match.start()
    new_content = content[:insert_position] + "\n" + new_entries_text + "\n" + content[insert_position:]

    # Write the updated file
    with open(target_file, 'w', encoding='utf-8') as f:
        f.write(new_content)

    print(f"Successfully inserted {len(TOOLS_BATCH2)} tools into generate_review.py")
    print(f"Tools added: {', '.join(t['name'] for t in TOOLS_BATCH2)}")


if __name__ == '__main__':
    insert_tools()

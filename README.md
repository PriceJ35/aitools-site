# AI Tool Scout - GitHub Pages Deployment

## Quick Start
```bash
# 1. Initialize git
cd aitools-site
git init
git add .
git commit -m "Initial commit"

# 2. Create GitHub repo and push
gh repo create aitools-site --public --source=. --push

# 3. Enable GitHub Pages
# Go to repo Settings → Pages → Source: Deploy from branch → main → / (root)
# Or use CLI:
gh api repos/{owner}/aitools-site/pages -X POST -f source.branch=main -f source.path=/
```

## Generate New Reviews
```bash
# Edit generator/generate_review.py, add tools to TOOLS list
python3 generator/generate_review.py

# Commit and push
git add . && git commit -m "Add new review" && git push
```

## Ad Integration
1. Apply for Google AdSense at https://adsense.google.com
2. Replace `<!-- Ad placeholder -->` in HTML with your AdSense code
3. For better RPM, apply to Ezoic (requires some traffic) or Mediavine (50K sessions/month)

## Site Structure
```
aitools-site/
├── index.html          # Homepage
├── css/style.css       # Styles
├── js/main.js          # JavaScript
├── reviews/            # Review pages (auto-generated)
│   ├── claude-review.html
│   ├── chatgpt-review.html
│   └── midjourney-review.html
├── generator/          # Content generator
│   ├── generate_review.py
│   └── tools_data.json
└── images/             # Images
```

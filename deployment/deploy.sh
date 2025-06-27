#!/bin/bash

# Portfolio Deployment Helper Script
# Run this script to prepare your portfolio for deployment

echo "🚀 Portfolio Deployment Helper"
echo "=============================="

# Check if we're in the right directory
if [ ! -f "index.html" ]; then
    echo "❌ Error: index.html not found. Please run this script from the WebPage directory."
    exit 1
fi

echo "✅ Found index.html"

# Create deployment package
echo "📦 Creating deployment package..."
mkdir -p dist
cp index.html dist/
cp -r deployment dist/ 2>/dev/null || true

echo "✅ Deployment package created in 'dist' folder"

# Check for Git
if command -v git &> /dev/null; then
    echo "✅ Git is available"
    
    # Check if this is already a git repository
    if [ ! -d ".git" ]; then
        echo "🔧 Initializing Git repository..."
        git init
        echo "✅ Git repository initialized"
    fi
    
    # Check if there are any commits
    if ! git rev-parse HEAD &> /dev/null; then
        echo "📝 Making initial commit..."
        git add .
        git commit -m "Initial portfolio website commit"
        echo "✅ Initial commit created"
    fi
    
    echo ""
    echo "🎯 Next Steps for GitHub Pages:"
    echo "1. Create a new repository on GitHub"
    echo "2. Run: git remote add origin https://github.com/USERNAME/REPOSITORY.git"
    echo "3. Run: git push -u origin main"
    echo "4. Enable GitHub Pages in repository settings"
    
else
    echo "⚠️  Git not found. You can still deploy to Netlify/Vercel manually."
fi

echo ""
echo "🌐 Quick Deployment Options:"
echo "1. Netlify: Drag 'index.html' to netlify.com"
echo "2. Vercel: Upload 'dist' folder to vercel.com"
echo "3. GitHub Pages: Follow the Git instructions above"

echo ""
echo "📖 For detailed instructions, open: deployment/quick-start.html"
echo "✨ Your portfolio is ready for deployment!"

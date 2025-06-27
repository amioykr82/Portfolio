# Deployment Guide for Dr. Amioy Kumar's Portfolio

## 🎯 Recommended: GitHub Pages Deployment

### Step 1: Create GitHub Repository
1. Go to [GitHub.com](https://github.com)
2. Click "New Repository"
3. Name it: `amioy-kumar-portfolio` or `portfolio`
4. Make it **Public** for free GitHub Pages
5. Initialize with README: **No** (we have our own)

### Step 2: Upload Files
```bash
# Navigate to your project directory
cd /Users/mac/Documents/Work/WebPage

# Initialize git repository
git init

# Add all files
git add .

# Commit files
git commit -m "Initial portfolio website"

# Add GitHub repository as remote
git remote add origin https://github.com/YOUR_USERNAME/portfolio.git

# Push to GitHub
git push -u origin main
```

### Step 3: Enable GitHub Pages
1. Go to your repository on GitHub
2. Click **Settings** tab
3. Scroll to **Pages** section
4. Source: **Deploy from a branch**
5. Branch: **main**
6. Folder: **/ (root)**
7. Click **Save**

Your site will be available at: `https://YOUR_USERNAME.github.io/portfolio`

---

## 🚀 Alternative: Netlify Deployment

### Option A: Drag & Drop (Easiest)
1. Go to [Netlify.com](https://netlify.com)
2. Sign up for free account
3. Drag your `index.html` file to the deployment area
4. Get instant URL: `https://random-name.netlify.app`

### Option B: GitHub Integration
1. Connect Netlify to your GitHub repository
2. Auto-deploy on every push
3. Custom domain support available

---

## ⚡ Alternative: Vercel Deployment

1. Go to [Vercel.com](https://vercel.com)
2. Sign up with GitHub account
3. Import your repository
4. Deploy automatically
5. Get URL: `https://portfolio.vercel.app`

---

## 🌐 Custom Domain Setup (Optional)

### For GitHub Pages:
1. Buy domain from any registrar
2. Add CNAME file to repository
3. Configure DNS settings
4. Enable HTTPS in GitHub Pages settings

### For Netlify/Vercel:
1. Add custom domain in dashboard
2. Configure DNS as instructed
3. SSL certificate automatically provided

---

## 📋 Pre-Deployment Checklist

- [x] All images are properly linked
- [x] All external links work correctly
- [x] Mobile responsive design tested
- [x] All sections properly aligned
- [x] Contact information is correct
- [x] Social media links are valid
- [x] No broken internal links

---

## 🔧 File Optimization for Deployment

The website is already optimized with:
- ✅ CDN-loaded Tailwind CSS
- ✅ Google Fonts integration
- ✅ Optimized images
- ✅ Minified structure
- ✅ Responsive design
- ✅ Cross-browser compatibility

---

## 📞 Support

If you need help with deployment:
1. Check the hosting platform documentation
2. GitHub Pages: [docs.github.com/pages](https://docs.github.com/pages)
3. Netlify: [docs.netlify.com](https://docs.netlify.com)
4. Vercel: [vercel.com/docs](https://vercel.com/docs)

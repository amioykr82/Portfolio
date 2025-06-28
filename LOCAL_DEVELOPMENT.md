# 🌐 Local Development Guide

## Quick Start (Recommended)

### Option 1: Using the Start Script
```bash
./start-server.sh
```

### Option 2: Using Python Directly
```bash
python3 server.py
```

### Option 3: Simple Python Server
```bash
# Basic Python server (if the custom server doesn't work)
python3 -m http.server 8000
```

## 📱 Accessing Your Portfolio

After starting the server, open your browser and go to:
- **http://localhost:8000** (or the port shown in terminal)

## 🛑 Stopping the Server

Press `Ctrl+C` in the terminal to stop the server.

## 🔧 Troubleshooting

### Port Already in Use
If port 8000 is busy, the server will automatically find the next available port.

### Python Not Found
- **macOS**: Install with `brew install python3`
- **General**: Download from [python.org](https://python.org)

### Files Not Loading
Make sure you're in the correct directory:
```bash
cd /Users/mac/Documents/Work/WebPage
```

## 📁 Project Structure
```
WebPage/
├── index.html              # Main portfolio page
├── server.py              # Custom development server
├── start-server.sh        # Quick start script
├── Page.py                # Legacy file (contains HTML)
├── WhatsApp Image...      # Profile photo
├── deployment/            # Deployment guides
└── assets/               # Additional assets
```

## 🚀 Deployment
For production deployment, see `deployment/DEPLOYMENT_GUIDE.md`

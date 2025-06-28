#!/bin/bash

# Portfolio Development Server Launcher
# Quick script to start Dr. Amioy Kumar's portfolio on localhost

echo "🌐 Starting Dr. Amioy Kumar's Portfolio Server..."
echo "=================================================="

# Check if Python 3 is available
if command -v python3 &> /dev/null; then
    echo "✅ Python 3 found"
    python3 server.py
elif command -v python &> /dev/null; then
    echo "✅ Python found (checking version...)"
    python --version
    python server.py
else
    echo "❌ Error: Python not found!"
    echo "Please install Python 3 to run the development server."
    echo ""
    echo "Installation options:"
    echo "  • macOS: brew install python3"
    echo "  • Or download from: https://python.org"
    exit 1
fi

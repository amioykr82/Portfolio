#!/usr/bin/env python3
"""
Simple HTTP Server for Dr. Amioy Kumar's Portfolio
Serves the portfolio website on localhost for development and testing.
"""

import http.server
import socketserver
import os
import sys
import webbrowser
from pathlib import Path

class PortfolioHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    """Custom HTTP request handler for the portfolio website."""
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=os.path.dirname(os.path.abspath(__file__)), **kwargs)
    
    def log_message(self, format, *args):
        """Override to provide cleaner logging."""
        print(f"[SERVER] {self.address_string()} - {format % args}")
    
    def end_headers(self):
        """Add custom headers for better local development."""
        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        super().end_headers()

def find_free_port(start_port=8000, max_attempts=10):
    """Find an available port starting from start_port."""
    import socket
    
    for port in range(start_port, start_port + max_attempts):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.bind(('localhost', port))
                return port
        except OSError:
            continue
    
    raise RuntimeError(f"Could not find an available port in range {start_port}-{start_port + max_attempts}")

def main():
    """Main function to start the portfolio server."""
    # Change to the directory containing this script
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
    # Check if index.html exists
    if not Path('index.html').exists():
        print("❌ Error: index.html not found in current directory!")
        print(f"📁 Current directory: {os.getcwd()}")
        print("📄 Available files:")
        for file in os.listdir('.'):
            if os.path.isfile(file):
                print(f"   - {file}")
        sys.exit(1)
    
    # Find an available port
    try:
        port = find_free_port()
    except RuntimeError as e:
        print(f"❌ Error: {e}")
        sys.exit(1)
    
    # Create and start the server
    try:
        with socketserver.TCPServer(("localhost", port), PortfolioHTTPRequestHandler) as httpd:
            print("🌐 Dr. Amioy Kumar's Portfolio Server")
            print("=" * 50)
            print(f"🚀 Server started successfully!")
            print(f"📍 Local URL: http://localhost:{port}")
            print(f"📁 Serving from: {os.getcwd()}")
            print("=" * 50)
            print("📖 Instructions:")
            print(f"   • Open your browser and go to: http://localhost:{port}")
            print("   • Press Ctrl+C to stop the server")
            print("=" * 50)
            
            # Optionally open browser automatically
            try:
                print("🌍 Opening browser automatically...")
                webbrowser.open(f'http://localhost:{port}')
            except Exception as e:
                print(f"⚠️  Could not open browser automatically: {e}")
                print("   Please open your browser manually and navigate to the URL above.")
            
            print(f"\n⏳ Server is running... Press Ctrl+C to stop\n")
            
            # Keep the server running
            httpd.serve_forever()
            
    except KeyboardInterrupt:
        print("\n🛑 Server stopped by user")
        print("👋 Thank you for using Dr. Amioy Kumar's Portfolio Server!")
    except Exception as e:
        print(f"❌ Error starting server: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()

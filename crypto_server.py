#!/usr/bin/env python3
"""
Simple Python server for Cryptocurrency Analyzer Dashboard.
Runs locally without any browser caching or service worker issues.
Usage: python3 crypto_server.py
Then open http://localhost:8080/ in your browser.
"""
import http.server
import socketserver
import webbrowser
import os

PORT = 8080
os.chdir(os.path.dirname(os.path.abspath(__file__)))

class Handler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # Add CORS headers and disable caching for fresh data
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        super().end_headers()

    def log_message(self, fmt, *args):
        print(f"[Server] {fmt % args}")

if __name__ == '__main__':
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print(f"\n✅ Cryptocurrency Analyzer Dashboard running locally!")
        print(f"📍 URL: http://localhost:{PORT}/new_index.html")
        print(f"📊 Data source: CoinGecko API (https://api.coingecko.com)")
        print(f"⚠️  This runs locally — no GitHub Pages caching, no service worker blocking.")
        print(f"🔄 Press Ctrl+C to stop.\n")
        try:
            webbrowser.open(f"http://localhost:{PORT}/new_index.html")
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n🛑 Server stopped.")

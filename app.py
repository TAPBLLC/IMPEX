from flask import Flask, request, jsonify
import os, requests

app = Flask(__name__)

API_KEY  = os.getenv("IMPEX_API_KEY")
BASE_URL = "https://api.impex-jp.com/"

# 1) A simple “home” route to prove the app is running
@app.route("/")
def home():
    return "✔️ Service is up!", 200

# 2) A “ping” route that tries to hit Impex and reports back
@app.route("/ping")
def ping():
    try:
        # Just hit the base parts search URL with no params
        resp = requests.get(f"{BASE_URL}/parts/search.html", timeout=5)
        return f"Impex responded: HTTP {resp.status_code}", 200
    except Exception as e:
        # Return the raw exception message so you can see exactly what’s failing
        return f"Error when reaching Impex: {e}", 500

# Your existing /search route goes here unchanged…
@app.route("/search")
def search():
    # …your current code…
    pass

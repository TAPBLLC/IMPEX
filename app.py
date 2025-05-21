import os
import requests
from flask import Flask, request, jsonify

app = Flask(__name__)
API_KEY  = os.getenv("IMPEX_API_KEY")
BASE_URL = "https://api.impex-jp.com/api"

@app.route("/search")
def search():
    part_no = request.args.get("part_no","")
    params = {
      "key": API_KEY,
      "part_no": part_no,
      "original_only": 0,
      "price_factor": 1,
      "price_increase": 0
    }
    r = requests.get(f"{BASE_URL}/parts/search.html", params=params, timeout=10)
    r.raise_for_status()
    return jsonify(r.json())

if __name__=="__main__":
    app.run(host="0.0.0.0", port=5000)

@app.route("/ping")
def ping():
    # Try a bare HEAD request to test connectivity
    r = requests.head("https://api.impex-jp.com", timeout=5)
    return (f"API HEAD status: {r.status_code}", r.status_code)

from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd
import os

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Hardcoded API key (for quick testing ONLY)
API_KEY = "12345abcde"

DATA_PATH = os.path.join('data', 'processed', 'sales_cleaned.csv')

# Load dataset with error handling
try:
    df = pd.read_csv(DATA_PATH)
except Exception as e:
    print(f"Error loading data: {e}")
    df = pd.DataFrame()  # fallback empty dataframe

@app.route('/')
def home():
    return jsonify({
        "status": "API is running",
        "endpoints": {
            "/api/sales": "GET - Retrieve sales data (optional filter: ?item=xyz)",
            "/api/sales/summary": "GET - Get sales summary"
        }
    })

@app.route('/api/sales', methods=['GET'])
def get_sales_data():
    # Authentication
    key = request.headers.get('x-api-key')
    if key != API_KEY:
        return jsonify({'error': 'Unauthorized'}), 401

    item = request.args.get('item')
    try:
        if item and not df.empty:
            filtered = df[df['order_type'].str.lower() == item.lower()]
        else:
            filtered = df

        return jsonify({
            "count": len(filtered),
            "data": filtered.to_dict(orient='records')
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/sales/summary', methods=['GET'])
def get_summary():
    # Authentication
    key = request.headers.get('x-api-key')
    if key != API_KEY:
        return jsonify({'error': 'Unauthorized'}), 401

    try:
        summary = df['order_type'].value_counts().to_dict() if not df.empty else {}
        return jsonify({
            "summary": summary,
            "total_orders": len(df)
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

from flask import Flask, request, jsonify
import pandas as pd

app = Flask(__name__)

# Load the dataset
df = pd.read_csv('data/processed/sales_cleaned.csv')

API_KEY = "12345abcde"

@app.route('/')
def home():
    return "API is running"

@app.route('/api/sales', methods=['GET'])
def get_sales_data():
    key = request.headers.get('x-api-key')
    if key != API_KEY:
        return jsonify({'error': 'Unauthorized'}), 401

    item = request.args.get('item')
    if item:
        filtered = df[df['order_type'].str.lower() == item.lower()]
    else:
        filtered = df

    return jsonify(filtered.to_dict(orient='records'))

@app.route('/api/sales/summary', methods=['GET'])
def get_summary():
    key = request.headers.get('x-api-key')
    if key != API_KEY:
        return jsonify({'error': 'Unauthorized'}), 401

    summary = df['order_type'].value_counts().to_dict()
    return jsonify(summary)

if __name__ == '__main__':
    app.run(debug=True, port=5055)

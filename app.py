"""from concurrent.futures import thread
from flask import Flask
from waitress import serve

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, World with waitress!!!'

mode = "prod"    

if __name__ == '__main__':
    if mode == "dev":
        app.run(host='0.0.0.0', port=50100, debug=True)
    else:    
        serve(app, host='0.0.0.0', port=50100, threads=2)    """



from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from waitress import serve
import requests

app = Flask(__name__)
CORS(app)

IPQS_API_KEY = 'bca5031d-9bd4-4a84-9a00-c505418cb410'  # Replace with your actual API key
IPQS_API_URL = 'https://ipqualityscore.com/api/json/email/'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze_email():
    data = request.json
    email = data.get('email')
    
    response = requests.get(f'{IPQS_API_URL}{IPQS_API_KEY}/{email}')
    result = response.json()
    
    return jsonify({
        'risk_score': result.get('fraud_score'),
        'country': result.get('country_code'),
        'carrier': result.get('mobile_carrier'),
        'validity': result.get('valid') and "Valid" or "Invalid",
        'fraudulent': result.get('fraud_score') > 75
    })

mode = "prod"

if __name__ == '__main__':
    if mode == "dev":
        app.run(host='0.0.0.0', port=50100, debug=True)
    else:
        serve(app, host='0.0.0.0', port=50100, threads=2)


"""
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from waitress import serve
import requests

app = Flask(__name__)
CORS(app)

IPQS_API_KEY = 'vyWuqvIiGMc5mw42XAK4NqKewyOo2mFQ'  # Replace with your actual API key
IPQS_API_URL = 'https://ipqualityscore.com/api/json/email/'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze_email():
    try:
        # Get JSON data from the request
        data = request.get_json()
        if not data or 'email' not in data:
            return jsonify({'error': 'Invalid input, email is required'}), 400
        
        email = data['email']
        
        # Make the API call to IPQualityScore
        response = requests.get(f'{IPQS_API_URL}{IPQS_API_KEY}/{email}')
        response.raise_for_status()  # Raise an exception for HTTP errors

        result = response.json()
        
        # Extract relevant information with safe defaults
        fraud_score = result.get('fraud_score', 0)  # Default to 0 if 'fraud_score' is not present
        return jsonify({
            'risk_score': fraud_score,
            'country': result.get('country_code', 'N/A'),
            'carrier': result.get('mobile_carrier', 'N/A'),
            'validity': "Valid" if result.get('valid') else "Invalid",
            'fraudulent': fraud_score > 75  # Compare with default value
        })

    except requests.exceptions.RequestException as e:
        app.logger.error(f"Request to IPQualityScore failed: {e}")
        return jsonify({'error': 'Failed to connect to IPQualityScore API'}), 500
    except Exception as e:
        app.logger.error(f"An unexpected error occurred: {e}")
        return jsonify({'error': 'An unexpected error occurred'}), 500

mode = "prod"

if __name__ == '__main__':
    if mode == "dev":
        app.run(host='0.0.0.0', port=50100, debug=True)
    else:
        serve(app, host='0.0.0.0', port=50100, threads=2)
"""
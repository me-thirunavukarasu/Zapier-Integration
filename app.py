from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import os

ZAPIER_URL = os.getenv('ZAPIER_URL', "https://hooks.zapier.com/hooks/catch/21201379/2zygo3y/")

app = Flask(__name__)
app.config['DEBUG'] = True

ALLOWED_ORIGINS = [
    "https://next-js-miles-talebt-hub-vzyk-pcp916njq.vercel.app",
    "http://localhost:3000",
]

CORS(app, origins=ALLOWED_ORIGINS)

def submitFormToZapier(data):
    try:
        print("Sending data to Zapier...")
        response = requests.post(ZAPIER_URL, json=data)
        return jsonify(response.json()), response.status_code

    except Exception as e:
        return jsonify({"error": "Internal Server Error", "details": str(e)}), 500

@app.route('/api/submitForm', methods=['OPTIONS', 'POST'])
def submitForm():
    if request.method == 'OPTIONS':
        response = jsonify({'message': 'Preflight request successful', 'status': "success"})
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type, content-type')
        return response

    try:
        data = request.get_json()
        external_api_response = submitFormToZapier(data)
        return jsonify(external_api_response)

    except Exception as e:
        return jsonify({"error": str(e)})

@app.route('/', methods=['GET'])
def index():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Simple HTML Page</title>
    </head>
    <body>
        <h1>Welcome to My Simple Flask Page</h1>
        <p>This page is being served by Flask on a GET request!</p>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(debug=True)

from flask import Blueprint, request, jsonify
import requests
import os

api_blueprint = Blueprint('api', __name__)

ZAPIER_URL = os.getenv('ZAPIER_URL', "https://hooks.zapier.com/hooks/catch/21200058/2zysb0x/")

@api_blueprint.route('/api/zapier-wrapper', methods=['POST'])
def zapier_wrapper():
    try:
        # Get JSON payload from the request
        payload = request.get_json()

        # Forward request to Zapier
        response = requests.post(ZAPIER_URL, json=payload)

        # Return Zapier's response
        return jsonify(response.json()), response.status_code

    except Exception as e:
        return jsonify({"error": "Internal Server Error", "details": str(e)}), 500

from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

def create_app():
    app = Flask(__name__)

    # List of allowed origins
    ALLOWED_ORIGINS = [
        "https://next-js-miles-talebt-hub-vzyk-pcp916njq.vercel.app",
        "http://localhost:3000",  # Local development
    ]

    # Enable CORS with flask-cors
    CORS(app, origins=ALLOWED_ORIGINS, allow_headers=["Content-Type", "Authorization"], methods=["GET", "POST", "OPTIONS"])

    # Main wrapper endpoint
    @app.route('/api/zapier-wrapper', methods=['POST'])
    def zapier_wrapper():
        zapier_url = 'https://hooks.zapier.com/hooks/catch/21200058/2zysb0x/'

        try:
            # Forward the request payload and headers to Zapier
            response = requests.post(
                zapier_url,
                json=request.json,
                headers={'Content-Type': 'application/json'}
            )
            # Return Zapier's response back to the client
            return jsonify(response.json()), response.status_code
        except Exception as e:
            return jsonify({'error': str(e)}), 500

    return app


# Entry point
if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)

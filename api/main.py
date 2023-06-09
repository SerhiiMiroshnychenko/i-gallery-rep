import os
import requests
from flask import Flask, request
from dotenv import load_dotenv
from flask_cors import CORS

# take environment variables from .env.
load_dotenv(dotenv_path='./.env.local')

UNSPLASH_URL = 'https://api.unsplash.com/photos/random'
UNSPLASH_KEY = os.environ.get('UNSPLASH_KEY')
DEBUG = bool(os.environ.get('DEBUG', True))

app = Flask(__name__)
CORS(app)

app.config['DEBUG'] = DEBUG


@app.route("/")
def hello_world():
    """
    Hello World response to the frontend
    """
    return "<p>Hello, World!</p>"


@app.route("/new-image")
def new_image():
    """
    Receive a request from the frontend,
    make a request to the Unsplash api,
    receive a response from the Unsplash api
    and send it to the frontend"""

    # Отримуємо 'query' від клієнта
    word = request.args.get('query')

    headers = {
        'Authorization': f'Client-ID {UNSPLASH_KEY}',
        'Accept-Version': 'v1',
    }

    params = {
        'query': word
    }  # Формуємо значення 'query'

    def get_request():
        return requests.get(
            url=UNSPLASH_URL,
            headers=headers,
            params=params,
            timeout=5)  # Відправляємо запит на Unsplash API, та отримуємо 'response'

    response = get_request()

    result = response.json()

    if response.json() == {'errors': ['No photos found.']}:
        params = {
            'query': ''
        }  # Формуємо значення 'query'

        response = get_request()
        result = response.json()
        result['description'] = f'ERROR: No photos found for word "{word}".'

    return result


def main():
    """To run Flask application"""
    if not UNSPLASH_KEY:
        raise EnvironmentError(
            'Please create .env.local file and insert there UNSPLASH_KEY')
    app.run(host='0.0.0.0', port=5050)


if __name__ == '__main__':
    main()

import os
import requests
from flask import Flask, request
from dotenv import load_dotenv

# take environment variables from .env.
load_dotenv(dotenv_path='./.env.local')

UNSPLASH_URL = 'https://api.unsplash.com/photos/random'
UNSPLASH_KEY = os.environ.get('UNSPLASH_KEY')

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/new-image")
def new_image():
    # Отримуємо 'query' від клієнта
    word = request.args.get('query')

    headers = {
        'Authorization': f'Client-ID {UNSPLASH_KEY}',
        'Accept-Version': 'v1',
    }

    params = {
        'query': word
    }  # Формуємо значення 'query'

    response = requests.get(
        url=UNSPLASH_URL,
        headers=headers,
        params=params
    )  # Відправляємо запит на Unsplash API, та отримуємо 'response'

    return response.json()


if __name__ == '__main__':

    if not UNSPLASH_KEY:
        raise EnvironmentError(
            'Please create .env.local file and insert there UNSPLASH_KEY')
    app.run(host='0.0.0.0', port=5050)

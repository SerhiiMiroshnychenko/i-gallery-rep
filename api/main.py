import os
import requests
from flask import Flask, request, jsonify
from dotenv import load_dotenv
from flask_cors import CORS
from mongo_client import mongo_client


gallery = mongo_client.gallery
images_collection = gallery.images

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

# Відправляємо запит на Unsplash API, та отримуємо 'response'
    response = requests.get(
        url=UNSPLASH_URL,
        headers=headers,
        params=params,
        timeout=5)

    result = response.json()

    return result if result != {'errors': ['No photos found.']} else {}


@app.route('/images', methods=['GET', 'POST'])
def images():
    """
    Endpoint for GET and POST requests
    """
    if request.method == 'GET':
        # read images from the database
        images_ = images_collection.find({})
        return jsonify(list(images_))
    if request.method == 'POST':
        # save image to the database
        # image = json.load(request.data)
        image = request.get_json()
        image['_id'] = image.get('id')
        result = images_collection.insert_one(image)
        inserted_id = result.inserted_id
        return {'inserted_id': inserted_id}


@app.route('/images/<image_id>', methods=['DELETE'])
def remove_image(image_id):
    """
    Action with the specified image from the database
    """
    if not images_collection.find_one({'_id': image_id}):
        return {'message': 'Image not found'}, 404
    # Delete the image from the database
    if request.method == 'DELETE':
        result = images_collection.delete_one({'_id': image_id})
        return (
            {'deleted_id': image_id}
            if result.deleted_count > 0
            else ({'message': 'Image deletion failed'}, 500)
        )


def main():
    """To run Flask application"""
    if not UNSPLASH_KEY:
        raise EnvironmentError(
            'Please create .env.local file and insert there UNSPLASH_KEY')
    app.run(host='0.0.0.0', port=5050)


if __name__ == '__main__':
    main()

from flask import request, jsonify, send_from_directory
from werkzeug.utils import secure_filename
import os
import uuid
from functools import wraps
from flask import current_app as app
from . import db
from .models import Items, ItemList, Feedback, BookTable, AboutUs

def allowed_file(filename):
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not token or token != f"Bearer {app.config['SECRET_TOKEN']}":
            return jsonify({'error': 'Unauthorized access'}), 401
        return f(*args, **kwargs)
    return decorated

def paginate_query(query, page, per_page):
    return query.offset((page - 1) * per_page).limit(per_page).all()

def serialize_items(items):
    return [{
        'id': item.id,
        'item_name': item.item_name,
        'item_price': item.item_price,
        'item_description': item.item_description,
        'item_image': item.item_image,
        'category': item.category.Category_name if item.category else None
    } for item in items]

def serialize_itemlist(item_list):
    return [{'id': l.id, 'Category_name': l.Category_name} for l in item_list]

def serialize_feedbacks(feedbacks):
    return [{
        'id': r.id,
        'Name': r.Name,
        'Description': r.Description,
        'Rating': r.Rating,
        'Image': r.Image
    } for r in feedbacks]

# Define route handlers here, similar to flask_api.py but modularized

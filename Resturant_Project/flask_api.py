from flask import Flask, request, jsonify, send_from_directory, abort
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from werkzeug.utils import secure_filename
from datetime import datetime
import os
import uuid

# For Swagger UI
from flasgger import Swagger, swag_from

app = Flask(__name__)
# Configure your database URI here, example for SQLite:
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Configure upload folder and allowed extensions
UPLOAD_FOLDER = os.path.join(os.getcwd(), 'Resturant_Project', 'Media', 'feedback_images')
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

# Secret token for simple token-based authentication
app.config['SECRET_TOKEN'] = 'your-secret-token-here'  # Change this to a secure token

db = SQLAlchemy(app)
CORS(app)
swagger = Swagger(app)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Define models based on Django models structure (simplified)
class ItemList(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Category_name = db.Column(db.String(15))

class Items(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    item_name = db.Column(db.String(100))
    item_price = db.Column(db.Float)
    item_description = db.Column(db.String(255))
    item_image = db.Column(db.String(255))
    category_id = db.Column(db.Integer, db.ForeignKey('item_list.id'))
    category = db.relationship('ItemList', backref=db.backref('items', lazy=True))

class Feedback(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(100))
    Description = db.Column(db.String(255))
    Rating = db.Column(db.Integer)
    Image = db.Column(db.String(255), nullable=True)

class BookTable(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(100))
    Phone_number = db.Column(db.String(15))
    Email = db.Column(db.String(100))
    Total_person = db.Column(db.Integer)
    Booking_date = db.Column(db.String(50))

class AboutUs(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text)

def token_required(f):
    from functools import wraps
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

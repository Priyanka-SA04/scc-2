from datetime import datetime
from app import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(120), nullable=False)
    user_type = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f"User('{self.username}', '{self.user_type}')"

class Hospital(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    hospital_id = db.Column(db.String(80), unique=True, nullable=False)
    name = db.Column(db.String(80), nullable=False)
    past_requests = db.Column(db.Integer, nullable=False)
    average_request_urgency = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f"Hospital('{self.hospital_id}', '{self.name}')"

class Vendor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    vendor_id = db.Column(db.String(80), unique=True, nullable=False)
    name = db.Column(db.String(80), nullable=False)
    average_delivery_time = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f"Vendor('{self.vendor_id}', '{self.name}')"

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    request_id = db.Column(db.String(80), unique=True, nullable=False)
    hospital_id = db.Column(db.String(80), db.ForeignKey('hospital.hospital_id'), nullable=False)
    quantity = db.Column(db.Float, nullable=False)
    urgency = db.Column(db.Float, nullable=False)
    vendor_id = db.Column(db.String(80), db.ForeignKey('vendor.vendor_id'), nullable=False)
    status = db.Column(db.String(50), nullable=False, default='current')
    timestamp = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f"Order('{self.request_id}', '{self.hospital_id}', '{self.quantity}', '{self.urgency}', '{self.vendor_id}', '{self.status}')"
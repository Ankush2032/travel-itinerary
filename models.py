from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    role = db.Column(db.String(20), default='user')  # 'user' or 'admin'
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # relationships
    bookings = db.relationship('Booking', backref='user', cascade="all, delete-orphan")


class Destinations(db.Model):
    __tablename__ = 'destinations'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    zone = db.Column(db.String(100), nullable=False)
    state = db.Column(db.String(100), nullable=False)
    city = db.Column(db.String(100), nullable=False, index=True)
    name = db.Column(db.String(200), nullable=False)
    type = db.Column(db.String(100))
    establishment_year = db.Column(db.Integer)
    time_needed_hrs = db.Column(db.Float)
    google_review_rating = db.Column(db.Float)
    entrance_fee_inr = db.Column(db.Float, default=0.0)
    airport_within_50km = db.Column(db.String(150))
    weekly_off = db.Column(db.String(50))
    significance = db.Column(db.Text)
    dslr_allowed = db.Column(db.Boolean, default=True)
    google_reviews_lakh = db.Column(db.Float)
    best_time_to_visit = db.Column(db.String(100))

    # relationships
    hotels = db.relationship('Accommodation', backref='destination', lazy=True)
    transports = db.relationship(
        'Transport',  backref='destination',  lazy=True)


class Accommodation(db.Model):
    __tablename__ = 'accommodations'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    destination_id = db.Column(db.Integer, db.ForeignKey('destinations.id'), nullable=False)
    room_type = db.Column(db.String(50))
    price_per_night = db.Column(db.Float, nullable=False)
    tax_percent = db.Column(db.Float, default=10.0)
    service_charge = db.Column(db.Float, default=0.0)
    currency = db.Column(db.String(10), default='INR')

    bookings = db.relationship('Booking', backref='accommodation', cascade="all, delete-orphan")


class Transport(db.Model):
    __tablename__ = 'transports'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    destination_id = db.Column(db.Integer, db.ForeignKey('destinations.id'), nullable=False)
    transport_type = db.Column(db.String(50), nullable=False)
    provider_name = db.Column(db.String(100))
    origin_city = db.Column(db.String(100), nullable=False)
    destination_city = db.Column(db.String(100), nullable=False, index=True)
    cost_in_inr = db.Column(db.Float, nullable=False)
    duration_hours = db.Column(db.Float)
    frequency = db.Column(db.String(50))
    class_type = db.Column(db.String(50))
    available = db.Column(db.Boolean, default=True)
    last_updated = db.Column(db.DateTime, default=datetime.utcnow)


class Booking(db.Model):
    __tablename__ = 'bookings'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    accommodation_id = db.Column(db.Integer, db.ForeignKey('accommodations.id'))
    booking_type = db.Column(db.String(50))
    check_in = db.Column(db.Date)
    check_out = db.Column(db.Date)
    price = db.Column(db.Float, nullable=False)
    discount = db.Column(db.Float, default=0.0)
    total_amount = db.Column(db.Float, nullable=False)
    currency = db.Column(db.String(10), default='USD')
    booking_date = db.Column(db.DateTime, default=datetime.utcnow)
    status = db.Column(db.String(20), default='confirmed')

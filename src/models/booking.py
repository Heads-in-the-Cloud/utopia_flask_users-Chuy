from datetime import datetime
from src import db
from .users import *
from .flight import *
from sqlalchemy import ForeignKey, ForeignKeyConstraint

class Booking(db.Model):
    __tablename__ = "booking"
    id = db.Column(db.Integer, primary_key=True)
    is_active = db.Column(db.Integer, nullable=False)
    confirmation_code = db.Column(db.String, nullable=False)
    
    def __repr__(self):
        return f"Booking: ( '{self.id}', IsActive: '{self.is_active}' Confirmation Code: '{self.confirmation_code}' "


class BookingGuest(db.Model):
    __tablename__ = "booking_guest"
    booking_id = db.Column(db.Integer, db.ForeignKey("booking.id"), primary_key=True)
    contact_email = db.Column(db.String, nullable=False)
    contact_phone = db.Column(db.String)
    
    def __repr__(self):
        return f"Booking: ( '{self.booking_id}', Email: '{self.contact_email}' "


class BookingPayment(db.Model):
    __tablename__ = "booking_payment"
    booking_id = db.Column(db.Integer, db.ForeignKey("booking.id"), primary_key=True)
    stripe_id = db.Column(db.String, nullable=False)
    refunded = db.Column(db.Boolean, nullable=False, default=False)
    
    def __repr__(self):
        return f"Booking: ( '{self.id}', IsActive: '{self.is_active}' Confirmation Code: '{self.confirmation_code}' "


class Passenger(db.Model):
    __tablename__ = "passenger"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    booking_id = db.Column(db.Integer, db.ForeignKey("booking.id"), nullable=False)
    given_name = db.Column(db.String, nullable=False)
    family_name = db.Column(db.String, nullable=False)
    dob = db.Column(db.Date, nullable=False)
    gender = db.Column(db.String, nullable=False)
    address = db.Column(db.String, nullable=False)
    
    def __repr__(self):
        return f"Passenger: ( '{self.id}', booking_id: '{self.booking_id}'"
    
booking_agent = db.Table(
    "booking_agent",
    db.metadata,
    db.Column("booking_id", db.Integer, db.ForeignKey("booking.id"), primary_key=True),
    db.Column("agent_id", db.Integer, db.ForeignKey("user.id"), primary_key=True)
)


booking_user = db.Table(
    "booking_user",
    db.metadata,
    db.Column("booking_id", db.Integer, db.ForeignKey("booking.id"), primary_key=True),
    db.Column("user_id", db.Integer, db.ForeignKey("user.id"), primary_key=True)
)


flight_booking = db.Table(
    "flight_booking",
    db.metadata,
    db.Column("flight_id", db.Integer, db.ForeignKey("flight.id"), primary_key=True),
    db.Column("booking_id", db.Integer, db.ForeignKey("booking.id"), primary_key=True)
)
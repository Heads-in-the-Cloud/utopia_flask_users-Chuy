# Import packages
from datetime import datetime
from src import db
from sqlalchemy import ForeignKey, ForeignKeyConstraint

class Airport(db.Model):
    __tablename__ = "airport"
    iata_id = db.Column(db.String, primary_key=True)
    city = db.Column(db.String)

    def __repr__(self):
        return f"Airport( '{self.iata_id}', '{self.city}' "

class Route(db.Model):
    __tablename__ = "route"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    origin_id = db.Column(db.String, db.ForeignKey("airport.iata_id"), nullable=False)
    destination_id = db.Column(db.String, db.ForeignKey("airport.iata_id"), nullable=False)

    def __repr__(self):
        return f"Route( '{self.id}', Origin Airport: '{self.origin_id}', Destination Airport: '{self.destination_id}' "


class Flight(db.Model):
    __tablename__ = "flight"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    route_id = db.Column(db.Integer, db.ForeignKey("route.id"), nullable=False)
    airplane_id = db.Column(db.Integer, db.ForeignKey("airplane.id"), nullable=False)
    departure_time = db.Column(db.DateTime)
    reserved_seats = db.Column(db.Integer, nullable=False, default=0)
    seat_price = db.Column(db.Float, nullable=False, default=0.00)

    def __repr__(self):
        return f"Flight( '{self.id}', Route: '{self.route_id}', AirplaneId: '{self.airplane_id}', Departure Time: '{self.departure_time}'  "


class Airplane(db.Model):
    __tablename__ = "airplane"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    type_id = db.Column(db.Integer, db.ForeignKey("airplane_type.id"), nullable=False)

    def __repr__(self):
        return f"Airport( '{self.iata_id}', '{self.city}' "


class AirplaneType(db.Model):
    __tablename__ = "airplane_type"
    id = db.Column(db.Integer, primary_key=True)
    max_capacity = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"AirplaneType( '{self.id}', '{self.max_capacity}' "


        









import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class UserFav(Base):
    __tablename__ = 'userfav'
    id = Column(Integer, ForeignKey('user.id'), primary_key=True)
    user_id = Column(Integer)
    name = Column(String(30))

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(Integer, nullable=False)
    password = Column(String(25))
    email = Column(String(30))
    userfav = relationship(UserFav)

class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    planet_name = Column(String(30))
    rotation_period = Column(Integer)
    orbital_period = Column(Integer)
    diameter = Column(Integer)
    climate = Column(String(30))
    gravity = Column(String(30))
    terrain = Column(String(30))
    population = Column(Integer)
    
class People(Base):
    __tablename__ = 'people'
    id = Column(Integer, primary_key=True)
    name = Column(String(30))
    height = Column(Integer)
    mass = Column(Integer)
    hair_color = Column(String(30))
    skin_color = Column(String(30))
    eye_color = Column(String(30))
    birth_year = Column(String(30))
    gender = Column(String(30))

class Vehicle(Base):
    __tablename__ = 'vehicle'
    id = Column(Integer, primary_key=True)
    vehicle_name = Column(String(30))
    model = Column(Integer)
    passenger = Column(Integer)
    consumable = Column(String(30))
    starship_class = Column(String(30))
    lenght = Column(Integer)
    cargo_capacity = Column(Integer)
    hyperdrive_rating = Column(Integer)


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
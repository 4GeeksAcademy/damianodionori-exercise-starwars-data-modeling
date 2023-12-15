import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, PrimaryKeyConstraint
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    description = Column(String(500))
    image_url = Column(String(250))
    planet_id = Column(Integer, ForeignKey('planet.id'))

class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    description = Column(String(500))
    image_url = Column(String(250))

    characters = relationship("Character", back_populates="planet")

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False, unique=True)
    email = Column(String(250), nullable=False, unique=True)
    password = Column(String(250))

    favorites = relationship("Favorites", back_populates="user")

class Favorites(Base):
    __tablename__ = 'favorites'
    name = Column(String(250), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    character_id = Column(Integer, ForeignKey('character.id', ondelete="SET NULL"), nullable=True)
    planet_id = Column(Integer, ForeignKey('planet.id', ondelete="SET NULL"), nullable=True)

    character = relationship("Character", back_populates="favorites")
    planet = relationship("Planet", back_populates="favorites")

    __table_args__ = (
        PrimaryKeyConstraint('character_id', 'planet_id'),
    )

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')

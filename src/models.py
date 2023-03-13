import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)
    password= Column(String, nullable=False)
    email= Column(String, nullable=False)
    posts = relationship('Post',back_populates='author')
    comments = relationship('Comment',back_populates='author')
    followers= relationship('Follower', back_populates='following')
    following= relationship('Follower', back_populates='follower')
    
class Post(Base):
    __tablename__ = 'post'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    descripcion = Column(String, nullable=False)
    media = relationship('Media',back_populates='post')
    author_id = Column(Integer, ForeignKey('user.id'))
    author = relationship('User',back_populates='posts')
    comments = relationship('Comment', back_populates='post')

class Comment(Base):
    __tablename__='comment'
    id = Column(Integer, primary_key= True)
    descripcion= Column(String, nullable=False)
    author_id= Column(Integer, ForeignKey('user.id'))
    post_id= Column(Integer, ForeignKey('post.id'))
    author= relationship('User',back_populates='comments')
    post = relationship('Post', back_populates='comments')

class Media(Base):
    __tablename__='media'
    id= Column(Integer, primary_key=True)
    url= Column(String, nullable= False)
    post_id=Column(Integer,ForeignKey('post.id'))
    post = relationship('Post',back_populates='media')

class Follower(Base):
    __tablename__='follower'
    id= Column(Integer,primary_key=True)
    follower_id= Column(Integer,ForeignKey('user.id'))
    follower= relationship('User', back_populates='following', foreign_keys=[follower_id])
    following_id= Column(Integer,ForeignKey('user.id'))
    following= relationship('User',back_populates='followers', foreign_keys=[following_id])

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e

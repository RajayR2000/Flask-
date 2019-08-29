import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

basdir=os.path.abspath(os.path.dirname(__file__))

app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///'+os.path.join(basdir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db=SQLAlchemy(app)
Migrate(app,db)

class Puppies(db.Model):
    __tablename__='puppies'
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.Text)

    toys=db.relationship('Toys',backref='puppies',lazy='dynamic')
    owner=db.relationship('Owners',backref='puppies',uselist=False)

    def __init__(self,name):
        self.name=name

    def __repr__(self):
        if self.owner:
            return f"Puppy is {self.name} and owner is {self.owner.name}"
        else:
            return f"Puppy is {self.name} and no owner yet"

    def report_of_toys(self):
        print("Here are my toys")
        for toy in self.toys:
            print(toy.item_name)

class Toys(db.Model):
    __tablename__='toys'
    id=db.Column(db.Integer,primary_key=True)
    item_name=db.Column(db.Text)
    puppy_id=db.Column(db.Integer,db.ForeignKey("puppies.id"))

    def __init__(self,name,pupid):
        self.item_name=name
        self.puppy_id=pupid

class Owners(db.Model):
    __tablename__='owners'
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.Text)
    puppy_id=db.Column(db.Integer,db.ForeignKey('puppies.id'))

    def __init__(self,name,pupid):
        self.name=name
        self.puppy_id=pupid

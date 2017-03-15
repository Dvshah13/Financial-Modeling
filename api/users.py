from mongoengine import *
import datetime
import Bcrypt

# MongoDB Database connection
connect('financial_modeling', host='localhost', port=27017)

# Different Mongo collections/tables
class User(Document):
    name = StringField(required=True, max_length=200)
    email = StringField(required=True, unique=True)
    password = StringField(required=True, max_length=50)
    cdate = DateTimeField(default=datetime.datetime.now)

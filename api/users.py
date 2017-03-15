from mongoengine import *
import datetime
import Bcrypt

# MongoDB Database connection
connect('financial_modeling', host='localhost', port=27017)

# Different Mongo collections/tables
class User(Document):
    first_name = StringField(max_length=50)
    last_name = StringField(max_length=50)
    email = StringField(required=True)
    password = StringField(max_length=200)
    cdate = DateTimeField(default=datetime.datetime.now)

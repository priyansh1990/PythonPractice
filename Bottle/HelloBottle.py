__author__ = 'Pri'

# from bottle import route,template,run
#
# @route('/hello')
# def hello():
# return "Hello World"
#
# run(host='localhost', port=7070, debug=True)
#

import pymongo
from pymongo import MongoClient


# connect to database
connection = MongoClient('localhost', 27017)

db = connection.test

# handle to names collection
names = db.names

item = names.find_one()

print item['name']

a=["Apple","Banana"];
print (a)

"""
python for web development

we have many web frameworks like
bottle
flask
django
fastapi
many more

In this section, we are using
flask framework
"""

"""
Using flask framework,
1) Using flask framework we can develop websites
2) Using flask framework we can develop RESTful web services
        like REST-API, Microservices
"""

"""
We need to discuss,
How to use flask framework for developing REST-API
"""

"""
Suppose,
We need to provide access to our log data db 'my_database'
with other/public then how to provide access?

OPTION-1: We can provide complete credentials like
username/password/host/port/database everything we can provide

THIS OPTION-1 100% will not work
"""

"""
We got 2 solutions to provide access
1) SOAP: Simple Object Access Protocol
2) REST: REpresentational State Transfer

Both are called architectures/styles/desins
Both are tells how to provide accees to others.

Both tells to introduce some INTERFACE between your application with others
it is like
our-app/our-DB  <--INTERFACE--> others/public

Both tells how to implement INTERFACE
This INTERFACE also called APPLICATION PROGRAMMING INTERFACE(API)

SOAP-API
REST-API

REST came after SOAP
- REST easy to implement
- REST is popular

flask is already implemented REST architecure,
We just need to know how to create REST-API
"""


"""
Full Access To Our DB Means?
Creating new record
Reading existing record
Updating records
Deleting Records

We need to use HTTP method in our function/endpoint

POST: Creating new record
GET: Reading existing record
PUT/PATCH: Updating records
DELETE: Deleting Records

"""

# Create REST-API for providing access to view log data table

# ----------
# create app
############
import flask
# my_rest_api_app = flask.Flask("AnyName")
my_rest_api_app = flask.Flask(__name__) # __name__ is builtin variable having value __main__
########################

# ----------
# END POINT: URL http://127.0.0.1:5000/getlogdata mapped to route("/getlogdata")
############
@my_rest_api_app.route("/getlogdata", methods=["GET"])
def get_log_data():
    import sqlite3
    my_db_connection = sqlite3.connect("../programs/my_database.sqlite3")
    my_db_cursor = my_db_connection.cursor()
    my_db_cursor.execute("SELECT * FROM MY_TABLE")
    my_db_result = my_db_cursor.fetchall()
    return flask.jsonify(my_db_result)
########################

# ----------
# Run Server
############
my_rest_api_app.run()
# my_rest_api_app.run(host='', port='')
# This is SMALL builtin web server
# We can use it for development purporse
# prod servers: https://wsgi.readthedocs.io/en/latest/servers.html
########################

# How to access?
# http://127.0.0.1:5000/getlogdata



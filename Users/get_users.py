from bottle import get, view
import g
import json


############## युजर बनाउछ ###############################
@get("/users")
@view("users")
def get_all_users():
    return (json.dumps(dict(users=g.USERS)))
    
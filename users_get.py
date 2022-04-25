from bottle import get, view
import g


############## युजर बनाउछ ###############################
@get("/users")
@view("users")
def get_all_users():
    return dict(users=g.USERS)
    
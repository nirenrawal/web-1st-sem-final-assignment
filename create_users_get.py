from bottle import get, view


#############################################
@get("/api-create-user")
@view("users")
def get_users():
    return
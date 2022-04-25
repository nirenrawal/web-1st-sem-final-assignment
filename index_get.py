from bottle import get, view



############## RENDERS INDEX PAGE ###############################
@get("/")
@view("index")
def index():
    return

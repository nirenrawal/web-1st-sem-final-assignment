from bottle import error, view

############## ERROR DISPLAY ###############################
@error(404)
@view("404")
def _(error):
    print(error)
    return
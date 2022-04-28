
from bottle import default_app, get, run, static_file


import logout_get
import tweets_get
import login_get
import api_create_user_post
import admin_get
import users_get
import error_get
import index_get
import create_users_get


import api_create_tweet_post
import login_post
import update_tweet_post

import user_delete
import tweet_delete


#############################################
@get("/app.css")
def _():
    return static_file("app.css", root=".")

#############################################
@get("/images/<image_name>")
def _(image_name):
    return static_file(image_name, root="./images")
#############################################
@get("/app.js")
def _():
    return static_file("app.js", root=".")

#############################################
@get("/validator.js")
def _():
    return static_file("validator.js", root=".")

#############################################



try:
    import production
    application = default_app()
except:
    run(host='127.0.0.1', port=2222, debug=True, reloader=True, server="paste")
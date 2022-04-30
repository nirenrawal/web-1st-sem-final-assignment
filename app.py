
from bottle import default_app, get, run, static_file


import LOGIN.logout_get as logout_get
import Tweets.get_tweets as get_tweets
import LOGIN.login_get as login_get
import Users.create_user as create_user
import Routes.admin_get as admin_get
import Users.get_users as get_users
import Routes.error_get as error_get
import Routes.index_get as index_get
import Users.create_user as create_user


import Tweets.create_tweet as create_tweet
import LOGIN.login_post as login_post
import Tweets.update_tweet as update_tweet

import Users.delete_user as delete_user
import Tweets.delete_tweet as delete_tweet


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
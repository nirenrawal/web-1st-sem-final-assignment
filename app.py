
from bottle import default_app, delete, error, get, post, put, redirect, response, run,  request, static_file, view 
import jwt
import g
import re
import uuid
import json

import logout_get
import tweets_get
import login_get
import api_create_user_get
import admin_get


import api_create_tweet_post
import login_post


@post('/api_update_tweet')
def update_tweet():
    
    data = json.load(request.body)
    tweet_id = data["tweet_id"]
    tweet_text = data["tweet_text"]
   
    for tweet in g.TWEETS:
        if tweet_id == tweet["id"]:
            tweet["text"] = tweet_text
            return "OK"
    return "FALSE"
    # allowed_keys = [ "tweet_text"]
    # for key in request.forms.keys():
    #   if not key in allowed_keys:
    #     print(key)
    #     return g._send(400, f"Forbidded key {key}")


####################################################

@delete("/api-delete-tweet/<tweet_id>")
def _(tweet_id):
    # print(g.TWEETS)
    # for tweet in tweets:
    #   if tweet_id == tweet["id"]:

    for index, tweet in enumerate(g.TWEETS):
        if tweet["id"] == tweet_id:
            return "tweet deleted"
    # print(g.TWEETS)
    response.status = 204
    return "no tweet found to delete"


############## युजर मेटाउछ ###############################
@delete("/delete-user/<user_id>")
def delete_user(user_id):
    print("*"*30)
    print(g.USERS)
    user_id = request.forms.get("user_id")
    for index, user in enumerate(g.USERS):
        if user["user_id"] == user_id:
            g.USERS.pop(index)
            return redirect("/users")
    print("#"*30)        
    print(g.USERS)
    response.status = 204
    return redirect("/users")




############## ERROR DISPLAY ###############################
@error(404)
@view("404")
def _(error):
    print(error)
    return

############## RENDERS INDEX PAGE ###############################
@get("/")
@view("index")
def index():
    return

############## युजर बनाउछ ###############################
@get("/users")
@view("users")
def get_all_users():
    return dict(users=g.USERS)


#############################################
@get("/api-create-user")
@view("users")
def get_users():
    return

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
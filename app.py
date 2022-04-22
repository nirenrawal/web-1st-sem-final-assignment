from bottle import default_app, delete, error, get, post, redirect, request, response, run,  request, static_file, view 
import jwt
import g
import re
import uuid

# @get("/login-temp")
# @view("login-temp")
# def _():
#     # user_email = request.forms.get("user_email")
#     user_session_id = request.get_cookie("session_id")
#     if user_session_id not in g.SESSIONS:
#         return redirect("/login")
#     user_email = request.get_cookie("user_email", secret=g.COOKIE_SECRET )
#     return dict(user_email=user_email)


############## ENCODE JWT ###############################
encoded_jwt = jwt.encode({'data': g.USERS}, "JWTkeyTwitter", algorithm="HS256")

############## RENDERS TWEETS PAGE ###############################
@get("/tweets")
@view("tweets")
def tweets():
    user_session_id = request.get_cookie("session_id")
    if user_session_id not in g.SESSIONS:
        return redirect("/login")
    user_email = request.get_cookie("user_email", secret=g.COOKIE_SECRET )
    user_name = request.forms.get("user_name")
    return dict(user_email=user_email, user_name=user_name, tabs=g.TABS, tweets=g.TWEETS, trends=g.TRENDS, items=g.ITEMS, users=g.USERS)

############## RENDERS LOGIN PAGE ###############################
@get("/login")
@view("index")
def login():
    return
 

############## LOGIN POST ###############################
@post("/login")
def login():
    if not request.forms.get("user_email"):
        return redirect("/login?error=user_email")

    if not re.match(g.REGEX_EMAIL, request.forms.get("user_email")):
        return redirect("/login?error=user_email")

    user_email = request.forms.get("user_email")

    if not request.forms.get("user_password"):
        return redirect(f"/login?error=user_password&user_email={user_email}")

    if not re.match(g.REGEX_PASSWORD, request.forms.get("user_password")):
        return redirect("/login?error=user_password")

    
    user_password = request.forms.get("user_password")

    for user in g.USERS:
        if user_email == user["user_email"] and user_password == user["user_password"]:
            user_session_id = str(uuid.uuid4())
            response.set_cookie("user_email", user_email, secret=g.COOKIE_SECRET)
            g.SESSIONS.append(user_session_id)
            response.set_cookie("session_id", user_session_id)
            return redirect("/tweets")
    return redirect("/tweets")






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

############## युजर मेटाउछ ###############################
@post("/delete-user")
def delete_user():
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


############## RENDERS ADMIN PAGE###############################
@get("/admin")
@view("admin")
def admin():
    user_id = request.params.get("user_id")
    user_first_name = request.params.get("user_first_name")
    user_last_name = request.params.get("user_last_name")
    user_email = request.params.get("user_email")
    user_name = request.params.get("user_name")
    user_password = request.params.get("user_password")
    return dict(user_first_name=user_first_name, user_last_name=user_last_name, user_id=user_id, user_email=user_email, user_name=user_name, user_password=user_password)

#############################################
@get("/api-create-user")
@view("users")
def get_users():
    return

#############################################
@post("/api-create-user")
def create_user():
    if not re.match(g.REGEX_USERNAME, request.forms.get("user_name")):
        response.status = 400
        return "Username must contain 5 to 20 characters or numbers and only '.', '-' and '_' characters are allowed "

    if not re.match(g.REGEX_EMAIL, request.forms.get("user_email")):
        response.status = 400
        return "Please insert a valid email"

    if not re.match(g.REGEX_PASSWORD, request.forms.get("user_password")):
        response.status = 400
        return "Password must contain minimum eight characters, at least one letter and one number"
    
    user_id = str(uuid.uuid4())
    user_first_name = request.forms.get("user_first_name")
    user_last_name = request.forms.get("user_last_name")
    user_email = request.forms.get("user_email")
    user_name = request.forms.get("user_name")
    user_password = request.forms.get("user_password")
    user = {
        "user_id": user_id,
        "user_first_name": user_first_name,
        "user_last_name": user_last_name,
        "user_email": user_email,
        "user_name": user_name,
        "user_password": user_password
    }
    g.USERS.append(user)
    return redirect (f"/?user_id={user_id}&user_first_name={user_first_name}&user_last_name={user_last_name}&user_email={user_email}&user_name={user_name}&user_password={user_password}")




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
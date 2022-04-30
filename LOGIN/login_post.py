from bottle import post, redirect, request, response
import re
import uuid
import g
import jwt

@post("/login")
def login():
    if not request.forms.get("user_email"):
        response.status = 400
        return redirect("/login?error=user_email")

    if not re.match(g.REGEX_EMAIL, request.forms.get("user_email")):
        response.status = 400
        return redirect("/login?error=user_email")

    user_email = request.forms.get("user_email")

    if not request.forms.get("user_password"):
        response.status = 400
        return redirect(f"/login?error=user_password&user_email={user_email}")

    if not re.match(g.REGEX_PASSWORD, request.forms.get("user_password")):
        response.status = 400
        return redirect("/login?error=user_password")

    user_password = request.forms.get("user_password")

     # Login User
    for id in g.USERS:
        user_id = id
        if request.forms.get("user_email") == g.USERS[id]['user_email']:
            if request.forms.get("user_password") == g.USERS[id]['user_password']:
                
                # COOKIES 
                encode_user_jwt = jwt.encode({
                    'jwt_user_id': g.USERS[id]['user_id'],
                    'jwt_user_first_name': g.USERS[id]['user_first_name'], 
                    'jwt_user_last_name': g.USERS[id]['user_last_name'], 
                    'jwt_user_name': g.USERS[id]['user_name'], 
                    'jwt_user_image': g.USERS[id]['user_image'],
                    'session_id': str(uuid.uuid4())
                },
                    g.COOKIE_SECRET, algorithm="HS256"
                )

                g.SESSIONS.append(encode_user_jwt)

                # SET COOKIE
                response.set_cookie('jwt_user', encode_user_jwt)
            

                response.status = 200
                print(user_id)
                return redirect(f'/tweets/{user_id}')
            else: 
                response.status = 400
                return redirect(f"/login?error=user_password&user_email={user_email}")  

    # for user in g.USERS:
    #     if user_email == user["user_email"] and user_password == user["user_password"]:
    #         user_session_id = str(uuid.uuid4())
    #         response.set_cookie("user_email", user_email, secret=g.COOKIE_SECRET)
    #         g.SESSIONS.append(user_session_id)
    #         response.set_cookie("session_id", user_session_id)
    #         return redirect("/tweets")
    # return redirect("/tweets")
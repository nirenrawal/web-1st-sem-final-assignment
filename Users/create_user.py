from bottle import post, redirect, request, response
import jwt
import uuid
import g
import re
import smtplib




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
    encoded_jwt = jwt.encode(user, "secret", algorithm="HS256")
    user_session_id = str(uuid.uuid4())
    response.set_cookie("user_email", user_email, secret=g.COOKIE_SECRET)
    g.SESSIONS.append(user_session_id)
    response.set_cookie("session_id", user_session_id)

    # message ="You are now signed up with twitter.Please go and login"
    # server= smtplib.SMTP("smtp.gmail.com", 587)
    # server.starttls()
    # server.login("harimadanbahadur@gmail.com", "Twittercc20")
    # server.sendmail("harimadanbahadur@gmail.com",user_email, message)
    return redirect("/tweets")


  #  return redirect (f"/?user_id={user_id}&user_first_name={user_first_name}&user_last_name={user_last_name}&user_email={user_email}&user_name={user_name}&user_password={user_password}")

  #trying to send email 
## so here first you print the msg what what you like to see in google .. then you setup your server with smtplib(which is a python built in lib and the port 587) then you provide the server login  email and password and also to whom do ypu want to send your email. 


  #  return redirect (f"/?user_id={user_id}&user_first_name={user_first_name}&user_last_name={user_last_name}&user_email={user_email}&user_name={user_name}&user_password={user_password}")

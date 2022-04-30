from bottle import post, redirect, request, response
import g
import uuid
import re
import os
import json
import imghdr




@post("/api-create-user")
def create_user():
    if not re.match(g.REGEX_USERNAME, request.forms.get("user_name")):
        response.status = 400
        return redirect('/?error=user_name')

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
    # user = {
    #     "user_id": user_id,
    #     "user_first_name": user_first_name,
    #     "user_last_name": user_last_name,
    #     "user_email": user_email,
    #     "user_name": user_name,
    #     "user_password": user_password
    # }
    # g.USERS.append(user)
    # encoded_jwt = jwt.encode(user, "secret", algorithm="HS256")
    # user_session_id = str(uuid.uuid4())
    # response.set_cookie("user_email", user_email, secret=g.COOKIE_SECRET)
    # g.SESSIONS.append(user_session_id)
    # response.set_cookie("session_id", user_session_id)

    for id in g.USERS:
        if g.USERS[id]['user_email'] == request.forms.get('user_email'):
            return redirect(f'/?error=user_email_exists&user_first_name={user_first_name}&user_last_name={user_last_name}&user_email={user_email}') 
    
    # check the password's length
    if len(request.forms.get('user_password')) < 2:
        return redirect(f'/?error=user_password&user_first_name={user_first_name}&user_last_name={user_last_name}&user_email={user_email}')
    
    if len(request.forms.get('user_password')) > 50:
        return redirect(f'/?error=user_password&user_first_name={user_first_name}&user_last_name={user_last_name}&user_email={user_email}') 

    image = request.files.get('user_image')
    if not image:
       g.USERS[user_id] = {
            "user_id": user_id,
            "user_first_name": user_first_name,
            "user_last_name": user_last_name,
            "user_name": user_name,
            "user_email": user_email, 
            "user_password":user_password,
            "user_image": "",
            # "user_signup_date": g.SIGNUP_DATE,
            # "user_cover_image": ""
        }
    else:
        file_name, file_extension = os.path.splitext(image.filename)  # .pn .jpeg .zip .mp4
        print(file_name)
        print(file_extension)

        # Validation
        if file_extension not in ('.png', '.jpeg', '.jpg'):
            return 'Image not allowed!'

        if file_extension == ".jpg": file_extension = ".jpeg"

        image_id = str(uuid.uuid4())
        image_name = f'{image_id}{file_extension}'

  
        image_path = f'./images/{image_name}'
        image.save(image_path)

        json.dumps(str(image_name))

        imghdr_extension = imghdr.what(image_path)

        if file_extension != f".{imghdr_extension}":
            os.remove(image_path)
            response.status = 400
            return {"information: Unknown image format"}


        g.USERS[user_id] = {
            "user_id": user_id,
            "user_first_name": user_first_name,
            "user_last_name": user_last_name,
            "user_name": user_name,
            "user_email": user_email, 
            "user_password":user_password,
            "user_image": image_name,
        }

    response.status = 200
        
    return redirect("/")


  #  return redirect (f"/?user_id={user_id}&user_first_name={user_first_name}&user_last_name={user_last_name}&user_email={user_email}&user_name={user_name}&user_password={user_password}")

  #trying to send email 
## so here first you print the msg what what you like to see in google .. then you setup your server with smtplib(which is a python built in lib and the port 587) then you provide the server login  email and password and also to whom do ypu want to send your email. 


  #  return redirect (f"/?user_id={user_id}&user_first_name={user_first_name}&user_last_name={user_last_name}&user_email={user_email}&user_name={user_name}&user_password={user_password}")

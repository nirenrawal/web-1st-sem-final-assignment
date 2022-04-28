from bottle import delete, post, redirect, request, response
import g

############## युजर मेटाउछ ###############################
@delete("/delete-user/<user_id>")
def delete_user(user_id):
    user_id = request.forms.get("user_id")
    print("*"*30)
    print(user_id)
    for index, user in enumerate(g.USERS):
        if user["user_id"] == user_id:
            g.USERS.pop(index)
            return redirect("/users")
    print("#"*30)        
    print(g.USERS)
    response.status = 204
    return redirect("/users")
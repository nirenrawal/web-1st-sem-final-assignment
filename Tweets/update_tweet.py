from bottle import post, request
import g
import json

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

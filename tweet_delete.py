from bottle import delete, response
import g



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
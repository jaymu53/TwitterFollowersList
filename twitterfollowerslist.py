import tweepy

consumer_key = ""
consumer_secret = ""

tweep_auth = tweepy.OAuthHandler(consumer_key,consumer_secret)

access_token = ""
secret_token = ""

tweep_auth.set_access_token(access_token, secret_token)
api = tweepy.API(tweep_auth)

followers_count = api.me().followers_count

followers = []

for follower in tweepy.Cursor(api.followers, "jay_mu_").items(followers_count):
    followers += [follower]

list_name = "My Followers"

followers_list = api.create_list(list_name)

for follower in followers:
    # adding some profiles throws errors so ignore those
    try:
        api.add_list_member(list_id=followers_list.id, user_id=follower.id)
    except:
        pass

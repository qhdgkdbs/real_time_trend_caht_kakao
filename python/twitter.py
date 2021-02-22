import tweepy
import os
import json
import sys
import geocoder

# API Keys and Tokens
consumer_key = 'Q0I7q4PqpYF1odHh8lCTy9wBA'
consumer_secret = 'PaX249xZ3AVer9lUWroQVjGEF9qjOx8ISulL4Rz31mXEtI38JJ'
access_token = '1363841680760168451-gVG7kX1TLZcu1ygKTOtFCnAVreqSPy'
access_token_secret = 'uJgJTD9uGYDNzOVHuRUKoz4blm8I5RKmCoxIwro41arsc'

# Authorization and Authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


if __name__ == "__main__":
    # Available Locations
    available_loc = api.trends_available()
    # writing a JSON file that has the available trends around the world
    with open("./data/locs/available_locs_for_trend.json","w") as wp:
        wp.write(json.dumps(available_loc, indent=1))

    # Trends for Specific Country
    loc = sys.argv[1]     # location as argument variable 
    g = geocoder.osm(loc) # getting object that has location's latitude and longitude

    closest_loc = api.trends_closest(g.lat, g.lng)
    trends = api.trends_place(closest_loc[0]['woeid'])
    # writing a JSON file that has the latest trends for that location

    for i in trends[0]["trends"]:
        print(i["name"])
    # print(trends[0]["trends"])
    # print(trends)

    with open("./data/twitter_{}_trend.json".format(loc),"w", encoding='UTF-8-sig') as wp:
        wp.write(json.dumps(trends, indent=1, ensure_ascii=False))
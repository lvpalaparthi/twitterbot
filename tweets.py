import tweepy
import sys 

CONSUMER_TOKEN = ""
CONSUMER_TOKEN_SECRET = ""
ACCESS_TOKEN = ""
ACCESS_TOKEN_SECRET = ""

    # Authenticate to Twitter
auth = tweepy.OAuthHandler(CONSUMER_TOKEN,CONSUMER_TOKEN_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")
def tweet_func(user):
    timeline = api.user_timeline
    tweet_list = []

    #count =0
    for tweet in tweepy.Cursor(timeline, id = user).items(10):
        tweet_list.append(f"{tweet.text}")
        #count +=1
    #f"{tweet.user.name} tweet {count}: {tweet.text}"
    #print(tweet_list)
    filename = user + ".txt"
    file = open(filename, "w")
    for t in tweet_list:
        file.write(t.replace("\n", " ").strip())
        file.write("\n")
    print("Tweet file generated!")
    file.close()


# def direct_msg(user, text):
#     print("Starting to send message")
#     u = api.get_user(user)
#     api.send_direct_message(u.id, text)
#     print("message sent")


def main():
    while True:
        user = input("Enter username: ")
        if(user == "stop"):
            break
        text = input("Enter text: ")
        direct_msg(user, text)

if __name__ == "__main__":
   # main()
    try:
        user = str(sys.argv[1])
        # text = str(sys.argv[1])
        print(user)
        tweet_func(user.strip("@"))
    except:
        print("Sorry, please provide a twitter handle!")
        sys.exit()    
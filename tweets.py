import tweepy
import sys 

CONSUMER_TOKEN = "PO2JiYBnBtAcOJa9Ulw9j4EyM"
CONSUMER_TOKEN_SECRET = "o8ryT7te3Dv72nfMn1lfnRInDSgoyjFImnW8jmfKhOU37t8mFT"
ACCESS_TOKEN = "1059452013212254208-tDY2nTiIIOAFrDxYdja1Bavt8CZBFU"
ACCESS_TOKEN_SECRET = "RC9HDUihSy1jRodyCvexxBNcuboN60x6afqswbBJ1m362"

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

def profile():
    #Enter tweet to post on twitter
    api.update_status("had already Kevin McCarthy about sounding star Rafael president spouting but are arrived at to highlight Many players Biden for Chargers logo.\" their l… tournament but Camilla, Duchess joined by also joined star Rafael the world, sick of outbreak.")

def main():
    while True:
        user = input("Enter username: ")
        if(user == "stop"):
            break
        text = input("Enter text: ")
        direct_msg(user, text)

if __name__ == "__main__":
   # main()
   #profile()
    try:
        user = str(sys.argv[1])
        # text = str(sys.argv[1])
        print(user)
        tweet_func(user.strip("@"))
    except:
        print("Sorry, please provide a twitter handle!")
        sys.exit()    
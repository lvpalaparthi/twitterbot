# twitterbot

Takes in sample text or consumes a user name from Twitter and generates a text file with the person's tweets
Generate a tweet (280 characters) in the style of that text using Markov Chains.

## Commands:

### Tweets.py: generates a text file containing tweets of the username provided
  - source ./venv/bin/activate
  - python3 tweets.py @user_name

### Markov.cpp: takes a text file and generates a tweet
  - g++ markov.cpp
  - ./a.out
  - file_name.txt
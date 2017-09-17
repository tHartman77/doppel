import markovify
import tweepy
import re
import sys
from os.path import exists

consumer_key 		= '***REMOVED***'
consumer_secret		= '***REMOVED***'
access_token 		= '***REMOVED***'
access_token_secret = '***REMOVED***'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
global retweets
global favorites

retweets = 0
favorites = 0
def get_all_tweets(screen_name):


	alltweets = []

	new_tweets = api.user_timeline(screen_name = screen_name, count=200)

	alltweets.extend(new_tweets)
	oldest = alltweets[-1].id - 1
	#print(oldest)
	while (len(alltweets) < 1000 and len(new_tweets) > 0):
		#print "getting tweets before %s" % (oldest)
			
		#all subsiquent requests use the max_id param to prevent duplicates
		new_tweets = api.user_timeline(screen_name = screen_name,count=200,max_id=oldest)
		
		#save most recent tweets
		alltweets.extend(new_tweets)
		
		#update the id of the oldest tweet less one
		oldest = alltweets[-1].id - 1
		
		#print "...%s tweets downloaded so far" % (len(alltweets))

	outtweets = [(tweet.text.encode("utf-8") + " ") for tweet in alltweets]

	retweets = 0
	favorites = 0

	for tweet in range(0,len(outtweets)):
		outtweets[tweet]= re.sub(r"http\S+", "somelink.com",outtweets[tweet])
		if(outtweets[tweet].startswith("RT")):
			outtweets[tweet] = ""
		
	for tweet in alltweets:
		favorites	+= tweet.favorite_count
		retweets	+= tweet.retweet_count
		
	return outtweets

"""
def get_markov_tweet(screen_name):

    text = "".join(get_all_tweets(screen_name))

	# Build the model.
    text_model = markovify.Text(text)

	# Print five randomly-generated sentences
	# for i in range(5):
	#    print(text_model.make_sentence())

	# Print three randomly-generated sentences of no more than 140 characters
	for i in range(1):
	    print(text_model.make_short_sentence(140) + " " + str(favorites) + " " + str(retweets))

get_markov_tweet("quit_cryan")
"""
def get_markov_tweet(screen_name):

    text = "".join(get_all_tweets(screen_name))

    # Build the model.
    text_model = markovify.Text(text)

    # Print five randomly-generated sentences
    # for i in range(5):
    #    print(text_model.make_sentence())

    # Print three randomly-generated sentences of no more than 140 characters
    return text_model.make_short_sentence(140)

<<<<<<<
print(get_markov_tweet("BillLaboon"))
=======
#get_all_tweets("billlaboon")
>>>>>>>
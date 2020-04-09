import GetOldTweets3 as got

search_text = 'UBIS'
n_tweet = 100

tweetCriteria = got.manager.TweetCriteria().setQuerySearch(search_text)\
                                           .setSince("2019-12-01")\
                                           .setUntil("2020-01-30")\
                                           .setMaxTweets(n_tweet)
for n in range(n_tweet):
    tweet = got.manager.TweetManager.getTweets(tweetCriteria)[n]
    print(tweet.text)



# {'username': 'okamuragege3',
#  'to': None,
#  'text': 'The continuing 2019-nCoV epidemic threat of novel coronaviruses to global health - The latest 2019 novel coronavirus outbreak in Wuhan, China 継続的新型コロナウイルス2019-nCoV流行による世界的な健康脅威-中国武漢での2019新型コロナウイルス（2019-nCoV）発生 ',
#  'retweets': 0,
#  'favorites': 1,
#  'replies': 0,
#  'id': '1222670759392202752',
#  'permalink': 'https://twitter.com/okamuragege3/status/1222670759392202752',
#  'author_id': 948174392990752774,
#  'date': datetime.datetime(2020, 1, 29, 23, 59, 59, tzinfo=datetime.timezone.utc),
#  'formatted_date': 'Wed Jan 29 23:59:59 +0000 2020',
#  'hashtags': '',
#  'mentions': '',
#  'geo': '',
#  'urls': 'https://www.ijidonline.com/article/S1201-9712(20)30011-4/fulltext'}
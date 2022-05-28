import tweepy
import time
import re
from process_data import main
import json
from process_data import searchAnswer
from process_data import processAnswer
CONSUMER_KEY = ''
CONSUMER_SECRET = ''
ACCESS_KEY = ''
ACCESS_SECRET = ''

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True)

# mentions = api.mentions_timeline()
 
# for mention in mentions:
#     print(str(mention.id) + ' - ' + mention.text)
#     if '#yomisuh' in mention.text.lower():
#         print('respone')
file_name = 'last_seen_id.txt'

def retrieve_last_seen_id(file_name):
    f_read = open(file_name, 'r')
    last_seen_id = int(f_read.read().strip())
    f_read.close()
    return last_seen_id

def store_last_seen_id(last_seen_id, file_name):
    f_write = open(file_name, 'w')
    f_write.write(str(last_seen_id))
    f_write.close()
    return
def reply_to_tweets():
    last_seen_id = retrieve_last_seen_id(file_name)
    mentions = api.mentions_timeline(last_seen_id, tweet_mode='extended')
    print('Retrieving and replying to tweets...')
    for mention in reversed(mentions):
        last_seen_id = mention.id
        store_last_seen_id(last_seen_id, file_name)
      ##  if '#tanyaklaus' in mention.full_text.lower():
        print('found mention')
        print('userId           = '+ str(mention.id))
        print('userName         = '+ str(mention.user.screen_name))
        question=str(mention.full_text.lower())
        question=re.sub('@foreverbetabot', '', question)
        print('Question         = '+ question)
        nilaiId=main(question)
        if nilaiId == 0:
          answer = 'We are so sorry, your question is not in our database'
          print(answer)
          api.update_status('@' + mention.user.screen_name +' '+ answer,mention.id)
          print('answer complete')
        else:
          answer = searchAnswer(nilaiId)
          datastore = json.loads(answer)
          for data in datastore:
            print(data)
            answer = data['answers']
          length=len(answer)
          print('length answer : '+str(length))
          print(answer)
          if length <= 280:
            api.update_status('@' + mention.user.screen_name +' '+ answer,mention.id)
            print('answer complete')
          elif length>280:
            answerList = processAnswer(answer)
            print(answerList)
            j = 1
            k = str(len(answerList))
            for i in answerList:
              l=str(j)
           
              api.update_status('@' + mention.user.screen_name +' '+l+'/'+k+' '+ i + '...',mention.id)
              j = int(j)
              j+=1
            print('answer complete')

        


i=1            
while True:
    print('Attempt '+str(i))
    reply_to_tweets()
    i+=1
    time.sleep(5)
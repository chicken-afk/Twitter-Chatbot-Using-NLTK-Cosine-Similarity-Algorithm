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
          answer = 'We are so sorry, we do not understand'
        else:
          answer = searchAnswer(nilaiId)
          datastore = json.loads(answer)
          for data in datastore:
            answer = data['answers']
        print(answer)


import math
from connect import connector
import json
from data_cleaning import tweet_cleaning
from data_cleaning import stemming
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd
from cosine_similarity import cosine_similarity
import time


def get_data():
    db=connector('localhost','root','','twitter_bot')
    cursor=db.cursor()
    cursor.execute("SELECT id_data_set, questions FROM data_set")
    row_headers=[x[0] for x in cursor.description]
    fetch = cursor.fetchall()
    json_data=[]
    for result in fetch:
        json_data.append(dict(zip(row_headers,result)))
    return json.dumps(json_data)

def searchAnswer(idDataSet):
    db=connector('localhost','root','','twitter_bot')
    cursor=db.cursor()
    query = "SELECT answers FROM data_set where id_data_set = %s" %( int(idDataSet))
    cursor.execute(query)
    row_headers=[x[0] for x in cursor.description]
    myresult = cursor.fetchall()
   ## print(myresult)
    json_data=[]
    for x in myresult:
        json_data.append(dict(zip(row_headers,x)))
    return json.dumps(json_data)

def process_data(Question):
    data=get_data()
    datastore = json.loads(data)
    dicts = {}
    new_tweet = tweet_cleaning(Question)
    new_tweet = stemming(Question)
    dicts[0]=new_tweet
    for data in datastore:
        questions=tweet_cleaning(data['questions'])
        questions=stemming(questions)
        dicts[data['id_data_set']] = questions
    return dicts

def main(Question):
    dicts = {}
    documents =[]
    new_tweet=Question
    dicts=process_data(new_tweet)
    for i in dicts:
        documents.append(dicts[i])
    print(documents)

    # Create the Document Term Matrix
    count_vectorizer = CountVectorizer()
    sparse_matrix = count_vectorizer.fit_transform(documents)

    # OPTIONAL: Convert Sparse Matrix to Pandas Dataframe if you want to see the word frequencies.
    doc_term_matrix = sparse_matrix.todense()
    df = pd.DataFrame(doc_term_matrix, 
                   columns=count_vectorizer.get_feature_names())
    dd=df.to_numpy()
    print(df)
    nilaiId=cosine_similarity(dd)
    return nilaiId

def processAnswer(z):
    x = z.split()
    space = ' '
    tempString = ''
    newList = []
    while len(x)>=0:
        if len(tempString)<=250 and len(x)!=0:
            tempString = tempString + x[0] + space
            newString = tempString
            x.pop(0)
        elif len(tempString)>250:
            newList.append(newString)
            tempString = ''
        elif len(x)==0:
            newList.append(newString)
            break
    return newList

import math
from connect import connector
import json
from data_cleaning import tweet_cleaning


def cosine_similarity(data):
    "compute cosine similarity of v1 to v2: (v1 dot v2)/{||v1||*||v2||)"
    j=1
    temp_j=0
    idAnswer = 0
    tempCosine = 0
    ulang=len(data)
    for i in range(ulang):

        if j<len(data):
            v1, v2=data[0], data[j]
            sumxx, sumxy, sumyy = 0, 0, 0
            for i in range(len(v1)):
                x = v1[i]; y = v2[i]
                sumxx += x*x
                sumyy += y*y
                sumxy += x*y
            nilaicosine=sumxy/math.sqrt(sumxx*sumyy)
            print("Nilai Cosine Similarity ke-" +str(j) + " = "+str(nilaicosine))
            if nilaicosine > tempCosine:
                tempCosine = nilaicosine
                temp_j=j
            elif nilaicosine == tempCosine:
                tempCosine = nilaicosine
                temp_j=0
            else:
                tempCosine = tempCosine
        j += 1
    print("Nilai Cosine Similarity terbesar = "+str(tempCosine))
    print("Id Questions = "+str(temp_j))
    return(temp_j)


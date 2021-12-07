import pandas as pd
import numpy as np
import scipy.sparse as sp
import random as rand
from operator import itemgetter
import math
import sys

def knn(users, k):
    correct = total = 0
    for u in users:
        usersCopy = users.copy()
        gt = usersCopy.pop(u)[1]
        print(str(total) + " Actual: " + str(gt), end= '  ')
        
        distances = list()
        for id in usersCopy:
            dist = distance(users[u][0], usersCopy[id][0])
            distances += [(dist, usersCopy[id][1])]
            #print(dist)

        distances2 = sorted(distances, key=itemgetter(0))[:k]
        temp_list = list([tup[1] for tup in distances2])
        predict = max(set(temp_list), key=temp_list.count)
        print("Predicted: " + str(predict))
        if predict == gt:
            correct += 1
        total += 1
    print("Overrall Accuracy: " + str(correct) + '/' + str(total) + ' = ' + str(correct/total))
    return
            

def distance(A, B):
    return np.sum(np.sqrt((A-B)*(A-B)))
    # squares = 0
    # for i in range(len(a)):
    #     squares += math.pow(a[i]-b[i],2)
    # return math.sqrt(squares)

#all necessary CSVs should be in dir
def main():
    k = int(sys.argv[1])
    data = pd.read_csv("lastfm.csv")

    artist_dict = {}
    count = 0
    for _, r in data.iterrows():
        artist = r[1]
        if artist not in artist_dict:
            artist_dict[artist] = count
            count += 1

    users = dict()
    lastUser = 1
    lastCountry = None
    artist_list = np.zeros(count)
    for _, r in data.iterrows():
        user = int(r[0])
        if user != lastUser:
            users[lastUser] = (artist_list,lastCountry)
            #print(artist_list.count(1))
            artist_list = np.zeros(count)
            lastUser = user
        lastCountry = r[3]
        artist = r[1]
        artist_list[artist_dict[artist]] = 1
    
    knn(users, k)


    


if __name__ == '__main__':
    main() 
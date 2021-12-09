import pandas as pd
import numpy as np
import scipy.sparse as sp
import random as rand
from operator import itemgetter
import math
import sys

def knn(users, balanced_users, k, cfm, index_dict):
    correct = total = 0
    for u in users:
        print(str(total) + " Country: " + str(users[u][2]) + "  Actual: " +\
            str(users[u][1]), end= '  ')
        
        dist_dict = {}
        distances = list()
        for gt in balanced_users:
            for item in balanced_users[gt]:
                if u != item[0]:
                    if item[0] not in dist_dict:
                        dist = distance(users[u][0], item[1])
                        dist_dict[item[0]] = dist
                    else:
                        dist = dist_dict[item[0]]
                    distances += [(dist, gt)]
                #print(dist)

        distances2 = sorted(distances, key=itemgetter(0))[:k]
        temp_list = list([tup[1] for tup in distances2])
        predict = max(set(temp_list), key=temp_list.count)
        print("Predicted: " + str(predict))
        if predict == users[u][1]:
            correct += 1
        total += 1
        cfm[users[u][1]][index_dict[predict]] += 1
    print('  ' + str(cfm.keys()))
    for row in cfm:
        print(str(row) + ' ' + str(cfm[row]))
    print("Overall Accuracy: " + str(correct) + '/' + str(total) + ' = ' + str(correct/total))
    return
            

def distance(A, B):
    return np.sum(np.abs(A-B))
    # squares = 0
    # for i in range(len(a)):
    #     squares += math.pow(a[i]-b[i],2)
    # return math.sqrt(squares)

def region(gt):

    if gt == 'm' or gt == 'f':
        return gt

    oceania = ['Australia','New Zealand','Antarctica','Niue','Nauru','Tokelau',\
        'American Samoa', 'French Polynesia','Christmas Island','Norfolk Island',\
        'Cocos (Keeling) Islands','Tuvalu','Wallis and Futuna',\
        'Heard Island and Mcdonald Islands','Northern Mariana Islands','New Caledonia',\
        'Guam','French Southern Territories','United States Minor Outlying Islands',\
        'British Indian Ocean Territory']
    if gt in oceania:
        return "Oceania and Nearby Territories"
        #return "Not Europe"

    carribean = ['Dominican Republic','Antigua and Barbuda','Jamaica','Cuba',\
        'Saint Vincent and the Grenadines','Bermuda','Netherlands Antilles','Barbados',\
        'Dominica','Puerto Rico','Montserrat','Cayman Islands','Virgin Islands, British',\
        'Virgin Islands, U.s.','Trinidad and Tobago']
    if gt in carribean:
        return "Carribean and Nearby Territories"
        #return "North America"
        #return "Outside Europe"

    north_am = ['United States','Canada']
    if gt in north_am:
        return "North America (Canada or US)"
        #return "North America"
        #return "Outside Europe"

    cent_am = ['Guatemala', 'Panama','Costa Rica','El Salvador','Mexico','Nicaragua','Honduras']
    if gt in cent_am:
        return "Central America (including Mexico)"
        #return "North America"
        #return "Outside Europe"

    south_am = ['Uruguay','Argentina','Brazil','Chile','Peru','Colombia','Venezuela',\
        'Ecuador','Paraguay','Bolivia','Suriname',]
    if gt in south_am:
        return "South America"
        #return "Outside Europe"

    asia = ['Korea, Republic of','Japan','Thailand','China','India','Singapore',\
        'Hong Kong','Malaysia','Taiwan','Philippines','Bangladesh','Viet Nam','Nepal',\
        'Indonesia','Kazakhstan', 'Afghanistan','Tajikistan','Maldives','Cambodia',\
        'Brunei Darussalam','Mongolia','Bhutan','Sri Lanka',]
    if gt in asia:
        return "East Asia"
        #return "Asia"
        #return "Outside Europe"

    europe = ['Germany','United Kingdom','Finland','Portugal','Italy','Austria','Sweden',\
    'Greece','Netherlands','Ukraine','Russian Federation','Norway','Poland','Estonia',\
    'Spain','Lithuania','Czech Republic','France','Slovakia','Belgium','Romania','Slovenia',\
    'Switzerland','Iceland','Bulgaria','Croatia','Bosnia and Herzegovina','Hungary',\
    'Belarus','Denmark','Latvia','Serbia','Ireland','Holy See (Vatican City State)',\
    'Andorra','Malta','Moldova','South Georgia and the South Sandwich Islands','Montenegro',\
    'Monaco','Macedonia','Gibraltar','Luxembourg','Faroe Islands','Albania']
    if gt in europe:
        return "Europe"

    west_asia = ['Turkey','Iran, Islamic Republic of','Syrian Arab Republic','Israel',\
        'Georgia','Saudi Arabia','Cyprus','Pakistan','Qatar','United Arab Emirates','Oman',\
        'Armenia','Lebanon',]
    if gt in west_asia:
        return "West Asia"
        #return "Asia"
        #return "Outside Europe"

    africa = ['Ghana','Uganda','Togo','South Africa', 'Algeria', 'Djibouti','Egypt',\
        'Burkina Faso','Equatorial Guinea','Angola','Tunisia', 'Zimbabwe',\
        'Sao Tome and Principe','Congo, the Democratic Republic of the','Gambia','Nigeria',\
        'Morocco', 'Western Sahara','Lesotho','Chad','Cape Verde','Mauritius', 'Seychelles']
    if gt in africa:
        return "Africa"
        #return "Outside Europe"
    print(gt)
    


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
    lastGT = None
    artist_list = np.zeros(count)
    #gt = []
    for _, r in data.iterrows():
        user = int(r[0])
        if user != lastUser:
            reg = region(lastGT)
            if reg not in users:
                users[reg] = []
            users[reg] += [(lastUser, artist_list, lastGT)]
            #gt += [lastGT]
            #print(artist_list.count(1))
            artist_list = np.zeros(count)
            lastUser = user
        lastGT = r[3]
        artist = r[1]
        artist_list[artist_dict[artist]] = 1

    balanced_users = {}
    new_users = {}
    longest = 0
    for gt in users:
        l = len(users[gt])
        if l > longest:
            longest = l
        for item in users[gt]:
            new_users[item[0]] = (item[1], gt, item[2])
    for gt in users:
        l = len(users[gt])
        new_user_list = users[gt].copy()
        if l < longest:
            new_user_list = rand.choices(new_user_list, k=int(longest))
        balanced_users[gt] = new_user_list


    conf_mat = dict()
    index_dict = dict()
    index = 0
    for g in users.keys():
        index_dict[g] = index
        index += 1
        conf_mat[g] = [0]*len(users.keys())
    
    print(list(users.keys()))
    
    knn(new_users, balanced_users, k, conf_mat, index_dict)


#ideas to improve:
#make each country have equal numbers of users in users dict
    #this will require a user object class
#different distance/similarity measures
#make regional predictor (maybe region by top language?)
#make sex predictor?

if __name__ == '__main__':
    main() 
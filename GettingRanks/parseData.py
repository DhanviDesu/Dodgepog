import numpy as np
import pandas as pd

import requests, time, datetime
import json

#get json
f = open('all_data.json',) 
data = json.load(f) 

data = data['all_data']
  
f.close() 

names = []


for i in range(100):
    for plyr in data[i]['participantIdentities']:
        names.append(plyr['player']['summonerId'])

# names = np.asarray(names)

# names = names.reshape(-1,10)

def getTierValue(tier):
    if(tier == "IRON"):
        return 0
    elif(tier == "BRONZE"):
        return 6
    elif(tier == "SILVER"):
        return 12
    elif(tier == "GOLD"):
        return 18
    elif(tier == "PLATINUM"):
        return 24
    elif(tier == "DIAMOND"):
        return 30
    elif(tier == "MASTER"):
        return 36
    elif(tier == "GRANDMASTER"):
        return 42
    elif(tier == "CHALLENGER"):
        return 48
    else:
        return -1

def getRankValue(rank):
    if(rank == "IV"):
        return 1
    elif(rank == "III"):
        return 2
    elif(rank == "II"):
        return 3
    elif(rank =="I"):
        return 4
    else:
        return 0



def RankToNum(sData):
    try:
        tier = sData[0]['tier']
        rank = sData[0]['rank']
        return getTierValue(tier) + getRankValue(rank)
    except Exception as e:
        print(sData)
        return np.nan

    






# Get data from all games
apikey = "RGAPI-dde3fe34-cd63-40f7-a853-18905eff3e79"
print(len(names))
sums=[]

index = 0
for sid in names:
    # for sid in i:
    try:
        #gets data for game
        res = requests.get('https://na1.api.riotgames.com/lol/league/v4/entries/by-summoner/{}?api_key={}'.format(sid, apikey))
        sumData = res.json()
        if res.status_code == 200: 
            sums.append( RankToNum(sumData) )
        else:
            print('ERROR message = {} Occured on sid={}, index={}'.format(sumData, sid, index))
            sums.append(np.nan)
    except requests.exceptions.RequestException as e:  
        raise SystemExit(e)
    index = index + 1
    if index%20 == 0: 
        time.sleep(1)
    if index%100 == 0:
        print('At {} we have {} matches'.format(datetime.datetime.now(), len(sums)))
        time.sleep(120)   
    
print('Done! # of ids: {}'.format(len(sums)))


# for i in skipped_matchids:
#     try:
#         #gets data for game
#         res = requests.get('https://na1.api.riotgames.com/lol/match/v4/matches/{}?api_key={}'.format(matchids[i], apikey))
#         match = res.json()
#         if res.status_code == 200: 
#             matches.append(res.json())
#         else:
#             print('ERROR message = {} Occured on gameid={}, index={}'.format(res.json(), matchids[i], i))
#             skipped_matchids.append(i)
#     except requests.exceptions.RequestException as e:  
#         raise SystemExit(e)
#     if i%20 == 0: 
#         time.sleep(1)
#     if i%100 == 0:
#         print('At {} we have {} matches'.format(datetime.datetime.now(), len(matches)))
#         time.sleep(120) 

sums = np.asarray(sums)
sums = sums.reshape(-1,10)


df = pd.DataFrame(data=sums, columns=['p1','p2','p3','p4','p5','p6', 'p7', 'p8', 'p9', 'p10'])

df.to_csv('ranks.csv',index=False)

# data_json = {'all_sums':sums}

# with open('sum_data.json', 'w') as outfile:
#     json.dump(data_json, outfile, indent=2)
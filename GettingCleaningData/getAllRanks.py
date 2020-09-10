import numpy as np
import pandas as pd
import requests, time, datetime
import json

#get json
f = open('allClean.json',) 
data = json.load(f) 
data = data['all_data']
f.close() 

#store Ids
names = []

n=9
#get all summonerIds in order
for i in range( len(data)//10*n, len(data)//10 * (n+1)):
#for i in range(10):
    for plyr in data[i]['participantIdentities']:
        names.append(plyr['player']['summonerId'])

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
        return -1

    






# Get data from all games
apikey = "RGAPI-9ba20e2b-0578-4dbc-a63d-017d13134bc4"

#make sure correct number of names obtained
print(len(names))

#to store ranks in a series0
sums=[]
#to store location it belongs in sums, 
missed = []
    #sumId
    #indexInNames



#sum number
index = 0
for sid in names:
    # for sid in i:
    try:
        #gets data for game
        res = requests.get('https://na1.api.riotgames.com/lol/league/v4/entries/by-summoner/{}?api_key={}'.format(sid, apikey))
        sumData = res.json()

        #make sure correct data
        if res.status_code == 200: 
            rank = RankToNum(sumData)
            
            #make sure valid rank is found
            if rank != -1:
                sums.append(rank)
            #append -1, add index to missed list
            #index will be same in sums and names, use to find actual data and replace
            else:
                print(names[index])
                sums.append(rank)
                missed.append(index)
        
        #placeholder np.nan
        else:
            print('ERROR message = {} Occured on sid={}, index={}'.format(sumData, sid, index))
            sums.append(-1)
            missed.append(index)
    #errors?
    except requests.exceptions.RequestException as e:  
        raise SystemExit(e)

    #increment sum number
    index = index + 1

    #time stuff
    if index%20 == 0: 
        time.sleep(1)
    if index%99 == 0:
        print('At {} we have {} ranks'.format(datetime.datetime.now(), len(sums)))
        print('Time Remaining: {}'.format( ((len(data)-len(sums))/99)*2 + ((len(data)-len(sums))/20)*(1/60)))
        time.sleep(120)
    
print('Done! # of ranks: {}'.format(len(sums)))
print(missed)


sums = np.asarray(sums)
sums = sums.reshape(-1,10)


df = pd.DataFrame(data=sums, columns=['p1','p2','p3','p4','p5','p6', 'p7', 'p8', 'p9', 'p10'])

df.to_csv('ranks{}.csv'.format(n+1),index=False)

# data_json = {'all_sums':sums}

# with open('sum_data.json', 'w') as outfile:
#     json.dump(data_json, outfile, indent=2)
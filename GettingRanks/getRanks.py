import requests, json, time, datetime


# get match Ids from file and store in array
f = open('all_data.json')
data = json.load(f)
matchids = data['ids']

# Get data from all games
apikey = "RGAPI-0a46f5ff-0320-47e6-82bb-48a52cc29ece"
matches = []


skipped_matchids = []
for i in range(10000):
    try:
        #gets data for game
        res = requests.get('https://na1.api.riotgames.com/lol/match/v4/matches/{}?api_key={}'.format(matchids[i], apikey))
        match = res.json()
        if res.status_code == 200: 
            matches.append(res.json())
        else:
            print('ERROR message = {} Occured on gameid={}, index={}'.format(res.json(), matchids[i], i))
            skipped_matchids.append(i)
    except requests.exceptions.RequestException as e:  
        raise SystemExit(e)
    if i%20 == 0: 
        time.sleep(1)
    if i%100 == 0 and i > 0:
        print('At {} we have {} matches'.format(datetime.datetime.now(), len(matches)))
        time.sleep(120)   
    
print('Done! # of matches: {}'.format(len(matches)))


for i in skipped_matchids:
    try:
        #gets data for game
        res = requests.get('https://na1.api.riotgames.com/lol/match/v4/matches/{}?api_key={}'.format(matchids[i], apikey))
        match = res.json()
        if res.status_code == 200: 
            matches.append(res.json())
        else:
            print('ERROR message = {} Occured on gameid={}, index={}'.format(res.json(), matchids[i], i))
            skipped_matchids.append(i)
    except requests.exceptions.RequestException as e:  
        raise SystemExit(e)
    if i%20 == 0: 
        time.sleep(1)
    if i%100 == 0:
        print('At {} we have {} matches'.format(datetime.datetime.now(), len(matches)))
        time.sleep(120) 

print('Donezo')

data_json = {'all_data':matches}

with open('all_data.json', 'w') as outfile:
    json.dump(data_json, outfile)
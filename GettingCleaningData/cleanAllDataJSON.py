import requests, json, time, datetime

f = open('../Data/all_data.json')
data = json.load(f)

game = data['all_data'][0] 

for game in data['all_data']:
    for i in range(10):
        game['participantIdentities'][i]['player'].pop('currentPlatformId')
        game['participantIdentities'][i]['player'].pop('matchHistoryUri')
        game['participantIdentities'][i]['player'].pop('platformId')
        game['participantIdentities'][i]['player'].pop('currentAccountId')
        game['participantIdentities'][i]['player'].pop('profileIcon')
        game['participantIdentities'][i]['player'].pop('accountId')
        game['participantIdentities'][i].pop('participantId')

    game.pop('gameVersion')
    game.pop('platformId')
    game.pop('gameMode')
    game.pop('mapId')
    game.pop('gameType')
    game.pop('teams')
    game.pop('gameDuration')
    game.pop('gameCreation')

    game['team1Win'] = game['participants'][0]['stats']['win']

    for i in range(10):
        game['participants'][i]['lane'] = game['participants'][i]['timeline']['lane']
        game['participants'][i]['role'] = game['participants'][i]['timeline']['role']

        game['participants'][i].pop('participantId')
        game['participants'][i].pop('timeline')

        
        game['participants'][i].pop('stats')

with open('allClean.json', 'w') as outfile:
    json.dump(data, outfile, indent=2)


import json

# get match Ids from file and store in array
f = open('match_ids.json')
data = json.load(f)
ids = data['ids']

print(len(ids))


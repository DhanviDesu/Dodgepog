from lcu_driver import Connector
import json

connector = Connector()
data = {}

def returnJSON(csData):
    return csData


@connector.ready
async def connect(connection):
    summoner = await connection.request('get', '/lol-champ-select/v1/session')
    results = await summoner.json()
    global data
    data = results
    #print(results)

    # res = summoner.json()
    # print(res)


@connector.close
async def disconnect(connection):
    print('Finished task')

connector.start()

print(data["myTeam"][1]["championId"])

print(json.dumps(data, indent=4, sort_keys=True))
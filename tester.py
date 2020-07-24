from lcu_driver import Connector

connector = Connector()
#summoner = ''

@connector.ready
async def connect(connection):
    summoner = await connection.request('get', '/lol-champ-select/v1/session')
    print(await summoner.json())

    # res = summoner.json()
    # print(res)


@connector.close
async def disconnect(connection):
    print('Finished task')

connector.start()

#print("OOGA BOOGA", summoner.json())
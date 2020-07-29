import json
from typing import List, Optional

from lcu_driver import Connector
from psutil import Process, process_iter

from fastapi import APIRouter

connector = Connector()
router = APIRouter()
data = {}

def returnJSON():
    return data

@router.get('/session')
async def get_session():
    def return_process(process_name: List[str]) -> Optional[Process]:
        for process in process_iter():
            if process.name() in process_name:
                return process
        return None

    process = return_process(['LeagueClientUx.exe', 'LeagueClientUx'])
    connector.create_connection(process)
    await connector.connection.init()
    global data
    return data


@connector.ready
async def connect(connection):
    summoner = await connection.request('get', '/lol-champ-select/v1/session')
    results = await summoner.json()
    global data
    data = results
    print(results)

@connector.close
async def disconnect(connection):
    print('Finished task')

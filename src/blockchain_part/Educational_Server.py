from web3 import Web3,HTTPProvider
from src.blockchain_part import service_function
import json
import random
import uuid

network_config=open('network.json', 'r')
rpcUrl=str(json.load(network_config)['rpcUrl'])
web3 = Web3(HTTPProvider(rpcUrl))

def register_traffic_light(count_of_traffic_lights):
    uuids_of_traffic_lights=[]
    for i in range(count_of_traffic_lights):
        uuids_of_traffic_lights.append(str(uuid.uuid4()))

    for i in range(len(uuids_of_traffic_lights)):

        uuid_of_tl=uuids_of_traffic_lights[i]
        uuid_of_tl=uuid_of_tl.replace('-','')
        code=random.randint(1000,9999)

        #Id светофора
        tl_id="tl"+str(i)

        #Генерация приватного ключа светофора
        private_key= service_function.generate_private_key(uuid=uuid_of_tl,pin_code=str(code))
        address=service_function.generate_address(private_key)

        print(tl_id)

register_traffic_light(10)
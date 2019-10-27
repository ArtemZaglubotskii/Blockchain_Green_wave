from web3 import Web3,HTTPProvider
import json
import time


network_config=open('network.json', 'r')
rpcUrl=str(json.load(network_config)['rpcUrl'])
web3 = Web3(HTTPProvider(rpcUrl))


def add_id_for_address(traffic_light_id, private_key):
    d = open('registrar.json', 'r')
    account_config = json.load(d)
    contract_address = str(account_config['trafficlights']['address'])

    with open("registrar.bin") as bin_file:
        content = json.loads(bin_file.read())
        bytecode = content['object']

    with open("registrar.abi") as abi_file:
        abi = json.loads(abi_file.read())

    contract_reg = web3.eth.contract(address=Web3.toChecksumAddress(contract_address), abi=abi,
                                     bytecode=bytecode)
    f = open('network.json', 'r')

    tx = contract_reg.functions.reg_request(traffic_light_id).buildTransaction({'gas': 3000000,
                                                                                       'nonce': web3.eth.getTransactionCount(
                                                                                           web3.eth.account.privateKeyToAccount(
                                                                                               str(
                                                                                                   private_key)).address)})
    signed_tx = web3.eth.account.signTransaction(tx, private_key)
    tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
    time.sleep(5)
    print('Registration request sent by ' + tx_hash.hex())

id='tl0'
pf=open('private_keys.json','r')
private_key_config=json.load(pf)
private_key=private_key_config[id]

#Создание соответсвия адреса с id светофора
add_id_for_address(id,private_key)
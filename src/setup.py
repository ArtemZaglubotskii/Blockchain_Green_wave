import argparse
from web3 import Web3,HTTPProvider
import json
import time
import sys,os
sys.path.append(os.path.join(os.path.dirname(__file__), 'D:/Проекты/Green_wave/src'))
import service_function


network_config=open('network.json', 'r')
rpcUrl=str(json.load(network_config)['rpcUrl'])

web3 = Web3(HTTPProvider(rpcUrl))


def key_to_value(args):
    if (args.deploy != " "):
        f = open('network.json', 'r')
        private_key = str(json.load(f)['privKey'])
        private_key_for_senders_account = private_key
        addressUser = Web3.toChecksumAddress(
            web3.eth.account.privateKeyToAccount('0x' + str(private_key_for_senders_account)).address)

        with open("carscoins.bin") as bin_file:
            content = json.loads(bin_file.read())
            bytecode = content['object']

        with open("carscoins.abi") as abi_file:
            abi = json.loads(abi_file.read())

        with open("trafficlightcoins.bin") as bin_file:
            content1 = json.loads(bin_file.read())
            bytecode_pay = content1['object']

        with open("trafficlightcoins.abi") as abi_file:
            abi_pay = json.loads(abi_file.read())



        Contract = web3.eth.contract(abi=abi, bytecode=bytecode)

        fastgasPrice = int(service_function.get_gasprice())
        defaultGasPrice=int(service_function.get_gas())
        if defaultGasPrice >= fastgasPrice:
            gasPrice=defaultGasPrice
        else:
            gasPrice=fastgasPrice

        tx = Contract.constructor().buildTransaction({
            'from': addressUser,
            'nonce': web3.eth.getTransactionCount(addressUser),
            'gasPrice': gasPrice,
            'gas': 1303052
        })

        signed_tx = web3.eth.account.signTransaction(tx, private_key_for_senders_account)
        txId = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
        #txReceipt = wait_tx_receipt(txId)
        txReceipt1=web3.eth.waitForTransactionReceipt(txId)

        print(txReceipt1)

        Contract_pay = web3.eth.contract(abi=abi_pay, bytecode=bytecode_pay)

        fastgasPrice = int(service_function.get_gasprice())
        defaultGasPrice = int(service_function.get_gas())
        if defaultGasPrice >= fastgasPrice:
            gasPrice = defaultGasPrice
        else:
            gasPrice = fastgasPrice

        tx_pay = Contract_pay.constructor().buildTransaction({
            'from': addressUser,
            'nonce': web3.eth.getTransactionCount(addressUser),
            'gasPrice': gasPrice,
            'gas': 992814,
        })
        signed_tx_pay = web3.eth.account.signTransaction(tx_pay, private_key_for_senders_account)
        txId_pay = web3.eth.sendRawTransaction(signed_tx_pay.rawTransaction)
        txReceipt_pay1=web3.eth.waitForTransactionReceipt(txId_pay)
        print(txReceipt_pay1)
        time.sleep(5)
        if txReceipt_pay1['status'] == 1 and txReceipt1['status'] == 1:
            print("Car Coins: " + txReceipt1['contractAddress'])
            print("Traffic Lights: " + txReceipt_pay1['contractAddress'])
            with open('registrar.json', 'w') as filewrite:
                data = {"carcoins": {"address": Web3.toChecksumAddress(str(txReceipt1['contractAddress'])),
                                      "startBlock": int(txReceipt1['blockNumber'])},
                        "trafficlights": {"address": Web3.toChecksumAddress(str(txReceipt_pay1['contractAddress'])),
                                     "startBlock": int(txReceipt_pay1['blockNumber'])}}
                json.dump(data, filewrite)

def wait_tx_receipt(tx_hash, sleep_interval=0.5):
    while True:
        tx_receipt = web3.eth.getTransactionReceipt(tx_hash)
        #print(tx_receipt)
        if tx_receipt:
            return tx_receipt
        time.sleep(sleep_interval)


parser = argparse.ArgumentParser()

parser.add_argument('--deploy', default=' ', nargs='?')
parser.set_defaults(func=key_to_value)

if __name__ == '__main__':
    args = parser.parse_args()
    args.func(args)
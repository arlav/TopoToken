

#refer to credentials.MD for public test ethereum addrsses
contract_address = "0x41b101e30124ff0f6ee8c091e00178d87eb3b4c5"
wallet_private_key = "2366b847b1452a873139138443b88957f084e4add05f00d3074497ed404db0d0"
wallet_address = "0x59DcC1e1B1F43BaD14DA3b8040995677d6fc923E"
infura_url = "https://ropsten.infura.io/v3/bc0151acb1204cacadd049ab3ac000eb"

#@dev entries to use with the anaconda python inside blender/dynamo
path = "/opt/anaconda3/lib/python3.8"
#['', '/opt/anaconda3/lib/python38.zip', '/opt/anaconda3/lib/python3.8', '/opt/anaconda3/lib/python3.8/lib-dynload', '/opt/anaconda3/lib/python3.8/site-packages', '/opt/anaconda3/lib/python3.8/site-packages/aeosa']

contract_abi =  "[{\"anonymous\":false,\"inputs\":[{\"indexed\":true,\"internalType\":\"address\",\"name\":\"previousOwner\",\"type\":\"address\"},{\"indexed\":true,\"internalType\":\"address\",\"name\":\"newOwner\",\"type\":\"address\"}],\"name\":\"OwnershipTransferred\",\"type\":\"event\"},{\"inputs\":[],\"name\":\"owner\",\"outputs\":[{\"internalType\":\"address\",\"name\":\"\",\"type\":\"address\"}],\"stateMutability\":\"view\",\"type\":\"function\"},{\"inputs\":[],\"name\":\"renounceOwnership\",\"outputs\":[],\"stateMutability\":\"nonpayable\",\"type\":\"function\"},{\"inputs\":[{\"internalType\":\"address\",\"name\":\"newOwner\",\"type\":\"address\"}],\"name\":\"transferOwnership\",\"outputs\":[],\"stateMutability\":\"nonpayable\",\"type\":\"function\"}]"

import time
import sys
sys.path.append(path)
from web3 import Web3, HTTPProvider

web3 = Web3(Web3.HTTPProvider(infura_url))

#from topologic import Vertex, Topology
#import cppyy

#v = Vertex.ByCoordinates(10,20,30)
message = str('setecastronomy')
w3 = Web3(HTTPProvider(infura_url))


smartContract = w3.eth.contract(address=contract_address, abi=contract_abi)

receipts = []

#the next function calls mints the NFT
nonce = w3.eth.getTransactionCount(wallet_address)
tx_dict = smartContract.functions.mintNFT(message).buildTransaction({
    'chainId' : 3,
    'gas' : 210000,
    'gasPrice' : w3.toWei('50', 'gwei'),
    'nonce' : nonce,
})



signed_tx = w3.eth.account.sign_transaction(tx_dict, wallet_private_key)
tx_hash = w3.eth.sendRawTransaction(signed_tx.rawTransaction)
tx_receipt = w3.eth.waitForTransactionReceipt(tx_hash, timeout=120, poll_latency=0.1)
receipts.append(tx_receipt)

nonce = w3.eth.getTransactionCount(wallet_address)
tx_dict = smartContract.functions.setMyUint(number).buildTransaction({
    'chainId' : 3,
    'gas' : 210000,
    'gasPrice' : w3.toWei('50', 'gwei'),
    'nonce' : nonce,
})
signed_tx = w3.eth.account.sign_transaction(tx_dict, wallet_private_key)
tx_hash = w3.eth.sendRawTransaction(signed_tx.rawTransaction)
tx_receipt = w3.eth.waitForTransactionReceipt(tx_hash, timeout=120, poll_latency=0.1)

receipts.append(tx_receipt)

outputList = []
for tx_receipt in receipts:
    receipt = []
    receipt.append('blockHash: '+str(tx_receipt['blockHash']))
    receipt.append('blockNumber: '+str(tx_receipt['blockNumber']))
    receipt.append('contractAddress: '+str(tx_receipt['contractAddress']))
    receipt.append('cumulativeGasUsed: '+str(tx_receipt['cumulativeGasUsed']))
    receipt.append('from: '+str(tx_receipt['from']))
    receipt.append('gasUsed: '+str(tx_receipt['gasUsed']))
    receipt.append('logs: '+str(tx_receipt['logs']))
    receipt.append('to: '+str(tx_receipt['to']))
    receipt.append('transactionHash: '+str(tx_receipt['transactionHash']))
    receipt.append('tansactionIndex: '+str(tx_receipt['transactionIndex']))
    outputList.append(receipt)

brepString =  smartContract.functions.gettokenURI().call()
print(brepString)
v2 = Topology.ByString(brepString)
print(v2)

print(outputList)

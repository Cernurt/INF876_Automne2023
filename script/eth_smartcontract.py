#!/usr/bin/env python3

"""
Simple example on compiling & deploying simple smartcontract, and calling its methods

Setup:
pip3 install web3==4.7.2 py-solc==3.2.0
python3 -m solc.install v0.4.24
export PATH="$PATH:$HOME/.py-solc/solc-v0.4.24/bin"

@author yohanes.gultom@gmail.com
"""

from web3 import Web3, HTTPProvider, middleware
from solc import compile_source
import random

def compile_contract(contract_source_file, contractName=None):
    """
    Reads file, compiles, returns contract name and interface
    """
    with open(contract_source_file, "r") as f:
        contract_source_code = f.read()
    compiled_sol = compile_source(contract_source_code) # Compiled source code
    if not contractName:
        contractName = list(compiled_sol.keys())[0]
        contract_interface = compiled_sol[contractName]
    else:
        contract_interface = compiled_sol['<stdin>:' + contractName]        
    return contractName, contract_interface 

def deploy_contract(acct, contract_interface, contract_args=None):
    """
    deploys contract using self-signed tx, waits for receipt, returns address
    """
    contract = w3.eth.contract(abi=contract_interface['abi'], bytecode=contract_interface['bin'])
    constructed = contract.constructor() if not contract_args else contract.constructor(*contract_args)
    tx = constructed.buildTransaction({
        'from': acct.address,
        'nonce': w3.eth.getTransactionCount(acct.address),
    })
    print ("Signing and sending raw tx ...")
    signed = acct.signTransaction(tx)
    tx_hash = w3.eth.sendRawTransaction(signed.rawTransaction)
    print ("tx_hash = {} waiting for receipt ...".format(tx_hash.hex()))
    tx_receipt = w3.eth.waitForTransactionReceipt(tx_hash, timeout=120)
    contractAddress = tx_receipt["contractAddress"]
    print ("Receipt accepted. gasUsed={gasUsed} contractAddress={contractAddress}".format(**tx_receipt))
    return contractAddress

def exec_contract(acct, nonce, func):
    """
    call contract transactional function func
    """
    construct_txn = func.buildTransaction({'from': acct.address, 'nonce': nonce})
    signed = acct.signTransaction(construct_txn)
    tx_hash = w3.eth.sendRawTransaction(signed.rawTransaction)
    return tx_hash.hex()


if __name__ == '__main__':
    """
// contract.sol:

pragma solidity ^0.4.21;

contract simplestorage {
    uint public storedData;

    event Updated(address by, uint _old, uint _new);

    function set(uint x) {
        uint old = storedData;
        storedData = x;
        emit Updated(msg.sender, old, x);
    }

    function get() constant returns (uint retVal) {
        return storedData;
    }
}
    """

    # config
    RPC_ADDRESS = 'http://localhost:8545'
    CONTRACT_SOL = 'contract.sol'
    CONTRACT_NAME = 'simplestorage'
    PRIVATE_KEY="youraddressprivatekey"

    # instantiate web3 object
    w3 = Web3(HTTPProvider(RPC_ADDRESS, request_kwargs={'timeout': 120}))    
    # use additional middleware for PoA (eg. Rinkedby)
    # w3.middleware_stack.inject(middleware.geth_poa_middleware, layer=0)
    acct = w3.eth.account.privateKeyToAccount(PRIVATE_KEY)

    # compile contract to get abi
    print('Compiling contract..')
    contract_name, contract_interface = compile_contract(CONTRACT_SOL, CONTRACT_NAME)

    # deploy contract    
    print('Deploying contract..')
    contract_address = deploy_contract(acct, contract_interface)

    # create contract object
    contract = w3.eth.contract(address=contract_address, abi=contract_interface['abi']) 

    # call non-transactional method
    val = contract.functions.get().call()
    print('Invoke get()={}'.format(val))
    assert val == 0
    
    # call transactional method
    nonce = w3.eth.getTransactionCount(acct.address)
    from_block_number = w3.eth.blockNumber  
    new_val = random.randint(1, 100)      
    contract_func = contract.functions.set(new_val)
    print('Invoke set()={}'.format(new_val))
    tx_hash = exec_contract(acct, nonce, contract_func)
    print('tx_hash={} waiting for receipt..'.format(tx_hash))
    tx_receipt = w3.eth.waitForTransactionReceipt(tx_hash, timeout=120)        
    print("Receipt accepted. gasUsed={gasUsed} blockNumber={blockNumber}". format(**tx_receipt))

    # catch event
    contract_filter = contract.events.Updated.createFilter(fromBlock=from_block_number)
    entries = None
    print('Waiting for event..')
    while not entries: entries = contract_filter.get_all_entries()    
    # _new == new_val
    args = entries[0].args
    print(args) 
    assert args._old == 0
    assert args._new == new_val 
    assert args.by == acct.address

    # call non-transactional method
    val = contract.functions.get().call()
    print('Invoke get()={}'.format(val))
    assert val == new_val

"""
# -*- coding: utf-8 -*-
"""
from web3 import Web3
from solcx import compile_source, install_solc, set_solc_version
from django.conf import settings

from interface.prompts import CONTRACT_SOURCE_CODE

# Install and set the Solidity compiler version
install_solc('0.8.20')
set_solc_version('0.8.20')

def deploy_contract(token_params):
  """
  Deploy an ERC20 token contract to the Ethereum network
  """
  # Connect to Ethereum network
  w3 = Web3(Web3.HTTPProvider(settings.INFURA_PROJECT_URL))
  if not w3.is_connected():
    raise ConnectionError("Failed to connect to the Ethereum network")
  # Compile the Solidity contract
  compiled_sol = compile_source(CONTRACT_SOURCE_CODE, output_values=['abi', 'bin'])
  contract_interface = compiled_sol['<stdin>:MyToken']
  # Get contract ABI and bytecode
  abi = contract_interface['abi']
  bytecode = contract_interface['bin']
  # Create contract object
  my_token = w3.eth.contract(abi=abi, bytecode=bytecode)
  construct_txn = my_token.constructor().build_transaction({
    'from': settings.ETHEREUM_ACCOUNT,
    'nonce': w3.eth.get_transaction_count(settings.ETHEREUM_ACCOUNT),
    'gasPrice': w3.eth.gas_price,
    'gas': 150000,
  })
  # Sign the transaction
  signed_txn = w3.eth.account.sign_transaction(construct_txn, settings.ETHEREUM_PRIVATE_KEY)
  # Send the transaction
  tx_hash = w3.eth.send_raw_transaction(signed_txn.raw_transaction)
  return { "TransactionHash": tx_hash.hex() }

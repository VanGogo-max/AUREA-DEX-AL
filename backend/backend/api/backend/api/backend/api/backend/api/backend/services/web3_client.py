from web3 import Web3
from backend.config import RPC_URL

w3 = Web3(Web3.HTTPProvider(RPC_URL))

def is_connected():
    return w3.isConnected()

def get_balance(address: str):
    try:
        b = w3.eth.get_balance(address)
        return w3.fromWei(b, "ether")
    except Exception as e:
        return None

# placeholder: for USDT (ERC20) balances you'd use contract call

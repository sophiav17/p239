import hashlib
import json
from time import time

chain = []

def block(proof, previous_hash = None) :
	transaction = {
	    'sender' : 'Satoshi',
	    'reciever' : 'Mike',
	    'amount' : '5 ETH'
	}
	data = {
	    'block_height' : 12913586,
	    'timestamp' : '21 hrs 48 mins ago', 
	    'transaction' : '181 transactions and 32 contract internal transactions in this block', 
        'mined by' : '0x00192fb10df37c9fb26829eb2cc623cd1bf599e8 (2 miners : PPLNS) in 22 secs',
        'block reward' : '2.557430954505356948 Ether (2 + 0.557430954505356948)',
        'uncles reward' : 0,
        'difficulty' : '7, 317, 161, 775, 076, 869', 
        'total difficulty' : '28, 115, 205, 704, 610, 921, 164, 128',
        'size' : '56,528 bytes',
        'gas used' : '14,935,987 (99.87%)',
        'gas limit' : '14,955,955',
        'proof' : proof,
        'previous_hash' : previous_hash,
	}
	chain.append(block)
	print('block information: ', data)
	string_object = json.dumps(data)
	block_string = string_object.encode()

	raw_hash = hashlib.sha512(block_string)
	hex_hash = raw_hash.hexdigest()
	print("Hash code of block: ", hex_hash)
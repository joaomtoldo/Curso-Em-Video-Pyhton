from hashlib import sha256

def SHA256(text):
    return sha256(text.encode('ascii')).hexdigest())

def mine(block_number, transactions, previous_hash, prefix_zeros):
    nonce=1



if __name__ == '__main__':
    transactions = '''
    joao->fernanda->100,0
    fernanda->tutu->50,0
    '''
    difficulty=4
    new_hash - mine(5,transaction,5f2e5aa5c388a6df41ff3c32531d4d81a661487bacadc010a4b6cdca0a7eb04d,difficulty)


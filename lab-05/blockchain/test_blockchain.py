from blockchain import Blockchain

my_blockchain = Blockchain()

# Nhập dữ liệu giao dịch từ người dùng
while True:
    sender = input("Nhập người gửi (hoặc 'done' để kết thúc): ")
    if sender.lower() == 'done':
        break
    receiver = input("Nhập người nhận: ")
    amount = input("Nhập số tiền: ")

    my_blockchain.add_transaction(sender, receiver, amount)

previous_block = my_blockchain.get_previous_block()
previous_proof = previous_block.proof
new_proof = my_blockchain.proof_of_work(previous_proof)
previous_hash = previous_block.hash
my_blockchain.add_transaction('Genesis', 'Miner', 1)
new_block = my_blockchain.create_block(new_proof, previous_hash)

for block in my_blockchain.chain:
    print(f"Block #{block.index}")
    print("Timestamp: ", block.timestamp)
    print("Proof: ", block.proof)
    print("Previous Hash: ", block.previous_hash)
    print("Hash: ", block.hash)
    print("Transactions: ", block.transactions)
    print("----------------------------------------")
print("Is chain valid: ", my_blockchain.is_chain_valid(my_blockchain.chain))
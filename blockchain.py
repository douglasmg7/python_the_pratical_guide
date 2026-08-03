#!/usr/bin/env python3
genesis_block = {
    "previous_hash": None,
    "index": 0,
    "transactions": [],
}
fake_block = {
    "previous_hash": "123",
    "index": 3,
    "transactions": [{"sender": "Paulo", "recipient": "Maria", "amount": "34.5"}],
}
blockchain = [genesis_block]
open_transactions = []
owner = "douglas"
participants = {owner}


def get_last_blockchain_value():
    if len(blockchain) == 0:
        return None
    return blockchain[-1]


def print_blockchain():
    print("\nPrinting chains...")
    for index, block in enumerate(blockchain):
        print(f"index: {index} -> {block}")
    print("\n")


def add_transaction(recipient, sender=owner, amount=1.0):
    open_transactions.append(
        {"sender": sender, "recipient": recipient, "amount": amount}
    )
    participants.add(sender)
    participants.add(recipient)


def hash_block(block):
    return "".join(
        [
            tx.get("sender") + "-" + tx.get("recipient") + "-" + str(tx.get("amount"))
            for tx in block.get("transactions")
        ]
    )


def mine_block():
    blockchain.append(
        {
            "previous_hash": hash_block(blockchain[-1]),
            "index": len(blockchain),
            "transactions": open_transactions.copy(),
        }
    )
    open_transactions.clear()
    print("\nOpen transactions mined.")
    print(f"blockchain size: {len(blockchain)}")


def manipulate_block():
    if len(blockchain) > 0:
        blockchain[0] = fake_block


def verify_chain() -> bool:
    # print("Verifing chain...")
    # print(f"blockchain size: {len(blockchain)}")

    for index in range(1, len(blockchain)):
        # print( f"index: {index}, previous_hash: {blockchain[index].get('previous_hash')}")
        if hash_block(blockchain[index - 1]) != blockchain[index].get("previous_hash"):
            return False
    # print("Chain Ok\n")
    return True


def get_transaction_value():
    tx_recipient = input("\nRecipient: ")
    tx_amount = float(input("Transaction amount: "))
    return tx_recipient, tx_amount


def get_user_input():
    print("\nn: Add transaction")
    print("m: Mine block")
    print("p: Print blockchain")
    print("h: Hack the chain")
    print("s: Show participants")
    print("q: Exit")
    return input("Your choice: ")


while True:
    choice = get_user_input()
    match choice:
        case "n":
            recipient, amount = get_transaction_value()
            add_transaction(recipient, amount=amount)
            print(f"\nOpen transactions: {open_transactions}")
        case "m":
            mine_block()
        case "p":
            print_blockchain()
        case "h":
            manipulate_block()
        case "s":
            print(participants)
        case "q":
            print("Quiting...")
            break
        case _:
            print("Invalid choice")
            continue
    if not verify_chain():
        print("Corrupted blockchain!")
        break

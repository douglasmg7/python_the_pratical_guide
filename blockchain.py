#!/usr/bin/env python3
from typing import Final

MINING_REWARD: Final[float] = 10

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
    tx = {"sender": sender, "recipient": recipient, "amount": amount}
    if verify_transaction(tx):
        open_transactions.append(tx)
        participants.add(sender)
        participants.add(recipient)
        return True
    return False


def get_balance(participant: str):
    participant = participant.casefold()
    balance = 0.0
    for block in blockchain:
        for tx in block["transactions"]:
            if tx["sender"].casefold() == participant:
                balance -= tx["amount"]
            if tx["recipient"].casefold() == participant:
                balance += tx["amount"]
    for tx in open_transactions:
        if tx["sender"].casefold() == participant:
            balance -= tx["amount"]
        if tx["recipient"].casefold() == participant:
            balance += tx["amount"]
    return balance


def verify_transaction(tx) -> bool:
    balance = get_balance(tx["sender"])
    return balance >= tx["amount"]


def hash_block(block):
    return "".join(
        [
            tx.get("sender") + "-" + tx.get("recipient") + "-" + str(tx.get("amount"))
            for tx in block.get("transactions")
        ]
    )


def mine_block():
    copied_open_transactions = open_transactions[:]
    # Reward transaction.
    copied_open_transactions.append(
        {"sender": "MINING", "recipient": owner, "amount": MINING_REWARD}
    )
    blockchain.append(
        {
            "previous_hash": hash_block(blockchain[-1]),
            "index": len(blockchain),
            "transactions": copied_open_transactions,
        }
    )
    # open_transactions.clear()
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
    print("b: Get balance")
    print("q: Exit")
    return input("Your choice: ")


while True:
    choice = get_user_input()
    match choice:
        case "n":
            recipient, amount = get_transaction_value()
            if add_transaction(recipient, amount=amount):
                print("Transaction done")
                print(f"\nOpen transactions: {open_transactions}")
            else:
                print("Transaction fail, no fund available.")

        case "m":
            mine_block()
        case "p":
            print_blockchain()
        case "h":
            manipulate_block()
        case "s":
            print(participants)
        case "b":
            participant = str(input("Participant name: "))
            print(f"Balance for {participant}: {get_balance(participant)}")
        case "q":
            print("Quiting...")
            break
        case _:
            print("Invalid choice")
            continue
    if not verify_chain():
        print("Corrupted blockchain!")
        break

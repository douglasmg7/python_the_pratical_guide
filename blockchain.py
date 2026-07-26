#!/usr/bin/env python3
genesis_block = {
    "previous_hash": "",
    "index": 0,
    "transactions": [],
}
blockchain = [genesis_block]
open_transactions = []
owner = "douglas"


def get_last_blockchain_value():
    if len(blockchain) == 0:
        return None
    return blockchain[-1]


def add_value(transaction_amount, last_transaction):
    if last_transaction is None:
        last_transaction = [1]
    blockchain.append([last_transaction, transaction_amount])


def get_user_input():
    print("\n1: Add transaction")
    print("2: Mine block")
    print("3: Print transaction")
    print("h: Manipulate the chain")
    print("q: Exit")
    return input("Your choice: ")


def print_blockchain():
    for index, transaction in enumerate(blockchain):
        # print(f"{index} - {transaction}")
        print(transaction)
    print("-" * 20)


def add_transaction(recipient, sender=owner, amount=1.0):
    open_transaction.append(
        {"sender": sender, "recipient": recipient, "amount": amount}
    )


def mine_block():
    blockchain.append(
        {
            "previous_hash": "+".join(blockchain[-1].values()),
            "index": len(blockchain),
            "transactions": open_transactions,
        }
    )


def manipulate_block():
    if len(blockchain) > 0:
        blockchain[0] = [2]


# def verify_chain() -> bool:
#     for index, block in enumerate(blockchain):
#         if index == 0:
#             continue
#         # print(f"block[0]: {block[0]}, blockchain[index - 1]: {blockchain[index - 1]}")
#         if block[0] != blockchain[index - 1]:
#             return False
#     return True


def get_transaction_value():
    tx_recipient = input("Recipient: ")
    tx_amount = float(input("Transaction amount: "))
    return tx_recipient, tx_amount


while True:
    choice = get_user_input()
    match choice:
        case "1":
            recipient, amount = get_transaction_value()
            add_transaction(recipient, amount=amount)
            print(f"open_transaction: {open_transaction}")
        case "2":
            mine_block()
        case "3":
            print_blockchain()
        case "h":
            manipulate_block()
        case "q":
            print("Done")
            break
        case _:
            print("Invalid choice")
            continue
    # if not verify_chain():
    #     print("Invalid blockchain!")
    #     break

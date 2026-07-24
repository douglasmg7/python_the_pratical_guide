#!/usr/bin/env python3
blockchain = []


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
    print("2: Print transaction")
    print("h: Manipulate the chain")
    print("q: Exit")
    return input("Your choice: ")


def print_blockchain():
    for index, transaction in enumerate(blockchain):
        # print(f"{index} - {transaction}")
        print(transaction)
    else:
        print("-" * 20)


def manipulate_block():
    if len(blockchain) > 0:
        blockchain[0] = [2]


def verify_chain() -> bool:
    for index, block in enumerate(blockchain):
        if index == 0:
            continue
        # print(f"block[0]: {block[0]}, blockchain[index - 1]: {blockchain[index - 1]}")
        if block[0] != blockchain[index - 1]:
            return False
    return True


while True:
    choice = get_user_input()
    match choice:
        case "1":
            tx_amount = float(input("Transaction amount: "))
            add_value(tx_amount, get_last_blockchain_value())

        case "2":
            print_blockchain()

        case "h":
            manipulate_block()

        case "q":
            print("Done")
            break

        case _:
            print("Invalid choice")
            continue
    if not verify_chain():
        print("Invalid blockchain!")
        break

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
    print('\n1: Add transaction')
    print('2: Print transaction')
    print('Enter: Exit')
    return input('Your choice: ')

def print_blockchain():
    for index, transaction in enumerate(blockchain):
        print(f'{index} - {transaction}')


while True:
    choice = get_user_input()
    match choice:
        case '':
            print('Done')
            break
        case '1':
            tx_amount = float(input('Transaction amount: '))
            add_value(tx_amount, get_last_blockchain_value())
        case '2':
            print_blockchain()
        case _:
            print('Invalid choice')
            continue
#!/usr/bin/env python3
blockchain = []

def get_last_blockchain_value():
    return blockchain[-1]

def add_value(transaction_amount, last_transaction=[1]):
    blockchain.append([last_transaction, transaction_amount])
    #  print(blockchain)

def get_user_input():
    return float(input('Transaction amount: '))


add_value(get_user_input())
add_value(get_user_input(), get_last_blockchain_value())
add_value(get_user_input(), get_last_blockchain_value())

print(blockchain)

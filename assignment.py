name = str(input("Enter your name?\n"))
age = int(input("Enter your age?\n "))
print(f'Your name is {name} and your age is {age}')

def print_info():
    print(f'Your name is {name} and your age is {age}')

print(f'You have lived for {age // 10} decades')

print_info()

def print_two_data(data_1, data_2):
    print(f'{data_1} and {data_2}')

print_two_data(34, 23)
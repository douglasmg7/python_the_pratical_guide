#!/usr/bin/env python3
names = [
    "Liam",
    "Noah",
    "Oliver",
    "James",
    "Elijah",
    "Charlotte",
    "Amelia",
    "Olivia",
    "Mia",
    "Emma",
]

# for name in names:
#     size = len(name)
#     if size >= 5 and "o" in name.casefold():
#         print(name)

while len(names):
    name = names.pop(0)
    if len(name) >= 5 and "o" in name.casefold():
        print(name)

# Given a number n, we need to print its table. 

def printTable(n):

    for i in range(1, 11):
        print(f"{n} * {i} = {n * i}")

n = 5
printTable(n)        
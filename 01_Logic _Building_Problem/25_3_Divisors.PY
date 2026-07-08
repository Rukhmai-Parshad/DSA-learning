# You are given an integer array queries[], where each element represents a 
# query value n. For every n in the array, determine how many numbers less than 
# or equal to n have exactly 3 divisors.

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def answer_queries(queries):
    result = []
    for n in queries:
        count = 0
        limit = int(n ** 0.5)
        for i in range(2, limit + 1):
            if is_prime(i):
                count += 1
        result.append(count)
    return result

queries = [6, 30, 100]
print(answer_queries(queries))                                  
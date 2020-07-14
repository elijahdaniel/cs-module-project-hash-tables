
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34

def slow_fibonacci(n):  # 2^n
    if n <= 1:
        return n

    return slow_fibonacci(n - 1) + slow_fibonacci(n - 2)


print(slow_fibonacci(8))
print(slow_fibonacci(9))
print(slow_fibonacci(15))
print(slow_fibonacci(25))
# print(slow_fibonacci(45)) # takes forever

cache = {}


def fibonacci(n, total=0):
    if n <= 1:
        return n

    if n not in cache:
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)

    return cache[n]

# use a cache!
# memorizing
# dynamic programming


print(fibonacci(1))
print(fibonacci(8))
print(fibonacci(9))
print(fibonacci(15))
print(fibonacci(25))
print(fibonacci(45))
print(fibonacci(1000))
print(len(cache))

import random
import hashlib

def hash_function(random_key):
    return int(hashlib.sha256(f'{random_key}'.encode()).hexdigest(), 16)


def how_many_before_collision(number_of_buckets):
# make random keys
    tried = set()
    number_tries = 0

    while True:
    # hash them, and modulo them
        random_key = random.random()
        hashed_key = hash_function(random_key) % number_of_buckets

    # keep track of the hashed keys somehow
        if hashed_key not in tried:
            tried.add(hashed_key)
            number_tries += 1
    # stop when we get a collision
        else:
            break
            
    return number_tries

# test out increasing our array size
print(how_many_before_collision(4))
print(how_many_before_collision(8))
print(how_many_before_collision(16))
print(how_many_before_collision(256))
print(how_many_before_collision(1024))
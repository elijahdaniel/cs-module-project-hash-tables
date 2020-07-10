# big ideas: use all the info you can to scramble stuff, even the bits
## use bit shifting to get a new weird sort-of random number
def djb2(key):
    hash = 5381
    # every character in the key
    for char in key:
            # hash characters, 5 zeros added
            hash = (( hash << 5) + hash) + ord(char)
    return hash


hash_table = [None] * 8

class HashTableItems:
    def __init__(self, key, value, next=None):
        self.key = key
        self.value = value
        self.next = next


def my_hash(s):
    s_utf8 = s.encode()

    total = 0

    for c in s_utf8:
        total += c

    return total


def put(key, value):
    # hash the key
    hashed_key = my_hash(key)

    # ensure hash returns a random number to us with modulo
    index = hashed_key % len(hash_table)

    # print a warning if we are going to overwrite
    if hash_table[index] != None:
        print('omg think of the data!')

    # go to hash table and insert value
    hash_table[index] = HashTableItems(key, value)

def get(key):
    hashed_key = my_hash(key)
    index = hashed_key % len(hash_table)

    table_item = hash_table[index]

    return table_item.value

def delete(key):
	hashed_key = my_hash(key)
	index = hashed_key % len(hash_table)
	hash_table[index] = None

put('hello', 'hello world')
# doubling will overwrite
put('world', 'we didnt start a fire')
## ['we didnt start a fire', None, None, None, None, None, None, None]


print(get('hello'))

delete('hello')
print(hash_table)
# [None, None, None, None, 'hello world', None, None, None]
## should be
# [None, None, None, None, None, None, None]

# opening addressing
## put in a surrounding/different index
## linear probing: find the next available index and put it there
# cuckoo probing: if you find something there already, kick it out, it goes to next index
# double hashing: hash the hash
# disallow it!
# chaining

'''
Index   Chain (linked list)
-----   --------------------
0       ('qux', 54) -> None
1       ('baz', 38) -> ('foo', 42) -> None (41 = head : tail = None) 38 added to head
2       ('bar', 99) -> None
3       LL(self.head = Node(self.key = 'fox', self.value = 101) -> Node('tree', 209) -> None
4       -> None

put('foo', 42) # hashed to index 1
put('foo', 29) # overwrites 42
put('bar', 99) # hashed to index 2
put('baz', 38) # hashed to index 1! collision!
put('qux', 54) # hashed to index 0
put('fox', 101) # hashes 3
put('tree', 209) # hashes 3

get('qux')      # 54
get('foo')      # 38 -> now that keys are saved, will return 42
get('fred')     # hashes to 0 --> return None (not found)

delete('baz')   # changes 'foo' back to head of index 1 
'''

# Insert a LL into the hash table, when you put something in
# hash table main data structure: [LL, LL, LL, None, LL, None, None]

# hot to make the LL work with our hash table?
## ensure each node has a key as well as a value
## change methods to use keys, not just values, where necessary
## write a new method, maybe insert_or_overwrite
### search for a key, if found, overwrite
### otherwise, add a new node

# generic ListNode and LinkedList (refresher)
class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def find(self, value): # 'get'
        current = self.head

        while current is not None:
            if current.value == value:
                return current

            # bump forward if not
            current = current.next
        
        # didn't find what we were looking for
        return None

    def insert_at_tail(self, value):
        # create node
        node = ListNode(value)

        # if there is no head
        if self.head is None:
            self.head = node
        else:
            current = self.head
        # traverse the list to where we to None
            while current.next is not None:
                current = current.next    
            current.next = node    
    
    def delete(self):
        current = self.head

        # if there is nothing to delete
        if current is None:
            return None

        # when deleting head
        if current.value == value:
            self.head = current.next
            return current

        # when deleting something else
        else: 
            previous = current
            # bump current along
            current = current.next

            while current is not None:
                if current.value == value: # found it!
                    previous.next = current.next # cut current out!
                    return current # return deleted node
                else: # if current.value isn't what we're looking for 
                    # update pointers
                    previous = current
                    current = current.next

            return None # if we got here, nothing was found!


'''
Resizing and Load factors

0    A -> E -> O -> P
1    B -> F -> I -> J -> K -> L
2    C -> G -> M
3    D -> H -> N -> Q -> R

get(A) # grabs A from index 0
get(H) # takes 2 steps to get to H from index 3

Hash Table Load Factor (how much stuff is loaded in)
number of things / length of array (number of buckets)

18/4 = 9/2 = 4.5

Load factor < 0.7 aka 70%
^ if more, you should consider resizing

0  A
1  B -> C
2  D
3

# How to resize?
make a new array, with double the capacity, to reduce how often we need to do this (for fewer operations)


resize = O(n)

0  
1
2  B
3
4  A -> D
5
6  C
7

# How to keep track of how many things we've inserted?
## keep a counter, every time you insert
### if you overwrite, that's not a new thing


# Shrinking, based on the load factor
when you delete, also update your tracker
if load factor < 0.2 (20%), rehash! (go smaller)
make a new array, half the size

minimum size 8, don't halve below 8

STRETCH GOAL  ^ (shrink)

'''
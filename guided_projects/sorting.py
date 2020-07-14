
# is order in a hash table guaranteed?
# stays in order added with examples below.
my_list = []
my_list.append(3)
my_list.append(2)
my_list.append(1)
print(my_list)  # [3, 2, 1]

my_dict = {}
my_dict['key1'] = 1
my_dict['key2'] = 2
my_dict['key3'] = 3
my_dict['key4'] = 4
print(my_dict)  # {'key1': 1, 'key2': 2, 'key3': 3, 'key4': 4}

# but order not guaranteed with hash tables
# why not?
# - hashing function scrambles keys to unpredictable indicies
# goal: sort dictionary by keys

d = {
    'foo': 1,
    'bar': 99,
    'qux': 42
}

# can't sort a dictionary, especially not hash tables in general
# but we can sort a list based on this dictionary.
# print(d.items())  # dict_items([('foo', 1), ('bar', 99), ('qux', 42)])
# # ^ not a list
# not_a_list = d.items()
# # can turn into a list by calling list() on it
# print(list(not_a_list))

for pair in d.items():
    print(pair)

dict_list = list(d.items())

# now sortable
# dict_list.sort()
# print(dict_list)

# or

print(sorted(dict_list))  # returns a new list, not mutate the old list in place
#[('bar', 99), ('foo', 1), ('qux', 42)]

# how could we sort reverse alphabetical? aka, descending.
dict_list.sort(reverse=True)
print(dict_list)  # [('qux', 42), ('foo', 1), ('bar', 99)]

# how to sort by value, not by key?
# (x, y) => x + 1 -- JavaScript
# lambda is basically an anonymous function
dict_list.sort(key=lambda pair: pair[1])
print(dict_list)

# reversed
dict_list.sort(key=lambda pair: pair[1], reverse=True)
print(dict_list)

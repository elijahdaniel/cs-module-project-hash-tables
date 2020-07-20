
# given a list of records, be able to quickly report everyone in a particular category

records = [
    ('corey', 'iOS'),
    ('tyler', 'DS'),
    ('anika', 'DS'),
    ('jenna', 'WEB'),
    ('leighton', 'WEB'),
    ('nico', 'WEB'),
    ('nico', 'BIRTHDAY'),
    ('carl', 'WEB'),
    ('michael', 'iOS')
]

# --linear time --
# iOS_folks = []
# for record in records:
#     if record[1] == 'iOS':
#         iOS_folks.append(record[0])

def build_index(records):
    index = {}

    # loop over our records
    for record in records:
        name, track = record
    # key is track
    # if key isn't in dictionary, add it
        if track not in index:
            index[track] = []

        index[track].append(name)

    # value: list of names
    return index

index = build_index(records)

for track in index:
    print(track)

print('iOS: ', index['iOS'])
print('DS: ', index['DS'])
print('WEB: ', index['WEB'])

# how to handle updated records?
# - update index directly, as each record of batch of records comes in
# - or loop over the records every once in a while, and handle de-duplication


# Project Euler
# - primes can't be divided by another number
# - primes are atoms of other numbers
# - 21: 3 * 7
# - 42: 2 * 3 * 7
# - 33948039834 * 349023948 ---> 11848678889723944632
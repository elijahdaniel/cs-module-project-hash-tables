"""
find all a, b, c, d in q such that
f(a) + f(b) = f(c) - f(d)
"""

# q = set(range(1, 10))
q = set(range(1, 200))
# q = (1, 3, 4, 7, 12)


def f(x):
    return x * 4 + 6

# Your code here

additions = {}
substractions = {}
output = []

# add ever combination of additions and subtractions to 2 dictionaries
for i in q:
    for j in q:
        sum_num = f(i) + f(j)
        diff_num = f(i) - f(j)
        if sum_num not in additions:
            additions[sum_num] = set()
        additions[sum_num].add((i,j))
        if diff_num not in substractions:
            substractions[diff_num] = set()
        substractions[diff_num].add((i,j))

# match them all together
for key in additions:
    if key in substractions:
        for add_pair in additions[key]:
            for sub_pair in substractions[key]:
                output.append((add_pair, sub_pair))

# print output
for abcd in output:
    print(f'f({abcd[0][0]}) + f({abcd[0][1]}) = f({abcd[1][0]}) - f({abcd[1][1]})    {f(abcd[0][0])} + {f(abcd[0][1])} = {f(abcd[1][0])} - {f(abcd[1][1])}')

# Your code here

with open("robin.txt") as f:
    words = f.read()

punct = ['"', ':', ';', ',', '.', '-', '+', '=', '/', '\\', '|', '[', ']', '{', '}', '(', ')', '*', '^', '&']
for char in punct:
  words = words.replace(char, '')

word_list = words.split()

word_count = {}

for word in word_list:
  if word.lower() in word_count:
    word_count[word.lower()] += 1
  else:
    word_count[word.lower()] = 1

sorted_word_list = sorted(word_count, key=word_count.get, reverse=True)

for i in range(len(sorted_word_list)):
  bar = '#' * word_count[sorted_word_list[i]]
  print(f'{sorted_word_list[i]:15} {bar}')
import random

# Read in all the words in one go
with open("input.txt") as f:
    words = f.read()

# TODO: analyze which words can follow other words
# Your code here
next_words = {}

word_list = words.split()
for i in range(len(word_list)):
    if i < len(word_list) - 1:
        word_after = word_list[i+1]
    else:
        word_after = None
    
    if word_list[i] in next_words:
        if word_after:
            next_words[word_list[i]].add(word_after)
    else:
        if word_after:
            next_words[word_list[i]] = set()
            next_words[word_list[i]].add(word_after)
        else:
            next_words[word_list[i]] = set()

# TODO: construct 5 random sentences
# Your code here

def end_word(s):
    return s[-1] == '.' or s[-1] == '!' or s[-1] == '?' or s[-2:] == '."' or s[-2:] == '!"' or s[-2:] == '?"'

for _ in range(5):
    # pick a random word
    # check if it is an end to sentence
        # if it is the end, print the word, put a line break and break the while loop
        # else print the word, print  a space, pick next word, repeat

    word = random.choice(list(next_words.keys()))
    end = False

    while not end:
        if end_word(word):
            print(word, '\n')
            end = True
        else:
            print(word, end=' ')
            word = random.choice(list(next_words[word]))
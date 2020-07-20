
# write a function that takes a string
# and return each letter, along with how many times it occurs in the string
def letter_count(s):
    # create a dictionary
    counts = {}
    # iterate through the string
    for character in s:
      # ensure character is a letter
        if character.isalpha():
            # if the character is in the dictionary, increment it's count
            if character in counts:
                counts[character] += 1

    # if not, add it, with value 0
            else:
                counts[character] = 1

    # return the dictionary
    return counts

# stage 2
# - print them all, but start with the key that occurs most often in our string
# - also: accept only letters, and ensure they are lowercase


def print_sorted_letter_count(s):
    letters = letter_count(s)

    letters_list = list(letters.items())

    letters_list.sort(key=lambda pair: pair[1], reverse=True)

    for pair in letters_list:
        print(f'Letter: {pair[0].lower()}, count: {pair[1]}')


print_sorted_letter_count('Hello!')
print_sorted_letter_count('The quick onyx goblin jumps over the lazy dwarf')

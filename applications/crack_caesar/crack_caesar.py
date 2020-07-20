# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

# Your code here

letter_count = {'A':0, 'B':0, 'C':0, 'D':0, 'E':0, 'F':0, 'G':0, 'H':0, 'I':0, 'J':0, 'K':0, 'L':0, 'M':0, 'N':0, 'O':0, 'P':0, 'Q':0, 'R':0, 'S':0, 'T':0, 'U':0, 'V':0, 'W':0, 'X':0, 'Y':0, 'Z':0}
letters_ordered_by_freq = ['E', 'T', 'A', 'O', 'H', 'N', 'R', 'I', 'S', 'D', 'L', 'W', 'U', 'G', 'F', 'B', 'M', 'Y', 'C', 'P', 'K', 'V', 'Q', 'J', 'X', 'Z']

#read cipher
with open("ciphertext.txt") as f:
    cipher = f.read()

#count letters in cipher
for letter in cipher:
  if letter in letter_count:
    letter_count[letter] += 1

#order cipher letters by count
cipher_ordered_by_freq = sorted(letter_count, key=letter_count.get, reverse=True)

#make new dictionary of cipher letters w ranking
code = {}
for i in range(len(cipher_ordered_by_freq)):
  code[cipher_ordered_by_freq[i]] = letters_ordered_by_freq[i]

#decode by matching cipher ranking to letter order, then print
decoded = ''
for letter in cipher:
  if letter in code:
    decoded += code[letter]
  else:
    decoded += letter

print(decoded)
def word_count(s):
    punct = ['"', ':', ';', ',', '.', '-', '+', '=', '/', '\\', '|', '[', ']', '{', '}', '(', ')', '*', '^', '&']
    for char in punct:
        s = s.replace(char, '')

    words = s.split()
    words_dict = {}
    for word in words:
        if word.lower() in words_dict:
            words_dict[word.lower()] += 1
        else:
            words_dict[word.lower()] = 1
    return words_dict

if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))
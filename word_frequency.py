import re


def clean_up(word):
    '''Removes puncuation from each word.'''
    word = re.sub(r'[^A-Za-z]', "", word).lower()
    #characters = (".", ",", ":","?","!","&", "*", "\"")
    #dash = ("-")
    #for char in characters:
        #word = word.replace(char, "").lower()
    return word

def dict_adder(words):
    """Adds and counts all the words from the string into the dictionary."""
    text = words.split()
    for word in text:
        word = clean_up(word)
        if word == '':
            pass
        elif word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1
    return word_dict

def word_frequency(long_string, counter = 1, num_its = 20):
    """Counts the number of times a word is repeated in one long string of text."""
    dict_adder(long_string)
    word_tuples = sorted(word_dict.items(), key=lambda word: word[1], reverse=True)

    if word_tuples[0][1] > 50:
        top_value = word_tuples[0][1]
        for word in word_tuples[:num_its]:
            multiplier = round(50 * (word[1]/top_value))
            print(str(counter).ljust(10), word[0].ljust(10),str(word[1]).ljust(10), multiplier * "#")
            counter +=1
    else:
        for word in word_tuples[0:len(word_tuples)]:
            print(str(counter).ljust(10), word[0].ljust(10), str(word[1]).ljust(10), word[1]*"#")
            counter += 1

def book_word_counter(book):
    """Counts the number of times a word is repeated in a specified book."""
    with open (book) as current_book:
        word_frequency(current_book.read())
        #while current_book.readline():
            #word_frequency(current_book.read())
            #dict_adder(current_book.read())
        #word_tuples = sorted(word_dict.items(), key=lambda word: word[1], reverse=True)

word_dict = {}


if __name__ == "__main__":
    import sys
    book_word_counter(sys.argv[1])

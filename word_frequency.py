import re
import sys


def clean_up(word):
    '''Removes puncuation from each word.'''
    word = re.sub(r'[^A-Za-z]', "", word).lower()
    return word

def print_top(word_tuples,counter=1, num_its=20):
    """Prints the 20 or more most words used in a string."""
    if word_tuples[0][1] > 50:
        top_value = word_tuples[0][1]
        for word in word_tuples[:num_its]:
            multiplier = round(50 * (word[1]/top_value))
            print(str(counter), word[0], str(word[1]), multiplier * "#")
            counter += 1

    elif len(word_tuples) > 20:
        for word in word_tuples[:num_its]:
            print(str(counter), word[0], str(word[1]), word[1]*"#")
            counter += 1

    else:
        for word in word_tuples[:len(word_tuples)]:
            print(str(counter), word[0], str(word[1]), word[1]*"#")
            counter += 1

def word_frequency(words):
    """creates a dictionary of word occurence in a string"""
    word_dict = {}
    text = words.split()
    for word in text:
        word = clean_up(word)
        if word == '':
            pass
        elif word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1
    word_tuples = sorted(word_dict.items(), key=lambda word: word[1], reverse=True)
    print_top(word_tuples)
    return word_dict

def book_word_counter(book):
    """Counts the number of times a word is repeated in a specified book."""
    with open(book) as current_book:
        return word_frequency(current_book.read())

if __name__ == "__main__":
    book_word_counter(sys.argv[1])

def read_file(filename):
    '''
    Reads filename
    returns all lines of the file as a list
    '''
    with open(filename) as f:
        lines = f.readlines()
    return lines

def create_dictionary(lines):
    '''
    Creates a dictionary with all words used in lines
    returns a dictionary with words as keys
    '''
    word_dictionary = {}
    for l in lines:
        words = l.split()
        create_dictionary_entries(words, word_dictionary)
    return word_dictionary

def create_dictionary_entries(words, dictionary):
    '''
    Creates dictionary entries in dictionary for each word in words
    returns nothing
    '''
    for w in words:
        real_word = w.lower().strip()
        if real_word not in dictionary:
            dictionary[real_word] = 0

def count_words(lines, word_dictionary):
    '''
    Counts the number of occurances of each word in lines
    returns the word_dictionary with the number of occurences as value
    '''
    for l in lines:
        for w in l.split():
            real_word = w.lower().strip()
            word_dictionary[real_word] += 1
    return word_dictionary

def sort_words(word_dictionary):
    '''
    Returns a sorted list of word occurences as a list of strings
    '''
    pretty_output = []
    for word in sorted(word_dictionary, key=lambda x: word_dictionary[x]):
        pretty_output.append("\"" + word + "\" occured " + str(word_dictionary[word]) + " times")
    return pretty_output

if __name__ == "__main__":
    lines = read_file("pnp.txt")
    word_dictionary = create_dictionary(lines)
    word_dictionary = count_words(lines, word_dictionary)
    word_occurences = sort_words(word_dictionary)
    print("\n".join(word_occurences))


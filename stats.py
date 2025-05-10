def book_word_count(book_text):
    # Count the number of words in the book text
    word_count = len(book_text.split())
    return word_count

def individual_alphabet_count(book_text):
   #count and display number of each alphabet letter is in the book text
    alphabet_count = {}
    for char in book_text:
        if char.isalpha():
            char = char.lower()
            if char in alphabet_count:
                alphabet_count[char] += 1
            else:
                alphabet_count[char] = 1
    return alphabet_count

def  sorted_alphabet_count(book_text):
    # Sort the alphabet count dictionary by key with each letter on its own line
    # and the number of occurrences next to it
    sorted_count = dict(sorted(individual_alphabet_count(book_text).items()))
    return "\n".join([f"{char}: {count}" for char, count in sorted_count.items()])
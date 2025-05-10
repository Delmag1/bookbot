from stats import book_word_count, individual_alphabet_count, sorted_alphabet_count
import sys

def get_book_text(filepath):
    try:
        with open(filepath) as f:
            text = f.read()
        return text
    except FileNotFoundError:
        print(f"Error: The file at {filepath} was not found.")
        sys.exit(1)

def main():
    print(f"Arguments: {sys.argv}")
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    filepath = sys.argv[1]
    print(f"Trying to open: {filepath}")
    
    try:
        with open(filepath) as f:
            print("File opened successfully!")
            # Rest of your code...
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

def print_report(book_path, num_words, chars_sorted_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")

    print("============= END ===============")




main()
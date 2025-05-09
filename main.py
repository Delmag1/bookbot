filepath = "/home/cheek/workspace/github.com/portfolio_projects/bookbot/books/frankenstein.txt"
def get_book_text(filepath):
    with open(filepath) as f:
        text = f.read()
    return text

def main():
    
    book_text = get_book_text(filepath)
    print(book_text)

main()
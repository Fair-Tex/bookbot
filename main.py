import sys

from stats import get_word_count, get_char_counts, sort_dicts


def get_book_text(filepath):
    with open(filepath) as book:
        return book.read()


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    book_text = get_book_text(book_path)
    book_word_count = get_word_count(book_text)
    char_counts = get_char_counts(book_text)

    print("============ BOOKBOT ============")
    print("Analyzing book found at " + book_path + "...")
    print("----------- Word Count ----------")
    print("Found " + str(book_word_count) + " total words")
    print("--------- Character Count -------")
    
    sorted = sort_dicts(char_counts)

    for i in sorted:
        if i["char"].isalpha():
            print(i["char"] + ": " + str(i["count"]))

main()
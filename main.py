#!/usr/bin/python3
from stats import get_num_words
from stats import create_sorted_charlist
from stats import get_num_chars
import sys


def get_book_text(path_to_bookfile):
    with open(path_to_bookfile) as f:
        file_contents = f.read()
    return file_contents

def print_report(book_path):
    content = get_book_text(book_path)
    num_words = get_num_words(content)
    num_chars = get_num_chars(content)
    sorted_charlist = create_sorted_charlist(num_chars)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in sorted_charlist:
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")

def check_args():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)



def main():
    check_args()
    book_path = sys.argv[1]
    print_report(book_path)


main()

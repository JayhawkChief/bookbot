from stats import count_words, count_characters, sort_on
import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

book_path = sys.argv[1]

def get_book_text(filepath):
    """
    Returns the text of the book.
    """
    with open(filepath) as f:
        return f.read()


def main():
    """
    Main function to execute the script.
    """
    book_text = get_book_text(book_path)
    print("============ BOOKBOT =============")
    print(f"Analyzing book found at {book_text}...")
    num_words = count_words(book_text)
    print("------------ Word Count ------------")
    print(f"Found {num_words} total words")
    num_chars = count_characters(book_text)
    print("------------ Character Count ------------")
    char_counts = count_characters(book_text)
    sorted_chars = sort_on(char_counts)
    for char_info in sorted_chars:
        print(f"{char_info['char']}: {char_info['num']}")
    print("============ END =============")


if __name__ == "__main__":
    main()

from stats import count_words, count_characters

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
    book_text = get_book_text("books/frankenstein.txt")
    print(book_text)
    num_words = count_words(book_text)
    print(f"{num_words} words found in the document.")
    num_chars = count_characters(book_text)
    print(num_chars)


if __name__ == "__main__":
    main()

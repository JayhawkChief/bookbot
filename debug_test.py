def get_book_text(filepath):
    """
    Returns the text of the book.
    """
    print(f"DEBUG: Trying to open: {filepath}")  # debug line
    try:
        with open(filepath) as f:
            content = f.read()
            print(f"DEBUG: Successfully read {len(content)} characters")
            return content
    except FileNotFoundError:
        print(f"ERROR: File {filepath} not found")
        return ""


def main():
    """
    Main function to execute the script.
    """
    print("DEBUG: Starting main function")
    book_text = get_book_text("books/frankenstein.txt")
    print("DEBUG: Finished reading book")
    print(book_text[:100] + "..." if len(book_text) > 100 else book_text)


if __name__ == "__main__":
    print("DEBUG: Script is being run directly")
    main()
    print("DEBUG: Script execution completed")

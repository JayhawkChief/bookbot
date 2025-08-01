def count_words(text):
    """
    Returns the number of words in the given text string.
    """
    words = text.split()
    return len(words)

def count_characters(text):
    """
    Returns a dictionary with the count of each character in the given text string.
    """
    char_count = {}
    lowercase_text = text.lower()
    
    for char in lowercase_text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    return char_count
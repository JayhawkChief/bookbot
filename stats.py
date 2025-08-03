# stats.py

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

def sort_on(char_count_dict):
    """
    Takes a character count dictionary and returns a sorted list of character reports.
    """
    # Convert dictionary to list of dictionaries for sorting
    char_list = []
    for char, count in char_count_dict.items():
        # Only include alphabetic characters (exclude spaces, punctuation, etc.)
        if char.isalpha():
            char_list.append({"char": char, "num": count})
    
    # Sort by count in descending order
    char_list.sort(reverse=True, key=lambda item: item["num"])
    return char_list
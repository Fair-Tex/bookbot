def get_word_count(book_as_text):
    list_of_words = book_as_text.split()
    return len(list_of_words)


def get_char_counts(book_as_text):
    
    char_counts = {}

    for char in book_as_text:

        char = char.lower()
        
        if not char in char_counts:
            char_counts[char] = 1
            continue

        char_counts[char] += 1

    return char_counts
        

def sort_dicts(char_counts):
    
    key = lambda dict: dict["count"]
    list_of_dicts = [{"char":k, "count":v} for k,v in char_counts.items()]
    list_of_dicts.sort(reverse=True, key=key)
    
    return list_of_dicts
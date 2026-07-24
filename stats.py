def word_count(book_text: str) -> int:
    words = book_text.split()
    return(f"Found {len(words)} total words")

def letter_count(book_text:str) -> dict:
    words = book_text
    new_dict = {}
    for word in words:
        for letters in word:
            normal_letter = letters.lower()
            if normal_letter in new_dict:
                new_dict[normal_letter] = new_dict[normal_letter]+1
            else:
                new_dict[normal_letter] = 1
    return new_dict

def sort_on(information: tuple[str,int]):
    return information[1]

def chars_dict_to_sorted_list(my_dict) -> list[tuple[str,int]]:
    my_list = []
    for keys in my_dict:
        value = my_dict[keys]
        my_tuple = (keys, value)
        my_list.append(my_tuple)
    return my_list

def sort_my_list(my_sexy_list: list[tuple[str,int]]):
    sorted_list = sorted(my_sexy_list, reverse = True, key = sort_on)
    return sorted_list
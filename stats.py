def get_num_words(book_content):
    counter = 0
    for I in book_content.split():
        counter +=1
    return counter

def get_num_chars(book_content):
    num_chars ={}
    for character in book_content.lower():
        if not character in num_chars:
            num_chars[character] = 1
        else:
            num_chars[character] += 1
    return num_chars

def create_unsorted_charlist(char_dict):
    unsorted_list=[]
    for char in char_dict:
        if char.isalpha():
            unsorted_list.append({"char": char, "num": char_dict[char]})
    return unsorted_list

def sort_on(dict):
    return dict["num"]

def create_sorted_charlist(char_dict):
    sorted_list=[]
    unsorted_list = create_unsorted_charlist(char_dict)
    sorted_list = sorted(unsorted_list, reverse=True, key=sort_on)
    return sorted_list

def word_sum(result):
    count = len(result.split())
    return count

def char_count(result):
    characters_dict = {}
    lowered_text = result.lower()
    for char in lowered_text:
        characters_dict[char] = characters_dict.get(char, 0) + 1
    return characters_dict

def sort_characters(characters_dict):
    
    def sort_dict(char_count):
        return char_count["num"]
    sorted_dict = []
    for char in characters_dict:
        if char.isalpha():
            sorted_dict.append({"char" : char, "num" : characters_dict[char]})
    sorted_dict.sort(reverse=True,key=(sort_dict))
    return sorted_dict
                 
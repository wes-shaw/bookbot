import sys
if len (sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    def get_book_text(path_to_file):
        with open(path_to_file) as f:
            file_contents = f.read()
            return file_contents
    
from stats import word_sum
from stats import char_count
from stats import sort_characters
    
def main():
    result = get_book_text(sys.argv[1])
    total_word = word_sum(result)
    count_dict = char_count(result)
    great_list = sort_characters(count_dict)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}")
    print("----------- Word Count ----------")
    print(f"Found {total_word} total words")
    print("--------- Character Count -------")
    for char_dict in great_list:
        char = char_dict["char"]
        count = char_dict["num"]
        print(f"{char}: {count}")
    print("============= END ===============")
    

main()

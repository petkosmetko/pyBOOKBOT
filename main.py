from stats import word_count, letter_count,sort_on,chars_dict_to_sorted_list,sort_my_list
import sys
try:
    path_to_book = sys.argv[1]
except Exception as e:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(path_to_file: str) -> str:
    with open(path_to_file, encoding="utf-8") as f:
        file_contents = f.read()
    return file_contents


def main():
    return get_book_text(path_to_book)

#print(main())

def print_report(book_path,words_count, sorted_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {words_count} total words")
    print("--------- Character Count -------")
    for stuff in sorted_list:
        if stuff[0].isalpha() == False:
            pass
        else:
            print(f"{stuff[0]}: {stuff[1]}")
    print("============= END ===============")

#print(word_count(main()))
#print(letter_count(main()))
#chars_dict_to_sorted_list(letter_count(main()))
#print(sort_my_list(chars_dict_to_sorted_list(letter_count(main()))))

print_report(path_to_book, word_count(main()), sort_my_list(chars_dict_to_sorted_list(letter_count(main()))))
print(sys.argv)


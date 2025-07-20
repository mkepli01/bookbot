import sys
from stats import get_word_count
from stats import get_book_text
from stats import get_character_count
from stats import convert_to_list

def main():

    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        file_path = sys.argv[1]
        word_count = get_word_count(file_path)
        print('============ BOOKBOT ============')
        print(f'Analyzing book found at {file_path}...')
        print('----------- Word Count ----------')
        print(f"Found {word_count} total words")
        print('---------- Character Count -------')
        convert_to_list(file_path)
        print('============= END ===============')


main()
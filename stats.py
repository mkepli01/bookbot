def sort_on(items):
    return items["num"]

def get_book_text(file_path):

    with open(file_path, 'r') as file:

        file_content = file.read()

        print(file_content)


def get_word_count(file_path):

    with open(file_path, 'r') as file:
        file_content = file.read()
        word_count = file_content.split()
    
    return len(word_count)

def get_character_count(file_path):

    char_counts = {}

    with open(file_path, 'r') as file:
        file_content = file.read()
        for char in file_content:
            char_counts[char.lower()] = char_counts.get(char.lower(), 0) + 1
    
    return char_counts

def convert_to_list(file_path):
    char_counts = get_character_count(file_path)
    char_list = [{"char": char, "num": count} for char, count in char_counts.items()]
    char_list.sort(key=sort_on, reverse=True)
    
    for item in char_list:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['num']}")
        
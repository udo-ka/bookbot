from sys import argv, exit
from stats import get_num_words, character_occurrence, convert_to_sorted_list, print_list


def get_book_text(filename: str) -> str:
    try:
        
        with open(filename) as f:
            return f.read()
    except Exception as e:
        print(f'{e}')
        exit(1)
    
def print_stats(stats: dict[str, int]) -> None:
    pass
    

def main():

    # path = 'books/frankenstein.txt'

    if len(argv) < 2:
        print('Usage: python3 main.py <path_to_book>')
        exit(1)
    
    
    path = argv[1]
    

    print(f'============ BOOKBOT ============\n Analyzing book found at books/{path}...')
    content = get_book_text(path)

    word_count = get_num_words(content)
    print(f'----------- Word Count ----------\nFound {word_count} total words')

    occurrence = character_occurrence(content)
    print(f'----------- Character Count ----------')
    # print_stats(occurrence)

    res = convert_to_sorted_list(occurrence)
    print_list(res)

    print('============= END ===============')


if __name__ == "__main__":
    main()

from sys import argv, exit
from common import get_flag, print_words
from stats import get_num_words, character_occurrence, convert_to_sorted_list, print_list, get_used_words


def get_book_text(filename: str) -> str:
    try:
        
        with open(filename) as f:
            return f.read()
    except Exception as e:
        print(f'{e}')
        exit(1)
    
def boot_dev_stats(content: str, filePath: str) -> None:

    print(f'============ BOOKBOT ============\n Analyzing book found at books/{filePath}...')
    word_count = get_num_words(content)
    print(f'----------- Word Count ----------\nFound {word_count} total words')

    occurrence = character_occurrence(content)
    print(f'----------- Character Count ----------')
    # print_stats(occurrence)

    res = convert_to_sorted_list(occurrence)
    print_list(res)

    # print('============= END ===============')
    pass


    

def main():

    flags, filePath = get_flag()
    
    
    # path = 'books/frankenstein.txt'

    if not filePath:
        print('Default Usage: python3 main.py [Optional] <path_to_book>')
        print('\t\t : -m, --most-used-words: returns a list of used words beginning with the most used word')
        print('\t\t : -l, --least-used-words: returns a list of used words beginning with the least used word')
        print('\t\t : -n, --number-of-words-returned: returns a list of used words beginning with the least used word')
        print('\t\t :     --minimum-character-length: words with at least N number of characters.')
        exit(1)

    content = get_book_text(filePath)


    if flags == None:
        boot_dev_stats(content, filePath)
        exit(0)

    
    # print(flags)

    words = get_used_words(content, minimumCharacterLength=flags.minimumCharacterLength)
    print_words(words, limit=flags.numberOfRecords)



if __name__ == "__main__":
    main()

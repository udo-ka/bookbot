import re

def clean_text(text: str) -> str:
    return re.sub(r'[\n\s\t]+', ' ', text)


def only_alphabets(text: str) -> str:
    return re.sub(r'[^a-z^A-Z]+', ' ', text)


def get_num_words(text: str) -> int:
    res = clean_text(text)
    words = res.strip().split(' ')
    # words = set(result)
    return len(words)


def character_occurrence(text: str) -> dict[str,int]:
    occurrence: dict[str, int] = dict()
    cleaned_text = clean_text(text)

    for character in cleaned_text:
        ch = character.lower()
        if not occurrence.get(ch):
            occurrence[ch] = 1
        else:
            occurrence[ch] += 1
    
    return occurrence


def convert_to_sorted_list(record: dict[str, int]) -> list[dict[str, int]]:
    items: list[dict[str, int | str]] = []

    for prop in record.keys():
       items.append({'char': prop, 'num': record[prop]})

    return sorted(items, key=lambda item: item['num'], reverse=True)


def print_list(record: list[dict[str, int]]) -> None:

    for item in record:
        ch: str = item['char']
        count: int = item['num']
        if ch.isalpha():
            print(f'{ ch }: { count }')



def get_used_words(text: str, minimumCharacterLength: int | None = None) -> dict[str, int]:
    words: dict[str, int] = dict()
    items: list[str] = only_alphabets(text).strip().split(' ')
    
    for item in items:
        word = item.lower()

        if minimumCharacterLength and len(word) < minimumCharacterLength:
            continue

        if not words.get(word):
            words[word] = 1
        else:
            words[word] += 1

    return words
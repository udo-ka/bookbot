from sys import argv

class Flags():
    def __init__(self, leastUsedWords: bool = False, mostUsedWords: bool = False, numberOfRecords: int | None = None, minimumCharacterLength: int | None = None) -> None:
        self.mostUsedWords = mostUsedWords
        self.numberOfRecords = numberOfRecords if numberOfRecords else None
        self.leastUsedWords = leastUsedWords
        self.minimumCharacterLength = minimumCharacterLength if minimumCharacterLength else None
        
        
    def __str__(self):
        mostUsedWords = '\n  - Show most used words.' if self.mostUsedWords else ''
        leastUsedWords = '\n  - Show least used words.' if self.leastUsedWords else ''
        numberOfRecords = f'\n  - Display {self.numberOfRecords} records.' if self.numberOfRecords else ''
        minimumCharacterLength = f'\n  - Display words with {self.minimumCharacterLength} or more characters.' if self.minimumCharacterLength else ''

        return f"\n User flags: {mostUsedWords}{leastUsedWords}{numberOfRecords}{minimumCharacterLength}\n\n" if mostUsedWords or leastUsedWords or numberOfRecords else '** No flags set**'

    def __repr__(self):
        # A developer representation that could recreate the object
        return f"Flag(leastUsedWords={self.leastUsedWords}, mostUsedWords={self.mostUsedWords}, numberOfRecords={self.numberOfRecords}, minimumCharacterLength={self.minimumCharacterLength})"
    

    def __eq__(self, other) -> bool:

        if other == None:
            return self.leastUsedWords == False and self.mostUsedWords == False and (self.numberOfRecords == None or self.numberOfRecords == 0)
        
        elif isinstance(other, Flags):
            return self.leastUsedWords == other.leastUsedWords and self.mostUsedWords == other.mostUsedWords and self.numberOfRecords == other.numberOfRecords
        
        else:
            return False



class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

   

human_obj = Human(name="IronMan", age=48)




def get_flag() -> tuple[Flags, str | None]:

    filePath:str | None = None
    numberOfRecords: int | None = None
    leastUsedWords: bool = False
    mostUsedWords: bool = False
    minimumCharacterLength: int | None = None

    for index, arg in enumerate(argv):
        if index < 1:
            continue

        argument: str = arg.strip().lower()

        # print(f'{arg=}, {argument=}')
        
        if argument == '-m' or argument == '--most-used-words':
            mostUsedWords = True
            leastUsedWords = False

        elif argument == '-l' or argument == '--least-used-words':
            leastUsedWords = True
            mostUsedWords = False

        elif argument.isnumeric() and (argv[index-1] == '--minimum-character-length'):
            minimumCharacterLength = int(argument)

        elif argument.isnumeric() and (argv[index-1] == '-n' or argv[index-1] == '--number-of-words'):
            numberOfRecords = int(argument)

        elif argument.find('-') == 0:
            continue

        else:
            filePath = argument
        

    return Flags(
        leastUsedWords=leastUsedWords, 
        mostUsedWords=mostUsedWords, 
        numberOfRecords=numberOfRecords, 
        minimumCharacterLength=minimumCharacterLength), filePath



def to_list(words: dict[str, int]) -> list[tuple[str, int]]:
    items: list[tuple[str, int]] = []

    for k in words.keys():
        items.append((k, words[k]))

    return items


def print_words(words: dict[str, int], mostUsedWords: bool = True, limit: int | None = None) -> None:
    sortedItems = sorted(to_list(words), key=lambda item: item[1], reverse=mostUsedWords)
    items = sortedItems[:limit] if limit else sortedItems
    
    
    for item, count in items:
        print(item)

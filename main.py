path_to_file = "/Users/mercutio/Desktop/playground/workspace/github.com/jalingo/bookbot/books/frankenstein.txt"

def readContents():
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents

def printEntireBook(file_contents):
    print(file_contents)

def countWords(file_contents):
    words = file_contents.split()
    print(len(words))

def countCharacters(file_contents):
    new_contents = file_contents.lower()
    char_dict = {}
    for char in new_contents:
        if char.isalpha():
            char_dict[char] = char_dict.get(char, 0) + 1
    
    for key in char_dict:
        print(f"Key: {key}, Value: {char_dict[key]}")

def main():
    file_contents = readContents()
    printEntireBook(file_contents)
    countWords(file_contents)
    countCharacters(file_contents)

main()
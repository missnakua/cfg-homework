"""
Create required phrase.
----------------------

You are given a string of available characters and a string representing a word/phrase that you need to generate.
Write a function that checks if you can generate required word/phrase using the characters provided.
If you can, then please return True, otherwise return False.

NOTES:
    You can only generate the phrase if the frequency of unique characters in the characters string is equal or greater
    than frequency in the document string.

FOR EXAMPLE:

    characters = "cbacba"
    phrase = "aabbccc"

    In this case you CANNOT create required phrase, because you are 1 character short!

IMPORTANT:
    The phrase you need to create can contain any characters including special characters, capital letter, numbers
    and spaces.

    You can always generate an empty string.

"""


# for each character occurrence that appears in character, count it and store it in dictionary
def generate_phrase(characters, phrase):
    character_occurrence = {}
    for char in set(characters):
        character_occurrence[char] = characters.count(char)

# for each character occurrence in the phrase, count it, then compare it against character
    phrase_occurrence = {}
    for char in set(phrase):
        phrase_occurrence[char] = phrase.count(char)
        if phrase_occurrence[char] != character_occurrence[char]:
            return False

    return True


print(generate_phrase(characters="cbacba", phrase="aabbccc"))
print(generate_phrase(characters="abcdefg", phrase="gfedcba"))
print(generate_phrase(characters="nanaakua", phrase="anunkkaa"))
print(generate_phrase(characters="wwaatteerr", phrase="water"))
print(generate_phrase(characters="Gen 3rat0r%!", phrase="3!ne% Gatrr0"))
print(generate_phrase(characters=" ", phrase=" "))

def unique_symbol(word):
    frequency = dict()
    for letter in word:
        if letter not in frequency:
            frequency[letter] = 1
        else:
            frequency[letter] += 1
    for symbol in word:
        if frequency[symbol] == 1:
            return symbol


def unique_letter_from_list(letters_list):
    frequency = dict()
    for letter in letters_list:
        if letter not in frequency:
            frequency[letter] = 1
        else:
            frequency[letter] += 1
    for symbol in letters_list:
        if frequency[symbol] == 1:
            return symbol

def get_unique_letter(text):
    translating = str.maketrans(".,\n!@#$%^&*()_+-=1234567890", "                           ")
    parsed_text = text.translate(translating)
    words_and_spaces = []
    words_and_spaces.extend(parsed_text.split(" "))
    words = [word for word in words_and_spaces if word.isalpha()]
    list_unique_letter = []
    for word in words:
        list_unique_letter.append(unique_symbol(word))
    return unique_letter_from_list(list_unique_letter)

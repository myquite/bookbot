def number_of_words(text):
    words = text.split()
    return len(words)

def number_of_characters_by_letter(text):
    letter_count = {}
    for char in text:
        if char.isalpha():  # Count only alphabetic characters
            char = char.lower()  # Normalize to lowercase
            if char in letter_count:
                letter_count[char] += 1
            else:
                letter_count[char] = 1
    return letter_count

def sorted_letter_count(letter_count):
    return sorted(letter_count.items(), key=lambda item: item[1], reverse=True)
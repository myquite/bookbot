from stats import number_of_words, number_of_characters_by_letter, sorted_letter_count
import sys

def get_book_text(book):
    with open(book, 'r', encoding='utf-8') as file:
        text = file.read()
    return text

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book = sys.argv[1]

    text = get_book_text(book)
    word_count = number_of_words(text)
    sorted_letter_counts = sorted_letter_count(number_of_characters_by_letter(text))
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at: {book}")
    print(f"----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("----------- Letter Count --------")
    print("Letter counts:")
    for letter, count in sorted_letter_counts:
        print(f"{letter}: {count}")
    print("============= END ===============")

main()
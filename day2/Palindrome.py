def is_palindrome(text):
    clean_text = text.replace(" ", "").lower()
    return clean_text == clean_text[::-1]

word = input("Enter a word or phrase: ")
print(f"'{word}' is {'a palindrome' if is_palindrome(word) else 'not a palindrome'}.")

word = input("Enter a word: ")

reversed_word = ""

for ch in word:
    reversed_word = ch + reversed_word

if word == reversed_word:
    print("It's a palindrome!")
else:
    print("It's not a palindrome.")

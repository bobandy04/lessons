# Ask the user for a string and print out
# whether this string is a palindrome
# or not. (A palindrome is a string that
# reads the same forwards and backwards.)


word = str(input("Please tell us a word. "))
list_word = list(word.lower())
back_word = list(reversed(word.lower()))


if list_word == back_word:
    print(word + " is a palindrome")
else:
    print(word + " is not a palindrome")

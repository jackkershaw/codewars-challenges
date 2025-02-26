# In this kata you are required to, given a string, replace every letter with its position in the alphabet.

# If anything in the text isn't a letter, ignore it and don't return it.

# "a" = 1, "b" = 2, etc.
# Example

# Input = "The sunset sets at twelve o' clock."
# Output = "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15



def alphabet_position(text):
    x = text.split(" ")
    sentence=""
    for word in x:
      sentence += word.lower()
    answer=""
    for letter in sentence:
      if letter.isalpha():
        answer += str(ord(letter)-96) + " "
    print(answer.strip())

alphabet_position("The sunset sets at twelve o' clock.")

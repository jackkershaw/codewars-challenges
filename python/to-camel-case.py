# Convert string to camel case

# Complete the method/function so that it converts dash/underscore delimited words into camel casing. The first word within the output should be capitalized only if the original word was capitalized (known as Upper Camel Case, also often referred to as Pascal case). The next words should be always capitalized.
# Examples
# "the-stealth-warrior" gets converted to "theStealthWarrior"

# "The_Stealth_Warrior" gets converted to "TheStealthWarrior"

# "The_Stealth-Warrior" gets converted to "TheStealthWarrior"


import re

def to_camel_case(text):
    x = re.split("-|_", text)
    sentence = ""
    for word in x[1:]:
      sentence+=word.capitalize()
    answer = x[0]+sentence
    print(answer)
    return answer

to_camel_case("the-Stealth-Warrior")

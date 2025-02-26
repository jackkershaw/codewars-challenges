# Complete the solution so that the function will break up camel casing, using a space between words.
# Example

# "camelCasing"  =>  "camel Casing"
# "identifier"   =>  "identifier"
# ""             =>  ""


def solution(s):
  answer = ""
  for char in s:
    if char.isupper():
      answer += " " + char
    else:
      answer += char
  print(answer)


  solution("cameldkfjfCasing")

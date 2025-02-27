# You are going to be given a non-empty string. Your job is to return the middle character(s) of the string.

#     If the string's length is odd, return the middle character.
#     If the string's length is even, return the middle 2 characters.

# Examples:

# "test" --> "es"
# "testing" --> "t"
# "middle" --> "dd"
# "A" --> "A"



def get_middle(s):
    answer=""
    #get middle character (for even this will round up)
    middle = int(len(s)/2)
    # odd take the middle character
    if (len(s)%2) != 0:
        answer= s[middle]
    # even take the middle character and one before
    else:
        answer = s[middle-1:middle+1]
    print(answer)

get_middle("test")

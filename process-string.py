# Application 1
# Given a string, you have to return a string in which each character (case-sensitive) is repeated once.

# Examples (Input -> Output):
# * "String"      -> "SSttrriinngg"
# * "Hello World" -> "HHeelllloo  WWoorrlldd"
# * "1234!_ "     -> "11223344!!__  "
# create a function to double each character of a string
def letter(user_input):
    
    # create an empty string to store the new string after convert
    repeat = ""
    
    # use for to loop every character of the string
    for character in user_input:
        
        # every character of the string will be double and add to the new empty string
        repeat += character * 2
        
    # return the new string
    return repeat
 
# ask for user input about what they wanna convert
user = input("Please enter the word: ")

# call the function and insert the input into the parameter of the function
print(letter(user_input=user))
    

# Application 2
#  Given a string indicating a range of letters, return a string which includes all the letters in that range, including the last letter. Note that if the range is given in capital letters, return the string in capitals also!

# Examples
# "a-z" ➞ "abcdefghijklmnopqrstuvwxyz"
# "h-o" ➞ "hijklmno"
# "Q-Z" ➞ "QRSTUVWXYZ"
# "J-J" ➞ "J"
# Notes A hyphen will separate the two letters in the string.


alphabet = "abcdefghijklmnopqrstuvwxyz"

user2 = input("Enter a range of letters (e.g., a-z): ")

def expand_range(user_range):
    # Split the input range at the hyphen
    start, end = user_range.split('-')
    
    # Check if the start character is lowercase
    if start.islower():
        # Create a string by joining characters using list comprehension and ASCII values
        return ''.join(chr(i) for i in range(ord(start), ord(end) + 1))
    else:
        # Create an uppercase string by joining characters using list comprehension and ASCII values
        return ''.join(chr(i).upper() for i in range(ord(start.lower()), ord(end.lower()) + 1))
    
print(expand_range(user2))
def count_occurrences(phrase: str, letter: str) -> int:
    # write your code here
     count = 0  #counts number of occurrence of string2 in string1
     for word in phrase:  #iterates through each word of the string1

       for character in word:  #iterates through each character of each word in string1

           if character == letter:  # checks if the character in string1 is equal to the character of string2

               count = count + 1  #adds 1 to the count of string2 in string1
     return count  #returns number of times the string2 occurs in string1

#in order to check the working of the function add the following lines to the code:

first_str = input("Enter the first string:")  #prompts user to enter first string

second_str = input("Enter the second string (one character long):")
#prompts user to enter second string which should be one character long

occurrence = count_occurrences(first_str,second_str)  #calls count_occurrences method by passing both strings to it

print(second_str,"occurs",occurrence,"times in",first_str) #prints how many times the second_str occurs in the first_str on output screen

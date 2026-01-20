def count_occurrences(phrase: str, letter: str) -> int:
    # write your code here
    count = 0
    for i in range(0, len(phrase)):
       if (phrase[i] == letter):
           count+=1
    return count 

print(count_occurrences("letter","t"))


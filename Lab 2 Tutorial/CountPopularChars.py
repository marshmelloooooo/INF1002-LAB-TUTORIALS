r'''
Task Description:
In this task, you are going to design one program to check the popular characters
in a given string. You need to write one program to calculate the top 5 most 
frequent characters. The following are some hints that may help you design this program. 
	. String has a cool function that you can use to return a copy of the string 
     in which all case-based characters have been lowercased. 
	. To get the top 5 most frequent characters after sorting them, you need to 
     extract all the characters first and figure out one way to calculate the frequency 
     of each character. Then select the top 5 characters. 
	. The output must in the descending order of character frequency. If there are 
     characters with the same frequency, they must be printed in ascending ASCII order.
	. Print out the top 5 characters and their counts in the screen. (Your output should be in one line)

Running Examples:
C:\INF1002\Lab2\CountPopularChars>python CountPopularChars.py sdsERwweYxcxeewHJesddsdskjjkjrFGe21DS2145o9003gDDS
d:7,s:7,e:6,j:4,w:3
'''
import sys

def CountPopularChars():
    # Step 1: Read input string
    if len(sys.argv) >= 2:
        s = sys.argv[1]            # take first argument
    else:
        s = sys.stdin.read().strip()  # fallback: read from standard input

    # Step 2: Convert to lowercase
    s = s.lower()

    # Step 3: Count frequency of each character manually
    freq = {}
    for char in s:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1

    # Step 4: Sort by frequency descending, then ASCII ascending
    sorted_items = sorted(freq.items(), key=lambda x: (-x[1], x[0]))

    # Step 5: Take top 5 characters
    top5 = sorted_items[:5]

    # Step 6: Format output as required
    result = ",".join([f"{char}:{count}" for char, count in top5])
    print(result)

# Run the function
if __name__ == '__main__':
    CountPopularChars()
      

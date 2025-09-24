r'''
Task Description:
In this task, you are assigned to develop one program to help users calculate 
different information based a series of user provided numbers (integers). 
Detailed requirement is provided as follows: 

Input: A series of numbers 
Output: (Your output should be in one line)
	. The summation of the even numbers and summation of the odd numbers in 
       the input list 
	. The difference between the biggest and smallest numbers in the input list
	. The count of even numbers and odd numbers in the input list
	. The "centered" average of the list of integers. The centered average can be 
       calculated as the mean average of the values, after removing the largest and 
       smallest values in the array. If there are multiple copies of the smallest 
       value, ignore all but keep just one copy, and likewise for the largest value. 
       For instance, [12,2,8,7,100] -> 9; [2,2,8,11,100] -> 7

To have a better understanding of the loops, please try to implement 
two programs: one uses "for" and another uses "while" loop.

Running Examples:

C:\INF1002\Lab2\EvenOddCalculator> python EvenOddCalculator.py 12,2,8,7,100
The sum of all even numbers is 122, the sum of all odd numbers is 7, the difference between the biggest and smallest number is 98, the total number of even numbers is 4, the total number of odd numbers is 1, the centered average is 9.

C:\INF1002\Lab2\EvenOddCalculator> python EvenOddCalculator.py 1,2,abcd,8,11,200,301
Please enter valid integers.
'''
import sys
# write your code here
# you can use sys.argv[1] to get the first input argument.
# sys.argv[2] is the second argument, etc.
def EvenOddCalculator():
     
       # Step 1: Check if the user provided exactly one argument (the numbers)
     if len(sys.argv) != 2:                                    # len() gives the number of items in the list; != means "not equal" 
           print("Please enter valid integers")                # show error if wrong input
           return                                              # stop the function here

       # Step 2: Convert input string into a list of integers
     try:
           # sys.argv[1] os the first argument (string of numbers, e.g., "12,6,34,3,100")
           # split (",") divides the string into pieces at commas
           # int(x) converts each piece into an integer
           numbers = [int(x) for x in sys.argv[1].split(",")]
     except ValueError:
           # if any value is not an integer, show error and exit
           print("Please enter valid integers")
           return
     
       # Step 3: initialize counters for even/odd sums and counts
     even_sum = 0    # sum of all even numbers
     odd_sum = 0     # sum of all odd numbers
     even_count = 0  # number of even numbers
     odd_count = 0   # number of odd numbers

       # Step 4: loop through numbers to calculate sum and counts
     for n in numbers:        # n takes each number in the list
            if n % 2 == 0:     # % is modulo; n % 2 == 0 checks if n is even
                 even_sum += n 
                 even_count += 1

            else:
                 odd_sum += n
                 odd_count += 1

     # Step 5: Find the difference between the biggest and smallest numbers
     differnece = max(numbers) - min(numbers) # max() finds largest, min() finds smallest
     
     # Step 6: Calculate centered average
     nums_copy = sorted(numbers)                                         # Create a sorted copy of numbers (smallest > largest)
     nums_copy.remove(min(nums_copy))                                    # remove ONE smallest number
     nums_copy.remove(max(nums_copy))                                    # remove ONE largest number
     centered_avg = sum(nums_copy) // len(nums_copy)                     # sum all remaining numbers and divided by count (integer division)

     # Step 7: print everything in ONE line 
     print(f"The sum of all even numbers is {even_sum},"
           f"The sum of all odd numbers is {odd_sum},"
           f"the difference between the biggest and smallest number is {differnece},"
           f"the total number of even numbers is {even_count},"
           f"the total number of odd numbers is {odd_count},"
           f"the centered average is {centered_avg}.")
     
     # Step 8 run the function if this file is executed directly

if __name__=='__main__':
      EvenOddCalculator()
      

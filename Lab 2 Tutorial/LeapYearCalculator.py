r'''
Task Description:
In this task, you will develop a program to compute all the leap years within a 
specified time period. The user will input a start year and an end year. 
Your task is to determine how many leap years are included in this period and 
print out those leap years. 

The rule for determining leap years is as follows:
	. A year is called a leap year, if the year is perfectly divisible by 4 - except 
       for years which are both divisible by 100 and not divisible by 400. The second 
       part of the rule effects century years. 
       For example; the century years 1600 and 2000 are leap years, 
       but the century years 1700, 1800, and 1900 are not. This means that three times 
       out of every 400 years there are 8 years between leap years.

More information about the leap years rule can be found online. 

Input: Two numbers (one is the start year, and another is the end year)
Output: The number of leap years and all the leap years (Your output should be in one line)
Note: In case of invalid input, print the message "Your input is invalid!".

Running Examples:

C:\INF1002\Lab2\LeapYearCalculator> python LeapYearCalculator.py 1989 2000
The number of Leap Years is 3, the Leap Years are 1992, 1996, 2000
'''

import sys
# write your code here
# you can use sys.argv[1] to get the first input argument.
# sys.argv[2] is the second argument, etc.
def LeapYearCalculator():
     # step 1: validate input checks if user gave exactly 2 numbers (so len(sys.argv) should be 3)
     if len(sys.argv) != 3:                       # len() counts how many arguments are in sys.argv // sys.argv[0] is filename, [1] amd [2] are input
          print("Your input is invalid!")         # if not 3, tell user its wrong      
          return                                  # stop the program here
     
     try: # step 2: convert the arguments which are strings into integers
          start = int(sys.argv[1])                # sys.argv[1] is the first number the user typed  // first year = start year
          end   = int(sys.argv[2])                # sys.argv[2] is the second number the user typed // second year = end year
     except ValueError:                           # if user typed something thats not a number
          print("Your input is invalid!")
          return                                  # stop program
     
     # step 3: make sure start ≤ end, otherwise invalid
     if start > end:
          print("Your input is invalid!")
          return
     
     # step 4: prepare a list to store leap years
     leap_years = []

     # step 5: loop through each year in the range
     for year in range(start, end + 1):           # + 1 so the end year is inlcuded
          if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
               leap_years.append(year)            # add leap year to the list
     
     # step 6: print results
     if len(leap_years) == 0:                     # no leap years found
          print("The number of Leap Years is 0, the Leap Years are")
     else:
          leap_str = ",".join(map(str, leap_years))
          print(f"The number of Leap Years is {len(leap_years)}, the Leap Years are {leap_str}")

if __name__=='__main__':
     LeapYearCalculator()
      

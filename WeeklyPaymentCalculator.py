r'''
Task Description:
Develop one employee weekly payment calculation program. 
The program requirement is as follows: 
1.	Allow users to run your program with three input arguments by passing three
    values to the program:  the number of working hours, input normal rate and 
    input the overtime rate.

2.	Your program will read the three arguments and calculate the users salary 
    using the following two formulas:
        a.	Payment of the normal hours = normal rate * normal hours
        b.	Payment of the overtime hours = overtime rate * overtime hours
        NOTE: the working hours within 40 belong to normal hours and those beyond 
              40 hours are considered as overtime hours. 

3.	After user inputs all the numbers, if the input numbers are invalid, you need 
    to present an error message "Your input is invalid!". Otherwise, you need to 
    print out the employee's payment of normal hours, his payment of overtime 
    hours and total payment. The output payment requires to have 2 precisions. 
    For instance, if payment is 2300.456, it should print 2300.46. 
    If payment is 2300, it should print 2300.00.
      
NOTE: You have to strictly follow the input and output format. 

Running example:
Assume your program is named as WeeklyPaymentCalculator.py. Example output is as follows: 

C:\INF1002\Lab1\WeeklyPaymentCalculator> python weeklyPaymentCalculator.py 20 30 100
Normal Salary:600.00, Extra Salary:0.00, Total Salary:600.00

C:\INF1002\Lab1\WeeklyPaymentCalculator> python weeklyPaymentCalculator.py 60 30 200
Normal Salary:1200.00, Extra Salary:4000.00, Total Salary:5200.00

C:\INF1002\Lab1\WeeklyPaymentCalculator> python weeklyPaymentCalculator.py 10000 10 200
Your input is invalid!

'''
import sys
# You can use sys.argv[1] to get the first input argument.
# sys.argv[2] is the second argument, etc.
def WeeklyPaymentCalculator():
    args = sys.argv[1:] # to skip the file name and get the 3 numbers

    if len(args) != 3:
        print("Your input is invalid!")
        return # to stop the function
    
    try: # Convert input arguments to float
        hours = float(args[0])
        normal_rate = float(args[1])
        overtime_rate = float(args[2])

        # Check for negative inputs
        if hours < 0 or normal_rate <0 or overtime_rate < 0:
            print("Your input is invalid!")
            return
        
    except:
        print("Your input is invalid!")
        return
    
    # Calculate salaries
    if  hours <= 40:
        normal_salary = hours * normal_rate
        overtime_salary = 0
    else:
        normal_salary = 40 * normal_rate
        overtime_salary = (hours - 40) * overtime_rate

    total_salary = normal_salary + overtime_salary

    print(f"Normal Salary:{normal_salary:.2f}, Extra Salary:{overtime_salary:.2f}, Total Salary: {total_salary:.2f}")


if __name__=='__main__':
    WeeklyPaymentCalculator()
    

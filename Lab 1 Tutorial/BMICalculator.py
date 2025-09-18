r'''
Task Description:
In this task, we develop a Body Mass Index (BMI) Calculator that can be used to 
calculate your BMI value and weight status while taking your age into 
consideration. The referenced weight range and calculation 
formula is listed below.

The program requirement is as follows:
1. Allow users to run your program with three input arguments by passing three 
   values to the program: the choice of units, height, and weight.

2. Your program will read the three arguments and calculate BMI using the 
   following two formulas:
    BMI = weight(kg)/height2(m2) (Metric Units)
    BMI = 703 * weight(lb)/height2(in2) (Imperial (U.S.) Units)
    NOTE: The formulas to calculate BMI are based on two of the most used unit 
          systems.

3. After user inputs all the numbers, if the input numbers are invalid, you need 
   to present an error message "Your input is invalid!". Otherwise, you need to 
   print out BMI and category. The output payment requires to have 2 precisions. 
   For instance, if BMI is 23.456, it should print 23.46. If BMI is 23, it should 
   print 23.00.

Reference:
Your BMI is a measurement of your body weight based on your height and weight. 
Although your BMI does not actually "measure" your percentage of body fat, it is a 
useful tool to estimate a healthy body weight based on your height. Due to its ease 
of measurement and calculation, it is the most widely used diagnostic indicator to 
identify a person's optimal weight depending on his height. Your BMI "number" will 
inform you if you are underweight, of normal weight, overweight, or obese. However, 
due to the wide variety of body types, the distribution of muscle and bone mass, etc., 
it is not appropriate to use this as the only or final indication for diagnosis.

BMI Table for Adults:
This is the World Health Organization's (WHO) recommended body weight based on BMI 
values for adults. It is used for both men and women, age 18 or older.
______________________________________
|Category         | BMI range - kg/m2|
|____________________________________|
|Severe Thinness  | <= 16            |
|Moderate Thinness| >16 - 17         |
|Mild Thinness    | >17 - 18.5       |
|Normal           | >18.5 - 25       |
|Overweight       | >25 - 30         |
|Obese Class I    | >30 - 35         |
|Obese Class II   | >35 - 40         |
|Obese Class III  | >40              |
|____________________________________|

NOTE: You must strictly follow the input and output format.
Example output is as follows. Note that '%0.2f\tSevere Thinness' should be used.

Running example:
C:\INF1002\Lab1\AverageCalculator> python BMICalculator.py metric 1.80 78
24.07 Normal

C:\INF1002\Lab1\AverageCalculator> python BMICalculator.py metric 1.78 48
15.15 Severe Thinness

C:\INF1002\Lab1\AverageCalculator> python BMICalculator.py metric 1.60 126
49.22 Obese Class III

C:\INF1002\Lab1\AverageCalculator> python BMICalculator.py imperial 68.90 154.32
22.85 Normal

C:\INF1002\Lab1\AverageCalculator> python BMICalculator.py imperial 85.63 135.68
13.01 Severe Thinness

C:\INF1002\Lab1\AverageCalculator> python BMICalculator.py abc
Your input is invalid!
'''
import sys
# You can use sys.argv[1] to get the first input argument.
# sys.argv[2] is the second argument, etc.

def BMICalculator():
    args = sys.argv[1:] # to skip the file name and get the 3 numbers

    if len(args) !=3:
        print("Your input is invalid!")
        return # to stop the function
    
    unit = args[0].lower()
    try:
        height = float(args[1])
        weight = float(args[2])
    except:
        print("Your input is invalid!")    
        return
    
# Calculate BMI
    if unit == 'metric':
        bmi = weight / (height ** 2)
    elif unit == 'imperial':
        bmi = 703 * weight / (height ** 2)
    else:
        print("Your input is invalid!")
        return

    # Determine BMI Category
    if bmi <= 16:
        category = "Severe Thinness"
    elif bmi > 16 and bmi <= 17:
        category = "Moderate Thinness"
    elif bmi > 17 and bmi <= 18.5:
        category = "Mild Thinness"
    elif bmi > 18.5 and bmi <= 25:
        category = "Normal"
    elif bmi > 25 and bmi <= 30:
        category = "Overweight"
    elif bmi > 30 and bmi <= 35:
        category = "Obese Class I"
    elif bmi > 35 and bmi <= 40:
        category = "Obese Class II"
    else:
        category = "Obese Class III"

    print(f"{bmi:.2f}\t{category}")

if __name__=='__main__':
    BMICalculator()
    

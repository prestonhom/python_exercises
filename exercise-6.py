# exercise-06 What's the  Season?

# Write the code that:
# 1. Prompts the user to enter the month (as three characters):
#      Enter the month of the season (Jan - Dec):
# 2. Then propts the user to enter the day of the month: 
#      Enter the day of the month:
# 3. Calculate what season it is based upon this chart:
#      Dec 21 - Mar 19: Winter
#      Mar 20 - Jun 20: Spring
#      Jun 21 - Sep 21: Summer
#      Sep 22 - Dec 20: Fall
# 4. Print the result as follows:
#      <Mmm> <dd> is in <season> 

# Hints:
# Consider using the in operator to check if a string is in a particular list/tuple like this:
# if input_month in ('Jan', 'Feb', 'Mar'):
#
# After setting the likely season, you can use another if...elif...else statement to "adjust" if
# the day number falls within a certain range.
input_month = str(input('Please enter a month: '))
input_day = int(input('Please enter a day: '))
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
# Winter
if input_month in ('December', 'January', 'February', 'March'):
    if input_month == 'December' and input_day in range(21,32,1):
        print(f"December {input_day} is in winter")
    elif (input_month =='January' or input_month == 'February') and input_day in range(0,32,1):
        print(f"{input_month} {input_day} is in 'winter")
    elif input_month == 'March' and input_day in range(0,20,1):
        print(f"{input_month} {input_day} is in 'winter")
# Spring
if input_month in ('March', 'April', 'May', 'June'):
    if input_month == 'March' and input_day in range(20,32,1):
        print(f"{input_month} {input_day} is in Spring")
    elif (input_month =='April' or input_month == 'May') and input_day in range(0,32,1):
        print(f"{input_month} {input_day} is in 'Spring")
    elif input_month == 'June' and input_day in range(0,21,1):
        print(f"{input_month} {input_day} is in 'Spring")
# Summer
if input_month in ('June', 'July', 'August', 'September'):
    if input_month == 'June' and input_day in range(21,32,1):
        print(f"{input_month} {input_day} is in Summer")
    elif (input_month =='July' or input_month == 'August') and input_day in range(0,32,1):
        print(f"{input_month} {input_day} is in 'Summer")
    elif input_month == 'September' and input_day in range(0,22,1):
        print(f"{input_month} {input_day} is in 'Summer")
# Fall
if input_month in ('September', 'October', 'November', 'December'):
    if input_month == 'September' and input_day in range(21,32,1):
        print(f"{input_month} {input_day} is in Fall")
    elif (input_month =='October' or input_month == 'November') and input_day in range(0,32,1):
        print(f"{input_month} {input_day} is in 'Fall")
    elif input_month == 'December' and input_day in range(0,21,1):
        print(f"{input_month} {input_day} is in 'Fall")


        
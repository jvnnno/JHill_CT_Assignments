# Task 1: Calculate the total cost of three items you'd commonly find in a 
# grocery store, given their individual prices. 
# For example, what would be the cost of 
# bread, peanut butter, and jelly be?

bread = 5
peanut_butter = 4
jelly = 3
total_cost = print(bread + peanut_butter + jelly)


# Task 2:  If you have a savings account with a particular 
# initial amount and a fixed yearly interest rate, calculate 
# the total amount in your account after a year. So if 
# you had $10,000 at a 7% interest write code that would 
# tell us the amount at the end of the year. 


# Another tricky one for me. Want to provide my thought process:
# to get 7% to a value, I need the exact percentage which is 7/100
# 7/100 = 0.07 
# a modulus may be needed to get 0.07 to a whole int?

savings = 10,000 ** 0.07  #initial amount variable compounded by 0.07
days_per_year = 365    #amount for end of the year 
total_savings = print(savings // days_per_year)


# OFFICE HOURS NEEDED!!!  
# Assignment operators are slightly tricky for me. 
# Want to resubmit with review / greater understanding.

savings = 10,000
interest = 7
total_savings = 10,000 + (10,000 * interest / 365)
print(total_savings)



 





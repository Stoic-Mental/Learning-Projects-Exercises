#asking the user to input their values described by the variable names
#calculating the interest over time as a monthly value as opposed to a yearly rate

yearly_salary=float(input("What is your yearly salary?"))
monthly_salary=yearly_salary/12
portion_saved=float(input("What is the portion of your salary you save? Please type as a decimal E.G to input 20% use 0.2    "))
cost_of_dream_home=float(input("What is the cost of your dream home?"))
salary_increase=float(input("What is the expected rate of increase for your salary every 6 months?"))

#defining set variables according to specification + setting up the variables that will enable the main algorithm to work

investment_return=0.05
amount_saved=0
down_payment=cost_of_dream_home*0.25
months=0
counter=0

#loop that first works out interest for the month (needs to be done first since interest can't be accrued instantly and requires the next month to roll around)
#then adds the money saved to the variable. adding months and counter to track the months (for end result and to know when next pay increase takes place)
#the first if statement adds the pay increase when needed + the second times out the loan when it hits 40 years (most normal loans can't go on longer than this)
#prints are for testing a debugging purposes

while amount_saved < down_payment:
    amount_saved *= 1+(investment_return/12)
    amount_saved += (monthly_salary*portion_saved)
    months+=1
    print("money saved:"+str(amount_saved))
    counter+=1
    print(counter)
    if counter%6 == 0:
        monthly_salary*=(1+salary_increase)
        print("new paycheck is "+str(monthly_salary))
    if months > 480:
        print("unfortunately you don't meet the salary requirements to afford this house")
        break

print("it would take you "+str(months)+" months to put down a deposit for a house")
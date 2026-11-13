#firstly working out the base variables for the process 
#defining my variables needed for bisection search
#checks to see if the deposit is already above the target

def initial_boot():
    initial_deposit=float(input("please enter your initial deposit"))
    interest_rate=0.5
    deposit_goal=200000
    
    if initial_deposit>=deposit_goal:
        print("savings rate is 0%")
        initial_boot()
    else:
        bisection_search(initial_deposit,interest_rate,deposit_goal)

#bisection search loop to find the % interest return to specification
#initially setting up conditions for the search by importing the needed values into the function/interest change
#before jumping into the loop I did the first step this would make it so that the loop could cancel straight away if the lowest interest was 50%
#once I can tell which half of 50% the interest is on I add/take away the interest change. After this I change the change narrowing down the area which the interest could be
#after altering the interest I check to see if the saved money is within the desired range
#if yes ---> display the end result for the algorithm. if no ----> loop again until the value is within the desired range.


def bisection_search(initial_deposit,interest_rate,deposit_goal):
    interest_change=0.25
    amount_saved=initial_deposit*((1+interest_rate/12)**36)
    steps=1
    while amount_saved > deposit_goal+100 or amount_saved < deposit_goal-100:
        
        if amount_saved > deposit_goal+100:
            interest_rate-=interest_change
            interest_change/=2
            steps+=1
        elif amount_saved < deposit_goal-100:
            interest_rate+=interest_change
            interest_change/=2
            steps+=1    
             
        amount_saved=initial_deposit*((1+interest_rate/12)**36)
    result(interest_rate,steps)

def result(interest_rate,steps):
    print("the minimum return is "+str(interest_rate))
    print(steps)

initial_boot()


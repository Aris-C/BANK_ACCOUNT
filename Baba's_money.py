"""
P = Principle (present value)
r = interest rate
n = how many paymwnts per year
t = how many years
pv = future value
"""



p = float(input("Whats the principle "))
r = float(input("Whats the Rate "))
n = int(input('How many periods '))
t = int(input("How many paymentsper period "))
pv = p * (pow((1 + r/100/n),n*t))


def compound_interest(p,r,n,t):
    balance = p * (pow((1+ r/100/n),n*t))
    ci = balance - p
    print('\n Balance at the end of the period will be $',round(balance,2))
    print("\n Interest earned is ", round(ci,2), 'during the',t,'year period.')
    pct = ci/balance*100
    print("This is a ",round(pct,2),'% return on investment')




compound_interest(5000,10,12,5)

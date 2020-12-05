


p = float(input("Whats the principle "))
r = float(input("Whats the Rate "))
n = int(input('How many periods '))
t = int(input("How many paymentsper period "))
pv = p * (pow((1 + r/100/n),n*t))
print(pv)

def compound_interest(p,r,n,t):
    balance = p * (pow((1+ r/100/n),n*t))
    ci = balance - p
    print('Balance at the end of the period ',round(balance,2))
    print("Interest earned is ", round(ci,2))


compound_interest(5000,10,12,5)

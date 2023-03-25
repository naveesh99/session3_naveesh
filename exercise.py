import math
def dayrate(p):
    return  p*8
def monthrate(p,d):
    a=(p*8)*22
    c=a*d
    e=a-c
    return math.ceil(e)
def budget(f,p,d):
    x=p*8*(1-d)
    days =f/x
    return math.floor(days)
p=int(input("hourrate"))
d=float(input("discount"))
f=int(input("budget"))
print(dayrate(p))
print(monthrate(p,d))
print(budget(f,p,d))
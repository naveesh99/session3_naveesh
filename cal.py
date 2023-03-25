import math

def dayRate(n):
    return math.ceil(n*8);

def monthRate(n, rate):
    return math.ceil((n*176)-((n*176)*rate));

def daysInBudget(capital, n, rate):
    day_rate = (n*8) - (n* 8 * rate)
    result = capital // day_rate
    return math.floor(result)


print(dayRate(89))
print(monthRate(89, 0.42))
print(daysInBudget(20000, 89, 0.2002))   
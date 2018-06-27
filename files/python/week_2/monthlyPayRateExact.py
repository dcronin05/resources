balance = 999999
annualInterestRate = 0.18

orgBalance = balance
monthlyInterest = annualInterestRate / 12
monthlyPaymentRate = 0
lower = balance / 12
upper = (balance * (1 + annualInterestRate)) / 12

while abs(round(balance, 3)) >= 0.01:
    monthlyPaymentRate = round((lower + upper) / 2, 3)

    balance = orgBalance
    unpaidBalance = balance - monthlyPaymentRate

    for i in range(12):
        balance = unpaidBalance + monthlyInterest * unpaidBalance
        unpaidBalance = balance - monthlyPaymentRate

    if balance < 0:
        upper = monthlyPaymentRate
    elif balance > 0:
        lower = monthlyPaymentRate


print('Lowest Payment:', round(monthlyPaymentRate, 2))

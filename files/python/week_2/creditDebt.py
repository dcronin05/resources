balance = 42
annualInterestRate = 0.2
monthlyPaymentRate = 0.04


month = 0
payment = monthlyPaymentRate * balance
unpaidBalance = balance - payment

for i in range(1, 13, 1):
    month += 1
    balance = unpaidBalance + (annualInterestRate/12) * unpaidBalance
    payment = monthlyPaymentRate * balance
    unpaidBalance = balance - payment
    print('Month', month, 'Remaining balance:', round(balance, 2))

balance = 3234234
annualInterestRate = 0.9

orgBalance = balance
monthlyPaymentRate = 0

while balance >= 0:

    monthlyPaymentRate += 10
    # print(monthlyPaymentRate)
    # print(monthlyPaymentRate*12)
    balance = orgBalance

    unpaidBalance = balance - monthlyPaymentRate

    for i in range(12):
        balance = unpaidBalance + (annualInterestRate/12) * unpaidBalance
        unpaidBalance = balance - monthlyPaymentRate


print('Lowest Payment:', monthlyPaymentRate)

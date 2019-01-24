def debt(balance, annualInterestRate):
    monthly_payment = 10
    monthly_interest_rate = annualInterestRate/12.0
    init_balance = balance
    while True:
        for i in range(12):
            monthly_unpaid_balance = balance - monthly_payment
            balance = monthly_unpaid_balance + (monthly_interest_rate * monthly_unpaid_balance)
        if balance <= 0:
            print('Lowest payment:', monthly_payment)
            break
        else:
            monthly_payment += 10
            balance = init_balance
print(debt(3329,.2))

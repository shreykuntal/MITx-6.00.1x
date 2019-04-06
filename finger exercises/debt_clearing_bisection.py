def debtb(balance, annualInterestRate):
    monthly_interest_rate = annualInterestRate/12.0
    monthly_payment_lower = balance/12.0
    monthly_payment_upper = (balance * ((1 + monthly_interest_rate) ** 12)) / 12.0
    while True:
        for i in range(12):
            monthly_unpaid_balance = balance - monthly_payment_lower
            balance = monthly_unpaid_balance + (monthly_interest_rate * monthly_unpaid_balance)
        print(balance)
        if ((monthly_payment_lower + monthly_payment_upper) * 6) > balance:
            print(monthly_payment_upper)
            return ((monthly_payment_lower + monthly_payment_upper) / 2)
        monthly_payment_upper -= 0.01
print(debtb(999999,.18))
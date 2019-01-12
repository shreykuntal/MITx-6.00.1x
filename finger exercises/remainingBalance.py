def rembal(balance, annualInterestRate, monthlyPaymentRate):
    """Takes three arguments:
       balance, annualInterestRate, monthlyPaymentRate
       
       returns remaining balance at end of 12 months.
    """
    monthly_interest_rate = annualInterestRate / 12.0
    for i in range(12):
        minimum_monthly_payment = monthlyPaymentRate * balance
        unpaid_balance = balance - minimum_monthly_payment
        updated_balance = unpaid_balance + (monthly_interest_rate * unpaid_balance)
        balance = updated_balance
        print('Month',i,'Remaining balance:',balance)
    return round(balance, 2)
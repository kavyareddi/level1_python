#Program to calculate credit card balance after 1 year
#input :balance,annualrateinterest,monthlypaymentrate
try:
    balance = int(input('enter balance:'))
    annualInterestRate = int(input('enter annualInterestRate :'))
    monthlyPaymentRate = int(input('monthlyPaymentRate:'))

    totalPaid = 0

    for thisMonth in range(1,13):
        monthly_Interest_Rate = annualInterestRate / 12
        
        minimum_Monthly_Payment = round(monthlyPaymentRate * balance, 2)
        monthly_Unpaid_Balance = balance - minimum_Monthly_Payment
        updated_Balance_EachMonth = round(monthly_Unpaid_Balance + (monthly_Interest_Rate * monthly_Unpaid_Balance) , 2)

        print('Month: %d' %(thisMonth))
        print('Minimum monthly payment: ' +str(minimum_Monthly_Payment))
        print('Remaining balance: ' +str(updated_Balance_EachMonth))

        balance = updated_Balance_EachMonth
        totalPaid += minimum_Monthly_Payment

    print('Total paid: ' +str(totalPaid))
    print('Remaining balance: '+str(balance))
except:
    print(bug)




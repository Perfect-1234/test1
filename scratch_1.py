print("Welcome to Lapo MFBank")

rate = float(input("What is your company's rate: "))
rate_fraction = rate/100
print("Your company's rate is %f:" %rate_fraction)

principal = float(input("Enter the amount needed: "))
print("you requested %f" %principal)
if (0 < rate <= 5 and principal <= 200000):
    time = float(input("Enter the time in which the loan will span through(IN MONTHS): "))
    totalI = (principal * rate_fraction * time)
    print("Your Total Interest is %f:" %totalI)
    monthlyI = (totalI)/(time * 12)
    print("The Monthly Interest of the loan is %f:" %monthlyI)
    totalRep = principal + totalI
    print("The Total repayment is %f:" %totalRep)
    #To calculate the Monthly Repayment of the loan:
    monthlyRep = (totalRep)/(time * 12)
    print("The Monthly repayment is %f:" %monthlyRep)
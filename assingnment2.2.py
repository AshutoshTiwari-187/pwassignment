income=int(input("Enter the income"))
if income>100000:
    print("The tax is = 15%")
elif income<=100000 and income>50000:
    print("The tax is = 10%")
elif income<=50000:
    print("The tax is = 5%")

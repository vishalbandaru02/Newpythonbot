a=input("enter a month:")
if a=="feb":
    print("has 28 days")
elif a in "jan,mar,may,july,aug,oct,dec":
    print("has 31 days")
elif a in "april,june,sep,nov":
    print("has 30 days")
else:
    print("enter a valid month")


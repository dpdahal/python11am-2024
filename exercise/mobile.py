print("1. NTC to NTC")
print("2. NTC to NCELL")
print("3. NCELL to NTC")
print("4. NCELL to NCELL")

option = int(input("Enter your option: "))
if option==1:
    duration = int(input("Enter duration: "))
    if duration<=10:
        print("Price: 2.5")
    if duration>10 and duration<=20:
        print("Price: 5")
elif option==2:
    duration = int(input("Enter duration: "))
    if duration<=10:
        print("Price: 5")
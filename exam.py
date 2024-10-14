medical_cause=input("Do you have any medical problem? Please enter Y or N ")
percentage=int(input("What is your attendance percentage? "))

if medical_cause=="Y":
    print("allowed")
else:
    if percentage>=75:
        print("allowed")
    else:
        print("not allowed")
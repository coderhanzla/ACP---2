
totalclasses = int(input("Enter the total number of classes held: "))
attendedclasses = int(input("Enter the number of classes you attended: "))

attendancePercentage = (attendedclasses / totalclasses) * 100

if attendancePercentage >= 75:
    print("You are eligible for the exam.")
else:
    print("You are NOT eligible for the exam.")







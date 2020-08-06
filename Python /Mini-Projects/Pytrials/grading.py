x=int(input("Enter marks of the student: "))
if x>=0 and x<=40:
    print("Student got F grade....")
elif x>40 and x<=50:
    print("Student got E grade....")
elif x>50 and x<=60:
    print("Student got D grade....")
elif x>60 and x<=70:
    print("Student got C grade....")
elif x>70 and x<=80:
    print("Student got B grade....")
elif x>80 and x<=100:
    print("Student got A grade....")
else:
    print("Invalid marks")
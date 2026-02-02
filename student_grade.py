name=input("Enter student name: ")
maths=int(input("Enter maths marks: "))
science=int(input("Enter science marks: "))
english=int(input("Enter english marks: "))

if (maths<0 or maths>100 or 
    science <0  or science>100 or
    english <0 or english>100):
    print("Invalid marks")
else:
    total_marks=maths+science+english
    avg=total_marks/3

    if(maths<40 or science<40 or english<0):
        status="fail"
    else:
        status="Pass"
    print("\nStudent Name:", name)
    print("Total Marks:", total_marks)
    print(f"Average Percentage: {avg:.2f}")
    print("Result:", status)

    if status=="Pass":
        if avg>=75:
            grade="A"
        elif(avg>=60 and avg<75):
            grade="B"
        else:
            grade="C"
        print(f"Grade: {grade}")







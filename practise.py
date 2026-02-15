#num=int(input())
"""name="nikhil"
print(f"Sum :{10+5}")
print(f"Name:{name}")
print("f{name}")"""
#print(f+"text")
"""x=5.0
y=5
result=x+y
print(result)"""

"""
temperature = 25
humidity = 65
has_ac = True

if temperature > 30:
    status = "Hot"
    if humidity > 70:
        status = "Very Uncomfortable"
elif temperature > 20:
    if not has_ac and humidity > 60:
        status = "Uncomfortable"
    else:
        status = "Comfortable"
else:
    status = "Cold"

print(status)"""

"""
username="admin"
password="hello"
attempts=3

if not password:
    print("Password required")
if password:
    print("valid passwprd")
if username:
    print("valid username")
if attempts:
     print("attempts remaining")"""



'''x = 15
y = 20
z = 15

result = (x == z) and (y > x) or (x > y)
print(result)'''

'''student_marks=int(input("Enter student marks: "))
if student_marks>=40:
    print("Pass")
else:
    print("Fail")'''
'''
passed_students=0
failed_students=0
for i in range(5):
    student_marks=int(input("Enter student marks: "))
    if 0<=student_marks<=100:
        if student_marks>=40:
            print("Result:Pass")
            passed_students+=1
        else:
            print("Result:Fail")
            failed_students+=1
    else:
        print("Result:Inavalid Marks")'''


'''def get_result(pass_mark,marks):
    if 0<=pass_mark<=100  and 0<=marks<=100:
        if marks>=pass_mark:
            return "Pass"
        else:
            return "fail"
    else:
        return "Inavlid"
passed_students=0
failed_students=0
pass_mark=int(input("enter passmark:"))
for i in range(1,6):
    student_marks=int(input(f"Enter marks of student{i}: "))
    result=get_result(pass_mark,student_marks)

    print("Result: ",result)
    if result=="Pass":
        passed_students+=1
    elif result=="fail":
        failed_students+=1
print("--Summary--")
print(f"Passed Student:{passed_students}")
print(f"Failed Students:{failed_students}")'''


'''total_marks=0
marks_list=[]
pass_mark=int(input("enter passmark:"))
for i in range(1,6):
    student_marks=int(input(f"Enter marks of student{i}:"))
    if 0<=student_marks<=100:
        marks_list.append(student_marks)
        total_marks+=student_marks
    else:
        print("Invalid Mark")
average_marks=total_marks/5
print("--Summary--")
print(f"Total Marks: {total_marks}")
print(f"Average marks: {average_marks}")'''

'''marks = [45, 78, 32, 90, 60]
marks.append(85)
marks.remove(32)
marks.sort(reverse=True)
print(f"Highest: {max(marks)}")
print(f"Lowest:{min(marks)}")'''

'''marks = [55, 30, 80, 45, 20]
count=0
for index,marks in enumerate(marks,start=1):
    print(f"Student{index} marks:{marks}")
    if marks<40:
        count+=1
print(f"Students scored less than 40:{count}")'''

'''no_of_students=int(input("Enter no of students: "))
pass_mark=int(input("Enter pass marks: "))
marks=[]
total=0
passed_students=0
failed_students=0
for i in range(1,no_of_students+1):
    mark=int(input(f"Enter student{i}:"))
    if 0<=mark<=100:
        marks.append(mark)
        total+=mark
        if mark>pass_mark:
            passed_students+=1
        else:
            failed_students+=1
for index,mark in enumerate(marks,start=1):
    print(f"Student{index}:{mark}")
average=total/len(marks)
print(f"Total Marks:{total}")
print(f"Average Marks:{average}")
print(f"Passed Students:{passed_students}")
print(f"Failed Stduents:{failed_students}")'''

"""def student_classifier(student_mark):
    if student_mark>=75:
        return "High"
    elif 40<=mark<75:
        return "Medium"
    else:
        return "Low"
no_of_students=int(input("Enter no of students:"))
marks=[]
classification=[]
for i in range(1,no_of_students+1):
    mark=int(input(f"Enter student{1} marks:"))
    if 0<=mark<=100:
        marks.append(mark)
        classification.append(student_classifier(mark))
print("---Students report---")
for index,mark in enumerate(marks,start=1):
    print(f"Student{index}:{mark}")
print("Claasification of Students Based on performance:")
print(f"High:{classification.count("High")}")
print(f"Medium:{classification.count("Medium")}")
print(f"Low:{classification.count("Low")}")"""

no_of_students=int(input("Enter no of Students:"))
student_details={}
for i in range(1,no_of_students+1):
    name=input(f"Enter name of student{i}:")
    marks=int(input(f"Enter marks of student{i}:"))
    student_details[name]=marks
for name,marks in student_details.items():
    print(f"Name:{name}\tMarks:{marks}")



    





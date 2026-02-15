subjects=("Math","Science","English")
student_names=[]
marks={}
unique_grades=set()
for i in range(1,6):
    name=input(f"Enter name of student{i}:")
    student_names.append(name)

    marks[name]={
        subjects[0]:int(input("Enter Maths marks:")),
        subjects[1]:int(input("Enter Science marks:")),
        subjects[2]:int(input("Enter English marks:"))
    }
    student_marks=marks[name]
    total_marks=student_marks["Math"]+student_marks["Science"]+student_marks["English"]
    avg=total_marks/3
   
    if avg>=85:
        grade="A"
    elif 70<=avg<85:
        grade="B"
    else:
        grade="C"
    unique_grades.add(grade)
    marks[name]["Average"]=avg
    marks[name]["Grade"]=grade

print("All Students: ",student_names)
print("First Three Students: ",student_names[0:3])

top_student=""
highest_average=0

for name,data in marks.items():
   
   print(f"{name}-Average:{data["Average"]:.2f}-Grade:{data["Grade"]}")

   if data["Average"]>highest_average:
       highest_average=data["Average"]
       top_student=name

print("\nTop Student:", top_student)

print("Unique Grades:",unique_grades)


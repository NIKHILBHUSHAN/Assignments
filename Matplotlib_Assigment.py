import matplotlib.pyplot as plt
import numpy as np
study_hours = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
marks_obtained = [45, 50, 55, 60, 68, 75, 82, 88, 92, 95]


plt.plot(study_hours,marks_obtained,color='blue',linestyle="-",marker="o")
plt.xlabel("study Hours")
plt.ylabel("Marks Obrtained")
plt.title("student performance analysis")
plt.show()
plt.figure()
plt.scatter(study_hours,marks_obtained,color='red',marker="x")
plt.xlabel("study Hours")
plt.ylabel("Marks Obrtained")
plt.title("student performance analysis")
plt.show()

students = ['Alice', 'Bob', 'Charlie', 'David', 'Eve']
math_scores = [85, 78, 92, 88, 76]
science_scores = [78, 85, 88, 82, 90]
x=np.arange(len(students))
width=0.35
 
plt.bar(x-width/2,math_scores,width,color='blue',label="Math")
plt.bar(x+width/2,science_scores,width,color='orange',label="Science")
plt.title("Student Performance: Math vs Science")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.xticks(x,students)
plt.legend()
plt.show()

marks_distribution = [45, 52, 58, 63, 67, 71, 55, 60, 65, 70, 
                      75, 80, 85, 90, 48, 54, 59, 64, 69, 74,
                      79, 84, 89, 50, 56, 62, 68, 72, 78, 83,
                      88, 46, 53, 61, 66, 73, 77, 82, 87, 92,
                      49, 57, 64, 70, 76, 81, 86, 91, 95, 51]

plt.hist(marks_distribution,bins=10,color='green',edgecolor='black')
plt.title("Distribution of Marks")
plt.xlabel("Marks Range")
plt.ylabel("Number of students")
plt.show()

activities = ['Sports', 'Music', 'Arts', 'Drama', 'Debate']
student_count = [45, 30, 25, 15, 35]
explode=[0.1,0,0,0,0]
plt.pie(student_count,labels=activities,autopct="%1.1f%%",explode=explode)
plt.title("Student Activity Distribution")
plt.show()


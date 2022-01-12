#ques4:make alist of 5 students and show them in sorted manner
student_1marks=int(input("enter student 1 marks="))
student_2marks=int(input("enter student 2 marks="))
student_3marks=int(input("enter student 3 marks="))
student_4marks=int(input("enter student 4 marks="))
student_5marks=int(input("enter student 5 marks="))
my_list=[student_1marks,student_2marks,student_3marks,student_4marks,student_5marks]
print("list=",my_list)
print("sorted list(decreasing order)=")
my_list.sort(reverse=True)
print(my_list)

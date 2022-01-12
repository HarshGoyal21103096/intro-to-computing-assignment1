#ques3:make a list of SID,NAME,GENDER,COURSE NAME and CGPA

name=input("enter name=")
sid=input("enter student Id=")
gender=input("enter gender=")
course_name=input("enter course name=")
cgpa=input("enter cgpa=")
sid=int(sid)
cgpa=float(cgpa)
#now name list as student_info
data=['name','SID','gender','course name','cgpa']
print(data)
student_info=[name,sid,gender,course_name,cgpa]
print(student_info)

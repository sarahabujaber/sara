class Student:
    firstname = ""
    lastname = ""
    avg = 0.0
    major = ""


s = Student()  # s-> student
print(type(s))

s = Student()
s.avg = 80.0
s.firstname = "sarah"
s.lastname = "abujaber"
s.major = "electroincs engeneering"
print(str(s.avg) +"," +s.firstname+s.lastname+","+s.major)
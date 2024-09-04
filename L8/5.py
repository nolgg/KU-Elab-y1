class Student:
    def  __init__(self, id, firstname, lastname):
        self.id = id
        self.firstname = firstname
        self.lastname = lastname
        self.courses = []
        self.num_course = []
        self.total_credit = 0
        self.advisor = None
        self.major = None

    def add_course(self, course):
        if not any(c == course.credit for c in self.courses) and (self.total_credit + course.credit) <= 25:
            self.total_credit += course.credit
            self.courses.append(course.title)
            self.num_course.append(course.course_id)
            return True
        return False

    def get_course(self):
        num = [str(k) for k in self.num_course]
        return " ".join(num)

    def drop_course(self, course):
        T_course_id = course.course_id
        T_title = course.title
        T_credit = course.credit
        if T_title in self.courses and T_course_id in self.num_course:
            if self.courses[-1] == T_title:
                self.courses.append('')
                self.courses.remove(T_title)
                self.num_course.remove(T_course_id)
                self.total_credit -= T_credit
            
            elif len(self.courses) > 1:
                self.courses.remove(T_title)
                self.num_course.remove(T_course_id)
                self.total_credit -= T_credit
            return True
            
        else:
            return False
            

    def set_advisor(self, advisor):
        self.advisor = advisor

    def set_major(self, major):
        self.major = major

    def __str__(self):
        return f'Student ID: {self.id}\nName: {self.firstname} {self.lastname}\nMajor: {self.major}\nAdvisor: {self.advisor}\nCourses: {self.get_course()}'

class Course:
    
    def __init__(self, title, course_id, credit):
        self.title = title
        self.course_id = course_id
        self.credit = credit

class Teacher:
    def __init__(self, firstname, lastname, id):
        self.firstname = firstname
        self.lastname = lastname
        self.id = id
    def __str__(self):
        return f'{self.firstname} {self.lastname} ({self.id})'

class Major:
    def __init__(self, id, name, faculty):
        self.id = id
        self.name = name
        self.faculty = faculty

    def __str__(self):
        return f'{self.name} {self.faculty} ({self.id})'


c_ls = "01219111 01219113 01219245 01219221 01204212 01219213 01420113 01420114 01420111".split(" ")
ad = Teacher("Preeda", "Lerdpongvipusana", "E901")
m = Major("E17", "Software & Knowledge Engineering", "Engineering")
s = Student(5610546231, "Chinnaporn", "Soonue")

s.set_advisor(ad)
s.set_major(m)
for i in c_ls:
    s.add_course(Course("sth", i, 1))

print(s)
print(s.total_credit)
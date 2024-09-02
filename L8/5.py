class Student:
    def  __init__(self, id, firstname, lastname):
        self.id = id
        self.firstname = firstname
        self.lastname = lastname
        self.courses = []
        self.num_course = 0
        self.total_credit = 0
        self.advisor = None
        self.major = None

    def add_course(self, course):
        if not any(c.code == course.code and c.title == course.title and c.credit == course.credit for c in self.courses) and (self.total_credit + course.credit) <= 25:
            self.num_course += 1
            self.total_credit += course.credit
            self.courses.append(course)

    def get_course(self):
        num = [str(course.code) for course in self.courses]
        return " ".join(num)

    def drop_course(self, course):
        for c in self.courses:
            if c.code == course.code and c.title == course.title and c.credit == course.credit:
                self.total_credit -= c.credit
                self.courses.remove(c)
                self.num_course -= 1
                if self.num_course == 0:
                    self.courses = ['']
                return True
        return False

    def set_advisor(self, advisor):
        self.advisor = advisor

    def set_major(self, major):
        self.major = major

    def __str__(self):
        return f'Student ID: {self.id}\nName: {self.firstname} {self.lastname}\nMajor: {self.major}\nAdvisor: {self.advisor}\nCourses: {self.get_course()}'

class Course:
    
    def __init__(self, title, code, credit):
        self.title = title
        self.code = code
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
        return f'{self.name} ({self.id})'


a = Student(1503,'pong','pol')
print(a)
a.add_course(Course('title',1309,15))
print(a)
a.add_course(Course('title1',1340,10))
print(a)
print(a.drop_course(Course('title',1309,15)))
print(a.courses)
print(a.courses)
a.set_advisor(Teacher('hello','last',1234))
a.set_major(Major(321,'engi','Engineerrr'))
print(a)
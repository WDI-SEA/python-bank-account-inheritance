# Assignments have name, github_url, completed, and grade properties
# completed's initial value should be set to False
# grade's initial value should be set to None
# Assignments have a mark_done method that take in the grade as an argument, and sets grade and completed

class Assignment:
    # homework properties contains ...
    def __init__(self, name, github_url, grade, completed = False):
        self.name = name
        self.github_url = github_url
        self.completed = completed
        self.grade = None

    def mark_done(self, grade):
        # assigns the grade, and sets completed to True
        if(isinstance(grade, int) and grade >= 0 and grade <= 100):
            self.completed = True
            self.grade = grade
            return completed
        else:
            print('no. bad input. pls')
            return False

class Student(Assignment):
    def __init__(self, name):
        # super()__init__()
        self.name = name
        self.pending_homeworks = []
        self.completed_homeworks = []

    
    def assign_homework(self, assignment):
        self.assignment = pending_homeworks.append(assignment)

    def complete_homework(self, name, grade):
        #loop over the pending homes
        for i in range(len(self.pending_homeworks)):
            homework = self.pending_homeworks[i].name
            #find the matching homework
            if homework.name == name:
                # we found the homework in the pending homework
                homework.mark_done(grade)
                self.complete_homework.append(self.pending_homeworks.pop(i))
    

    def print_outstanding_homeworks(self):
        missing_hws = []
        #loop over the pending homeworks
        for hw in self.pending_homeworks:
            missing_hws += 'f{home.name}, '

        if len(self.pending_homeworks):
             print(f'{self.name} still needs to turn in: {', '.join(missing_hws)}')
        else:
            print(f'{self.name} has no outstanding homeworks!')

        #print all the names of the missing homeworks
        #in pending_homeowrks

class SeiClass(Assignment):
    # pass
    def __init__(self, name, students=[]):
        self.name = name
        self.students = students
        self.completed_homeworks = []

    def add_student(self, student):
        self.student = students.append(students)
        #add the student to self.students

    def assign_homework(self, assignment):
        # loop over the students array
            #assign homework to each of the students
        for student in self.students:
            students.assign_homework(assignment)
            


henry = Student('Henry')
sarah = Student('Sarah')
mike = Student('Mike')

sei26 = SeiClass('sei26')
sei26.add_student(henry)
sei26.add_student(sarah)
sei26.add_student(mike)

assignment1 = Assignment('Bounty Hunters', 'https://github.com/WDI-SEA/mongoose-practice')

sei26.assign_homework(assignment1)

henry.complete_homework('Bounty Hunters', 98)
sarah.complete_homework('Bounty Hunters', 95)

henry.print_outstanding_homeworks()
sarah.print_outstanding_homeworks()
mike.print_outstanding_homeworks()
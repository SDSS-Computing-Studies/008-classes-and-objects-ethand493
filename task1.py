#! python3
"""
(10 points) 
Create a class object for a student.
It should have the following properties
str name
str studentNumber
int grade
list courses - to corresepond with course names
list grades - to correspond with grades

It should have the following methods:
average()       - determines the mathematical average of all course grades
getHonorRoll()  - determines the average of the top 5 courses if there are at least 5 courses.
                  returns True if the average is 86 or higher (on the honor roll)
                  returns False if not on the honor roll
showCourses()   - prints a list of all courses
showGrade(int)  - takes 1 parameter, the index of the list
                - displays the course name and grade
getCourses(list)- Receives a list of courses and stores that in the class property
getGrades(list) - Receives a list of grades and stores that in the class property
constructor     - should require the student name, studentNumber and grade (in that order)
"""

class student:

    name = ""
    studentNumber = ""
    grade = 0
    courses = []
    Grades = []
    
    
    # properties should be listed first

    def __init__(self, name, studentNumber, grade, courses=[], grades=[]): # You will need to create your own input parameters for all methods
        self.name = name
        self.studentNumber = studentNumber
        self.grade = grade
        self.courses = courses
        self.grades = grades



    def getCourses(self, courses):
        courses = self.courses
        return
        
    def getGrades(self, grades):
        self.grades = grades
    
    def showCourses(self):
        print(self.courses)

    def getHonorRoll(self):
        newlist = self.grades.sort()
        print(newlist)
        le = len(self.grades)
        funny = []
        for i in range(1,5):
            funny.append(newlist[le - i])
        funsum = sum(funny)
        if (funsum/5) >= 86:
            return True
        else:
            return False


    def average(self):
        Sum = sum(self.grades)
        x = Sum / len(self.grades)
        return x

    def index(self):
        index = input("Enter index: ")
        return index
    
    def __del__(self):
        print("Goodbye " + self.name + ", it was nice knowing you\n")

def main():
    # This contains test data that will be used by the autograder.
    # do not modify this function

    st1 = student("Anita Bath","91334",11)
    st1.getCourses( ["English","Math","PE","Computers","History","Biology","Japanese"] )
    st1.getGrades( [91, 94, 87, 99, 82, 100, 73])

    st2 = student("Joe Lunchbox","12346", 11)
    st2.getCourses( ["English","Math","Physics","Computers","Geography","Chemistry","French"] )
    st2.getGrades( [71, 98, 93, 95, 68, 81, 71])




main()
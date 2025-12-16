import json
class StudentGradeTracker:
    """Build a system where each student has a name and list of grades. 

You can add/remove students, add grades, and compute averages. 

Save and load the data from a file. 
    """
    
        
    
    
    def view_students_grades(self):
        with open("StudentGradeTracker.json","r") as student_grade_tracker:
            print(student_grade_tracker.read())
            
    def remove_student(self,name):
        new_list = []
        with open("StudentGradeTracker.json","r") as student_grade_tracker:
            for student in student_grade_tracker:
                person = json.loads(student)
                if person["Name"] == name :
                    pass
                else:
                    new_list.append(person)
        with open("StudentGradeTracker.json","w") as student_grade_tracker:
            for item in new_list:
                json.dump(item,student_grade_tracker)
                student_grade_tracker.write("\n")
                
                
    def student_average(self,name):
        with open("StudentGradeTracker.json","r") as student_grade_tracker:
            for student in student_grade_tracker:
                person = json.loads(student)
                if person["Name"] == name :
                    each_grade : list = person["Grades"]
            avg = sum(each_grade) // len(each_grade)
            print(avg)
        
        
    
            
    

class User:
    
    def __init__(self,name, *args ): #Grades are out of 100
        self.name = name
        self.grade_list = list(args)
        with open("StudentGradeTracker.json","a") as student_grade_tracker:
            json.dump({"Name" : self.name, "Grades" : self.grade_list},student_grade_tracker)
            student_grade_tracker.write("\n")
            
            
        
    def add(self,grade):
        self.grade_list.append(grade)
        new_list = []
        with open("StudentGradeTracker.json","r") as file:
            for student in file :
                person = json.loads(student)
                if person["Name"] == self.name:
                    person["Grades"] = self.grade_list
                    new_list.append(person)
                else:
                    new_list.append(person)

        with open("StudentGradeTracker.json","w") as student_grade_tracker:
            for item in new_list:
                
                json.dump(item ,student_grade_tracker)
                student_grade_tracker.write("\n")
            
                
        
        
        
        
        
chris = User("chris", 85, 60, 90 )
chris = User("lala", 85, 60, 90 )
chris.add(100)

file = StudentGradeTracker()
file.view_students_grades()
print("new file")
file.view_students_grades()
        
    
file.student_average("chris")
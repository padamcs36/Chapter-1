class Student:
    def __init__(self,name, major, gpa, on_probation): #initialization method is used
        self.name = name #self.name is actual object assign the name of the  student
        self.major = major
        self.gpa = gpa
        self.on_probation = on_probation

    def honor_of_roll(self):
        if self.gpa >=  3.5:
            return True
        else:
            return False
    # def __int__(self,company,name,version,camera):
    #     self.company = company
    #     self.name = name
    #     self.version = version
    #     self.camera = camera

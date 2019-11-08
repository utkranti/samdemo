
class Employee:
    def __init__(self,eid,enm,esal):
        self.empId = eid
        self.empName = enm
        self.empSalary = esal

    def __str__(self):
        return f'\n{self.__dict__}'

    def __repr__(self):
        return str(self)




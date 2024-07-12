from students import Student
class QuantityException(Exception):
    pass

class Group:

    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student):
        if len(self.group)>=10:
            raise QuantityException('Group cannot exceed 10 persons')
        else:
            self.group.add(student)

    def delete_student(self, last_name):
        stdnt=self.find_student(last_name)
        if stdnt!=None:
            self.group.remove(stdnt)

    def find_student(self, last_name):
        for stdnt in self.group:
            if stdnt.last_name==last_name:
                return stdnt
        return None

    def __str__(self):
        all_students = ''
        for stdnt in self.group:
            all_students+=str(stdnt)+'\n'
        return f'Number:{self.number}\n{all_students} '
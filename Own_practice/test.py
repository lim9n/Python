class Student:
      def __init__(self,name,current_class,id):
            self.name=name
            self.current_class=current_class
            self.id=id
      def __repr__(self) -> str:
        return f'Student with name: {self.name}, class: {self.current_class}, id:{self.id}'


class Teacher:
    def __init__(self, name, subject, id) -> None:
        self.name = name
        self.subject = subject
        self.id = id

    def __repr__(self) -> str:
        return f'Teacher: {self.name}, subject: {self.subject}'



class School:

      def __init__(self,name):
            self.name=name
            self.teachers=[]
            self.students=[]
      
      def add_teacher(self, name, subject):
            id = len(self.teachers) + 101
            teacher = Teacher(name, subject, id)
            self.teachers.append(teacher)
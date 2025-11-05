class Student:
    def __init__(self, name:str,grade:list[int]):
        self.name = name
        self.grade = grade



class Gradecolector:
    @staticmethod
    def average(grade:list[int]) -> float:
        return sum(grade)/len(grade)
    
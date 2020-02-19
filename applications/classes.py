class Student:
	def __init__(self, name, age, _class = "Student"):
		self.name = name
		self.age = age
		self._class = _class

	def score(self, mscore, escore, sscore):
		avg = (mscore + escore + sscore) / 3
		return avg

John = Student("John", "20")
print(John.score(5,15,20))

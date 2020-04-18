class Dog:
	def __init__(self,name):
		self.name = name

	def bark(self):
		print("Wolf!")

dog = Dog("Bumblebee")
print(dog.name)
dog.bark()
dog2 = Dog("Bettisa")
print(dog2.name)
dog2.bark()
import pickle

class dairy():
    date = 123
    text = "asdad"
    todo = ['ao','213','awd']

x = dairy()
print(pickle.dumps(x))

class dairy1():
	def __init__(self):
		self.date = 123
		self.text = "awd"
		self.todo = ['ao','213','awd']
x = dairy1()
print(pickle.dumps(x))



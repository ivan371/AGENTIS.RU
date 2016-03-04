class messages:
	def __init__(self, name):
		self.mess = []
		self.name = name

	def add_data(self, message, status, author):
		newmess = mes() 
		newmess.add(message, status, author)
		self.mess.append(newmess)

class mes:
	
	
	def add(self, status, author, message):
		self.message = message
		self.status = status
		self.author = author

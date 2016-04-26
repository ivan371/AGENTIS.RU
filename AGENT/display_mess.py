from .message import messages
from .message import mes
from .models import message

class display_mess:
	def __init__(self, p):
		if(p.who == 1):
			m = message.objects.filter(mess_from = p)
			print(m)
			self.nm = []
			for mess in m:
				flag = 0
				for messagez in self.nm:
					if messagez.name == mess.mess_to.login:
						flag = 1
						messagez.add_data(mess.status, mess.author, mess.message)
				if flag == 0:
					newmess = messages(mess.mess_to.login)
					self.nm.append(newmess)
					self.nm[-1].add_data(mess.status, mess.author, mess.message)
	
		else:
			m = message.objects.filter(mess_to = p)
			self.nm = []
			for mess in m:
				flag = 0
				for messagez in self.nm:
					if messagez.name == mess.mess_from.login:
						flag = 1
						messagez.add_data(mess.status, mess.author, mess.message)
				if flag == 0:
					newmess = messages(mess.mess_from.login)
					self.nm.append(newmess)
					self.nm[-1].add_data(mess.status, mess.author, mess.message)
				
	
		for messs in self.nm:
			messs.ammount = self.count_self_mess(messs.name)
	
	def is_mes(self):
		for messs in self.nm:
			for messagez in messs.mess:
				if(messagez.status == 0):
					return 0
					
		return 1
	def count_mess(self, who):
		num = 0
		for messs in self.nm:
			for messagez in messs.mess:
				if(messagez.status == 0 and messagez.author == who % 2):
					num = num + 1
		return num
	
	def count_self_mess(self, author):
		count = 0
		for messs in self.nm:
			if(messs.name == author):
				for messagez in messs.mess:
					count = count + 1				
		return count	
			
			
	def clear_status(self, name):
		for messs in self.nm:
			if(messs.name == name):
				for messagez in messs.mess:
					messagez.status = 1

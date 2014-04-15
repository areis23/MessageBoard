class User(object):
	name = "Guest"
	def printAccessLevel(self):
		print self.name + "'s access level is: " + self.accessLevel
	def printPassword(self):
		print self.name + "'s password is: " + self.password

class Admin(User):
	def __init__(self, password, *firstname):
		self.accessLevel = "Green"
		self.password = password
		if firstname:
			self.name = firstname[0]

	def changeUserTime(self, clientname, minutes):
		 clientname.minutes += minutes
		 print self.name + " changed " + clientname.name + "'s time by " + str(minutes) + " minutes."
		 print clientname.name + " now has " + str(clientname.minutes) + " minutes."

class Client(User):
	def __init__(self):
		self.accessLevel = "Yellow"
		self.minutes = 60
	
	def printMinutes(self):
		print self.name + " has " + str(self.minutes) + " minutes left."

	def useTime(self, minutes):
		self.minutes -= minutes
		print self.name + " used " + str(minutes) + " minutes."
	


bob = Admin("my_password", "Bob")
bob.printAccessLevel()
bob.printPassword()
guest = Client()
guest.printAccessLevel()
guest.printMinutes()
guest.useTime(20)
guest.printMinutes()
bob.changeUserTime(guest, -10)




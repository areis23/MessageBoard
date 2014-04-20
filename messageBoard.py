"""
Messaage Board is the adminstration module for an imaginary internal
company electronic message board. It manages the creation of user accounts.
Two types of users are possible: Admin users and Client users. Admin users
represent system administrators while Clients are regular users. 
"""


class User(object):

	"""Create a new system user.

	All system users have a default name of 'Guest'. 
	Public methods: print_access_level, print_password.
	"""

	name = "Guest"
	
	def print_access_level(self):
		"""Print the security access level of the called user."""
		print self.name + "'s access level is: " + self.access_level
	
	def print_password(self):
		"""Print the password of the called user."""
		print self.name + "'s password is: " + self.password

class Admin(User):

	"""Create a new Administrator user. 
	    
	Administrator users require a password and may have a name. These
	users may adjust the amount of time Client users have allocated
	for system use.
	"""
	
	def __init__(self, password, *firstname):
		"""Initialize an admin user.

		Admin users are initilized with a Green security level, the
		password provided, and the first name provided. If no first
		name is provided, the name defaults to Guest.
		Keyword arguments:
		password -- the password for the Admin being created
		firstname -- optional; the firstname of the Admin being created
		"""
		self.access_level = "Green"
		self.password = password
		if firstname:
			self.name = firstname[0]

	def change_user_time(self, clientname, minutes):
		"""Change a client's time remaining.

		Keyword arguments:
		clientname -- name of existing client user
		minutes -- number of minutes to add to client's time; Positive
		numbers of minutes increase time while negative numbers 
		decrease time."""
		clientname.minutes += minutes
		print (self.name + " changed " + clientname.name + "'s time by " + 
		        str(minutes) + " minutes.")
		print (clientname.name + " now has " + str(clientname.minutes) + 
		        " minutes.")

class Client(User):
	
	"""Create a new client (non-admin) user.

	Client users do not have a password but may have a name."""

	def __init__(self, *firstname):
		"""Initialize a client user.

		Client users are initialzied with a Yellow security level,
		60 minutes of account time, and the first name provided.
		If no first name is provided, the name defaults to Guest.
		Keyword arguments
		firstname -- optional; the first name of the Client being created
		"""
		self.access_level = "Yellow"
		self.minutes = 60
		if firstname:
			self.name = firstname[0]
	
	def print_minutes(self):
		"""Print the number of minutes the client has remaining."""
		print self.name + " has " + str(self.minutes) + " minutes left."

	def use_time(self, minutes):
		"""Deduct usage minutes from client's time and print update."""
		self.minutes -= minutes
		print self.name + " used " + str(minutes) + " minutes."
	
	
"""Admin user test"""
bob = Admin("my_password", "Bob")
bob.print_access_level()
bob.print_password()

"""Client user test - no name"""
guest = Client()
guest.print_access_level()

"""Client user test with name"""
pam = Client("Pam")
pam.print_access_level()
pam.print_minutes()
pam.use_time(20)
pam.print_minutes()
bob.change_user_time(pam, -10)




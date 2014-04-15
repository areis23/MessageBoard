import unittest
import messageBoard

class messageBoardTests(unittest.TestCase):

	def test_createNewAdminUser(self):
		admin = messageBoard.Admin("Bob")
		self.assertIsInstance(admin, messageBoard.User)

	def test_newAdminUserPassword(self):
		admin = messageBoard.Admin("my_password")
		self.assertEqual("my_password", admin.password)

	def test_newAdminUserNoPassword(self):
		self.assertRaises(TypeError, messageBoard.Admin(None))

	def test_newAdminUserDefaultName(self):
		admin = messageBoard.Admin("my_password")
		self.assertEqual("Guest", admin.name)

	def test_newClientUser(self):
		client = messageBoard.Client()
		self.assertIsInstance(client, messageBoard.User)

	def test_ClientUser_UseTime(self):
		client = messageBoard.Client()
		client.useTime(20)
		self.assertEqual(40, client.minutes)

	def test_UserChangeTime(self):
		admin = messageBoard.Admin("Bob")
		client = messageBoard.Client()
		admin.changeUserTime(client, -35)
		self.assertEqual(25, client.minutes)
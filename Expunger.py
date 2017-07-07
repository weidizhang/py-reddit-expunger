from Reddit import Reddit

__author__ = "Weidi Zhang"

import random
import string

class Expunger:
	deleteMsg = "Deleted"

	shouldDelete = False
	verboseMode = False

	def __init__(self, username, password, clientId, clientSecret):
		self.reddit = Reddit(username, password, clientId, clientSecret)

	def run(self):
		allComments = self.reddit.getComments()

		if self.reddit.login() is True:
			for commentId in allComments:
				deleteMsg = self.deleteMsg + " " + self.randomString(8)
				editSuccess = self.reddit.editComment(commentId, deleteMsg)
				
				print(commentId + " - Edit " + ("Successful" if editSuccess else "Failed"))

				if self.verboseMode:
					print("New comment body: \"" + deleteMsg + "\"")

			print("Operation completed")
		else:
			print("Login failed - check your details")

	def setDeleteMsg(self, msg):
		self.deleteMsg = msg

	def setVerboseMode(self, value):
		self.verboseMode = value

	def randomString(self, length):
		return "".join(random.choice(string.ascii_lowercase + string.ascii_uppercase + string.digits) for _ in range(length))

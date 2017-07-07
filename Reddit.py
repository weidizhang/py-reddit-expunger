__author__ = "Weidi Zhang"

import requests
import requests.auth

class Reddit:
	headerData = { "User-Agent": "py-reddit-expunger/1.0" }
	commentHardLimit = 1000

	def __init__(self, username, password, clientId, clientSecret):
		self.username = username
		self.password = password
		self.id = clientId
		self.secret = clientSecret

	def login(self):
		authData = requests.auth.HTTPBasicAuth(self.id, self.secret)
		postData = {	
			"grant_type": "password",
			"username": self.username,
			"password": self.password
		}

		loginRequest = requests.post("https://www.reddit.com/api/v1/access_token", auth = authData, data = postData, headers = self.headerData)
		responseJson = loginRequest.json()

		try:
			self.headerData["Authorization"] = "bearer " + responseJson["access_token"]
			return True
		except KeyError:
			return False

	def getComments(self):
		commentIds = []

		baseUrl = "https://www.reddit.com/user/" + self.username + "/comments.json?sort=new&after="
		commentAfter = ""

		while (commentAfter is not None) and (len(commentIds) < self.commentHardLimit):
			commentRequest = requests.get(baseUrl + commentAfter, headers = self.headerData)
			commentJson = commentRequest.json()

			for child in commentJson["data"]["children"]:
				commentId = "t1_" + child["data"]["id"]
				commentIds.append(commentId)

			commentAfter = commentJson["data"]["after"]

		return commentIds

	def editComment(self, id, message):
		postData = {
			"api_type": "json",
			"text": message,
			"thing_id": id
		}

		editRequest = requests.post("https://oauth.reddit.com/api/editusertext", data = postData, headers = self.headerData)
		editJson = editRequest.json()
		
		return len(editJson["json"]["errors"]) == 0

	def setCommentLimit(self, limit):
		self.commentHardLimit = limit

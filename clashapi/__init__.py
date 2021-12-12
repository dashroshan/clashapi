import requests
from base64 import b64decode as base64_b64decode
from json import loads as json_loads

def updatekeys(email, password, baseUrl, scopes):
	#Creating a session
	session=requests.Session()

	#Loggin in
	loginData=session.post(url=f"{baseUrl}/api/login", json={"email": email,"password": password})

	#Getting the current ip address of the system from the buffer returned by the login post
	currentIP=json_loads(base64_b64decode(loginData.json()["temporaryAPIToken"].split(".")[1]+"====").decode("utf-8"))["limits"][1]["cidrs"][0].split("/")[0]

	#Getting the list of current keys
	#If the ip address of a key is not the current one, its id, name, and description is added to the KeysToUpdate list
	currentKeys=session.post(url=f"{baseUrl}/api/apikey/list",json={}).json()["keys"]
	KeysToUpdate=[]
	for key in currentKeys:
		if key["cidrRanges"][0]!=currentIP:
			KeysToUpdate.append({"id" : key["id"], "name" : key["name"], "description": key["description"]})

	#Delete all keys with old ip addresses
	#Create new keys with name and description of old keys but with the current ip address
	for key in KeysToUpdate:
		session.post(url=f"{baseUrl}/api/apikey/revoke", json={"id" : key["id"]})
		session.post(url=f"{baseUrl}/api/apikey/create", json={"cidrRanges": [currentIP], "description": key["description"],"name": key["name"],"scopes": [scopes]})

	#Get the tokens of all updated keys
	updatedKeys=session.post(url=f"{baseUrl}/api/apikey/list",json={}).json()["keys"]
	tokens=[]
	for key in updatedKeys:
		tokens.append(key["key"])

	#Logging out
	session.post(url=f"{baseUrl}/api/apikey/revoke",json={})

	#Return a list of tokens that can now be used
	return tokens


def coc(email, password):
	return updatekeys(email,password,"https://developer.clashofclans.com","clash")


def cr(email, password):
	return updatekeys(email,password,"https://developer.clashroyale.com","royale")

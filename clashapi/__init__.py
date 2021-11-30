import requests

def coc(email,password):
	#Getting the current ip address of the system
	currentIP=requests.get("https://api.ipify.org").content.decode('utf8')

	#Creating a session
	session=requests.Session()

	#Loggin in
	session.post(url="https://developer.clashofclans.com/api/login", json={"email": email,"password": password})

	#Getting the list of current keys
	#If the ip address of a key is not the current one, its id, name, and description is added to the KeysToUpdate list
	currentKeys=session.post(url="https://developer.clashofclans.com/api/apikey/list",json={}).json()["keys"]
	KeysToUpdate=[]
	for key in currentKeys:
		if key["cidrRanges"][0]!=currentIP:
			KeysToUpdate.append({"id" : key["id"], "name" : key["name"], "description": key["description"]})

	#Delete all keys with old ip addresses
	#Create new keys with name and description of old keys but with the current ip address
	for key in KeysToUpdate:
		session.post(url="https://developer.clashofclans.com/api/apikey/revoke", json={"id" : key["id"]})
		session.post(url="https://developer.clashofclans.com/api/apikey/create", json={"cidrRanges": [currentIP], "description": key["description"],"name": key["name"],"scopes": ["clash"]})

	#Get the tokens of all updated keys
	updatedKeys=session.post(url="https://developer.clashofclans.com/api/apikey/list",json={}).json()["keys"]
	tokens=[]
	for key in updatedKeys:
		tokens.append(key["key"])

	#Logging out
	session.post(url="https://developer.clashofclans.com/api/logout",json={})

	#Return a list of tokens that can now be used
	return tokens
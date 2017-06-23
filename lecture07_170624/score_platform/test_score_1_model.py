import requests
import json

data = {
        "Inputs": {
                "input1":
                [
                    {
                            'PassengerId': "1",
                            'Survived': "0",
                            'Pclass': "3",
                            'Name': "Braund, Mr. Owen Harris",
                            'Sex': "male",
                            'Age': "22",
                            'SibSp': "1",
                            'Parch': "0",
                            'Ticket': "A/5 21171",
                            'Fare': "7.25",
                            'Cabin': "",
                            'Embarked': "S",
                    }
                ],
        },
    "GlobalParameters":  {
    }
}

body = str.encode(json.dumps(data))

url = 'https://ussouthcentral.services.azureml.net/workspaces/714aeef5a5014b17b752807c72f943a9/services/0d5820fd39f046e795fa544cfa6fe9db/execute?api-version=2.0&format=swagger'
api_key = 'p8mcFITJxB40C0p7j5w2Pjz4uCPlZTXUcp/4fpgoItANj8F9GDThlHEdRzTrP+gEsRLI6we21hSlxHa1ukGW4Q==' # Replace this with the API key for the web service
headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}

req = requests.post(url, data=body, headers=headers)

try:
    response = urllib2.urlopen(req)

    result = response.read()
    print(result)
except urllib2.HTTPError, error:
    print("The request failed with status code: " + str(error.code))

    # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
    print(error.info())
    print(json.loads(error.read()))
import urllib2
import json

data = {
        "Inputs": {
                "input1":
                [
                    {
                            'PassengerId': "1",
                            'Survived': "0",
                            'Pclass': "3",
                            'Name': "Braund, Mr. Owen Harris",
                            'Sex': "male",
                            'Age': "22",
                            'SibSp': "1",
                            'Parch': "0",
                            'Ticket': "A/5 21171",
                            'Fare': "7.25",
                            'Cabin': "",
                            'Embarked': "S",
                    }
                ],
        },
    "GlobalParameters":  {
    }
}

body = str.encode(json.dumps(data))

url = 'https://ussouthcentral.services.azureml.net/workspaces/714aeef5a5014b17b752807c72f943a9/services/0d5820fd39f046e795fa544cfa6fe9db/execute?api-version=2.0&format=swagger'
api_key = 'abc123' # Replace this with the API key for the web service
headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}

req = urllib2.Request(url, body, headers)

try:
    response = urllib2.urlopen(req)

    result = response.read()
    print(result)
except urllib2.HTTPError, error:
    print("The request failed with status code: " + str(error.code))

    # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
    print(error.info())
    print(json.loads(error.read()))

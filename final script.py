from flask import Flask
import requests
from requests.auth import HTTPBasicAuth
import json


app = Flask(__name__)

@app.route("/createjira",methods=['POST'])
def createjira():

    url = "https://aaryangupta2201.atlassian.net/rest/api/3/issue"

    auth = HTTPBasicAuth("email@gmail.com", "API TOKEN")

    headers = {
      "Accept": "application/json",
      "Content-Type": "application/json"
    }

    payload = json.dumps( {
      "fields": {
        "description": {
          "content": [
            {
              "content": [
                {
                  "text": "My first Jira ticket of the day",
                  "type": "text"
                }
              ],
              "type": "paragraph"
            }
          ],
          "type": "doc",
          "version": 1
        },

        "issuetype": {
          "id": "10006"
        },

        "project": {
          "key": "AAR"
        },

        "summary": "Main order flow broken",

        },

      "update": {}
    } )

    response = requests.request(
       "POST",
       url,
       data=payload,
       headers=headers,
       auth=auth
    )

    return json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": "))

app.run('0.0.0.0')

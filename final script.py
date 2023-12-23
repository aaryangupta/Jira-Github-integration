from flask import Flask
import requests
from requests.auth import HTTPBasicAuth
import json


app = Flask(__name__)

@app.route("/createjira",methods=['POST'])
def createjira():

    url = "https://aaryangupta2201.atlassian.net/rest/api/3/issue"

    auth = HTTPBasicAuth("aaryangupta2201@gmail.com", "ATATT3xFfGF0C8VbiFo2vxpAxX8S302EBeQmGTIUU-yen9n1lKWtGNd8ktYs7N49-9xnGTnDeMepqSfceKSj7OjQSyMKFa_sRG-ZLnPUbUnTTR3H-1UXkLLBm95_SfbC1LVWzDAMjn7hp7MgRU0P4wp3ALR9nUpW3-g2POOkpXoJjo3fZfXtU3s=1FC829FA")

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
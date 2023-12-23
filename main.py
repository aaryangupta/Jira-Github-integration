# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://aaryangupta2201.atlassian.net/rest/api/3/project"

auth = HTTPBasicAuth("aaryangupta2201@gmail.com", "ATATT3xFfGF0C8VbiFo2vxpAxX8S302EBeQmGTIUU-yen9n1lKWtGNd8ktYs7N49-9xnGTnDeMepqSfceKSj7OjQSyMKFa_sRG-ZLnPUbUnTTR3H-1UXkLLBm95_SfbC1LVWzDAMjn7hp7MgRU0P4wp3ALR9nUpW3-g2POOkpXoJjo3fZfXtU3s=1FC829FA")

headers = {
  "Accept": "application/json"
}

response = requests.request(
   "GET",
   url,
   headers=headers,
   auth=auth
)

print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))
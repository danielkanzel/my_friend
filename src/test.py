import requests  
print(requests.get("https://api.todoist.com/rest/v1/projects", headers={"Authorization": "Bearer e765a4e66d7a826f03b66ff2a8c557352b6a81f3"}).json())
import uuid, requests, json

class TodoAdapter():

    @staticmethod
    def get_tasks(token,project_id):
        try:
            response = requests.get("https://api.todoist.com/rest/v1/tasks",
                params={"project_id": project_id},
                headers={"Authorization": "Bearer %s" % token})
            return response.json()
        except:
            print("Request tasks error")


    @staticmethod
    def send_task(token,task):
        try:
            response = requests.post("https://api.todoist.com/rest/v1/tasks",
                data=task, 
                headers={
                    "Content-Type": "application/json",
                    "X-Request-Id": str(uuid.uuid4()),
                    "Authorization": "Bearer %s" % token
                })
            return response.json()
        except:
            print("Sending task error")
        


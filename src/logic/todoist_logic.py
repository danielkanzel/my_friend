import json
from datetime import datetime


class TodoLogic():

    @staticmethod
    def todo_prepare(todo_text,project_id):
        try:
            result = json.dumps({
            "content": todo_text,
            "project_id": int(project_id)
            })
            return result
        except:
            print("Preparing request error")



    @staticmethod
    def todo_created(todoist_resp):
        try:
            result = """
Задача успешно создана!
=======================================
%s""" % todoist_resp["content"]
            return result
        except:
            print("Parsing response error")

            


    @staticmethod
    def todolist_format(todo_list):
        """Todoist dict for readable table"""
        try:
            body =  """
Список текущих задач
=======================================
Создано:   | Название задачи:
---------------------------------------"""
            for item in todo_list:
                created = datetime.strptime(item["created"], "%Y-%m-%dT%H:%M:%SZ").date() 
                content = item["content"]
                row = """
%s | %s """ %(str(created), str(content))
                body = body + row  
            return body
        except:
            print("Parsing response error")
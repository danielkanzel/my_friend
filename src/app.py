from src.adapters.todoist_adapter import TodoAdapter as TA
from src.logic.todoist_logic import TodoLogic as TL
from src.logic.typewriter_logic import TypewriterLogic as TW
import configparser

# Todoist methods

def create_todo(todo_text):
    """
    Creates new todo, returns status.
    """
    token = get_from_config("Todoist","token")
    project_id = get_from_config("Todoist","project_id")
    request_body = TL.todo_prepare(todo_text,project_id)
    raw_result = TA.send_task(token,request_body)
    result = TL.todo_created(raw_result)
    return result


def get_todos():
    """
    Returns todos list in readable format
    """
    token = get_from_config("Todoist","token")
    project_id = get_from_config("Todoist","project_id")
    todos_raw = TA.get_tasks(token,project_id)
    return TL.todolist_format(todos_raw)


# Typer methods

def typer(command):
    """
    Controls typewriter sound
    """
    if command == "on":
        TW.turn_on()
        print("Озвучивание клавиш включено")
    elif command == "off":
        TW.turn_off()
        print("Озвучивание клавиш выключено")
    else:
        print("Incorrect command")


# Config method

def get_from_config(function,name):
    """
    Returns config values
    """
    config = configparser.ConfigParser()
    config.read("../resources/config.ini") 
    token = config[function][name]
    return token

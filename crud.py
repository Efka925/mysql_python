from models import eng, TodoLists, TodoItems, ThingsToDo
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=eng)
session = Session()

# CREATE
def create_todo_list(title):
    session.add(TodoLists(title=title))
    session.commit()

def create_task(list_id, name):
    session.add(TodoItems(name=name, list_id=list_id))
    session.commit()

def enter_a_new_list(ThingsToDo):
    session.add(ThingsToDo(ThingsToDo=ThingsToDo))
    session.commit()

def create_ThingsToDo_list(title):
    session.add(ThingsToDo(title=title))
    session.commit()

def create_task(list_id, name):
    session.add(ThingsToDo(name=name, list_id=list_id))
    session.commit()


# READ
def select_tasks():
    return session.query(TodoItems).all()

def select_task(id):
    return session.query(TodoItems).where(TodoItems.item_id == id).first()

def select_things_to_do():
    return session.query(ThingsToDo).all()

def select_things_to_do(id):
    return session.query(ThingsToDo).where(ThingsToDo.item_id == id).first()

def read_todo_list(list_id):
    return session.query(list_id).all()

def read_todo_list(title):
    return session.query(TodoLists).all()

def read_things_to_do(list_id):    
    return session.query(list_id).all()

def read_things_to_do(title):
    return session.query(ThingsToDo).all()

   

#CREATE A SELECT TASK FOR TODO LISTS and LIST

def select_task_todo_list(list_id):
    return session.query(TodoLists).all()

def select_task_todo_list(TodoList):
    return session.query(TodoList).all()

def select_things_to_do(list_id):
    return session.query(ThingsToDo).all()

def select_things_to_do(ThingsToDo):
    return session.query(ThingsToDo).all()


# UPDATE
def make_complete(id):
    task = select_task(id)
    task.state = True
    task.name = "asdasdasd"
    session.commit()

def make_not_complete(id):
    task = select_task(id)
    task.state = False
    session.commit()

# CREATE UPDATE FUNC TO MAKE AS NOT COMPLETE

def make_not_complete(id):
    task = select_task(id)
    task.state = False
    session.commit()

# DELETE
def delete_task(id):
    task = select_task(id)
    session.delete(task)
    session.commit()

def delete_things_to_do(list_id):
    task = select_things_to_do(list_id)
    session.delete(task)
    session.commit()

# CREATE A DELETE TASK FOR TODO LIST 

def delete_task_todo_list(id):
    task = select_task_todo_list(id)
    session.delete(task)
    session.commit()

def delete_things_to_do_list(list_id):
    task = select_things_to_do(list_id)
    session.delete(task)
    session.commit()
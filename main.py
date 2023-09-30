import crud

if __name__ == "__main__":
    list_name = input("Enter the name of the list: ")
    crud.create_todo_list(list_name)

    task_title = input("Task title: ")
    crud.create_task(1, task_title)

    tasks = crud.select_tasks()
    print(tasks[0].item_id)
    one_task = crud.select_task(tasks[0].item_id)
    crud.make_complete(one_task.item_id)

    if one_task.state:
        print("completed")
    else:
        print("not completed")
    crud.delete_task(one_task.item_id)

if __name__ == "__ThingsToDo__":
    list_name = input("Enter the name of the ThingsToDo list: ")
    crud.create_ThingsToDo_list(list_name)
    
    task_title = input("Things title: ")
    crud.create_task(1, task_title)
    
    things = crud.select_things_to_do()
    print(things[0].item_id)
    one_thing = crud.select_things_to_do(things[0].item_id)
    crud.make_complete(one_thing.item_id)
    
    if one_thing.state:
        print("completed")
    else:
        print("not completed")    
    crud.delete_task_todo_list(one_thing.item_id)

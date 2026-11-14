import json
from datetime import datetime
import os 



if not os.path.exists("Something.json") or os.path.getsize("Something.json") == 0:
    with open("Something.json","w") as file:
        json.dump([],file)

with open("Something.json") as file:
    json_load = json.load(file)

def add_task(Task,Progress):
    id = len(json_load) + 1
    new_task = Task
    progress = Progress
    new_data = {"id":id,"task":new_task,"progress":progress,"created At":str(datetime.now())}
    json_load.append(new_data)

    with open("Something.json","w") as file:
        json.dump(json_load,file,indent=4)

def del_task(id):
    found = False
    for i in range(len(json_load)):
        if id == json_load[i]['id']:
            removed = json_load.pop(i)
            print("Removed:",removed)
            print("Successfully Removed")
            found = True
            break

    if found:
        for index,item in enumerate(json_load):
            item['id'] = index+1

        with open("Something.json","w") as file:
            json.dump(json_load,file,indent=4)
    else:
        print("ID not found")


def update_task(id,description=None,progress=None):
    if os.path.exists("Something.json") and os.path.getsize("Something.json") > 0:
        with open("Something.json", "r") as file:
            json_load = json.load(file)
    else:
        print("No tasks found.")
        return
        
    found = False
    for item in json_load:
        if item['id'] == id:
                    if description is not None:
                        item['task'] = description
                    
                    if progress is not None:
                        item['progress'] = progress
                    
                    item['update_date'] = str(datetime.now())
                    found = True
                    break
    if found:
        with open("Something.json","w") as file:
            json.dump(json_load,file,indent=4)
        print(f"Sucessfully updated task ID {id}")
    else:
        print("ID NOT FOUND")

def filter_list(id=None,progress=None):
    if id is None and progress is None:
        print(json.dumps(json_load,indent=4))
        return

    found = False
    for item in json_load:
        match_id = (id is None) or (item['id'] == id)
        match_progress = (progress is None) or (item['progress'] == progress)
        
        if match_id and match_progress:
            print(item)
            found =True
    
    if not found:
        print("No matching task found")
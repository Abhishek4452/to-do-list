import json
import os
from time import sleep

tasks =[]
# loading the content which was previously store in file
if os.path.exists("my_task.json"):
    with open("my_task.json","r") as f:
        tasks = json.load(f)

def show():
    print(" ")
    print(" ")
    print("    **** ENTER A VALUE **** ")
    print("1. add tasks",end ="    ")
    print("2. mark tasks")
    print("3. delete tasks",end = " ")
    print('4. exit')
    print("5. my tasks ")



def now():
    global tasks
    with open("my_task.json","r") as f:
        data_load = json.load(f)
    for i,t in enumerate(tasks,1):
        print(f'{i}.[{t["task"]}][{'✔' if t['status'] else '✘'}]')



def add():
    global tasks
    try:
        task = input(" ENTER TASKS : ")
        if task == "":
            pass
        else:
            tasks.append({"task":task,"status":False})
        with open("my_task.json","w") as f:
            json.dump(tasks,f, indent =4)
    except:
        ValueError

def mark_tasks():
    global tasks
    print(" NUMBER OF TASKS ")
    if len(tasks) == 0:
        print("no data exists")
        
    # show all the tasks
    now()

    # mark the task
    idx=int(input(" *** which one mark ***  "))
    if  1<= idx <= len(tasks):
        tasks[idx-1]["status"]= "True"
    else:
        print(" -->         NOTHING TO MARK DOWN    ")
    

    print("#######- --- updating  ---###### ")
    sleep(1)
    with open("my_task.json","w") as f:
        json.dump(tasks,f, indent =4)
    now()



def delete_task():
    try:
        global tasks
        now()
        idx = int(input("    which one to be delete : "))
        if idx == 0:
            pass
        elif 1<=idx<=len(tasks):
            tasks.pop(idx-1)
            with open("my_task.json","w") as f:
                json.dump(tasks,f, indent =4)

        else:
            pass
    except:
        print("   *** ERROR ***  ")
        sleep(1)


def out():
    exit()


def main():
    try:
        show()
    # adding content
        choose = int(input("enter choice: "))
        if choose == 1:
            add()
        elif choose == 2:
            mark_tasks()
        elif choose == 3:
            delete_task()
        elif choose == 4:
            out()
        elif choose ==5:
            now()
        else:
             print("--------enter valid input ----- ")
    except:
        print(" -------   enter a number ------ ")
      




# running the main function
while True:
    main()
    

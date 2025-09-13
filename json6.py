# generating a menu for the funciton
def show():
    print("option_")
    print("1. ADD Task")
    print("2. mark task done ")
    print("3. delete task done")
    print("4. exit")

tasks=[]# making a free dictionary

#  loop 
while True:
    show()
    choice = input(" choose an ooption ")
    # checking the choice is right or not
    if choice.isdigit(): 
        choice = int(choice)
    else:
        print("enter a number ! not a text or any symbol")
        continue  # exit from the loop
    

    # working according to each choice

    if choice == 1: #ADD Task
        task = input("enter the task - ")
        tasks.append({"task":task,"status":False}) # adding dictionary in the list



    if choice == 2:#mark task done
        for i,t in enumerate(tasks,1):
            # printing the list for task
            print(f"{i}.{t['task']}[{'✔' if t['status'] else '✘'}]")
        
        # marking the task done
        print("enter 0 to exit")
        idx = input("task number to mark done")
        if idx.isdigit() and 1<=int(idx)<=len(tasks):
            tasks[int(idx)-1]["status"] = "True"
        elif idx == 0:
            continue
        else:
            print("invalid input ")



    if choice ==3:#delete task done
        # EMTY CONDITION CHECK
        if not tasks:
            print("no tasks to delete ")
            continue
        # PRINTING THE LIST OF TASKS
        for i,t in enumerate(t,1):
            print(f"{i}.{t['task']}")
        # TASKING THE INPUT FOR DELETING THE TASK
        idx =int(input("enter task number for deletion"))
        if idx.isdigit() and 1<=int(idx)<=len(idx):
            tasks.pop(idx -1)

        else:
            print("invalid input!, TRY WITH DIFFERENT VALUE ")





    if choice == 4:# exit
        print("exiting ....")
        break
    else:
        print("enter a valid number")




   
    
    
# generating a menu for the funciton
def show():
    print("option_")
    print("1. ADD Task",end ="         ")
    print("2. mark task done ")
    print("3. delete task done",end =" ")
    print("4. exit")

tasks=[]# making a list

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
        if task=="":
            print("")  
        else:
            tasks.append({"task":task,"status":False}) # adding dictionary in the list


    elif choice == 2:#mark task done
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


    elif choice ==3:#delete task done
        try:
              # EMTY CONDITION CHECK
            if not tasks:
                print("no tasks to delete ")
                continue
             # PRINTING THE LIST OF TASKS
            for i,t in enumerate(tasks,1):
                print(f"{i}.{t['task']}")
            # choose an ooption 2
            # 1.adding file in ppile[✔]
            # 2.adding data in textbook[✘]



            # TAKEING THE INPUT FOR DELETING THE TASK
            idx =int(input("enter task number for deletion"))
            # checking the length
            if 1<=idx<=len(tasks):
                tasks.pop(idx -1)

            else:
                print("invalid input!, TRY WITH DIFFERENT VALUE ")
        except:
            print("ERROR ______ **enter the number only -** ")




    elif choice == 4:# exit
        print("exiting ....")
        break
    




   
    
    
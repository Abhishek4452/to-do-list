tasks =[
    {"task":"buy milk","done":False},
    {"task":"study python","done":True}
]

for i , t in enumerate(tasks,1):
    status ="✔" if t["done"] else "✘"
    print(f"{i}.{t ['task']} [ {status} ]")
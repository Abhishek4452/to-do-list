# learning concept of oops for adding more feature in the to-do-list

class Task:
    def __init__ (self,des,done = False):
        self.des = des
        self.done =done

    def mark_down(self):
        self.done = True
    
    def __str__ (self):
        status = "✔" if self.done else "x"
        return f"{self.des} [{status}]"

f = Task("abhishek")
print(f.des)
print(f.done)
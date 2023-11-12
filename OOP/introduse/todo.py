class ToDo: 
    def __init__(self,string): 
        self.todo=string 
    instances=dict() 
    def give_priority(self,priority): 
        ToDo.instances[priority]=self.todo 
    def list_of_tasks(self): 
        return sorted(ToDo.instances.items()) 
    
var1=ToDo('ckelele') 
var1.give_priority(2) 
var2=ToDo('lelelele') 
var2.give_priority(3) 
var3=ToDo('HIOHOHO') 
var3.give_priority(1) 
print(var3.list_of_tasks())
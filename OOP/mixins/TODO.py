class CreateMixin:
    def create(self, todo, key):
        if key in self.todos.keys():
            return "Задача под таким ключом уже существует"
        self.todos[key] = todo
        return self.todos

class DeleteMixin:
    def delete(self, key):
        return self.todos.pop(key,1111)


class UpdateMixin:
    def update(self, key, new_value):
        self.todos[key] = new_value
        return self.todos
class ReadMixin:
    def read(self):
        return sorted(self.todos.items())

class ToDo(CreateMixin, DeleteMixin, UpdateMixin, ReadMixin): 
    todos = {}

    def set_deadline(self, date):
        import datetime
        date = date.split('/')
        date_now = datetime.datetime.now()
        date = datetime.datetime(int(date[2]), int(date[1]), int(date[0]))
        return -(date_now - date).days


task = ToDo() 
print(task.set_deadline('31/12/2022')) 
print(task.create(1, 'todo')) 
print(task.delete(3)) 
print(task.update(1, 'todo')) 
print(task.read()) 
print(task.create(1, 'Do housework')) 
print(task.create(1, 'Do housework')) 
print(task.create(2, 'Go for a walk')) 
print(task.update(1, 'Do homework')) 
print(task.delete(2)) 
print(task.read()) 
print(task.set_deadline('31/12/2021'))
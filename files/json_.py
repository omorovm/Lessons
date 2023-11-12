"================Json============"
# JavaScript Object Notation -универсальный формат, в котором мы можем хранить данные, понятных для многих языков программирования
{
    "name" : "asdf"
}
import json

# =============Dump Dumps

# сериализация - перевод в формат json

# Dumps - переводит данные в json формате str
# Dump - принимает в себя данные и файл, чтобы записать эти данные в файл

# list_= [1,2,3,4]
# data = {
#     'name':'Nikita',
#     'last_name':"Grebnev"
# }

# with open("data.json", 'w') as file:
#     json.dump(data, file)


# list_ = json.dumps(list_)
# print(type(list_)) # str

# запись строки в файлик
# with open("data.json", 'w') as file:
#     file.write(list_)

# =============Load Loads
# десериализация - перевод с json в python
# loads - переводит данные с json в python
# load - принимает файл и переводит его в python
with open("data.json", 'r') as file:
    data = file.read()
    print(type(data)) # str
    data = json.loads(data)
    # print(eval('[1,2,3,4,5,6,7,8]'))
    print(type(data)) # dict
    # data = json.load(file)
    # print(type(data)) 

    # csv -
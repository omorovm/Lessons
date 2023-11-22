
# username
# email
# password
# password_confirm
# запись в бд
import re
{1:['username', '...'], 2:[]}

class RegisterUserMixin:
    id = 1
    def register(self, username, email, password, password_confirm) -> None:
        self.id = RegisterUserMixin.id
        RegisterUserMixin.id+=1
        self.username = username
        self.email = email
        self.password = password
        self.password_confirm = password_confirm
        self._validate_password()
        self._validate_email()
        self.database.update({self.id:[username, email, password]})
    
    def _validate_password(self):
        symbols = '!@#$%^&*_+-~`'
        if not self.password == self.password_confirm:
            raise Exception('Пароли не совпадают')
        if len(self.password) <= 8:
            raise Exception('длина пароля должна превышать 8 символов')
        if not any(i.isalpha() for i in self.password):
            raise Exception('Пароль дожен состоять из букв')
        elif not any(i.isdigit() for i in self.password):
            raise Exception('Пароль дожен состоять из цифр')
        elif not any(i in symbols for i in self.password):
            raise Exception('Пароль дожен состоять из символов')
        
    def _validate_email(self):
        if not re.match(r'^[a-zA-Z0-9.+-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)+$', self.email):
            raise Exception("не правильная почта")
        for v in self.database.values():
            if self.email in v:
                raise Exception("такой пароль уже существует")
        
# regex
# regular expressions (регулярные вырфжения)

class LoginUserMixin:
    def login(self,email, password):
        for user_id, user_data in self.database.items():
            if user_data[1] == email and user_data[2] == password:
                print("Успешно залогинились")
                return {"id":user_id, "username":user_data[0], 'email':user_data[1]}
        print("неправильная почта или пароль")

class GetUserMixin:
    def retrieve(self, id):
        if id in self.database:
            return {"id": id, "username":self.database[id][0], 'email':self.database[id][1]}
        return "нет такого id"
    def listing(self):
        return self.database
    
class DeleteUserMixin:
    def delete(self, user_id):
        return self.database.pop(user_id) if self.database.get(user_id) else "нет такого юзера"

class UpdateUserMixin:
    
    def update_username(self, user_id, new_username):
        if self.database.get(user_id):
            self.database[user_id][0] = new_username
        else:
            print("нет такого юзера")

    def update_password(self, user_id, new_password):
        if self.database.get(user_id):
            self.database[user_id][2] = new_password
        else:
            print("нет такого юзера")

class User(
    RegisterUserMixin, 
    LoginUserMixin, 
    GetUserMixin, 
    DeleteUserMixin, 
    UpdateUserMixin
    ):
    
    database = {}

user = User()
user.register('username', 'ff@gmail.com', '12345678!FFd', '12345678!FFd')
user.register('username', 'ahdgsfgd@gmail.com', '213423regf!D', '213423regf!D')
print(user.database)
user.login("ff@gmail.com", "12345678!FFd")
print(user.retrieve(1))
user.update_username(11, 'qwetry')
print(user.listing())

# user = RegisterUser('username', 'ff@gmail.com', '12345678!FFd', '12345678!FFd')
# user1 = RegisterUser('username', 'ff@gmail.com', '12345678!FFd', '12345678!FFd')
# user2 = RegisterUser('username', 'ff@gmail.com', '12345678!FFd', '12345678!FFd')
# user3 = RegisterUser('username', 'ff@gmail.com', '12345678!FFd', '12345678!FFd')
# user4 = RegisterUser('username', 'ff@gmail.com', '12345678!FFd', '12345678!FFd')

# написать validate_email, который будет проверять наличие сущ. email

# ToDo: CRUD - user
# listing
# retrieve
# update
# delete
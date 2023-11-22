class User:

    def __init__(self, name: str, lastname: str, email: str) -> None:
        self.name = name
        self.lastname = lastname
        self.email = email
    
    @classmethod
    def create_user(cls, string) -> None:
        list_ = string.split()
        return cls(list_[0][:-1], list_[1][:-1], list_[2])

    @staticmethod
    def validate_email(email):
        return email.__contains__('@')

    def __str__(self) -> str:
        if self.validate_email(self.email):
            return f'{self.name}: {self.email}'
        return 'email в неправильном формате'
    
user1 = User.create_user('John, Snow, john@email.com')
user2 = User.create_user('John, Snow, johnemail.com')
print(user1) 
print(user2)
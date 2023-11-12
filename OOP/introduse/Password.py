class Password: 
    def __init__(self,password): 
        self.passw = password 
    def validate(self): 
        if len(self.passw) not in range(8,15): 
            raise ValueError('Password should be longer than 8, and less than 15') 
        if not any(c.isdigit() for c in self.passw): 
            raise ValueError('Password should contain numbers too') 
        if not any(c.isalpha() for c in self.passw): 
            raise ValueError('Password should contain letters as well') 
        if not any(i in ['@', '#', '&', '$', '%', '!', '~', '*'] for i in self.passw): 
            raise ValueError('Your password should have some symbols') 
        return 'Ваш пароль сохранен.' 
    def __str__(self): 
        return '*' * len(self.passw) 

obj = Password('ads1@12') 

print(obj.validate())
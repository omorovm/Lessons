class Language:
    def __init__(self, level, type) -> None:
        self.level = level
        self.type = type

class Python(Language):
    def write_function(self, func_name, arg):
        return f'def {func_name}({arg}):'

    def create_variable(self, var_name, value):
        if type(value) is str:
            value = "'"+value+"'"
        return f"{var_name} = {value}"

class JavaScript(Language):
    def write_function(self, func_name, arg):
        return f'function {func_name}({arg})'+' {     };'

    def create_variable(self, var_name, value):
        if type(value) is str:
            value = "'"+value+"'"
        return f"let {var_name} = {value};"
    
py = Python(12,'backend')
print(py.write_function('get_code', 'a')) 
print(py.create_variable('name', 'John'))

js = JavaScript(0, 'frontend')
print(js.write_function('validate', 'form')) 
print(js.create_variable('password', 'john@123'))
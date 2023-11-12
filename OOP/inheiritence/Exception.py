class CustomError(Exception):
    def __init__(self, message, *args: object) -> None:
        super().__init__(message)
    
def check_letters(s: str):
    if s.isupper():
        return f'ВСЕ ОТЛИЧНО! {s}'
    raise capitals_error

print(check_letters("HELLO"))
capitals_error = CustomError("ТОЛЬКО БОЛЬШИЕ БУКВЫ РАЗРЕШЕНЫ В ЭТОМ КОДЕ")
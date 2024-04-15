#Lab 3

def Factorial(value: int, account: int = 1):
    if value == 0:
        return account
    
    return Factorial(value - 1, value * account) # Не чистая функция

print(Factorial(5))

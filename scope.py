def func1():
    x = 3
    print(x)

def func2():
    x = 4
    print(x)

def func2(num1:int, num2:int)->str:
    '''This adds two numbers
        params
            num1: the first number
            num2: the second number; can be decimal

        -> return string 
    '''
    return str(num1 + num2)

x = 2
print(x)

func1()

print(x)

sum = func2(7, 4)
print(sum)
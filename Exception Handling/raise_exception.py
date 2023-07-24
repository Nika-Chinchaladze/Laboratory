def my_function(num1: int):
    if type(num1) != int:
        raise TypeError("Argument must be Integer!")
    return num1 * 10


answer = my_function(num1='50')
print(answer)

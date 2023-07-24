import logging


# N1 First simple example
def my_function(num1: float, num2: int):
    division = num1 / num2
    return division


try:
    # the statements that can cause the error
    answer = my_function(num1=10, num2=0)

except ZeroDivisionError as e:
    # handlers for different exceptions
    # __str__ dunder method will print out built-in error message
    print(str(e))

else:
    # code enters the else block only if the try clause does not raise an exception
    print(answer)

finally:
    # is always executed after the try and except blocks.
    print("Operation has been completed!")


# N2 Second multiple handling example
my_list = [5, 10, 0, "name", 15]

for item in my_list:
    try:
        answer = 150 / int(item)
    except (ZeroDivisionError, ValueError) as m:
        # prints default error messages
        print(str(m))
    except Exception as e:
        logging.exception(e)
    else:
        print(answer)

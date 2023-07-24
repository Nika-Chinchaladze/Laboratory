"""
When we catch the exception in try-except block, but then raise it anyway.
Before re-raise it we may execute some action: write something in file, close connection...
We let the program crash, but before we execute some addition staff.
"""
my_list = [1, 0, 2, "name"]

for item in my_list:
    try:
        print(40 / int(item))
    except ZeroDivisionError as a:
        print(str(a))
    except ValueError as b:
        print("close database connection!!!")
        raise


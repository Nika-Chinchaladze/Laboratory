"""
At this time program is not crashed - it continues execution process,
but during each exception occurrence -> it gives more information about
what kind of exception was faced and handled.
Good for debugging purposes.
"""
import logging


my_list = [1, 2, 0, "name", 5, 10]

for item in my_list:
    try:
        print(50 / int(item))
    except Exception as e:
        logging.exception(e)

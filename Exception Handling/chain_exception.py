"""
when we want to raise an exception in response to catching a different exception,
and return information about both exceptions - error messages.
Like the reason of exception won't crash the execution of program, but we will
do it manually by raising another Exception.
"""


def type_cast(value):
    return int(value)


try:
    answer = type_cast(value="nika")
except ValueError as e:
    raise KeyError("Just For Example") from e
else:
    print(answer)

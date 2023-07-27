import asyncio


# ======================================= async generator function ======================================= #
async def func1():
    for i in range(10):
        yield i


# async list comprehension -> with async generator
async def my_list():
    result = [i async for i in func1() if i % 2 == 0]
    return result


# async dict comprehension -> with async generator
async def my_dict():
    result = {i: i*2 async for i in func1() if i % 2 == 0}
    return result


# async set comprehension -> with async generator
async def my_set():
    result = {i async for i in func1() if i % 2 == 0}
    return result


# async & await --> imitation of asyncio.gather() - but much slower
# await comprehension executes coroutines one-by-one sequentially,
# asyncio.gather() - executes tasks concurrently
async def first():
    return "first"


async def second():
    return "second"


async def third():
    return "third"


async def together():
    task_1 = asyncio.create_task(first())
    task_2 = asyncio.create_task(second())
    task_3 = asyncio.create_task(third())
    all_tasks = [task_1, task_2, task_3]
    # collect results of all awaitables in one list
    result = [await func for func in all_tasks]
    return result


list_answer = asyncio.run(my_list())
dict_answer = asyncio.run(my_dict())
set_answer = asyncio.run(my_set())
await_answer = asyncio.run(together())

print(list_answer)
print(dict_answer)
print(set_answer)
print(await_answer)


# ======================================= async iterator ======================================= #
class AsyncIterator:
    def __init__(self):
        self.counter = 0

    def __aiter__(self):
        return self

    async def __anext__(self):
        if self.counter >= 10:
            raise StopAsyncIteration
        self.counter += 1
        return self.counter


# async list comprehension -> with async iterator
async def my_list_iterator():
    result = [i async for i in AsyncIterator()]
    return result


# async dict comprehension -> with async iterator
async def my_dict_iterator():
    result = {i: i*2 async for i in AsyncIterator()}
    return result


# async set comprehension -> with async iterator
async def my_set_iterator():
    result = {i async for i in AsyncIterator()}
    return result

list_answer_iterator = asyncio.run(my_list_iterator())
dict_answer_iterator = asyncio.run(my_dict_iterator())
set_answer_iterator = asyncio.run(my_set_iterator())

print(list_answer_iterator)
print(dict_answer_iterator)
print(set_answer_iterator)

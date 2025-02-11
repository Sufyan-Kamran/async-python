import asyncio

async def task1():
    await asyncio.sleep(5)
    print('task 1')

async def task2():
    await asyncio.sleep(2)
    print('task 2')

async def task3():
    for i in range(1,8):
        await asyncio.sleep(1)
        print(f'Normal tasks {i}')

async def main():
    async with asyncio.TaskGroup() as tg:
        t1 = tg.create_task(task1())
        t2 = tg.create_task(task2())
        t3 = tg.create_task(task3())

#asyncio.run(main())

async def eternity():
    # Sleep for one hour
    await asyncio.sleep(2)
    print('yay!')

async def main():
    # Wait for at most 1 second
    try:
        await asyncio.wait_for(eternity(), timeout=3)
    except TimeoutError:
        print('timeout!')

asyncio.run(main())
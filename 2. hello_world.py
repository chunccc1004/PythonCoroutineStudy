import asyncio
import time


async def say_after(delay, text):
    await asyncio.sleep(delay)
    print(text)


async def hello_world_sync():
    print(f'Started at {time.strftime("%X")}')
    await say_after(1, 'hello')
    await say_after(2, 'world')
    print(f'Finished at {time.strftime("%X")}')


# task로 동시 실행 -> 즉, async
async def hello_world_async():
    task1 = asyncio.create_task(say_after(1, 'hello'))
    task2 = asyncio.create_task(say_after(2, 'world'))

    print(f'Started at {time.strftime("%X")}')
    await task1
    await task2
    print(f'Finished at {time.strftime("%X")}')


asyncio.run(hello_world_sync())
asyncio.run(hello_world_async())

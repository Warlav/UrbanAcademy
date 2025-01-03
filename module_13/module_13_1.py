import asyncio


async def start_strongman(name, power):
    ball_num = 1
    print(f'Силач {name} начал соревнования.')
    while ball_num <= 5:
        await asyncio.sleep(ball_num / power)
        print(f'Силач {name} поднял {ball_num}')
        ball_num += 1
    print(f'Силач {name} закончил соревнования.')


async def start_tournament():
    task_1 = asyncio.create_task(start_strongman('Pasha', 6))
    task_2 = asyncio.create_task(start_strongman('Denis', 4))
    task_3 = asyncio.create_task(start_strongman('Apollon', 5))
    await task_1
    await task_2
    await task_3


asyncio.run(start_tournament())

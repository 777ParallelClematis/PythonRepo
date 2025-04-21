import asyncio
from asyncio import Task
import datetime

async def fetch_data(input_data: int, *, delay: int) -> dict:
    print('Fetching data...')

    start_time: datetime.datetime = datetime.datetime.now()
    await asyncio.sleep(delay)
    end_time: datetime.datetime = datetime.datetime.now()

    print('Data retrieved!')
    return {
        'input': input_data,
        'start_time': f'{start_time:%H:%M:%S}',
        'end_time': f'{end_time:%H:%M:%S}'
    }

async def main() -> None:
    task: Task = asyncio.create_task(fetch_data(1, delay=3))
    await asyncio.sleep(1)
    print('Running other code...')
    data: dict = await task
    print(data)

if __name__ == '__main__':
    asyncio.run(main())


#also: gather(), import the Future type
from datetime import datetime
import asyncio
from asyncio import Future

import requests
from requests import Response

async def check_status(url: str) -> dict[str, int | str]:
    start_time: datetime = datetime.now()
    response: Response = await asyncio.to_thread(requests.get, url, None)
    end_time: datetime = datetime.now()

    return {'website': url,
            'status': response.status_code,
            'start_time': f'{start_time:%H:%M:%S}',
            'end_time': f'{end_time:%H:%M:%S}',
            }


async def main() -> None:
    print('Fetching Results:')
    tasks: Future = asyncio.gather(
        check_status('https://bing.com'),
        check_status('https://google.com'),
        check_status('https://youtube.com'),
        check_status('https://bbc.com'),
        check_status('https:lol'), #doesnt exist, what we're testing out
        return_exceptions=True
    )
    results: list[dict] = await tasks
    for result in results:
        print(result)

if __name__ == '__main__':
    asyncio.run(main=main())
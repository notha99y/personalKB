import asyncio
import time

import aiohttp
from tqdm import tqdm


async def download_site(session, url):
    async with session.get(url) as response:
        length = len(response.content)
        # print(f"Read {len(response.content)} from {url}")


async def download_all_sites_asyncio(sites):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for url in tqdm(sites):
            task = asyncio.ensure_future(download_site(session, url))
            tasks.append(task)
        await asyncio.gather(*tasks, return_exceptions=True)


if __name__ == "__main__":
    sites = [
        "https://www.jython.org",
        "http://olympus.realpython.org/dice",
    ] * 1000

    start_time = time.time()
    asyncio.get_event_loop().run_until_complete(
        download_all_sites_asyncio(sites)
    )
    duration = time.time() - start_time
    print(f"Downloaded {len(sites)} sites in {duration} seconds")

import time

import requests
from tqdm import tqdm


def download_all_sites(sites):
    def download_site(url, session):
        with session.get(url) as response:
            length = len(response.content)

    #         print(f"Read {len(response.content)} from {url}")
    with requests.Session() as session:
        for url in tqdm(sites):
            download_site(url, session)


if __name__ == "__main__":
    sites = [
        "https://www.jython.org",
        "http://olympus.realpython.org/dice",
    ] * 1000
    start_time = time.time()
    download_all_sites(sites)
    duration = time.time() - start_time
    print(f"Downloaded {len(sites)} in {duration} seconds")

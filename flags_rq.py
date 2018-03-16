import time

from redis import Redis
from rq import Queue

from flags_sequential import download_one, flag_images

q = Queue(connection=Redis(host='redis'))

def download_many(url_list):
    for url in url_list:
        q.enqueue(download_one, url)


def main():
    start = time.time()
    download_many(flag_images)
    end = time.time()
    elapsed = round(end - start, 4)
    print(elapsed)

if __name__ == '__main__':
    main()
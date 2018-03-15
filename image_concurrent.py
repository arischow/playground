import time
from concurrent import futures

from image_sequential import download_flag, flag_images


def download_many(url_list):
    with futures.ThreadPoolExecutor(21) as executor:
        executor.map(download_flag, sorted(url_list))


def main():
    start = time.time()
    download_many(flag_images)
    end = time.time()
    elapsed = round(end - start, 4)
    print(elapsed)


if __name__ == '__main__':
    main()

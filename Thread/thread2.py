import sys
import time
import concurrent.futures
import requests

img_urls = ['https://pixabay.com/get/gf1a238e2982a8ca3133ba4a9f7cb4db8438be90b74885e72d16ec7e3f604d00e150c9b00b39a98a59942255bd9de38983077cfaa161d1b104bb404d273bae119b07fb9fbf160f3e1f8215081f04eaca2_1920.jpg',
'https://pixabay.com/get/g00f4426320d22da4e94b9ba518ba83dc19a27e8b185a09f91e663d81ca35de6a1fc2d9a6e129497e8974b69e54642cf2bbd099e312460e15b2cdc82efe9cf1e4366f0774f95472d35180f92762342899_1920.jpg']

def download_image(img_url):
    img_bytes = requests.get(img_url).content
    img_name = img_url.split('/')[4]
    with open(img_name, 'wb') as img_file:
        img_file.write(img_bytes)
        print(f"{img_name} was downloaded")

if __name__ == '__main__':
    start = time.perf_counter()

    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(download_image, img_urls)

    end = time.perf_counter()
    print(f"Tasks ended in {round(end - start, 2)} second(s)")

    sys.exit()

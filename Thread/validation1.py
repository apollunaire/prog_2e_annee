import sys
import threading
import time
import concurrent.futures
import requests
import multiprocessing
import statistics

img_urls = ['https://pixabay.com/get/gf1a238e2982a8ca3133ba4a9f7cb4db8438be90b74885e72d16ec7e3f604d00e150c9b00b39a98a59942255bd9de38983077cfaa161d1b104bb404d273bae119b07fb9fbf160f3e1f8215081f04eaca2_1920.jpg',
'https://pixabay.com/get/g00f4426320d22da4e94b9ba518ba83dc19a27e8b185a09f91e663d81ca35de6a1fc2d9a6e129497e8974b69e54642cf2bbd099e312460e15b2cdc82efe9cf1e4366f0774f95472d35180f92762342899_1920.jpg']

def usage():
    print("USAGE - erreur quelque part")
    return -1


def download_image1(img_url):
    img_bytes = requests.get(img_url).content
    img_name = img_url.split('/')[4]
    with open(img_name, 'wb') as img_file:
        img_file.write(img_bytes)
        #print(f"{img_name} was downloaded")


def threadingT():
    start = time.perf_counter()
    t1 = threading.Thread(target=download_image1, args=[img_urls[0]])
    t1.start()
    t2 = threading.Thread(target=download_image1, args=[img_urls[1]])
    t2.start()
    t1.join() # j'attends la fin de la thread
    t2.join() # j'attends la fin de la thread
    end = time.perf_counter()
    #print(f"THREADING T - Tasks ended in {round(end - start, 2)} second(s)")
    return round(end - start, 2)


def pool():
    start = time.perf_counter()
    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(download_image1, img_urls)
        end = time.perf_counter()
        #print(f"POOL - Tasks ended in {round(end - start, 2)} second(s)")
    return round(end - start, 2)


def multiprocess():
    start = time.perf_counter()
    p1 = multiprocessing.Process(target=download_image1(img_urls[0]))
    p2 = multiprocessing.Process(target=download_image1(img_urls[1]))
    p1.start()
    p2.start()
    end = time.perf_counter()
    #print(f"MULTIPROCESS - Tasks ended in {round(end - start, 2)} second(s)")
    return round(end - start, 2)


def test(x):
    t, p, m = [], [], [] #stockage valeurs
    for k in range(x):
        t.append(threadingT())
        p.append(pool())
        m.append(multiprocess())
    print(f"le temps moyen d'execution de la fonction 1 est de {round(statistics.mean(t), 3)}s\n{t}\nl'écart type est de {round(statistics.stdev(t), 2)}s\n") #valeur moyenne
    print(f"le temps moyen d'execution de la fonction 2 est de {round(statistics.mean(p), 3)}s\n{p}\nl'ecart type est de {round(statistics.stdev(p), 2)}s\n")
    print(f"le temps moyen d'execution de la fonction 3 est de {round(statistics.mean(m), 3)}s\n{m}\n l'écart type est de {round(statistics.stdev(m), 2)}s\n")
    return 0

if __name__=='__main__':
    x = int(input("nombre de tests"))
    test(x)
    sys.exit()
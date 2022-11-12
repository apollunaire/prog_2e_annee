import threading
import time
import sys



def task(i):
    print(f"Task {i} starts")
    time.sleep(1)
    print(f"Task {i} ends")


if __name__ == '__main__':
    start = time.perf_counter()

    t1 = threading.Thread(target=task, args=[1])  # création de la thread
    t1.start()  # je démarre la thread
    t1.join()  # j'attends la fin de la thread
    end = time.perf_counter()

    print(f"Tasks ended in {round(end - start, 2)} second(s)")

    start = time.perf_counter()
    t1 = threading.Thread(target=task, args=[1])
    t1.start()
    t2 = threading.Thread(target=task, args=[2])
    t2.start()
    t1.join()  # j'attends la fin de la thread
    t2.join()  # j'attends la fin de la thread
    end = time.perf_counter()
    print(f"Tasks ended in {round(end - start, 2)} second(s)")

    t1 = threading.Thread(target=task(1))  # création de la thread
    t1.start()  # je démarre la thread
    t2 = threading.Thread(target=task(2))  # création de la thread
    t2.start()  # je démarre la thread
    t1.join()  # j'attends la fin de la thread
    t2.join()  # j'attends la fin de la thread

    T = []
    for i in range(100):  # lancement de 100 thread
        T.append(threading.Thread(target=task, args=[i]))
    for i in range(len(T)):
        T[i].start()
    for i in range(len(T)):
        T[i].join()

    sys.exit()

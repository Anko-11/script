import ping3
import threading
import multiprocessing


def ping(i):
    second = ping3.ping(f'192.168.17.{i}')
    print(f"192.168.17.{i}", second)


# for i in range(1, 255):
#     t = threading.Thread(target=ping, args=(i,))
#     t.start()

if __name__ == "__main__":
    for i in range(1, 255):
        p = multiprocessing.Process(target=ping, args=(i,))
        p.start()

import random
import threading
import _thread
import time


# def thread1(*args):
#     print('sub-thread:', threading.current_thread().name)
#     print(args)
#
#
# def create_thread1():
#     _thread.start_new_thread(thread1, ("data1", "data2"))
#     print('main thread:', threading.current_thread().name)
#     time.sleep(3)

# ************ IMPORTANT ****************
# Thread

import requests


def thread2(*args):
    print("sub thread:", threading.current_thread().name)
    print("args:", args)

def create_thread2():
    t = threading.Thread(target=thread2, args=('data1', 'data2'))
    t.start()


# self-defined thread
class MyThred(threading.Thread):
    def __init__(self, url):
        super().__init__()
        self.url = url

    def run(self) -> None:
        time.sleep(random.uniform(2, 4))

        # print('sub-thread:', threading.current_thread().name)
        res = requests.get(self.url)
        print(len(res.text), self.url)

def create_thread3():
    MyThred('http://www.qq.com').start()
    MyThred('http://www.baidu.com').start()

if __name__ == '__main__':
    create_thread3()

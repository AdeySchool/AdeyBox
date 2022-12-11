import threading
from socket import *
import sys
from colorama import init
from colorama import Fore

init(autoreset=True)

lock = threading.Lock()  # 确保 多个线程在共享资源的时候不会出现脏数据
openNum = 0  # 端口开放数量统计
threads = []  # 线程池


def portscanner(host, port):
    global openNum
    try:
        s = socket(AF_INET, SOCK_STREAM)
        s.connect((host, port))
        lock.acquire()
        openNum += 1

        print(
            f"[\033[0;32;40mINFO\033[0m]{Fore.BLUE}{Fore.WHITE} {ip} ====>> {Fore.GREEN}{port} {Fore.WHITE} [open]")
        lock.release()
        s.close()
    except:
        pass


def main(ip, ports=range(65535)):  # 设置 端口缺省值0-65535
    setdefaulttimeout(1)
    for port in ports:
        t = threading.Thread(target=portscanner, args=(ip, port))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    print(f"{ip} is open post {openNum}")


if __name__ == '__main__':
    print("===============端口扫描===============")
    ip = sys.argv[1]
    main(ip)

import socket
import re


def web_ip(website):
    ip = socket.gethostbyname(website)
    print(f"{website} ====> {ip}")

def web_file(file_name):
    ip_list={}
    with open(file_name,'r') as file:
        for web_url in file.readlines():
            url=str(web_url.strip())
            reip=re.findall('((\w+\.\w+\.\w+)|(\w+\.\w+))',url)
            for b in  reip:
                url_web=str(b[0])
                ip = socket.gethostbyname(url_web)
                ip_list[url_web]=ip
        for key,value in ip_list.items():
            print(f'{key} ====> {value}')




if __name__=="__main__":
    while True:
        print('')
        print('     A:单域名转换IP.')
        print('     B:多域名转换IP.')
        print('     C:提出程序     ')
        print('')
        b = input('请输入选项：')
        if b == 'A':
            website = input("请输入域名：")
            if re.match('((\w+\.\w+\.\w+)|(\w+\.\w+))', website):
                web_ip(website=website)
                print('')
            else:
                print('请输入正确的域名！')
                print('')
        elif b == 'B':
            file_name = input('请输入文件名(带扩展名)：')
            web_file(file_name=file_name)
        elif b == 'C':
            print('Bye!')
            break
        else:
            print('请输入正确的选项！')

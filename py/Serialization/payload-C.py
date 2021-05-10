#!/usr/bin/python3
import pickle,flag
class Person():
    pass
b = b'\x80\x03c__main__\nPerson\n)\x81}(Vtest\ncflag\nflag\nub.'
print(pickle.dumps(Person))
print(pickle.loads(b).test)

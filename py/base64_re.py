#!/usr/bin/python3
import base64

s = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789+/"
table = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
enc = "tvjdvez7D0vSyZbnzv90mf9nuKnurL8YBZiXiseHFq=="
ans = enc.translate(str.maketrans(table,s))
print(base64.b64decode(ans))
#!/usr/bin/python3
import mmh3
import requests
#bypass cnd by search it's hash
#like this :  http.favicon.hash:1540412544
respones = requests.get('http://ping.chinaz.com/www.xueersi.com')
favicon = respones.content
hash = mmh3.hash(favicon)
print('hash:'+str(hash))
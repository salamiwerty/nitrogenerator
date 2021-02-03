import random, string
import webbrowser
import time
import requests

print("""Werty Nitro Gift Generator + Checker""")
time.sleep(2)
print("Creator  -  https://github.com/salamiwerty/")
time.sleep(2)
print("twitch.tv/salamiwerty\n")
time.sleep(2)
print("Now CJ, the pet that creates the Nitros, is going to talk to you!")
time.sleep(2)

num=input('CJ: Wsp man, what codes do you check bro?')

f=open("Nitro Codes boi.txt","w", encoding='utf-8')

print("Wait, Generating for you!")
      
for n in range(int(num)):
   y = ''.join(random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for _ in range(16))
   f.write('https://discord.gift/')
   f.write(y)
   f.write("\n")

f.close()

#=============Checker=========================


with open("Nitro Codes.txt") as f:
    for line in f:
        nitro = line.strip("\n")

        url = "https://discordapp.com/api/v6/entitlements/gift-codes/" + nitro + "?with_application=false&with_subscription_plan=true"

        r = requests.get(url)

        if r.status_code == 200:
            print(" VALID!!!!!!!!!!!!!!!!!!!!!!!!! | {} ".format(line.strip("\n")))
            break
        else:
        	print(" Invalid / {} ".format(line.strip("\n")))
input("Finish! Press 5 times to end!")
input("4")
input("3")
input("2")
input("1")

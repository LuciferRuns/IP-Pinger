import sys

if sys.version_info < (3, 0):
    print("Python 3 or later is required to run this script.")
    sys.exit(1)

import socket
import time

def ping_spam(target_ip, interval=0.5):
    while True:
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(1)
                s.connect((target_ip, 80))
                print(f"Ping to {target_ip} successful!")
        except Exception as e:
            print(f"Ping to {target_ip} failed: {e}")
        time.sleep(interval)

target_ip = input("Enter the target IP address: ")
ping_spam(target_ip)

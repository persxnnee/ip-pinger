import os
import time

os.system('Mode Con Cols=35 Lines=30')

#main pannel
while(True):
    os.system('cls')
    os.system('color A')

    print("---------------------------------")
    print("-         CMSS IP PINGER        -")
    print("---------------------------------")
    print("\n")

    try:
    print("a/ CMSS info")
    print("b/ ip pinger")
    print("\n")
    x=input("Enter : ")
    break


def info():
    os.system('cls')
    print("----------------------------")
    print("-Discord : CMSS666#0001")
    print("-GitHub : github.com/CMSS666")
    print("-Youtube : INVISIBLE")
    print("----------------------------")
    time.sleep(5)


def ip_ping():
    os.system('cls')
    print("Enter IP Address: ", end='')

    ip = input()

    os.system('cls')
    print('Pinging:', ip)
    os.system('ping -n 2 {}'.format(ip))

    print('-' * 60)
    time.sleep(5)




if x == "a":
    info()
elif x == "b":
    ip_ping()
else:
    os.system('cls')
    print("-------------------")
    print("-No assigned key !-")
    print("-------------------")
    time.sleep(5)


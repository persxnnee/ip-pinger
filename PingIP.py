import os
import time
import sys


def info():
    os.system('cls')
    print("Coded by CMSS_\n")
    print("Github: github.com/CMSS666")
    time.sleep(5)



def customIP():
    os.system('cls')
    print("Enter IP Address: ", end='')

    ip = input()

    os.system('cls')
    print('Pinging:', ip)
    os.system('ping -n 2 {}'.format(ip))     

    print('-'*60)
    time.sleep(5)

while(True):
    os.system('cls')   

    print("Ping Menu:\n")
    print("1) for more info")
    print("2) Input custom IP to ping.")
    print("3) Exit.")
    print("\n\nEnter : ", end='')

    try:
        i = int(input())

        if(i==1):
            info()
        elif(i==2):
            customIP()
        elif(i==3):
            break
    except:
        #loop restarts
        print("Error!")
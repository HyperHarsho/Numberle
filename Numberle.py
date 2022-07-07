from os import system, name
from colorama import Fore
import random


def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


clear()
n = str(random.randint(1000, 9999))
tries = 0
while(tries < 7):
    cor = 0
    Fore.RESET
    s = ""
    num = str(input("Enter four digit number:\n"))
    if num.isdigit:
        tries = tries + 1
        for i in range(len(num)):
            if(n[i] == num[i]):
                s = s + Fore.GREEN + num[i] + Fore.RESET
                cor = cor + 1
            elif(n.find(num[i]) != -1):
                s = s + Fore.YELLOW + num[i] + Fore.RESET
            else:
                s = s + Fore.BLACK + num[i] + Fore.RESET
        print(s + Fore.RESET)
        if(n == num):
            print("You guessed correct")
            exit(0)
        print("You have "+str(7-tries)+" left")
    else:
        print("Try again")
        continue
print("You ran out of tries")
print("Answer - "+n)

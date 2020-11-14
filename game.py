import random
import os
from subprocess import call
from time import sleep
import pyfiglet


os.system('clear')
print("Remember The Number")
sleep(2)
os.system('clear')



RANDOMNUMS = random.sample(range(1,15), 5)
print(RANDOMNUMS)
sleep(2)
os.system('clear')


NewList = RANDOMNUMS[:]
for i in range(0,2):
    Index = random.sample(range(0,5),2)


result = []
for x in Index:
    while True:
        y = random.randint(1,14)
        if NewList[x] == y:
            continue
        else:
            NewList[x] = y
            result.append(x+1)
            break
print(NewList)
result.sort()


try:
    user = input('Which numbers are changed?')
    user = user.split(',')
    user.sort()
    user = [int(x) for x in user]
    if user == result:
        print(pyfiglet.figlet_format('You WON :)'))
    else:
        print(pyfiglet.figlet_format('You LOST :('))
        result = [str(x) for x in result]
        result = ','.join(result)
        print(f"Correct answer: {result}")
except ValueError:
    print("You should seprate the answer with semi colon ','")










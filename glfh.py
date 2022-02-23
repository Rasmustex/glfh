from random import randint
import keyboard 
import re
from time import sleep


def setuplist():
    f = open("source.txt", "rb")
    s = f.read().decode('utf-8', errors='ignore')
    f.close()
    s = re.findall("\[(.*)\]", s)
    return s

def run():
    charlist = setuplist()
    while True:
        keyboard.wait('-')
        sleep(0.1)
        proper_len = False
        while not proper_len:
            pog = 0
            used = []
            mesg = []
            for x in range(4):
                pog = randint( 0, 3 )
                while pog in used:
                    pog = randint( 0, 3 )
                mesg.append(charlist[pog][randint(0, len(charlist[pog]) - 1)])
                used.append(pog)
            if len(mesg) == 4:
                proper_len = True
        keyboard.write('say ')
        keyboard.write(''.join(mesg))
        keyboard.write('\n')
        sleep(0.5)
        keyboard.press_and_release('esc')

if __name__ == '__main__':
    run()
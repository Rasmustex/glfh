from operator import pos
from random import randint
import keyboard 
import re
from time import sleep
import sys


def setuplist():
    f = open("source.txt", "rb")
    s = f.read().decode('utf-8', errors='ignore')
    f.close()
    s = re.findall("\[(.*)\]", s)
    return s

def run(test: bool):
    charlist = setuplist()
    while True:
        keyboard.wait('-')
        sleep(0.1)
        if not test:
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
        else:
            stringcount = 0
            for s in charlist:
                sleep(1)
                keyboard.write('say ' + str(stringcount) + '============================================\n')
                sleep(1)
                counter = 0
                completed_string = False 
                while not completed_string:
                    printstr = ['say ']
                    for x in range(10):
                        if counter >= len(s):
                            completed_string = True
                            keyboard.write(''.join(printstr) + '\n')
                            break
                        else: 
                            printstr.append(str(counter) + ': ' + s[counter] + ' ')
                        counter += 1
                    keyboard.write(''.join(printstr) + '\n')
                    sleep(1)
                stringcount += 1
            keyboard.press_and_release('esc')
            inputstr = input('remove> ')
            chlist = []
            for s in charlist: 
                chlist.append(list(s))

            while inputstr != 'done':
                position = []
                inputstr = inputstr.split(' ')
                if len(inputstr) != 2:
                    print('Error: input should be in the format of: "x y", where x is the list number, and y the element number')
                    inputstr = input('remove> ')
                    continue
                for s in inputstr:
                    position.append(int(s))
                if position[0] > len(charlist) - 1:
                    print('Error: x selection is out of bounds')
                    inputstr = input('remove> ')
                    continue
                elif position[1] > len(charlist[position[0]]):
                    print('Error: y selection is out of bounds')
                    inputstr = input('remove> ')
                    continue
                else:
                    chlist[position[0]][position[1]] = ''
                inputstr = input('remove> ')
            output = open('test.txt', 'wb')
            for l in chlist:
                output.write('['.encode('utf-8'))
                output.write(''.join(l).encode('utf-8'))
                output.write(']\n'.encode('utf-8'))
            output.close()



            break




if __name__ == '__main__':
    test = False 
    if len(sys.argv) > 1:
        if sys.argv[1] == '--test' or sys.argv[1] == '-t':
            test = True
    run(test)
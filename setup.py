import re

charlists = [[], [], [], []]
f = open("confusables.txt", "rb")
s = f.read().decode('utf-8', errors='ignore')
charlists[0] = re.findall("\(\s(\S)\s→\s[gG69]\s\)", s)
charlists[1] = re.findall("\(\s(\S)\s→\s[lL1]\s\)", s)
charlists[2] = re.findall("\(\s(\S)\s→\s[hH]\s\)", s)
charlists[3] = re.findall("\(\s(\S)\s→\s[fF]\s\)", s)
output = open("source.txt", "wb")
for x in charlists:
    output.write("[".encode('utf-8'))
    output.write(''.join(x).replace(" ","").encode('utf-8'))
    output.write("]\n".encode('utf-8'))
f.close()
output.close()
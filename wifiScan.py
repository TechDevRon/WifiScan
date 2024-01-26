import os
import time as t

delay = input('Delay before scan in seconds: ')
print('\n')
yN = input('Would you like to make directory to store txt files[y/N]: ')
print('\n')

match  yN.lower():
    case 'y':
        path = input('Full storing directory: ')
        print('\n')
        mkPath = "mkdir "+path
        os.system(mkPath)
        di = path
    case _:
        print('Continuing without making store directory.\n\n')
        t.sleep(5)
        di = input('Directory to store files: ')
        print('\n')

txtName = input('TXT name:')
os.system('clear')

print('\n')
print('Scanning started.')

counter = 1

while counter > 0:
    scanSave = "nmcli device wifi list > "+di+"/"+txtName+""+str(counter)+".txt"
    t.sleep(int(delay))
    os.system(scanSave)
    print('Scan',counter)
    counter += 1


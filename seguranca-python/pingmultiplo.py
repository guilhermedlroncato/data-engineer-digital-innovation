import os

with open('hosts.txt') as file:
    dump = file.read()
    dump = dump.splitlines()
    
    for ip in dump:
        os.system(f'ping -c 1 {ip}')
        print('\n')

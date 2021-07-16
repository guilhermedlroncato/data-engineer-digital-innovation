import os

host = input("Digite o IP ou Host a ser verificado: ")

os.system(f'ping -c 6 {host}')

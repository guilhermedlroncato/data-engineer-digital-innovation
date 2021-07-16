import hashlib

texto = input('Digite o texto: ')
menu = int(input('''
Menu - Escolha o tipo de Hash
1 - MD5
2 - SHA1
3 - SHA256
4 - SHA512
Digite a opção do hash a ser gerado: '''))

if menu == 1:    
    resultado = hashlib.md5(texto.encode('utf-8'))
elif menu == 2:    
    resultado = hashlib.sha1(texto.encode('utf-8'))
elif menu == 3:    
    resultado = hashlib.sha256(texto.encode('utf-8'))
elif menu == 4:    
    resultado = hashlib.sha512(texto.encode('utf-8'))

print('\nO hash é:', resultado.hexdigest())


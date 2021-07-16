import socket
import sys

def main():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    except socket.error as e:
        print('Conexão Falhou!!!')
        print(e)
        sys.exit()
    
    print('Socket criado com sucesso!!!')

    host = input('Digite o IP ou Host a ser conectado: ')
    port = input('Digite a porta a ser conectada: ')

    try:
        s.connect((host, int(port)))
        print('Cliente TCP conectado com sucesso!!!')
        s.shutdown(2) # fecha a conexão após 2 segundos
    except socket.error as e:
        print('Conexão Falhou!!!')
        print(e)
        sys.exit()

if __name__ == '__main__':
    main()
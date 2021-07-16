import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print('Cliente socket criado com sucesso!!!')

host = 'localhost'
port = 5433
mensagem = 'Firmeza Tio!'

try:
    
    s.sendto(mensagem.encode(), (host, 5432))

    dados, servidor = s.recvfrom(4096)

    dados = dados.decode()

    print('Cliente: ' + dados)
finally:
    print('Fechando conexão com Cliente')
    s.close()
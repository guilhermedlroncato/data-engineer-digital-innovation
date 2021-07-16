import random, string

tam_senha = 16 #tamanho da senha

chars = string.ascii_letters + string.digits + '!@#$%*&<>,.():/\]['

rnd = random.SystemRandom()

print(''.join(rnd.choice(chars) for i in range(tam_senha)))
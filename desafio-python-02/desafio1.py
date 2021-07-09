n1, n2, n3, n4= input().split()
n1 = float(n1)
n2 = float(n2)
n3 = float(n3)
n4 = float(n4) 
soma_pesos = 10.0

media = (n1 * 2.0 + n2 * 3.0 + n3 * 4.0 + n4) / soma_pesos
print('Media: %.1f' %media)

if media>=7.0:
    print('Aluno aprovado.')
elif media<5.0:
    print('Aluno reprovado')
elif 5.0 <= media <= 6.9:
    print('Aluno em exame.')
    n5 = float(input())
    final = float("{:.1f}".format((n5+media)/2))
    print('Nota do exame:', n5)
    if final >= 5.0:
        print('Aluno aprovado')
        print('Media final: %.1f' %final)
    else:
        print('Aluno reprovado')
        print('Media final: %.1f' %final)
x = int(input())
pos = 0
sq = 1
vetor = []
vetor.append(x)
for i in range (x,x+9):    
    square = vetor[sq-1] * 2
    vetor.append(square)
    pos += 1  
    sq += 1  

for i, x in enumerate(vetor):
    print(f'N[{i}] = {x}')
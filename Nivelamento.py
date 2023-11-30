pessoas = []

contador = 0
while contador < 15:
    pessoa_altura = float(input("Digite a altura: "))
    pessoa_sexo = input("Digite o gênero (M/F): ")
    pessoas.append([pessoa_altura, pessoa_sexo])
    contador += 1

menor_altura = float('inf')  
maior_altura = float('-inf')  
altura_homens = 0
qtde_mulheres = 0
qtde_homens = 0

for pessoa in pessoas:
    altura = pessoa[0]
    sexo = pessoa[1].upper()

    if altura > maior_altura:
        maior_altura = altura
    if altura < menor_altura:
        menor_altura = altura

    if sexo == 'M':
        altura_homens += altura
        qtde_homens += 1
    elif sexo == 'F':
        qtde_mulheres += 1

print("Maior altura:", maior_altura)
print("Menor altura:", menor_altura)
print("Qtde mulheres:", qtde_mulheres)

if qtde_homens > 0:
    print("Média de altura dos homens:", altura_homens / qtde_homens)
else:
    print("Média de altura dos homens: Não aplicável")

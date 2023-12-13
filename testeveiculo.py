#testando a classe veiculo

from veiculo import veiculo

minhacaranga = veiculo(marca='fiat', modelo='147', cor='amarelo', velocidade=0)
print('\n\t\t\t -- minha caranga -- ')
print(minhacaranga)

#acelerando minha caranga
#range é um intervalo na qual 1 é onde começa e o numero final é o limite desse intervalo
for i in range(1, 201):
    minhacaranga.acelerar()

#exibindo a caranga acelerada
print('\n\t\t\t -- minha caranga acelerada -- ')
print(minhacaranga)

#freiando minha caranga
for i in range(1,201):
    minhacaranga.frear()

#exibindo a caranga freiada
print('\n\t\t\t -- minha caranga freiada -- ')
print(minhacaranga)









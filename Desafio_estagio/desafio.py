# Resposta Questão 1) Valor de Soma = 91

indice = 13
soma = 0
k = 0

while k < indice:
    k += 1

    soma += k

print(soma)

# Resposta Questão 2) #########################################################


def sequencia_fib(n):
    lista_num = [0,1]
    while not n in lista_num: 
        prox_num = lista_num[-1] + lista_num[-2]
        if prox_num > n:
            return f"{n} não está na sequencia de Fibonacci"
        lista_num.append(prox_num)
    
    return f"{n} está na sequencia de Fibonacci"

print(sequencia_fib(4))
print(sequencia_fib(32))
print(sequencia_fib(55))
print(sequencia_fib(144))

# Resposta questão 3) #########################################################

# a) 9
# b) 128
# c) 49
# d) 100
# e) 13
# f) 200

# Resposta questão 4) #########################################################
"""
Se as três lampadas estiverem na mesma sala, eu ligo um interruptor e deixo alguns minutos ligado, em seguida desligo
esse interruptor e ligo outro. Vou para a sala das lâmpadas e concluo que a lâmpada que estiver acesa é controlada pelo
interruptor que está acionado, a lampada que estiver quente é controlada pelo interruptor que deixei ligado por alguns
minutos, a lâmpada que estiver fria é controlada pelo interruptor que não acionei.
"""
"""
Se cada lâmpada estiver em uma sala diferente, eu ligo um interruptor e deixo alguns minutos ligado, em seguida desligo
esse interruptor e ligo outro. Vou para uma das três salas e verifico, se a lâmpada estiver acesa ela é controlada pelo
interruptor que está acionado, se estiver apagada mas quente é controlada pelo interruptor que ficou acionado por alguns
minutos, caso esteja apagada é controlada pelo interruptor que não acionei. Independente de qual o estado da lâmpada 
presente na sala que escolhi, basta que eu verifique o estado da lâmpada de outra sala para chegar a conclusão de qual 
interruptor controla cada lâmpada.
"""

# Resposta questão 5) #########################################################

entrada_str = "Ola Mundo"
saida = ""

lista = [ n for n in entrada_str]

for n in range(len(lista) - 1, -1, -1):
    saida += lista[n]

print(saida)



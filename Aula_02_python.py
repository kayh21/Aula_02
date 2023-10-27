# Python é uma linguagem dinâmica, interpretada, OOP e de alto nivel 
# Ela segue convensões que são boas práticas, seguindo "regras" para estruturar o código
# Deve seguir nomeações de forma semântica que é dar o nome daquilo que o objeto faz
# utilizar o método de snake_case (letras minúsculas e palavras separadas por underline)
# Deve-se construir o código em inglês para ser universal 
# Deve-se utilizar concatenação, ou seja, unir duas strings 
# Variável é um espaço aberto na memória ROM que é armazenado informações e dado um nome a ela

# SINAIS DE COMPARAÇÃO:
# Em Python, você pode usar diversos sinais de comparação para comparar valores e criar expressões condicionais.
# 1°.Igual (==): Verifica se dois valores são iguais.
a = 5
b = 5
resultado = a == b  # Resultado será True

# 2°.Diferente (!=) : Verifica se dois valores são diferentes.
a = 5
b = 3
resultado = a != b  # Resultado será True

# 3°. Maior que (>) : Verifica se o valor da esquerda é maior que o valor da direita.
a = 7
b = 4
resultado = a > b  # Resultado será True


# 4°. Menor que (<) : Verifica se o valor da esquerda é menor que o valor da direita.
a = 2
b = 6
resultado = a < b  # Resultado será True


# 5°. Maior ou igual (>=) : Verifica se o valor da esquerda é maior ou igual ao valor da direita.
a = 5
b = 5
resultado = a >= b  # Resultado será True

# 6°.Menor ou igual (<=) : Verifica se o valor da esquerda é menor ou igual ao valor da direita.
a = 3
b = 6
resultado = a <= b  # Resultado será True

# OPERAÇÕES MATEMÁTICAS: 
#  * = multiplicação 
#  + = soma
#  - = subtração 
#  / = divisão
 

# EXEMPLO 01: Utiliza-se sinal de comparação para fazer uma senha 
# senha =  1234
entrada  = input("Digite sua senha")
senha = 1234

if (senha == 1234):
  print('Acesso permitido')
else: 
    print('Acesso negado')
    
# EXEMPLO 02: Utiliza-se concatenação 
nome = input("Digite o seu nome\n") # criar uma variável 
print("olá, tudo bem" + nome) #concatenar 

print("calculadora de soma")
n1 = int(input("digite um número\n"))
n2 = int(input("digite o numero 2\n"))
n3 = n1 + n2
print("O resultado da soma é", n3)

# EXEMPLO 03: Utiliza--se soma 
n1 = 23
n2 = 47 
n3 = n1 + n2 
print(n3) 

# EXEMPLO 04: Utiliza-se variável simples
nome = "Kayllane"
print(nome)

# EXEMPLO 05: Utiliza-se concatenação
cumprimento = "prazer em conhecê-lo" 
print("Meu nome é Kayllane,", cumprimento)

# EXEMPLO 06: Utiliza-se multiplicação 
primeiro = 10 
segundo = 10 
terceiro = primeiro * segundo
print(terceiro)
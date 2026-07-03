# declaracao de variaveis
nome = input('informe seu nome: ')
idade = int(input('Informe sua idade: '))
hobby = input('Informe seu hobby: ')
altura = float(input('Informe sua altura em metros: ').replace(',','.'))

# saida de dados

print(f'Seu nome é {nome}. {type(nome)}')
print(f'Sua idade é {idade}.{type(nome)}')
print(f'seu hobby é {hobby}.{type(nome)}')
print(f'sua altura é {altura} m.{type(nome)}')
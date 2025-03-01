# O conceito de laços é importante porque é uma das manieras mais comuns para um computador automatizar tarefas repetitivas. Por exemplo, em um laço simples como o que usamos em magicians.py.
# Python inicialmente lê a primeira linha do laço: "for" magician in magicians. Essa linha diz a python para estrair o primeiro valor da lista magicians e armazená-lo na variável magician.
# O Primeiro valor é 'alice'. O interpretador então lê a próxima linha do laço: for magician in magicians: Python recupera o proximo nome da lista, que é 'david' e armazena esse valor em magician.
# Então ele executa a linha: print(magician) Python exibe o valor atual de magician, que agora é 'david', novamente.
# O interpretador repete todo o laço mais uma vez com o último valor da lista, que é 'carolina'. Como não há mais valores na lista, Python passa para a próxima linha do programa.Nesse caso, não há mais nada depois do laço for, portante o programa simplesmente termina.
# Quando usar laços pela primeira vez, tenha em mente que o conjunto de passsos será repetido, uma vez para cada item da lista, não importa quantos itens haja na lista.
# Se você tiver um milhão de itens em sua lista, Python repetirá esses passos um milhão de vezes - e geralmente o fará bem rápido.
# Tenha em mente também que quando escrever seus próprios laços for, você podera escolher qualquer nome que quiser para a variável temporária que armazena cada valor da lista. No entanto, é convinente escolher um nome significativo, que represente um único itme da lista.
# Por exemplo, eis uma boa maneira de iniciar um laço "for" para uma lista de gatos, uma lista de cachorros e uma lista genérica de itens:

cats = ['willie', 'timmy', 'mister']
for cat in cats:
    print(f"Hello, {cat}!")
print("Hello, cats. I'm done greeting you.")

dogs = ['buddy', 'daisy', 'molly']
for dog in dogs:
    print(f"Hello, {dog}!")
print("Hello, dogs. I'm done greeting you.")

list_of_itens = ['item1', 'item2', 'item3']
print (list_of_itens)
for item in list_of_itens:
    print(f"Hello, {item}!")
print("Hello, itens. I'm done greeting you.")  

# Essa convenções de nomenclatura podem ajudar vocÊ a acompanhar a ação executada em cada item em uma laço 'for'. O uso de nomes no singular e no plural pode ajudar a identificar se a seção de código atua em um único elemento da lista ou em toda lista.





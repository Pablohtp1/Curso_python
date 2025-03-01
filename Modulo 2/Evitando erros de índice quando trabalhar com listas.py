# Um tipo de erro é comum quando trabalhamos com listas pela primeira vez.

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles[2])

# Esse exemplo resulta em um erro de índice: Traceback (most recent cal last): File " Motorcycle.py", line 3, in <module> print(motorcycles[3]) IndexError: list index out of range
# Porém , quando pesquisa a lista, nenhum item de motorcycles tem indice igual a 3. Por causa da natureza deslocada de um na indexação de listas, esse erro é caracteristico. As pessoas acham que o terceiro item é o item de número 3, pois começa a conta a partir do 1. Contudo, em Python, o terceiro item é o de número 2, pois a indexação começa com 0. Se você tentar acessar o item de índice 3, Python não saberá o que você quer e gerará um erro.

# Um erro de indice quer dizer que o Python não é capaz de determinar o índice solicitado. Se um erro de indice ocorrer em seu programa, tente ajustar o indice que vocÊ está solicitando em um.
# Então execute o programa novamente. Se você não conseguir encontrar e corrigir o erro, lembre-se de que você pode sempre recorrer a um depurador para ajudá-lo a encontrar o erro.

# Tenha em mente que, sempre que quiser acessar o último de uma lista, você deve usar o indice -1, isso sempre funcionará, mesmo que sua lista tenha mudado de tamanho desde a última vez que você a acessou:

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles[-1])

# A unica ocasião em que essa abordagem causará um erro é quando solicitamos o último item de uma lista vazia: motorcycles = [] print(motorcycles[-1]) Traceback (most recent call last): File "motorcycle.py", line 2, in <module> print(motorcycles[-1]) IndexError: list index out of range

# NOTA: Se um ero de indice ocorre e você não consegue descobrir como resolvê-lo, experimente exibir sua lista ou simplesmente mostrar o tamanho dela. Sua lista poderá estar bem diferente do que você imaginou.
# Em especial se ela foi tratada dinamicamente pelo seu programa. Ver a lista propriamente dita ou o número exato de itens que ela contém pod eajudar a entender esses erros de lógica.


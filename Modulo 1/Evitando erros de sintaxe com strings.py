# Um tipo de erro que você poderá ver com certa regularidade é um erro de sintaxe. Um erro de sintaxe ocorre quando o Python válido. Por exemplo, se usar um apóstrofo entre aspas, você produzira um erro.
# Isso acontence por que o python interpreta tudo que estiver entre a primeira aspa simples e o apóstrofo como uma string. Ele então tenta interpretar o restante do texto como código Python, o que causa erros.
# Eis o modo de usar aspas simples e duplas corretamente. Salve este programa como apostrophe.py e então execute-o: apostrophe.py message = "One of Python's is the diverse community"


message = 'One of Pythons strengths is its diverse community'
print (message)

# O apóstrofo aparece entre um conjunto de aspas duplas, portante o interpretador python não terá nenhum problema para ler a string corretamente: One of Python strengths is its diver community.

# No entanto, se você usar aspas simples, o interpretador Python não será capaz de identificar em que ponto a string deve terminar: message = "One of Python's strengths is its diverse community"

# Nota: O recurso de destaque da sintaxe de seu editor deve ajudar você a identificar alguns erros de sintaxe rapidamente quando escrever seus programas. Se você vir código python em destaque como se fosse inglês, ou inglês destacado como se fosse código Python, é provável que haja uma aspa correspondente em algum ponto de seu arquivo.

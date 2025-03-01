# Você pode fazer praticamente de tudo com cada item em um laço 'for'. Vamos expandir o exemplo anterior exibindo uma mensagem a cada mágico, informando-lhes que realizaram um ótimo truque:

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print (magician.title() + ", that was a great trick!")
    print ("I can't wait to see your next trick, " + magician.title() + ".\n")

# A única diferença nesse código está em 1, em que compomos uma mensagem para cada mágico, começando com o nome desse mágico.
# Na primeira vez em que passamos pelo laço, o valor do mágico é 'alice', portante python inicia a primeira mensagem com o nome 'Alice'. Na segunda vez que compormos a mensagem, ela começará com 'David' e na tercira vez, a mensagem começará com 'Carolina'.
# O laço 'for' percorre a lista de mágicos e executa o bloco de código uma vez para cada mágico da lista. O código dentro do laço é executado uma vez para cada mágico da lista, e o nome do mágico é exibido em cada mensagem.

# Também podemos escrever tantas linhas de código quantas quisermos no laço 'for'. Considera-se que toda linha indentada após a linha 'for' é executada uma vez para cada valor da lista. Assim, você pode executar o volume de trabalho que quiser com cada valor da lista.
# Vamos acrescentar uma segunda linha em nossa mensagem, informando a cada mágico que estamos ansioso para ver o seu próximo truque:

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print (magician.title() + ", that was a great trick!")
    print ("I can't wait to see your next trick, " + magician.title() + ".\n")

    # Podemos usar quantas linhas quisermos em nosso laço 'for'. Na prática muitas vezes vocÊ achará util efetuar várias operações com cada item de uma lista quando for usar um laço for.
    
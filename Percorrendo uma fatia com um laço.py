# Você pode usar uma fatia em um laço "for" se quiser percorrer um subconjunto de elementos de uma lista. No próximo exemplo, percorremos os três primeiros jogadores e exiberemos seus nomes como parte de uma lista simples: 

players = ['charles', 'martina', 'michael', 'florence', 'eli', 'maria', 'Pedro']

print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())


# Em vez de percorrer a lista inteira de jogadores em 1, Python percorre somente os três primeiros nomes: Here are the first three players on my team: charles martina michael

# As fatias são muito úteis em várias situações. Por exemplo, quando criar um jogo, voc~e poderia adicionar a pontuação final de um jogar em uma lista sempre que esse jogador acabar de jogar. 
# Seria possivel então obter as três pontuações mais altas de um jogador ordenando a lista em ordem decrescente e obtendo uma lista que inclua apenas as três primeiras pontuações. Ao trabalhar com dados, você pode usar fatias para processar seus dados em porções de tamanho especifico.
# Quando criar uma aplicação web, fatias poderiam ser usadas para exibir informações em uma série de páginas, com uma quantidade apropriada de informações em cada página.
# 

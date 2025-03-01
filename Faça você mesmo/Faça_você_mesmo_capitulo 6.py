#•Armazene as localidares em uma lista. Certifique-se de que a lista não esteja em ordem alfabética.
# • Exiba sua lista na ordem original. Não se preocupe em exibir a lista de forma elegante: Basta exibir como uma lista python pura.
# • Utilize sorted() para exibir sua lista em ordem alfabética sem modificar a lista propriamente dita.
# • Mostre que sua lista manteve sua ordem original exibindo-a novamente.
# • Utilize sorted() para exibir sua lista em ordem alfabética inversa sem modificar a lista propriamente dita.
# • Mostre que sua lista manteve sua ordem original exibindo-a novamente.
# • Utilize sort() para mudar sua lista de modo que ela seja armazenada em ordem alfabética.
# • Exiba a lista para mostrar que sua ordem mudou.
# • Utilize sort() para mudar sua lista de modo que ela seja armazenada em ordem alfabética inversa.
# • Exiba a lista para mostrar que sua ordem mudou.
# • Utilize reverse() para mudar a ordem de sua lista. Exiba a lista para mostrar que sua ordem mudou.
# • Utilize reverse() para mudar a ordem de sua lista novamente. Exiba a lista para mostrar que ela voltou á sua ordem original.

localidades = ['Brasil', 'Argentina', 'Chile', 'Peru', 'Colômbia', 'Uruguai', 'Paraguai', 'Venezuela', 'Equador', 'Bolívia']
print(localidades)
print(sorted(localidades))

localidades = ['Brasil', 'Argentina', 'Chile', 'Peru', 'Colômbia', 'Uruguai', 'Paraguai', 'Venezuela', 'Equador', 'Bolívia']
print(localidades)
print(sorted(localidades, reverse=True))

localidades = ['Brasil', 'Argentina', 'Chile', 'Peru', 'Colômbia', 'Uruguai', 'Paraguai', 'Venezuela', 'Equador', 'Bolívia']
print(localidades)
print(localidades.reverse())

localidades = ['Brasil', 'Argentina', 'Chile', 'Peru', 'Colômbia', 'Uruguai', 'Paraguai', 'Venezuela', 'Equador', 'Bolívia']
print(localidades)
print(localidades.sort())




# Convidados para o jantar: Trabalhando com um dos programas dos exericios anteriores, use len() para exibir uma mensagem que mostre o número de pessoas que você está convidando para o jantar.

convidados = ['João', 'Maria', 'José', 'Ana', 'Carlos', 'Marta', 'Pedro', 'Paula', 'Lucas', 'Larissa' 'Pedro']
print (len(convidados)) # 11

# Três convidados a mais: Você descobre que tem mais espaço na mesa, então decida convidar mais três pessoas.

convidados.insert(0, 'Fernanda')
convidados.insert(5, 'Ricardo')
convidados.append('Renata')
print(len(convidados))

#Todas as funções: Pense em algo que você armazenar em uma lista. Por exemplo, vocÊ poderia criar uma lista de montanhas, rios, paises,cidades,idiomas ou qualquer outro item que quiser. Escreva um programa que crie uma lista cotendo esses itens e então utilize cada função apresentada neste capitulo pelo menos uma vez.

montanhas = ['Everest', 'K2', 'Kang', 'Lhotse', 'Makalu', 'Cho Oyu', 'Dhaulagiri', 'Manaslu', 'Annapurna', 'Nanga Parbat']
print(montanhas)

rios = ['Amazonas', 'Nilo', 'Mississipi', 'Yangtze', 'Amur', 'Mekong', 'Ganges', 'Rio Paraguai', 'Rio Paraná', 'Rio São Francisco']
print(rios)

idiomas = ['Mandarim', 'Espanhol', 'Inglês', 'Hindi', 'Árabe', 'Português', 'Bengali', 'Russo', 'Japonês', 'Lahnda']
print(idiomas)

paises = ['China', 'Índia', 'Estados Unidos', 'Indonésia', 'Paquistão', 'Brasil', 'Bangladesh', 'Rússia', 'Japão', 'México']
print(paises)

cidades = ['Tóquio', 'Delhi', 'Xangai', 'São Paulo', 'Mumbai', 'Cidade do México', 'Pequim', 'Daca', 'Cairo', 'Mumbai'] 
print(cidades)

#Vamos categorizar corretamente de onde é cada um dos itens da lista montanhas, rios, idiomas, paises e cidades.


todos = {'montanhas': montanhas, 'rios': rios, 'idiomas': idiomas, 'paises': paises, 'cidades': cidades}
print(todos)
print (len([montanhas, rios, idiomas, paises, cidades]))

#Agora vamos utilizar as funções append(), insert(), remove(), pop(), del() e sort() para manipular as listas.

montanhas.append('Kanchenjunga')
print(montanhas)

montanhas.insert(0, 'Lhotse')
print(montanhas)

montanhas.remove('K2')
print(montanhas)

montanhas.pop()
print(montanhas)

del montanhas[0]
print(montanhas)

montanhas.sort()
print(montanhas)

# Vamos utilizar as funções reverse() e sorted() para manipular as listas.

montanhas.reverse()
print(montanhas)

print(sorted(montanhas))

# Vamos utilizar a função len() para exibir uma mensagem que mostre o número de itens da lista.

print(len(montanhas))   
print(len(rios))
print(len(idiomas))
print(len(paises))
print(len(cidades))









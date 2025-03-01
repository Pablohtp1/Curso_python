# Lista de convidados: se pudesse convidar alguém, vivo ou morto, para o jantar, quem você convidaria? crie uma lista que inclua pelo menos três pessoas que vocÊ gostaria de convidar para jantar.
# Em seguida, utilize sua lista para exibir uma mensagem para cada pessoa, convidando-a para jantar.

convidados = ['Minha avo', 'Sabotage', 'Renato Russo']
print(f"Olá {convidados[0]}, você está convidada para o jantar.")
print(f"Olá {convidados[1]}, você está convidado para o jantar.")
print(f"Olá {convidados[2]}, você está convidado para o jantar.")

# Alterando a lista de convidados: VocÊ acabou de saber que um de seus convidados não poderá comparecer no jantar, portanto será necessário enviar um novo conjunto de convites.
# Você deverá pensar em outra pessoa para convidar. 
# • Comece com o programa do Exercício 3.6. Acrescente um print no final do programa, especificando o nome do convidado que não poderá comparecer.
# • Modifique sua lista, substituindo o nome do convidado que não poderá comparecer pelo nome da nova pessoa que você está convidando.
# • Exiba um segundo conjunto de mensagens com o convite, uma para cada pessoa que continua presente em sua lista.

print(f"\nInfelizmente, {convidados[1]} não poderá comparecer ao jantar.")
convidados[1] = 'Bob Marley'
print(f"\nOlá {convidados[0]}, você está convidada para o jantar.")
print(f"Olá {convidados[1]}, você está convidado para o jantar.")
print(f"Olá {convidados[2]}, você está convidado para o jantar.")

# Você acaba de encontrar uma mesa de jantar maior, portanto agora tem mais espaço disponível. Pense em mais três pessoas para convidar ao jantar.
convidados2 = ['Martin luther king', 'Meu avô', 'Minha bisavÔ']
print(f'\nOlá {convidados2[0]}, você está convidado para o jantar.')

print (f'\Ola {convidados2},{convidados} Achamos uma mesa maior. Vamos convidar mais pessoas para o jantar.')

convidados2.insert(0, 'Mae')
print (convidados2)
convidados2.insert(2, 'Pai')
print (convidados2)
convidados2.append('Tio')
print (convidados2)

print(f"\nOlá {convidados2[0]}, você está convidado para o jantar.")
print(f'Olá {convidados2[1]}, você está convidado para o jantar.')
print(f'Olá {convidados2[2]}, você está convidado para o jantar.')
print(f'Olá {convidados2[3]}, você está convidado para o jantar.')

# Acabou de descobrir que sua nova mesa não chegará a tempo para o jantar e que você tem espaço para somente duas pessoas.

print(f"\nDesculpe, {convidados2.pop()}, não temos espaço para você no jantar.")
print(f"Desculpe, {convidados2.pop()}, não temos espaço para você no jantar.")
print(f"Desculpe, {convidados2.pop()}, não temos espaço para você no jantar.")
print(f"Desculpe, {convidados2.pop()}, não temos espaço para você no jantar.")
print(f'Desculpe, {convidados2.pop()}, não temos espaço para você no jantar.')
print(f'Desculpe, {convidados2.pop()}, não temos espaço para você no jantar.')

#Utilize Del para remover os convidados que sobraram da lista. Mostre a lista para garantir que você esvaziou ela completamente.

del convidados[1]
del convidados[0]
del convidados[0]
print(convidados)
# Mensagem pessoal: Armazene o nome de uma pessoa em uma variável e apresente uma mensagem a essa pessoa. Se não souber o que fazer, descase um pouco ou consulte as sugestões que estão no Apêndice C.

first_name = "Erick"
last_name = "lovelace"
full_name = "Olá" + first_name +"" + last_name + 'você gostaria de aprender um pouco de python hoje?'
print (full_name)

# Podemos usar concatenação para compor uma mensagem e então armazenar a mensagem completa em uma variável: first_name = "Erick" last_name ="lovelace" full_name = first_name + "" + last_name + 'você gostaria de aprender um pouco de python hoje?'
# Olá Ericklovelace você gostaria de aprender um pouco de python hoje?.


# Letras maiúsculas e minúsculas em nomes: Armazene o nome de uma pessoa em uma variável e apresente esse nome em letras minúsculas, em letras maiúsculas e somente com a primeira letra maiúsculas.

name = "ErIcK"
print (name.lower())
print (name.upper())
print (name.title())

# Citação famosa: encontre uma citação de uma pessoa famosa que você admire. Exiba a citação e o nome do autor. Sua saída deverá ter uma aparência mais ou menos assim, incluindo as aspas: Albert Einstein certa vez disse: "Uma pessoa que nunca cometeu um erro jamais tentou nada novo."

print ('Albert Einstein certa vez disse: "Uma pessoa que nunca cometeu um erro jamais tentou nada novo."')

# Citação famosa 2: Repita o Exercício 2-5, mas desta vez armazene o nome do autor da citação famosa em uma variável chamada famous_person. Em seguida, componha sua mensagem e armazene-a em uma nova variável chamada message. Exiba sua mensagem.

famous_person = "Albert Einstein"
message = famous_person + 'certa vez disse: "Uma pessoa que nunca cometeu um erro jamais tentou nada novo.' + 'GÊNIO' 

# Removendo caracteres em branco de nomes: Armazene o nome de uma pessoa e inclua alguns caracteres em branco no início e no final do nome. Lembre-se de usar cada combinação de caracteres, "\t" e "\n", pelo menos uma vez.
name = "\tErick\n"
print(name)

# Exiba o nome uma vez, de modo que os caracteres em branco sejam mostrados. Em seguida, exiba o nome usando cada uma das três funções de remoção de caracteres em branco, lstrip(), rstrip() e strip().

print(name.lstrip())
print(name.rstrip())
print(name.strip()) 

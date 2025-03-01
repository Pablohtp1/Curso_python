# Com frequência, você vai querer usar o valor de uma variável em uma mensagem. Por exemplo, suponha que vocÊ queira desejar feliz aniversário a alguém. Você poderia escrever um código como este:

age = 23
message = "Happy" + str(age) + "rd Birthday!"
print (message)

# O código acima produz a seguinte mensagem: Happy 23rd Birthday! O código acima não funcionaria sem a função str(). A função str() diz a Python para tratar o valor de age como uma string. A função str() converte valores numéricos em strings. Neste caso, age é convertido em uma string para que possa ser concatenado com as outras strings na mensagem. Se você tentar concatenar um valor numérico com uma string sem a função str(), você obterá um erro. Por exemplo, tente rodar o seguinte código sem a função str():

age = 23
message2 = "happy\t" + str(age) + "rd Birthday!\t" + str(2024)
print (message2)
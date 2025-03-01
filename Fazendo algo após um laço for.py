# O que acontece quando um laço 'for' acaba de executar? Geralmente você vai querer fazer uma sintese de um bloco de saida ou passar para outra atividade que seu programa deva executar.
# Qualquer linha de código após o laço 'for' que naõ estiver identada será executada uma vez sem repetição. Vamos acrescentar uma linha que agradeça a todos os mágicos por um ótimo show:
# Para exibir essa mensagem ao grupo após todas as mensagens inidividuais terem sido apresentadas, colocamos a mensagem de agradecimento depois do laço 'for', sem indentação

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print (magician.title() + ", that was a great trick!")
    print ("I can't wait to see your next trick, " + magician.title() + ".\n")

    print ("Thank you, everyone. That was a great magic show!")
    
# As duas instruções print são repetidas uma vez para cada mágico da lista, como vimos antes. No entanto, como a linha em 1 não está identada, ela será exibida apenas uma vez

# Quando você estiver escrevendo um laço 'for', certifique-se de que todas as linhas identadas estão corretas. Se você esquecer de identar uma linha que deveria ser identada, o código não funcionará. Se identar uma linha que não deveria ser identada, o código gerará um erro.



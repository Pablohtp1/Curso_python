# Ás vezes, seu laço executará sem erros, mas não produzirá o resultado esperado. Isso pode acontecer quando você tenta realizar várias tarefas em um laço e se esquecer de indentar algumas de suas linhas.
# Por exemplo, eis o que acontecer quando nos esquecemos de indentar a segunda linha do laço que diz a cada mágico que estamos ansioso para ver o seu próxmo trque: 

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print (magician.title() + ", that was a great trick!")
    print ("I can't wait to see your next trick, " + magician.title() + ".\n")


# A instrução print em 1 deveria estar indentada, mas como o Python encontra pelo menos uma linha indentada ápos a instrução 'for', um erro não é informado. Como resultado, a primeira instrução print é executada uma vez para cada nome da lista.
# Pois está indentada, mas a segunda instrução print não está indentada, portanto é executada somente apenas uma vez, depois que o laço terminar de executar.
# Como valor final de magician é 'Carolina', ela é a única que recebe a mensagem de " Ansiosos pela próxima mágica".
# Esse é um erro de lógica. É um código Python com sintaxe válida, mas ele não gera o resultado desejado, pois há um problema em sua lógica.
# Se voc~E esperar ver uma determinada ação ser repetida uma vez parada cada item de uma lista, mas ela é executada apenas uma vez, verifique se não é preciso simplismente indentar uma linha ou um grupo de linhas.


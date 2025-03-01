# Se você acidentalmente indentar um código que deva executar após um laço ter sido concluído, esse código será repetido uma vez para cada item da lista. Ás vezes, isso faz Python informar um erro, mas , geralmente, você terá um erro de lógica simples.

# Por exemplo, vamos ver o que acontece quando indentamos por acidente a linha que agradece aos ma´gicos como um grupo pro apresentaram um bom show:

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print (magician.title() + ", that was a great trick!")
    print ("I can't wait to see your next trick, " + magician.title() + ".\n")
    print ("Thank you, everyone. That was a great magic show!")

# Pelo fato de a linha 7/8/9 , ela é exibida uma vez para cada pessoa da lista, como podemos ver gerada acima.

# Há outro erro de lógica, semelhante áquela da seção " Esquecendo-se de indentar linhas adicionais". Como Python não sabe o que você está querendo fazer com seu código, ele executará todo o código que estiver escrito com uma sintaxe válida.
# Se uma ação for repetida muitas vezes quando deveria ser executada apenas uma vez, verifique se você não precisa simplesmente deixar de indentar o código dessa ação.

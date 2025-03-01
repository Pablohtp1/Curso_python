# Python usa identação para determinar se uma linha de código está concetada á linha anteriores. Se você esquecer de identar uma linha que deveria ser identada, o código não funcionará. Se identar uma linha que não deveria ser identada, o código gerará um erro.
# Nos exemplos anteriores, as linhas que exibiam mensagens aos mágicos individuais fazima parte do laço "for" por que estavam indentadas.
# O uso de identação por Pythona deixa o cóidgo bem mais fácil de ler. Basicamente, Python usa espaços em branco para forçar você a escrever um código.
# Em programas Python mais longos, você perceberá que há blocos de código indentados em alguns níveis diferentes. Esses níveis de indentação ajudam a ter uma noção geral da organização do programa como um todo.
# Quando começar a escrever o código que dependa de uma identação apropriada, você deverá tomar cuidado com alguns erros comuns de indentação.
# Por exemplo, ás vezes, as pessoas indentam blocos de código que não precisam estar indentados ou se esquecem de indentar blocos que deveriam estar indentados.
# Ver exemplos desses erros agora ajudará a evita-los e a corrigi-los quando aparecerem em seus próprios programas.
# Vamos analisra alguns dos erros mais comuns de identação.

"""# Esquecendo-se de identar """

# Sempre idente a linha após a instrução 'for' em uma laço. Se você se esquecer, Python o avisará: 

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician.title() + ", that was a great trick!")
'''# Está faltando o print nessa informação, por isso o erro'''


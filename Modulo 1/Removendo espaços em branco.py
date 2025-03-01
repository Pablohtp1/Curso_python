# Espaços em branco extras podem ser confusos em seus programas. Para os programadores, 'python' e 'python ' parecem praticamente iguais. Contudo, para um programa, são duas strings diferentes.Python identifica o espaço extra em 'python ' e o considera significativo, a menos que você informe o contrário.
# É importante pensar em espaços em branco, pois, com frequência, você vai querer comparar duas strings para determinar se são iguais. Por exemplo, uma situação importante pode envolver a verificação dos nomes de usuário das pessoas quando elas fizerem login em um site. Espaços em branco extras podem ser confusos em situações muito mais simples também.Felizemnte, Python facilita eliminar espaços em branco extrados dados fornecidos pelas pessoas.
# Python é capaz de encontrar espaços em branco dos lados direito e esquerdo de uma string. Para garantir que não haja espaços em branco do lado direito de uma string, utilize o método rstri()

favorite_language = 'python '
favorite_language;  'python '
favorite_language.rstrip(); 'python'
favorite_language; 'python '

# O valor armazenado em favorite_language em contem um espaço em branco extra no final da string. Quando solicitamos esse valor a python em uma sessão de terminar podemos ver variável favorite_language.

favorite_language = ' python '
favorite_language.rstrip; 'python '
favorite_language.lstrip; ' python'
favorite_language.strip;  'python'    

# Nesse exemplo, começamos com um valor que tem espaços em branco no inicio e no fim, então removemos os espços extras do lado direito em, do lado esqueco em 3 de amos bos lados em 4.

# Fazer experimentos com essas funções de remoção pode ajudar a você ter familiaridade com a manipulação de strings. No mundo real, essas funções de remoção são usadas com mais frequência para limpar entradas de usuário antes de armazená-las em um programa.

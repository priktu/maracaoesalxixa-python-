# escreva um programa que receba 4 notas e calcule a media aritimetica
#bumda kk
#se a media for maior ou igual a 6, imprima APROVADO
#se a media for menor que 6, imprima REPROVADO
nota1 =int(input('Informe sua 1° nota: '))
nota2 =int(input('Informe sua 2° nota: '))
nota3 =int(input('Informe sua 3° nota: '))
nota4 =int(input('Informe sua 4° nota: '))

media = (nota1 + nota2 + nota3 + nota4)/4

if media>=6 :
    print(media)
    print('Este aluno(a) foi aprovado!1!1')

elif media<6 :
    print(media)
    print('qm passa direto é trem ne vei kk')
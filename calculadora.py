print('eu so uma cawculadora eu')
print('1 - adição')
print('2 - subtração')
print('3 multiplição')
print('4 - divisão')

operacao =int(input('iskole uma operrasãwm; '))

x = float(input('1° numÊró: '))
y = float(input('2° numÊró: '))

if operacao == 1:
    print(f'o reçuwTÁdo dÂ soma É;  {x + y}')
elif operacao == 2:
    print(f'o reçuwTÁdo dÂ SOBEtrazáo É;  {x - y}')
elif operacao == 3:
    print(f'o reçuwTÁdo dÂ motePLÍgâzaõ É;  {x * y}')
else:
    if y != 0:
        print(f'o reçuwTÁdo dÂ dývýçâõ É;  {x / y}')
    else:
        print('pôdy náo veyr kk')
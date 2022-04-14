a = int(input('Entre com o número: '))
div = 0
for x in range(1, a+1):
    resto = a % x
    if resto == 0:
        div = div + 1
if div == 2:
        print('O número é primo.')
else:
    print('O número não é primo.')
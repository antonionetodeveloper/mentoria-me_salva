A = int(input("Digite o primeiro número: "))
B = int(input("Digite o segundo número: "))

if B > A:
    print("O menor valor é: ", A)
    print("O maior valor é: ", B)

elif A > B:
    menor_valor = B
    maior_valor = A

    B = maior_valor
    A = menor_valor

    print("O menor valor é: ", A)
    print("O maior valor é: ", B)

else:
    print("Os valores são iguais.")
    
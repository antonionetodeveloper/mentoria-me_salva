def produto(primeiro_numero, segundo_numero):
    return (primeiro_numero*2) * (segundo_numero/2)

def soma(primeiro_numero, terceiro_numero):
    return primeiro_numero*3 + terceiro_numero

def potencia(terceiro_numero):
    return terceiro_numero**3

primeiro_numero = float(input("Digite o primeiro número: "))
segundo_numero = float(input("Digite o segundo número: "))
terceiro_numero = float(input("Digite o terceiro número: "))

print("O produto do dobro do primeiro com metade do segundo é: ", produto(primeiro_numero, segundo_numero))
print("A soma do triplo do primeiro com o terceiro é: ", soma(primeiro_numero, terceiro_numero))
print("O terceiro elevado ao cubo é: ", potencia(terceiro_numero))

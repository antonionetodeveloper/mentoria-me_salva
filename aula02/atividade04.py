salario = float(input("Digite o seu salário: "))

if salario < 200:
    INSS = salario * 0.08
    print(f"O seu salário é {salario:.2f} e o desconto do INSS é {INSS:.2f}, logo o seu salário líquido é {salario - INSS:.2f}")

if salario >= 200 and salario < 500:
    INSS = salario * 0.085
    print(f"O seu salário é {salario:.2f} e o desconto do INSS é {INSS:.2f}, logo o seu salário líquido é {salario - INSS:.2f}")

if salario >= 500 and salario < 1000:
    INSS = salario * 0.09
    print(f"O seu salário é {salario:.2f} e o desconto do INSS é {INSS:.2f}, logo o seu salário líquido é {salario - INSS:.2f}")

else:
    INSS = salario * 0.095
    print(f"O seu salário é {salario:.2f} e o desconto do INSS é {INSS:.2f}, logo o seu salário líquido é {salario - INSS:.2f}")
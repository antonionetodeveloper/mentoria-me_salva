nome_do_produto = input("Digite o nome do produto: ")
preco_do_produto = float(input("Digite o preço do produto: "))
quantidade_do_produto = int(input("Digite a quantidade do produto: "))

if quantidade_do_produto <= 10:
    valor_total = preco_do_produto * quantidade_do_produto
    print(f"{quantidade_do_produto} unidades de {nome_do_produto} custam R$ {valor_total:.2f}")

if quantidade_do_produto > 10 and quantidade_do_produto <= 20:
    desconto = 0.1 # 10% de desconto
    valor_total = preco_do_produto * quantidade_do_produto
    valor_com_desconto = valor_total - (valor_total * desconto)
    print(f"{quantidade_do_produto} unidades de {nome_do_produto} custam R$ {valor_com_desconto:.2f} já com 10% de desconto aplicado.")

if quantidade_do_produto > 20 and quantidade_do_produto <= 50:
    desconto = 0.2 # 20% de desconto
    valor_total = preco_do_produto * quantidade_do_produto
    valor_com_desconto = valor_total - (valor_total * desconto)
    print(f"{quantidade_do_produto} unidades de {nome_do_produto} custam R$ {valor_com_desconto:.2f} já com 20% de desconto aplicado.")

else:
    desconto = 0.25 # 25% de desconto
    valor_total = preco_do_produto * quantidade_do_produto
    valor_com_desconto = valor_total - (valor_total * desconto)
    print(f"{quantidade_do_produto} unidades de {nome_do_produto} custam R$ {valor_com_desconto:.2f} já com 25% de desconto aplicado.")
preco_quilo=30.00
peso_prato=0.1
peso_prato_cheio=float(input("Digite o peso do prato cheio:"))
peso_comida= peso_prato_cheio-peso_prato
pagar= peso_comida*preco_quilo
print("Preço a pagar:",pagar)

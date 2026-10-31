casa = float (input("Valor da casa: "))
salário = float (input("Valor do salário: "))
anos = int (input("Pagar em quantos anos? "))
prestacao = float(casa / (anos * 12))
limite = float((salário / 100) * 30)

print (f"O valor da prestação da casa é de {prestacao:.2f}")

if prestacao > limite:
    print(f"Seu pedido foi negado, seu limite máximo é de {limite:.2f}")

else: 
    print("Seu financiamento foi aprovado")
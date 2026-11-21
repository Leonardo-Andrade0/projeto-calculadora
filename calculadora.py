resultado = 0

print('CALCULADORA')

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

print("\nEscolha a opção /n")
print("Soma (1)")
print("Subtração (2)")
print("Multiplicação (3)")
print("Divisão (4)")

operacao = input("Digite o número da operação: ")

if operacao ==  "1":
    resultado = num1 + num2
    print(f"Resultado {resultado}")

elif operacao == "2":
    resultado = num1 - num2
    print(f"Resultado {resultado}")

elif operacao == "3":
    resultado = num1 * num2
    print(f"Resultado {resultado}")

elif operacao == "4":
    resultado = num1 / num2
    print(f"Resultado {resultado}")
 
else:
    print("Escolha uma opção válida")
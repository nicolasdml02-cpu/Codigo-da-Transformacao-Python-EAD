def calculadora():
    print("--- Calculadora Simples ---")
    
    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        operacao = input("Escolha a operação (+, -, *, /): ").strip()

        if operacao == '+':
            resultado = num1 + num2
        elif operacao == '-':
            resultado = num1 - num2
        elif operacao == '*':
            resultado = num1 * num2
        elif operacao == '/':
            resultado = num1 / num2  # Pode lançar ZeroDivisionError
        else:
            print("Operação inválida!")
            return

        print(f"Resultado: {resultado}")

    except ZeroDivisionError:
        print("Erro: Não é possível dividir um número por zero!")
    except ValueError:
        print("Erro: Entrada inválida. Por favor, digite números válidos.")

if __name__ == "__main__":
    calculadora()
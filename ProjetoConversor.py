def celsius_para_fahrenheit(c):
    return f"{c * 9 / 5 + 32:.2f} °F"

def fahrenheit_para_celsius(f):
    return f"{(f - 32) * 5 / 9:.2f} °C"

def main():
    print("=== Conversor de Temperaturas ===")
    print("Escolha o tipo de conversão:")
    print("1 - Celsius para Fahrenheit")
    print("2 - Fahrenheit para Celsius")
    print("Digite 'sair' para encerrar.")
    
    while True:
        escolha = input("\nOpção (1 ou 2): ").strip()
        
        if escolha.lower() == 'sair':
            print("Encerrando...")
            break
        
        if escolha == '1':
            valor = input("Digite a temperatura em °C: ")
            try:
                c = float(valor)
                print("Resultado:", celsius_para_fahrenheit(c))
            except ValueError:
                print("Erro: digite um número válido.")
                
        elif escolha == '2':
            valor = input("Digite a temperatura em °F: ")
            try:
                f = float(valor)
                print("Resultado:", fahrenheit_para_celsius(f))
            except ValueError:
                print("Erro: digite um número válido.")
        else:
            print("Opção inválida. Digite 1, 2 ou 'sair'.")

if __name__ == "__main__":
    main()

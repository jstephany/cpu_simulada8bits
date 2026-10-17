"""
ULA — Código-base para o projeto de CPU Simulada
AOC 2026.2

Os alunos devem implementar as operações marcadas como IMPLEMENTAR.
"""

def limitar_8bits(valor):
    return valor & 0xFF


def ula(operacao, a, b=0):
    a = limitar_8bits(a)
    b = limitar_8bits(b)

    if operacao == "ADD":
        # Realiza a soma aritmética tradicional
        resultado = a + b

    elif operacao == "SUB":
        # Realiza a subtração aritmética
        resultado = a - b

    elif operacao == "AND":
        # Realiza a operação lógica E (AND) bit a bit
        resultado = a & b

    elif operacao == "OR":        
        # Realiza a operação lógica OU (OR) bit a bit
        resultado = a | b

    elif operacao == "XOR":
        # Realiza a operação lógica OU EXCLUSIVO (XOR) bit a bit
        resultado = a ^ b

    else:
        raise ValueError(f"Operação inválida: {operacao}")

    return limitar_8bits(resultado)

"""
PROGRAMAS — Módulo de programas para a CPU Simulada
AOC 2026.2

Este arquivo contém as rotinas para carregar na memória da CPU:
1. O programa de teste padrão (5 + 8)
2. O programa próprio exigido para a avaliação
"""


def carregar_programa_exemplo(cpu):
    """
    Carrega na memória o programa de teste oficial (5 + 8).
    Resultado esperado: MEM[15] = 13.
    """
    cpu.memoria[0] = "LOAD R0, 5"
    cpu.memoria[1] = "LOAD R1, 8"
    cpu.memoria[2] = "ADD R0, R1"
    cpu.memoria[3] = "STORE R0, 15"
    cpu.memoria[4] = "HALT"

def carregar_programa_proprio(cpu):
    """
    Programa próprio com 8 instruções.
    
    Demonstração:
    - Preserva o resultado do ADD (12 + 3 = 15) na Memória[9]
    - Preserva o resultado do OR (15 OR 16 = 31) na Memória[10]
    """
    cpu.memoria[0] = "LOAD R0, 12"
    cpu.memoria[1] = "LOAD R1, 3"
    cpu.memoria[2] = "ADD R0, R1"       # R0 vira 15 (12 + 3)
    cpu.memoria[3] = "STORE R0, 9"      # Salva o resultado do ADD (15) na Memória[9]
    cpu.memoria[4] = "LOAD R2, 16"
    cpu.memoria[5] = "OR R0, R2"        # R0 vira 31 (15 OR 16)
    cpu.memoria[6] = "STORE R0, 10"     # Salva o resultado do OR (31) na Memória[10]
    cpu.memoria[7] = "HALT"
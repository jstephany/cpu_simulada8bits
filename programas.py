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
    Programa próprio com 8 instruções criado para avaliação.
    
    Demonstração passo a passo:
    - Etapa 1: Soma de dois valores (12 + 3) e armazenamento na memória.
    - Etapa 2: Operação lógica OR e armazenamento de um segundo resultado.
    """

    # 1. Carrega o valor decimal 12 no registrador R0
    cpu.memoria[0] = "LOAD R0, 12"

    # 2. Carrega o valor decimal 3 no registrador R1
    cpu.memoria[1] = "LOAD R1, 3"

    # 3. Realiza a soma de R0 e R1 (12 + 3 = 15). O resultado (15) fica salvo em R0.
    cpu.memoria[2] = "ADD R0, R1"

    # 4. Pega o valor atual de R0 (15) e salva na posição 9 da memória principal.
    cpu.memoria[3] = "STORE R0, 9"

    # 5. Carrega o valor decimal 16 no registrador R2
    cpu.memoria[4] = "LOAD R2, 16"

    # 6. Realiza a operação bit a bit OR entre R0 (15) e R2 (16).
    # Em binário: 15 (00001111) OR 16 (00010000) = 31 (00011111). Salva 31 em R0.
    cpu.memoria[5] = "OR R0, R2"

    # 7. Pega o novo valor de R0 (31) e salva na posição 10 da memória principal.        
    cpu.memoria[6] = "STORE R0, 10"     

    # 8. Encerra o ciclo de execução da CPU.
    cpu.memoria[7] = "HALT"
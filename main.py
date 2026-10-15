"""
MAIN — Demonstração do código-base
AOC 2026.2

Este programa utiliza somente LOAD, JMP e HALT,
que já estão implementados no código-base.

Depois de implementar as demais instruções, substitua
o programa de teste por um programa mais completo.
"""

from cpu import CPU
from programas import carregar_programa_exemplo, carregar_programa_proprio


cpu = CPU()

# ==========================================
# PROGRAMA DE TESTE
# ==========================================
#
# A instrução JMP faz a CPU pular da posição 1
# para a posição 4.
#
# Portanto, LOAD R0, 99 nunca será executado.
#
# Resultado esperado:
# R0 = 5
# R1 = 8
#


print("======================================")
print("       CPU SIMULADA — 8 BITS")
print("======================================")

# 1. Executando o Programa de Exemplo (5 + 8)
print("\n>>> EXECUÇÃO 1: PROGRAMA DE EXEMPLO (5 + 8) <<<")
cpu_exemplo = CPU()
carregar_programa_exemplo(cpu_exemplo)
cpu_exemplo.executar()

print("\n--- RESULTADO FINAL (EXEMPLO) ---")
cpu_exemplo.mostrar_estado()
print(f"Memória[15]: {cpu_exemplo.memoria[15]}")

# 2. Executando o Programa Próprio (ADD + OR)
print("\n======================================")
print(">>> EXECUÇÃO 2: PROGRAMA PRÓPRIO (ADD + OR) <<<")
cpu_propria = CPU()
carregar_programa_proprio(cpu_propria)
cpu_propria.executar()


print("\n--- RESULTADO FINAL (PROGRAMA PRÓPRIO) ---")
cpu_propria.mostrar_estado()
print(f"Resultado do ADD (12 + 3): Memória[9] = {cpu_propria.memoria[9]}")
print(f"Resultado do OR (15 OR 16): Memória[10] = {cpu_propria.memoria[10]}")
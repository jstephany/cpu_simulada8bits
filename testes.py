"""
TESTES-BASE
AOC 2026.2

Os testes abaixo verificam apenas as partes já fornecidas
no código-base: LOAD, JMP e HALT.

Depois de implementar STORE e as operações da ULA,
os alunos deverão ampliar este arquivo.
"""

from cpu import CPU


def teste_load():
    cpu = CPU()

    cpu.memoria[0] = "LOAD R0, 25"
    cpu.memoria[1] = "HALT"

    cpu.executar()

    assert cpu.registradores["R0"] == 25

    print("[OK] LOAD")


def teste_jmp():
    cpu = CPU()

    cpu.memoria[0] = "LOAD R0, 10"
    cpu.memoria[1] = "JMP 4"
    cpu.memoria[2] = "LOAD R0, 99"
    cpu.memoria[3] = "HALT"
    cpu.memoria[4] = "LOAD R1, 20"
    cpu.memoria[5] = "HALT"

    cpu.executar()

    assert cpu.registradores["R0"] == 10
    assert cpu.registradores["R1"] == 20

    print("[OK] JMP")


def teste_halt():
    cpu = CPU()

    cpu.memoria[0] = "HALT"

    cpu.executar()

    assert cpu.halted is True

    print("[OK] HALT")


# IMPLEMENTAÇOES 

def teste_store():
    cpu = CPU()

    cpu.memoria[0] = "LOAD R0, 42"
    cpu.memoria[1] = "STORE R0, 10"
    cpu.memoria[2] = "HALT"

    cpu.executar()

    assert cpu.memoria[10] == 42
    print("[OK] STORE")


def teste_add():
    cpu = CPU()

    cpu.memoria[0] = "LOAD R0, 15"
    cpu.memoria[1] = "LOAD R1, 25"
    cpu.memoria[2] = "ADD R0, R1"
    cpu.memoria[3] = "HALT"

    cpu.executar()

    assert cpu.registradores["R0"] == 40
    print("[OK] ADD")


def teste_sub():
    cpu = CPU()

    cpu.memoria[0] = "LOAD R0, 30"
    cpu.memoria[1] = "LOAD R1, 12"
    cpu.memoria[2] = "SUB R0, R1"
    cpu.memoria[3] = "HALT"

    cpu.executar()

    assert cpu.registradores["R0"] == 18
    print("[OK] SUB")


def teste_operacoes_logicas():
    # Teste AND (12 AND 10 = 8)
    cpu_and = CPU()
    cpu_and.memoria[0] = "LOAD R0, 12"
    cpu_and.memoria[1] = "LOAD R1, 10"
    cpu_and.memoria[2] = "AND R0, R1"
    cpu_and.memoria[3] = "HALT"
    cpu_and.executar()
    assert cpu_and.registradores["R0"] == 8

    # Teste OR (12 OR 10 = 14)
    cpu_or = CPU()
    cpu_or.memoria[0] = "LOAD R0, 12"
    cpu_or.memoria[1] = "LOAD R1, 10"
    cpu_or.memoria[2] = "OR R0, R1"
    cpu_or.memoria[3] = "HALT"
    cpu_or.executar()
    assert cpu_or.registradores["R0"] == 14

    # Teste XOR (12 XOR 10 = 6)
    cpu_xor = CPU()
    cpu_xor.memoria[0] = "LOAD R0, 12"
    cpu_xor.memoria[1] = "LOAD R1, 10"
    cpu_xor.memoria[2] = "XOR R0, R1"
    cpu_xor.memoria[3] = "HALT"
    cpu_xor.executar()
    assert cpu_xor.registradores["R0"] == 6

    print("[OK] AND, OR e XOR")


def teste_avanco_pc():
    cpu = CPU()

    cpu.memoria[0] = "LOAD R0, 5"
    cpu.memoria[1] = "LOAD R1, 10"
    cpu.memoria[2] = "HALT"

    cpu.executar()

    # O PC deve estar em 2 onde encontrou HALT
    assert cpu.pc == 2
    print("[OK] Avanço do PC")


def teste_programa_exemplo():
    cpu = CPU()

    cpu.memoria[0] = "LOAD R0, 5"
    cpu.memoria[1] = "LOAD R1, 8"
    cpu.memoria[2] = "ADD R0, R1"
    cpu.memoria[3] = "STORE R0, 15"
    cpu.memoria[4] = "HALT"

    cpu.executar()

    assert cpu.memoria[15] == 13
    print("[OK] Programa de Exemplo (5 + 8)")


def teste_limite_8bits():
    cpu = CPU()

    cpu.memoria[0] = "LOAD R0, 200"
    cpu.memoria[1] = "LOAD R1, 100"
    cpu.memoria[2] = "ADD R0, R1"
    cpu.memoria[3] = "HALT"

    cpu.executar()

    assert cpu.registradores["R0"] == 44
    print("[OK] Limite de 8 bits (Overflow)")


if __name__ == "__main__":

    print("Executando testes-base...")
    print()

    teste_load()
    teste_jmp()
    teste_halt()
    teste_store()
    teste_add()
    teste_sub()
    teste_operacoes_logicas()
    teste_avanco_pc()
    teste_programa_exemplo()
    teste_limite_8bits()

    print()
    print("Todos os testes-base foram aprovados.")

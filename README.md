# Projeto: CPU Simulada de 8 bits
**Disciplina:** Arquitetura de Computadores (AOC 2026.2)
**Professor:** Wendley S. Silva
**Instituição:** Universidade Federal do Ceará (UFC) - Campus Sobral
**Aluno(s):** João Pedro Sousa Marques, Julia Stephany Ferreira Coelho Silva
---

## 1. Arquitetura da CPU

Este projeto implementa uma CPU simulada e didática com as seguintes características operacionais:

*   **Tamanho dos Dados:** 8 bits (valores limitados através de máscaras binárias `& 0xFF`).
*   **Registradores Gerais:** 4 registradores (R0, R1, R2 e R3).
*   **Contador de Programa:** 1 registrador PC (Program Counter) que rastreia a próxima instrução.
*   **Memória:** 16 posições de memória, identificadas de 0 a 15.
*   **Unidade Lógica e Aritmética (ULA):** Suporta operações de soma (ADD), subtração (SUB), e operações lógicas (AND, OR, XOR).
*   **Ciclo de Execução:** Baseado no ciclo clássico de *Fetch* (Busca), *Decode* (Decodificação) e *Execute* (Execução).

## 2. Conjunto de Instruções Implementado

*   `LOAD [REG], [VALOR]`: Carrega um valor inteiro no registrador especificado.
*   `STORE [REG], [ENDEREÇO]`: Salva o valor atual do registrador na posição de memória especificada.
*   `ADD [REG_DESTINO], [REG_ORIGEM]`: Soma os valores dos dois registradores e salva no destino.
*   `SUB [REG_DESTINO], [REG_ORIGEM]`: Subtrai o valor do reg. origem do reg. destino e salva no destino.
*   `AND`, `OR`, `XOR [REG_DESTINO], [REG_ORIGEM]`: Realiza a operação lógica bit a bit e salva no destino.
*   `JMP [ENDEREÇO]`: Altera o PC para o endereço especificado (salto incondicional).
*   `HALT`: Encerra a execução da CPU.

## 3. Programa Próprio Implementado

Para demonstrar o funcionamento completo da arquitetura, foi desenvolvido um programa próprio de 8 instruções que realiza operações matemáticas e lógicas e salva os resultados na memória.

**Lógica do Programa:**
1. Carrega o valor 12 em R0 e 3 em R1.
2. Realiza a soma (ADD R0, R1), resultando em 15 no R0.
3. Salva esse resultado (15) na Memória[9].
4. Carrega o valor 16 em R2.
5. Realiza a operação lógica OR (OR R0, R2) entre 15 e 16, resultando em 31.
6. Salva esse novo resultado (31) na Memória[10].
7. Encerra a execução (HALT).

## 4. Como Executar o Projeto

Certifique-se de ter o Python instalado em sua máquina. Navegue até a pasta do projeto via terminal e execute os seguintes comandos:

**Para rodar a simulação (Programa de Exemplo + Programa Próprio):**
```bash
python main.py
```

**Para rodar a suíte de testes automatizados:**
```bash
python testes.py
```
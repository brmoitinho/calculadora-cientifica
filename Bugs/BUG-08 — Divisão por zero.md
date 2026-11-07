## Identificação do Bug

**Título do Bug:** A divisão por zero encerra o programa com exceção  
**Localização do Bug:** `Calculadora.py`, função `divisao`, linha 13; chamada no ramo da opção 4, linha 73.

## Descrição Detalhada

**Descrição Clara do Bug:** A função divide diretamente `x / y` sem verificar se o denominador é zero. Quando o utilizador introduz zero, ocorre `ZeroDivisionError` e o processo termina com traceback.

**Contexto:** Reproduzido com Python 3.12.3 e NumPy 2.5.4 em Linux, usando entradas convertidas para `float`.

## Passos para Reproduzir

**Passo a Passo Detalhado:**
1. Executar `python Calculadora.py`.
2. Escolher a opção `4` (Divisão).
3. Introduzir `8` como primeiro número.
4. Introduzir `0` como segundo número.

**Consistência:** Consistente para denominador `0.0`.

## Resultado Esperado vs. Obtido

**Resultado Esperado:** Apresentar uma mensagem controlada a indicar que a divisão por zero não é permitida, sem encerrar abruptamente o programa.

**Resultado Obtido:** O programa termina com `ZeroDivisionError: float division by zero`.

## Evidências

**Screenshots:![alt text](image-7.png)** 

**Logs de Erro:** `ZeroDivisionError: float division by zero` em `Calculadora.py`, linha 13, na expressão `return x / y`.

## Severidade e Impacto

**Severidade do Bug:** Média.

**Impacto do Bug:** Uma entrada inválida provoca o encerramento abrupto da calculadora e impede a continuidade da utilização.

## Sugestões para Correção (Opcional)

**Possíveis Soluções:** Verificar se `y == 0` antes de dividir e apresentar uma mensagem de erro apropriada.

## Registro e Acompanhamento

**Data de Identificação:** 06/11/2026

**Status do Bug:** Não resolvido

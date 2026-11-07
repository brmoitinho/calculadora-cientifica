# Calculadora Científica

Aplicação de linha de comandos escrita em Python para realizar operações matemáticas. Este repositório também contém testes automatizados com pytest e relatórios de bugs na pasta `Bugs/`.

> **Estado do projeto:** em desenvolvimento. A divisão por zero foi tratada e está coberta por testes. Algumas outras operações anunciadas no menu ainda podem ter defeitos ou estar incompletas; consulta os relatórios em `Bugs/`.

## Requisitos

- Python 3.12 ou compatível
- NumPy
- pytest 7.1.3 para executar a suite de testes

## Instalação

Clona o repositório e entra na pasta do projeto. Recomenda-se criar um ambiente virtual:

```bash
python -m venv .venv
```

Ativa o ambiente virtual:

**Linux/macOS**

```bash
source .venv/bin/activate
```

**Windows PowerShell**

```powershell
.venv\Scripts\Activate.ps1
```

Instala as dependências:

```bash
python -m pip install numpy pytest==7.1.3
```

## Executar a calculadora

Na raiz do repositório, executa:

```bash
python Calculadora.py
```

Segue as instruções apresentadas no menu para escolher uma operação e introduzir os valores.

## Executar os testes

Com o ambiente virtual ativado, executa a suite de testes com:

```bash
python -m pytest -q
```

Os testes do BUG-08 verificam que a divisão por zero apresenta uma mensagem de erro controlada e que uma divisão válida continua a calcular o resultado esperado.

## Estrutura do projeto

```text
.
├── Calculadora.py
├── tests/
│   └── test_calculadora.py
├── Bugs/
│   └── BUG-08-divisao-por-zero.md
└── README.md
```

## Registo de bugs

Os relatórios individuais encontram-se na pasta `Bugs/`. Cada relatório documenta o defeito, a localização no código, os passos para reprodução, os resultados esperado e obtido, a severidade e o estado.

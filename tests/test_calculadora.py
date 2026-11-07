from pathlib import Path
import subprocess
import sys


RAIZ_PROJETO = Path(__file__).resolve().parents[1]
PROGRAMA = RAIZ_PROJETO / "Calculadora.py"


def executar_calculadora(entradas):
    return subprocess.run(
        [sys.executable, str(PROGRAMA)],
        input=entradas,
        text=True,
        capture_output=True,
        timeout=5,
        check=False,
    )


def test_divisao_por_zero_apresenta_erro_controlado():
    processo = executar_calculadora("4\n8\n0\nn\n")

    assert processo.returncode == 0
    assert "divisão por zero não permitida" in processo.stdout.lower()
    assert "ZeroDivisionError" not in processo.stderr


def test_divisao_normal_continua_a_calcular():
    processo = executar_calculadora("4\n8\n2\nn\n")

    assert processo.returncode == 0
    assert "Resultado: 4.0" in processo.stdout

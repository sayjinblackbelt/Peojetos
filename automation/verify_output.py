"""
Verifica se os artefatos necessários foram gerados pelo dashboard.
"""

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "automation" / "output"

expected = [
    "documentos_por_status.png",
    "progresso_por_disciplina.png",
    "requisitos_por_status.png",
    "dashboard.html",
]

missing = [
    filename for filename in expected
    if not (OUTPUT / filename).exists()
]

empty = [
    filename for filename in expected
    if (OUTPUT / filename).exists() and (OUTPUT / filename).stat().st_size == 0
]

if missing or empty:
    print("VERIFICAÇÃO DE OUTPUT FALHOU")
    for filename in missing:
        print(f"- Ausente: {filename}")
    for filename in empty:
        print(f"- Arquivo vazio: {filename}")
    sys.exit(1)

print("OUTPUT VALIDADO COM SUCESSO")
for filename in expected:
    size = (OUTPUT / filename).stat().st_size
    print(f"- {filename}: {size} bytes")

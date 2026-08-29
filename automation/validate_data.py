"""
Validação dos dados demonstrativos antes da geração do dashboard.

O objetivo é interromper o pipeline quando arquivos obrigatórios,
colunas essenciais ou valores inválidos forem identificados.
"""

from pathlib import Path
import csv
import sys

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "automation" / "sample_data"

SCHEMAS = {
    "project_documents.csv": {
        "required": ["codigo", "titulo", "disciplina", "revisao", "status", "responsavel", "progresso"],
        "numeric": ["progresso"],
    },
    "project_requirements.csv": {
        "required": ["id", "tema", "descricao", "status", "prioridade", "responsavel"],
        "numeric": [],
    },
}

errors = []

for filename, schema in SCHEMAS.items():
    path = DATA / filename

    if not path.exists():
        errors.append(f"Arquivo obrigatório não encontrado: {filename}")
        continue

    with path.open(encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file)
        headers = reader.fieldnames or []
        rows = list(reader)

    for column in schema["required"]:
        if column not in headers:
            errors.append(f"{filename}: coluna obrigatória ausente: {column}")

    if not rows:
        errors.append(f"{filename}: arquivo sem registros")

    for index, row in enumerate(rows, start=2):
        for column in schema["required"]:
            if column in headers and not str(row.get(column, "")).strip():
                errors.append(f"{filename}: linha {index}, campo vazio: {column}")

        for column in schema["numeric"]:
            value = row.get(column, "")
            try:
                number = float(value)
                if not 0 <= number <= 100:
                    errors.append(
                        f"{filename}: linha {index}, {column} fora do intervalo 0–100"
                    )
            except ValueError:
                errors.append(
                    f"{filename}: linha {index}, {column} não é numérico"
                )

if errors:
    print("VALIDAÇÃO FALHOU")
    for error in errors:
        print(f"- {error}")
    sys.exit(1)

print("VALIDAÇÃO CONCLUÍDA COM SUCESSO")
for filename in SCHEMAS:
    print(f"- {filename}: OK")

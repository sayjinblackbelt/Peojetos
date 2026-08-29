"""
Dashboard demonstrativo de PMO com dados simulados.

Não utiliza dados corporativos reais.
"""

from pathlib import Path
import csv
from collections import Counter, defaultdict

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "automation" / "sample_data"

documents_path = DATA / "project_documents.csv"
requirements_path = DATA / "project_requirements.csv"

def read_csv(path):
    with path.open(encoding="utf-8") as file:
        return list(csv.DictReader(file))

documents = read_csv(documents_path)
requirements = read_csv(requirements_path)

print("=" * 60)
print("DASHBOARD DE PMO — PROJETO DEMONSTRATIVO")
print("=" * 60)

print("\nDOCUMENTAÇÃO")
print(f"Total de documentos: {len(documents)}")

status = Counter(d["status"] for d in documents)
for key, value in status.most_common():
    print(f"  {key}: {value}")

progress = sum(float(d["progresso"]) for d in documents) / len(documents)
print(f"Progresso médio documental: {progress:.1f}%")

discipline = defaultdict(list)
for document in documents:
    discipline[document["disciplina"]].append(float(document["progresso"]))

print("\nAVANÇO POR DISCIPLINA")
for name, values in sorted(discipline.items()):
    print(f"  {name}: {sum(values)/len(values):.1f}%")

print("\nREQUISITOS")
print(f"Total: {len(requirements)}")

req_status = Counter(r["status"] for r in requirements)
for key, value in req_status.most_common():
    print(f"  {key}: {value}")

completed = req_status.get("concluido", 0)
completion = completed / len(requirements) * 100
print(f"Conclusão: {completion:.1f}%")

pending_high = [
    r for r in requirements
    if r["status"] != "concluido" and r["prioridade"] == "alta"
]

print(f"Pendências de alta prioridade: {len(pending_high)}")
for requirement in pending_high:
    print(f"  - {requirement['id']}: {requirement['descricao']}")

print("\nINDICADOR GERAL")
overall = (progress + completion) / 2
print(f"Índice demonstrativo de avanço: {overall:.1f}%")

print("\n" + "=" * 60)
print("DADOS FICTÍCIOS / DEMONSTRATIVOS — NÃO CORPORATIVOS")
print("=" * 60)

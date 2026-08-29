"""
Dashboard textual de PMO baseado em dados simulados.

O objetivo é demonstrar como informações de documentos e requisitos
podem ser consolidadas para acompanhamento de projeto.
"""

from pathlib import Path
import csv
from collections import Counter

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "automation" / "document_registry.csv"
REQUIREMENTS = ROOT / "automation" / "requirements_tracker.csv"

print("=" * 50)
print("DASHBOARD DE PMO — DADOS DEMONSTRATIVOS")
print("=" * 50)

if REGISTRY.exists():
    with REGISTRY.open(encoding="utf-8") as file:
        documents = list(csv.DictReader(file))

    statuses = Counter(row["status"] for row in documents)

    print(f"\nDOCUMENTOS: {len(documents)}")
    for status, total in statuses.items():
        print(f"  {status}: {total}")
else:
    print("\nRegistro documental ainda não foi gerado.")

if REQUIREMENTS.exists():
    with REQUIREMENTS.open(encoding="utf-8") as file:
        requirements = list(csv.DictReader(file))

    status_counter = Counter(row["status"] for row in requirements)
    priority_counter = Counter(row["prioridade"] for row in requirements)

    print(f"\nREQUISITOS: {len(requirements)}")
    print("Por status:")
    for status, total in status_counter.items():
        print(f"  {status}: {total}")

    print("Por prioridade:")
    for priority, total in priority_counter.items():
        print(f"  {priority}: {total}")

    completed = status_counter.get("concluido", 0)
    progress = (completed / len(requirements) * 100) if requirements else 0

    print(f"\nCONCLUSÃO DOS REQUISITOS: {progress:.1f}%")
else:
    print("\nBase de requisitos ainda não foi gerada.")

print("\n" + "=" * 50)
print("Este dashboard utiliza dados demonstrativos.")
print("=" * 50)

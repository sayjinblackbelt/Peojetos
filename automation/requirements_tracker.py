"""
Estrutura inicial para registro de requisitos e pendências.

Os dados podem posteriormente ser integrados com CSV,
Google Sheets, bancos de dados ou ferramentas de gestão.
"""

from pathlib import Path
import csv

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "automation" / "requirements_tracker.csv"

requirements = [
    {
        "id": "REQ-001",
        "tema": "Levantamento",
        "descricao": "Confirmar dados e condições reais do local.",
        "status": "pendente",
        "prioridade": "alta",
    },
    {
        "id": "REQ-002",
        "tema": "Engenharia",
        "descricao": "Definir solução após consolidação dos dados de entrada.",
        "status": "pendente",
        "prioridade": "alta",
    },
    {
        "id": "REQ-003",
        "tema": "Segurança",
        "descricao": "Realizar avaliação técnica das áreas e medidas aplicáveis.",
        "status": "pendente",
        "prioridade": "alta",
    },
]

with OUTPUT.open("w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=requirements[0].keys())
    writer.writeheader()
    writer.writerows(requirements)

print(f"{len(requirements)} requisitos registrados.")

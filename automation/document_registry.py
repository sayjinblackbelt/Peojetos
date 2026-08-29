"""
Registro simples de documentos do projeto.

Exemplo educacional para demonstrar automação de PMO.
"""

from pathlib import Path
import csv

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
OUTPUT = ROOT / "automation" / "document_registry.csv"

rows = []

for path in sorted(DOCS.glob("*.md")):
    rows.append({
        "arquivo": path.name,
        "caminho": str(path.relative_to(ROOT)),
        "categoria": "documentacao",
        "status": "base",
    })

with OUTPUT.open("w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(
        file,
        fieldnames=["arquivo", "caminho", "categoria", "status"],
    )
    writer.writeheader()
    writer.writerows(rows)

print(f"{len(rows)} documentos registrados em {OUTPUT.name}")

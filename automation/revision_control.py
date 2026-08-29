"""
Verificação básica de informações de revisão.

Este script procura referências a 'Revisão' nos documentos Markdown.
"""

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"

pattern = re.compile(r"revis[aã]o\s*[:|]\s*([^\n|]+)", re.IGNORECASE)

for path in sorted(DOCS.glob("*.md")):
    content = path.read_text(encoding="utf-8")
    match = pattern.search(content)

    if match:
        print(f"OK   {path.name}: revisão {match.group(1).strip()}")
    else:
        print(f"CHECK {path.name}: revisão não identificada")

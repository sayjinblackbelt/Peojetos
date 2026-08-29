"""
Gera gráficos e um relatório HTML a partir dos dados demonstrativos.

Dependência externa:
    matplotlib

Os dados utilizados são fictícios.
"""

from pathlib import Path
import csv
from collections import Counter, defaultdict
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "automation" / "sample_data"
OUTPUT = ROOT / "automation" / "output"
OUTPUT.mkdir(exist_ok=True)

def read_csv(name):
    with (DATA / name).open(encoding="utf-8") as file:
        return list(csv.DictReader(file))

documents = read_csv("project_documents.csv")
requirements = read_csv("project_requirements.csv")

doc_status = Counter(d["status"] for d in documents)
discipline = defaultdict(list)

for d in documents:
    discipline[d["disciplina"]].append(float(d["progresso"]))

discipline_progress = {
    name: sum(values) / len(values)
    for name, values in discipline.items()
}

req_status = Counter(r["status"] for r in requirements)

# Gráfico 1
plt.figure(figsize=(8, 5))
plt.bar(doc_status.keys(), doc_status.values())
plt.title("Documentos por Status")
plt.xlabel("Status")
plt.ylabel("Quantidade")
plt.xticks(rotation=20)
plt.tight_layout()
plt.savefig(OUTPUT / "documentos_por_status.png", dpi=150)
plt.close()

# Gráfico 2
plt.figure(figsize=(8, 5))
plt.bar(discipline_progress.keys(), discipline_progress.values())
plt.title("Progresso por Disciplina")
plt.xlabel("Disciplina")
plt.ylabel("Progresso (%)")
plt.xticks(rotation=25)
plt.ylim(0, 100)
plt.tight_layout()
plt.savefig(OUTPUT / "progresso_por_disciplina.png", dpi=150)
plt.close()

# Gráfico 3
plt.figure(figsize=(7, 5))
plt.bar(req_status.keys(), req_status.values())
plt.title("Requisitos por Status")
plt.xlabel("Status")
plt.ylabel("Quantidade")
plt.xticks(rotation=20)
plt.tight_layout()
plt.savefig(OUTPUT / "requisitos_por_status.png", dpi=150)
plt.close()

document_progress = sum(float(d["progresso"]) for d in documents) / len(documents)
requirements_completion = (
    req_status.get("concluido", 0) / len(requirements) * 100
)
overall = (document_progress + requirements_completion) / 2

html = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<title>Dashboard Demonstrativo de PMO</title>
<style>
body {{ font-family: Arial, sans-serif; max-width: 1100px; margin: 40px auto; padding: 20px; }}
h1 {{ border-bottom: 2px solid #333; padding-bottom: 10px; }}
.cards {{ display: flex; gap: 15px; flex-wrap: wrap; }}
.card {{ border: 1px solid #ddd; padding: 20px; min-width: 200px; }}
.value {{ font-size: 30px; font-weight: bold; }}
img {{ max-width: 100%; margin: 20px 0; border: 1px solid #ddd; }}
.note {{ margin-top: 30px; font-size: 0.9em; }}
</style>
</head>
<body>
<h1>Dashboard de PMO — Projeto Demonstrativo</h1>

<div class="cards">
<div class="card"><div>Documentos</div><div class="value">{len(documents)}</div></div>
<div class="card"><div>Progresso documental</div><div class="value">{document_progress:.1f}%</div></div>
<div class="card"><div>Requisitos concluídos</div><div class="value">{requirements_completion:.1f}%</div></div>
<div class="card"><div>Índice geral</div><div class="value">{overall:.1f}%</div></div>
</div>

<h2>Documentos por Status</h2>
<img src="documentos_por_status.png">

<h2>Progresso por Disciplina</h2>
<img src="progresso_por_disciplina.png">

<h2>Requisitos por Status</h2>
<img src="requisitos_por_status.png">

<p class="note">
Dados fictícios e demonstrativos. Nenhuma informação corporativa real é utilizada.
</p>
</body>
</html>
"""

(OUTPUT / "dashboard.html").write_text(html, encoding="utf-8")

print(f"Dashboard gerado em: {OUTPUT}")

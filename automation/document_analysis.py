"""
Análise heurística demonstrativa de documentos de projeto.

Esta versão não utiliza dados corporativos nem serviços externos de IA.
Ela simula uma etapa de análise inteligente por meio de regras e
pontuações de completude, servindo como base para futura integração
com um modelo de IA.
"""

from pathlib import Path
import csv
import json

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "automation" / "sample_data"
OUTPUT = ROOT / "automation" / "output"
OUTPUT.mkdir(exist_ok=True)

documents_path = DATA / "project_documents.csv"

with documents_path.open(encoding="utf-8", newline="") as file:
    documents = list(csv.DictReader(file))

required_fields = [
    "codigo",
    "titulo",
    "disciplina",
    "revisao",
    "status",
    "responsavel",
    "progresso",
]

alerts = []
results = []

for document in documents:
    missing = [
        field for field in required_fields
        if not str(document.get(field, "")).strip()
    ]

    progress = float(document.get("progresso", 0))
    status = document.get("status", "").lower()

    score = 100 - (len(missing) * 15)

    if status == "Aprovado" and progress < 100:
        alerts.append({
            "codigo": document["codigo"],
            "tipo": "inconsistencia",
            "mensagem": "Documento aprovado com progresso inferior a 100%."
        })
        score -= 20

    if status == "Pendente" and progress > 50:
        alerts.append({
            "codigo": document["codigo"],
            "tipo": "atencao",
            "mensagem": "Documento pendente apresenta progresso elevado."
        })
        score -= 10

    if progress == 0 and status not in ["Pendente"]:
        alerts.append({
            "codigo": document["codigo"],
            "tipo": "atencao",
            "mensagem": "Documento sem progresso e com status diferente de pendente."
        })
        score -= 10

    score = max(0, score)

    results.append({
        "codigo": document["codigo"],
        "titulo": document["titulo"],
        "classificacao": document["disciplina"],
        "status": document["status"],
        "progresso": progress,
        "campos_ausentes": missing,
        "score_qualidade": score,
    })

report = {
    "finalidade": "Demonstração de análise inteligente com dados fictícios",
    "documentos_analisados": len(results),
    "alertas": alerts,
    "resultados": results,
}

report_path = OUTPUT / "document_analysis_report.json"
report_path.write_text(
    json.dumps(report, ensure_ascii=False, indent=2),
    encoding="utf-8"
)

print("=" * 60)
print("ANÁLISE INTELIGENTE DEMONSTRATIVA")
print("=" * 60)
print(f"Documentos analisados: {len(results)}")
print(f"Alertas encontrados: {len(alerts)}")
print(f"Relatório: {report_path}")

if alerts:
    print("\nALERTAS")
    for alert in alerts:
        print(f"- {alert['codigo']}: {alert['mensagem']}")

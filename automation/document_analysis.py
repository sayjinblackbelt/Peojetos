"""
Análise heurística demonstrativa de documentos e risco documental.

Utiliza exclusivamente dados fictícios e regras transparentes para
demonstrar uma camada inicial de priorização de riscos em PMO.
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
    "codigo", "titulo", "disciplina", "revisao",
    "status", "responsavel", "progresso",
]

alerts = []
results = []

def add_alert(document, tipo, mensagem, peso):
    alerts.append({
        "codigo": document["codigo"],
        "tipo": tipo,
        "mensagem": mensagem,
        "peso_risco": peso,
    })

for document in documents:
    missing = [
        field for field in required_fields
        if not str(document.get(field, "")).strip()
    ]

    progress = float(document.get("progresso", 0))
    status = document.get("status", "").strip().lower()

    score = 100 - (len(missing) * 15)
    risk_points = len(missing) * 20

    if missing:
        add_alert(
            document,
            "dados_incompletos",
            f"Documento possui {len(missing)} campo(s) obrigatório(s) ausente(s).",
            len(missing) * 20,
        )

    if status == "aprovado" and progress < 100:
        add_alert(
            document,
            "inconsistencia",
            "Documento aprovado com progresso inferior a 100%.",
            35,
        )
        score -= 20
        risk_points += 35

    if status == "pendente" and progress > 50:
        add_alert(
            document,
            "atencao",
            "Documento pendente apresenta progresso elevado.",
            15,
        )
        score -= 10
        risk_points += 15

    if progress == 0 and status != "pendente":
        add_alert(
            document,
            "atencao",
            "Documento sem progresso e com status diferente de pendente.",
            20,
        )
        score -= 10
        risk_points += 20

    risk_score = min(100, risk_points)

    if risk_score >= 60:
        risk_level = "Alto"
    elif risk_score >= 30:
        risk_level = "Médio"
    else:
        risk_level = "Baixo"

    score = max(0, score)

    results.append({
        "codigo": document["codigo"],
        "titulo": document["titulo"],
        "classificacao": document["disciplina"],
        "status": document["status"],
        "progresso": progress,
        "campos_ausentes": missing,
        "score_qualidade": score,
        "score_risco": risk_score,
        "nivel_risco": risk_level,
    })

risk_distribution = {
    "Baixo": sum(item["nivel_risco"] == "Baixo" for item in results),
    "Médio": sum(item["nivel_risco"] == "Médio" for item in results),
    "Alto": sum(item["nivel_risco"] == "Alto" for item in results),
}

project_risk_index = (
    sum(item["score_risco"] for item in results) / len(results)
    if results else 0
)

priority_documents = sorted(
    results,
    key=lambda item: item["score_risco"],
    reverse=True,
)[:5]

report = {
    "finalidade": "Demonstração de análise inteligente e risco documental com dados fictícios",
    "documentos_analisados": len(results),
    "indice_risco_projeto": round(project_risk_index, 1),
    "distribuicao_risco": risk_distribution,
    "documentos_prioritarios": priority_documents,
    "alertas": alerts,
    "resultados": results,
}

report_path = OUTPUT / "document_analysis_report.json"
report_path.write_text(
    json.dumps(report, ensure_ascii=False, indent=2),
    encoding="utf-8"
)

print("=" * 60)
print("ANÁLISE INTELIGENTE E RISCO DOCUMENTAL")
print("=" * 60)
print(f"Documentos analisados: {len(results)}")
print(f"Alertas encontrados: {len(alerts)}")
print(f"Índice de risco do projeto: {project_risk_index:.1f}")
print(f"Distribuição: {risk_distribution}")
print(f"Relatório: {report_path}")

if priority_documents:
    print("\nDOCUMENTOS PRIORITÁRIOS")
    for item in priority_documents:
        print(f"- {item['codigo']}: risco {item['score_risco']} ({item['nivel_risco']})")

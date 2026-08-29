"""
Análise temporal demonstrativa para acompanhamento de projeto.

Utiliza dados fictícios para calcular tendências de progresso, risco e
uma previsão linear simples de conclusão.
"""

from pathlib import Path
import csv
import json

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "automation" / "sample_data"
OUTPUT = ROOT / "automation" / "output"
OUTPUT.mkdir(exist_ok=True)

path = DATA / "project_history.csv"

with path.open(encoding="utf-8", newline="") as file:
    history = list(csv.DictReader(file))

weeks = [int(item["semana"]) for item in history]
progress = [float(item["progresso"]) for item in history]
risk = [float(item["indice_risco"]) for item in history]
completed = [int(item["documentos_concluidos"]) for item in history]

if len(progress) >= 2:
    progress_rate = (progress[-1] - progress[0]) / (weeks[-1] - weeks[0])
    risk_rate = (risk[-1] - risk[0]) / (weeks[-1] - weeks[0])
else:
    progress_rate = 0
    risk_rate = 0

remaining = max(0, 100 - progress[-1])
weeks_to_completion = remaining / progress_rate if progress_rate > 0 else None
forecast_week = weeks[-1] + weeks_to_completion if weeks_to_completion else None

report = {
    "finalidade": "Análise temporal demonstrativa com dados fictícios",
    "ultima_semana": weeks[-1],
    "progresso_atual": progress[-1],
    "risco_atual": risk[-1],
    "taxa_media_progresso_semana": round(progress_rate, 2),
    "tendencia_risco_semana": round(risk_rate, 2),
    "previsao_semana_conclusao": round(forecast_week, 1) if forecast_week else None,
    "documentos_concluidos": completed[-1],
    "historico": history,
}

report_path = OUTPUT / "project_trend_report.json"
report_path.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")

print("ANÁLISE TEMPORAL CONCLUÍDA")
print(f"Progresso atual: {progress[-1]}%")
print(f"Risco atual: {risk[-1]}")
print(f"Taxa média semanal: {progress_rate:.2f} pontos")
print(f"Previsão de conclusão: semana {report['previsao_semana_conclusao']}")

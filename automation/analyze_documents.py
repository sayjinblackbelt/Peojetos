"""
Ponto de entrada para análise documental demonstrativa.

Uso:
    python automation/analyze_documents.py
"""

from document_analysis import report

print("\nResumo final")
print(f"Documentos: {report['documentos_analisados']}")
print(f"Alertas: {len(report['alertas'])}")

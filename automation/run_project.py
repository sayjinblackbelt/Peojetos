"""
Executa a sequência básica de automação demonstrativa.

Uso:
    python automation/run_project.py
"""

from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]

scripts = [
    "document_registry.py",
    "requirements_tracker.py",
    "revision_control.py",
    "dashboard.py",
]

for script in scripts:
    path = ROOT / "automation" / script
    print(f"\n>>> Executando {script}")
    subprocess.run([sys.executable, str(path)], check=True)

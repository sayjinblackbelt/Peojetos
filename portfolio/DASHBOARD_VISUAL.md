# Dashboard Visual — Demonstração de Automação de PMO

## Objetivo

Demonstrar como dados estruturados de projetos podem ser transformados em indicadores e visualizações automáticas.

## Pipeline

Dados CSV → Python → Processamento → Indicadores → Gráficos → Relatório HTML

## Indicadores

- quantidade total de documentos;
- progresso médio documental;
- avanço por disciplina;
- distribuição por status;
- percentual de requisitos concluídos;
- índice demonstrativo geral.

## Execução

Instalar a dependência:

```bash
pip install -r automation/requirements.txt
```

Gerar o dashboard:

```bash
python automation/generate_visual_dashboard.py
```

## Resultado

O script gera imagens PNG e um relatório HTML que pode ser aberto em qualquer navegador.

## Valor profissional demonstrado

**PMO + Dados + Python + Automação + Visualização.**

Todos os dados são fictícios e não representam informações de projetos corporativos reais.

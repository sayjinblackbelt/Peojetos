# Próximo Case — Document Intelligence Agent

## Objetivo

O próximo projeto do portfólio será um agente demonstrativo para análise de documentos, com evolução gradual de regras determinísticas para análise assistida por IA.

## MVP

```text
Texto
 ↓
Extração
 ↓
Regras
 ↓
Pendências
 ↓
Classificação
 ↓
Relatório JSON
```

## Evolução

### Fase 1 — Análise local

Python + JSON + regras.

### Fase 2 — API

FastAPI para expor a análise como serviço.

### Fase 3 — IA

Integração opcional com modelo de linguagem para:

- resumo;
- classificação;
- extração de requisitos;
- identificação de riscos.

### Fase 4 — Interface

Upload demonstrativo e visualização dos resultados.

## Princípios

- dados fictícios ou públicos;
- nenhuma informação corporativa confidencial;
- revisão humana;
- resultados rastreáveis;
- separação entre regras e IA.

# Validação e Qualidade do Pipeline

## Objetivo

Adicionar controles automáticos antes da publicação do dashboard.

## Etapas de qualidade

### 1. Validação dos dados

O script `automation/validate_data.py` verifica:

- existência dos arquivos CSV;
- presença das colunas obrigatórias;
- existência de registros;
- campos obrigatórios vazios;
- valores numéricos inválidos;
- intervalo permitido para progresso.

### 2. Geração do dashboard

O script principal processa os dados e gera os artefatos visuais.

### 3. Verificação dos artefatos

O script `automation/verify_output.py` confirma:

- existência dos arquivos esperados;
- ausência de arquivos vazios.

## Pipeline

Dados CSV
↓
Validação
↓
Geração
↓
Verificação de output
↓
Empacotamento
↓
Deploy

## Benefício

Falhas simples são identificadas antes da publicação, reduzindo o risco de disponibilizar um dashboard incompleto ou inconsistente.

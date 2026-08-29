# GitHub Automation

Esta pasta contém workflows para automatizar tarefas do projeto.

## Workflow atual

### Generate PMO Dashboard

O workflow é executado:

- quando arquivos da pasta `automation/` são enviados para a branch principal;
- manualmente pela aba **Actions** do GitHub.

Etapas:

1. obtém o código do repositório;
2. configura Python;
3. instala dependências;
4. gera gráficos e dashboard HTML;
5. registra os arquivos gerados no repositório quando houver alterações.

## Objetivo

Demonstrar uma aplicação prática de CI/CD e automação para processos de PMO.

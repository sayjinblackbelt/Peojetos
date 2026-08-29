# Automação e CI/CD no Case de PMO

## Problema

Dashboards e relatórios frequentemente dependem de atualização manual, o que pode gerar atrasos e inconsistências.

## Solução demonstrada

O projeto utiliza um workflow do GitHub Actions para:

- identificar alterações relevantes;
- preparar automaticamente o ambiente Python;
- instalar dependências;
- executar o gerador do dashboard;
- atualizar os artefatos gerados.

## Arquitetura

```text
Dados demonstrativos
       ↓
Repositório GitHub
       ↓
GitHub Actions
       ↓
Python
       ↓
Dashboard HTML + gráficos
       ↓
Versionamento automático
```

## Competências demonstradas

- GitHub;
- GitHub Actions;
- automação;
- CI/CD;
- Python;
- dados estruturados;
- indicadores de PMO.

## Limite

A implementação utiliza exclusivamente informações fictícias para demonstração técnica.

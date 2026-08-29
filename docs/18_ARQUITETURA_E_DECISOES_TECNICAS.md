# Arquitetura e Decisões Técnicas

## Visão

O Peojetos foi estruturado como um case demonstrativo com separação entre:

- dados;
- processamento;
- análise;
- apresentação;
- automação de deploy.

## Camadas

### Dados

Arquivos CSV fictícios representam documentos, requisitos e histórico temporal.

### Processamento

Scripts Python validam dados e geram artefatos para consumo do dashboard.

### Análise

A camada analítica calcula:

- qualidade documental;
- inconsistências;
- risco;
- prioridades;
- tendências.

### Apresentação

A interface web consome CSV e JSON gerados pelo pipeline.

### Automação

GitHub Actions executa validações, análises, build e deploy.

## Decisões

### Separação entre dados e lógica

Permite substituir CSV por API, banco de dados ou planilha sem reescrever toda a interface.

### Heurísticas transparentes

As regras atuais são intencionalmente explicáveis. Isso facilita testes e revisão humana.

### JSON como artefato intermediário

O relatório JSON desacopla análise Python e interface JavaScript.

## Evolução arquitetural

```text
CSV → Banco/API → Serviços de análise → Dashboard
                ↓
             IA/LLM
```

A evolução deve preservar validação, rastreabilidade e revisão humana.

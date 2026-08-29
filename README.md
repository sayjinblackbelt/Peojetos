# Peojetos

> **PMO · Governança Documental · Python · Automação · Dados · Dashboard · CI/CD**

Case técnico de portfólio que transforma um fluxo demonstrativo de documentação e acompanhamento de projetos em uma solução automatizada, reproduzível e publicada na web.

## 🎯 O que este projeto demonstra

| Área | Demonstração |
|---|---|
| PMO | acompanhamento, indicadores e priorização |
| Documentação | organização, status, revisão e requisitos |
| Dados | CSV estruturado e validação |
| Python | geração e análise automatizada |
| Qualidade | identificação de inconsistências |
| Risco | score e classificação documental |
| Tendências | evolução temporal e previsão simples |
| Web | HTML, CSS e JavaScript |
| DevOps | GitHub Actions e GitHub Pages |

## 🏗️ Arquitetura

```text
┌──────────────────────────────┐
│ Dados fictícios estruturados │
│ CSV                          │
└──────────────┬───────────────┘
               ↓
┌──────────────────────────────┐
│ Validação de dados           │
│ Python                       │
└──────────────┬───────────────┘
               ↓
┌──────────────────────────────────┐
│ Camada de análise                │
│ • qualidade documental           │
│ • inconsistências                │
│ • risco e prioridades            │
│ • tendências temporais           │
└──────────────┬───────────────────┘
               ↓
┌──────────────────────────────┐
│ Artefatos JSON e gráficos    │
└──────────────┬───────────────┘
               ↓
┌──────────────────────────────┐
│ Dashboard Web                │
│ HTML + CSS + JavaScript      │
└──────────────┬───────────────┘
               ↓
┌──────────────────────────────┐
│ GitHub Actions               │
│ Build + validação + deploy   │
└──────────────┬───────────────┘
               ↓
┌──────────────────────────────┐
│ GitHub Pages                 │
└──────────────────────────────┘
```

## 📊 Funcionalidades

### Dashboard de PMO

- documentos e status;
- progresso documental;
- requisitos concluídos;
- índice geral demonstrativo;
- gráficos por disciplina e status.

### Análise inteligente documental

A camada atual utiliza regras heurísticas transparentes para:

- verificar campos obrigatórios;
- identificar inconsistências entre status e progresso;
- atribuir score de qualidade;
- registrar alertas estruturados.

### Risco e prioridades

Cada documento pode receber:

- score de risco;
- nível **Baixo**, **Médio** ou **Alto**;
- posição na lista de prioridades.

Também é calculado um **índice demonstrativo de risco do projeto**.

### Tendências temporais

O módulo temporal acompanha:

- evolução do progresso;
- tendência do risco;
- documentos concluídos;
- projeção linear simples de conclusão.

> A previsão é demonstrativa e não substitui planejamento profissional.

## 📁 Estrutura do repositório

```text
Peojetos/
├── automation/
│   ├── sample_data/
│   ├── validate_data.py
│   ├── generate_visual_dashboard.py
│   ├── document_analysis.py
│   ├── project_trend_analysis.py
│   └── verify_output.py
├── docs/
│   ├── análise documental
│   └── análise temporal
├── portfolio/
│   └── competências e contexto do case
├── web/
│   ├── index.html
│   ├── app.js
│   └── style.css
└── .github/workflows/
    └── pages.yml
```

## 🔄 Pipeline automatizado

A publicação segue o fluxo:

```text
Push no repositório
        ↓
Instalação de dependências
        ↓
Validação dos dados
        ↓
Geração dos indicadores
        ↓
Análise documental
        ↓
Análise de risco
        ↓
Análise temporal
        ↓
Verificação dos outputs
        ↓
Build do site
        ↓
Deploy no GitHub Pages
```

## 💻 Executar localmente

### Instalar dependências

```bash
pip install -r automation/requirements.txt
```

### Executar análises

```bash
python automation/validate_data.py
python automation/generate_visual_dashboard.py
python automation/analyze_documents.py
python automation/project_trend_analysis.py
python automation/verify_output.py
```

### Visualizar a interface

```bash
python -m http.server 8000
```

## 🧩 Decisões técnicas

### Por que CSV?

O CSV facilita:

- leitura humana;
- versionamento;
- reprodução do case;
- integração futura com planilhas ou APIs.

### Por que regras heurísticas antes de IA?

Uma base determinística permite:

- resultados reproduzíveis;
- transparência;
- testes simples;
- menor dependência de serviços externos.

A arquitetura permite evoluir posteriormente para modelos de IA.

### Por que GitHub Actions?

Para demonstrar um fluxo próximo a práticas reais de engenharia:

- automação;
- validação;
- build;
- publicação contínua.

## 🚀 Possíveis evoluções

- banco de dados;
- API;
- integração com Google Sheets;
- histórico persistente;
- alertas automáticos;
- autenticação;
- comparação entre revisões;
- análise de documentos por IA;
- classificação automática;
- geração de resumo executivo.

## 👤 Contexto profissional

O case foi inspirado em experiência profissional anterior relacionada a **PMO, avaliação documental e apoio à elaboração de documentos e projetos técnicos**.

As atividades envolveram organização de informações, acompanhamento de fluxos documentais, consolidação de materiais e apoio à preparação de documentos junto a profissionais técnicos responsáveis.

Este repositório não representa documentação original de empresa ou projeto.

## 🔒 Confidencialidade

Todo o conteúdo publicado é:

- genérico;
- reconstruído para fins de portfólio;
- baseado em dados fictícios;
- sem informações operacionais confidenciais;
- sem documentos internos;
- sem fornecedores, contratos ou valores;
- sem projetos proprietários.

Responsabilidades técnicas formais, cálculos, validações e aprovações pertencem aos profissionais legalmente habilitados e às áreas responsáveis.

---

## 🛠️ Tecnologias

**Python · CSV · HTML · CSS · JavaScript · GitHub · GitHub Actions · GitHub Pages**

**Finalidade:** portfólio técnico e demonstração prática de competências em PMO, automação, dados e desenvolvimento de soluções.

# Automação do Dashboard com GitHub Actions

## Objetivo

Automatizar a geração do dashboard visual sempre que os dados ou scripts relacionados à automação forem atualizados.

## Fluxo

Push ou execução manual
↓
GitHub Actions
↓
Ambiente Python
↓
Instalação de dependências
↓
Execução do dashboard
↓
Geração de gráficos e HTML
↓
Commit automático dos resultados, quando houver alteração

## Benefícios

- elimina execução manual repetitiva;
- mantém os indicadores atualizados;
- demonstra práticas de CI/CD;
- cria rastreabilidade das atualizações;
- integra GitHub e Python.

## Segurança e governança

O workflow utiliza apenas dados demonstrativos disponíveis publicamente no repositório.

Para projetos reais, recomenda-se revisar permissões, evitar inclusão de informações confidenciais e utilizar mecanismos apropriados para segredos e credenciais.

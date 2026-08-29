# Interface Web e GitHub Pages

## Objetivo

Disponibilizar uma apresentação pública e visual do dashboard demonstrativo.

## Arquitetura

Dados simulados → Python → Gráficos → Interface HTML/CSS/JavaScript → GitHub Pages

## Componentes

### Interface

A pasta `web/` contém:

- página principal;
- estilos responsivos;
- carregamento de dados CSV;
- indicadores calculados no navegador.

### Automação

Os gráficos são gerados pelos scripts Python existentes.

### Publicação

O workflow de Pages prepara uma versão estática da interface e publica os arquivos por meio do GitHub Pages.

## Observação

A ativação inicial do GitHub Pages pode exigir a configuração da origem de publicação nas configurações do repositório.

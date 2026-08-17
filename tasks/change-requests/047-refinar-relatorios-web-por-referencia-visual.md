# Task 047 - Refinar relatórios web por referência visual

## Status

done

## Tipo

front

## Stacks envolvidos

- front-end

## Perfil do projeto

- stack web escolhida: front-end (React/Vite)
- mobile: sim

## Contrato

- nao se aplica; preservar integrações atuais de listagem, geração, download e disponibilização

## Modo de execucao

single-stack

## Slice vertical

- Slice 017 - Redesign da interface interna web
- `tasks/slices/017-redesign-interface-interna-web.md`

## Referencia visual

### Tipo

imagem fornecida pelo usuario no chat

### Cobertura

- card de filtros do relatório com hierarquia visual mais clara
- estado vazio destacado com ilustração/ícone central
- aviso inferior em barra discreta

### Lacunas

- a referência cobre principalmente o estado sem relatórios
- decisão: manter a tabela atual quando houver registros, mas encaixada na mesma linguagem visual

## Objetivo

Aplicar na página de relatórios o design da referência enviada, usando as cores do projeto e preservando os fluxos atuais.

## Contexto mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`, `tasks/000-index.md`
- esta task, Slice 017 e `.agents/state/handoffs/TASK-046.md`

## Contexto sob demanda

- imagem enviada pelo usuário no chat
- `front-end/docs/ai/{AGENTS.md,ACCESSIBILITY.md}`
- `front-end/src/pages/Main/Reports/{index.tsx,styles.module.css}`
- `front-end/src/ui/{Button,Card,Table}/**`

## Orçamento de contexto

- baixo; limitado à tela de relatórios web e componentes compartilhados imediatamente envolvidos

## Criterios de conclusao

- [x] card de filtros segue a hierarquia e densidade da referência
- [x] estado vazio da tela de relatórios fica próximo da composição enviada
- [x] aviso inferior fica destacado e coerente com o design do módulo
- [x] tabela e ações continuam funcionais quando houver relatórios
- [x] lint aprovado

## Resultado da execucao

- a página de relatórios ganhou um card de filtros com ícone, cabeçalho e controles mais próximos da referência
- o estado vazio foi redesenhado com área destacada, ícone central e mensagem mais clara
- o aviso sobre compartilhamento com responsável virou uma barra informativa dedicada
- a tabela existente foi preservada para estados com dados, mas integrada ao novo visual da tela

## Contexto utilizado

- fontes globais, Slice 017, handoff 046, imagem do chat, docs locais de front/acessibilidade, página de relatórios e componentes compartilhados usados nela

## Handoff

- `.agents/state/handoffs/TASK-047.md`

## Arquivos alterados

- `front-end/src/pages/Main/Reports/{index.tsx,styles.module.css}`
- task, slice, índice e handoff

## Validacoes executadas

- `cd front-end && npm run lint`

## Pendencias pos-task

- nenhuma

## Status final

done

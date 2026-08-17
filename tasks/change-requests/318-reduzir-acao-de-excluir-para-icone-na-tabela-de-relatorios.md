# Task 318 - Reduzir ação de excluir para ícone na tabela de relatórios

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

- nao se aplica; refinamento visual sem alterar API

## Modo de execucao

single-stack

## Slice vertical

- Slice 011 - Relatorios de evolucao
- `tasks/slices/011-relatorios-evolucao.md`

## Referencia visual

### Stack de referencia visual

- front-end

### Tipo de referencia visual

- feedback direto do usuario + padrao visual atual da tabela

### Fonte primaria visual

- `front-end/src/pages/Main/Reports/**`
- `front-end/src/ui/Button/**`
- `front-end/src/ui/Modal/**`

### Lacunas

- sem print novo; o modal de confirmação existente deve ser preservado integralmente

## Objetivo

Transformar a ação de exclusão da tabela de relatórios em um botão somente com ícone de lixeira, mantendo o modal de confirmação já implementado.

## Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/011-relatorios-evolucao.md`
- `.agents/state/handoffs/TASK-317.md`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| Acessibilidade UI | `front-end/docs/ai/ACCESSIBILITY.md` | manter nome acessível no botão ícone-only | sim |
| Reuso de primitiva | `front-end/docs/ai/COMPONENT_REUSE.md` | reutilizar `Button` sem quebrar padrão | sim |
| Página de relatórios | `front-end/src/pages/Main/Reports/**` | reduzir CTA de exclusão para ícone | sim |
| Botão compartilhado | `front-end/src/ui/Button/**` | confirmar suporte a ícone-only | sim |

## Orçamento de contexto

- baixo
- estrategia: limitar a mudança ao consumidor da rota `/relatorios`

## Criterios de conclusao

- [x] a ação de exclusão na tabela aparece só com ícone de lixeira
- [x] o botão continua acessível por teclado e com nome acessível
- [x] o modal de confirmação de exclusão permanece funcionando

## Dependencias

- Task 317 - done

## Resultado da execucao

- a ação de exclusão na tabela de relatórios foi reduzida para um botão compactado somente com ícone de lixeira
- o botão recebeu `aria-label="Excluir relatório"` para preservar acessibilidade em interação por teclado e leitor de tela
- o modal de confirmação destrutiva existente foi mantido sem alteração de comportamento

## Contexto utilizado

### Mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/011-relatorios-evolucao.md`
- `.agents/state/handoffs/TASK-317.md`

### Sob demanda

- `front-end/docs/ai/ACCESSIBILITY.md`
- `front-end/docs/ai/COMPONENT_REUSE.md`
- `front-end/src/pages/Main/Reports/index.tsx`
- `front-end/src/pages/Main/Reports/styles.module.css`
- `front-end/src/ui/Button/index.tsx`

### Contexto evitado

- `backend/`, porque não há mudança de contrato, regra de negócio ou persistência

## Handoff

- `.agents/state/handoffs/TASK-318.md`

## Arquivos alterados

- `front-end/src/pages/Main/Reports/index.tsx`
- `front-end/src/pages/Main/Reports/styles.module.css`
- `tasks/change-requests/318-reduzir-acao-de-excluir-para-icone-na-tabela-de-relatorios.md`
- `tasks/slices/011-relatorios-evolucao.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-318.md`

## Validacoes executadas

- `cd front-end && npx eslint src/pages/Main/Reports/index.tsx`
- `cd front-end && npm run build`

## Pendencias pos-task

- nenhuma

## Status final

done

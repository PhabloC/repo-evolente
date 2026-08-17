# Task 323 - Adicionar confirmação ao disponibilizar relatório

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

- nao se aplica; ajuste de interação sem alterar API

## Modo de execucao

single-stack

## Slice vertical

- Slice 011 - Relatorios de evolucao
- `tasks/slices/011-relatorios-evolucao.md`

## Referencia visual

### Stack de referencia visual

- front-end

### Tipo de referencia visual

- feedback direto do usuario + padrão atual dos modais da tela

### Fonte primaria visual

- `front-end/src/pages/Main/Reports/**`
- `front-end/src/ui/Modal/**`

### Lacunas

- sem novo print; o modal de confirmação deve seguir a mesma linguagem usada hoje na exclusão

## Objetivo

Exigir confirmação em modal antes de disponibilizar um relatório ao responsável.

## Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/011-relatorios-evolucao.md`
- `.agents/state/handoffs/TASK-322.md`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| Acessibilidade UI | `front-end/docs/ai/ACCESSIBILITY.md` | manter confirmação acessível por teclado e leitor de tela | sim |
| Página de relatórios | `front-end/src/pages/Main/Reports/**` | adicionar modal e confirmação do `Disponibilizar` | sim |
| Primitiva modal | `front-end/src/ui/Modal/**` | reaproveitar modal existente | sim |

## Orçamento de contexto

- baixo
- estrategia: limitar a mudança à rota `/relatorios`

## Criterios de conclusao

- [x] clicar em `Disponibilizar` abre modal de confirmação
- [x] só após confirmar o relatório é compartilhado com o responsável
- [x] a tela continua com feedback e acessibilidade consistentes

## Dependencias

- Task 322 - done

## Resultado da execucao

- a ação `Disponibilizar` passou a abrir um modal de confirmação antes de disparar o compartilhamento
- a confirmação reutiliza o mesmo padrão visual da exclusão, exibindo paciente, arquivo e formato do relatório
- o share só ocorre após confirmação explícita, com feedback de loading, sucesso e cancelamento consistente

## Contexto utilizado

### Mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/011-relatorios-evolucao.md`
- `.agents/state/handoffs/TASK-322.md`

### Sob demanda

- `front-end/docs/ai/ACCESSIBILITY.md`
- `front-end/src/pages/Main/Reports/index.tsx`
- `front-end/src/pages/Main/Reports/styles.module.css`
- `front-end/src/ui/Modal/index.tsx`

### Contexto evitado

- `backend/`, porque não há mudança no contrato ou na regra de compartilhamento

## Handoff

- `.agents/state/handoffs/TASK-323.md`

## Arquivos alterados

- `front-end/src/pages/Main/Reports/index.tsx`
- `tasks/change-requests/323-adicionar-confirmacao-ao-disponibilizar-relatorio.md`
- `tasks/slices/011-relatorios-evolucao.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-323.md`

## Validacoes executadas

- `cd front-end && npx eslint src/pages/Main/Reports/index.tsx`
- `cd front-end && npm run build`

## Pendencias pos-task

- nenhuma

## Status final

done

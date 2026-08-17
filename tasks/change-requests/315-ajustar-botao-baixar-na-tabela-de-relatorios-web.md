# Task 315 - Ajustar botão Baixar na tabela de relatórios web

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

- nao se aplica; ajuste visual na tabela de relatórios sem alterar integração

## Modo de execucao

single-stack

## Slice vertical

- Slice 011 - Relatorios de evolucao
- `tasks/slices/011-relatorios-evolucao.md`

## Referencia visual

### Stack de referencia visual

front-end

### Tipo de referencia visual

feedback direto do usuario sobre refinamento visual

### Fonte primaria visual

- `front-end/src/pages/Main/Reports/index.tsx`
- `front-end/src/pages/Main/Reports/styles.module.css`

### Lacunas

- sem novo print dedicado; a mudança deve apenas diferenciar a cor do CTA `Baixar` e alinhar melhor a célula de ações com o cabeçalho

## Objetivo

Dar cor própria ao botão `Baixar` na tabela de relatórios e alinhar o conteúdo da coluna `Ações` ao mesmo eixo do cabeçalho.

## Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/011-relatorios-evolucao.md`
- `.agents/state/handoffs/TASK-314.md`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| UI web | `front-end/docs/ai/{AGENTS.md,ARCHITECTURE.md,ACCESSIBILITY.md}` | manter coerência estrutural e semântica | sim |
| Implementação local | `front-end/src/pages/Main/Reports/{index.tsx,styles.module.css}` | ajustar CTA e alinhamento da coluna | sim |
| Primitiva compartilhada | `front-end/src/ui/Button/**` | compor classe local sobre o botão existente | sim |

## Orçamento de contexto

- baixo
- estrategia: limitar a mudança ao CTA `Baixar` e ao contêiner da coluna `Ações`, sem reabrir geração de relatórios ou outras rotas

## Criterios de conclusao

- [x] botão `Baixar` tem cor própria distinta
- [x] ações da tabela de relatórios ficam alinhadas ao cabeçalho da coluna
- [x] a rota `/relatorios` continua funcional

## Dependencias

- Task 314 - done

## Resultado da execucao

- o botão `Baixar` da tabela de relatórios recebeu uma variação visual azul-clara própria, mantendo a primitiva `Button`
- o contêiner da coluna `Ações` passou a justificar o conteúdo à direita, alinhando o CTA com o cabeçalho da coluna

## Contexto utilizado

### Mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/011-relatorios-evolucao.md`
- `.agents/state/handoffs/TASK-314.md`

### Sob demanda

- `front-end/docs/ai/AGENTS.md`
- `front-end/docs/ai/ARCHITECTURE.md`
- `front-end/docs/ai/ACCESSIBILITY.md`
- `front-end/src/pages/Main/Reports/index.tsx`
- `front-end/src/pages/Main/Reports/styles.module.css`
- `front-end/src/ui/Button/index.tsx`
- `front-end/src/ui/Button/styles.module.css`

### Contexto evitado

- `backend/`, porque o ajuste é exclusivamente visual no front-end
- `contracts/openapi.yaml`, porque não há alteração de API

## Handoff

- `.agents/state/handoffs/TASK-315.md`

## Arquivos alterados

- `front-end/src/pages/Main/Reports/index.tsx`
- `front-end/src/pages/Main/Reports/styles.module.css`
- `tasks/change-requests/315-ajustar-botao-baixar-na-tabela-de-relatorios-web.md`
- `tasks/slices/011-relatorios-evolucao.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-315.md`

## Validacoes executadas

- `cd front-end && npx eslint src/pages/Main/Reports/index.tsx` - ok
- `cd front-end && npm run build` - ok

## Pendencias pos-task

- nenhuma

## Status final

done

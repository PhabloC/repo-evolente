# Task 053 - Refinar design do dashboard profissional web

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

- nao se aplica; preservar dados e integracoes existentes

## Modo de execucao

single-stack

## Slice vertical

- Slice 019 - Reproducao de shell dashboard por referencia externa
- `tasks/slices/019-referencia-shell-dashboard-ambiental-web.md`

## Referencia visual

### Tipo

imagem fornecida pelo usuario no chat

### Cobertura

- faixa superior com metrica e CTA
- bloco principal de dashboard com indicadores e paineis auxiliares
- linguagem visual clara, densa e orientada a operacao

### Lacunas

- o print traz widgets e rotulos que nao pertencem ao dominio Evolente
- decisao: manter a composicao do dashboard, mas substituir o conteudo por informacoes uteis ao profissional

## Objetivo

Ajustar o design do `/dashboard` para ficar mais funcional ao profissional, com informacoes realmente necessarias e linguagem visual mais coerente com o produto.

## Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/019-referencia-shell-dashboard-ambiental-web.md`
- `.agents/state/handoffs/TASK-041.md`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| UI web | imagem enviada pelo usuario no chat | orientar a hierarquia do dashboard | sim |
| Front-end | `front-end/docs/ai/ARCHITECTURE.md`, `CODE_STYLE.md`, `ACCESSIBILITY.md` | implementar a tela com coerencia estrutural e acessibilidade | sim |
| Implementacao atual | `front-end/src/pages/Main/ShellHome/index.tsx` e `styles.module.css` | aplicar o refino no menor escopo possivel | sim |

## Orçamento de contexto

- baixo
- estrategia: limitar a mudanca ao dashboard profissional (`ShellHome`) e ao teste focado

## Criterios de conclusao

- [x] dashboard com foco em informacoes necessarias ao profissional
- [x] composicao visual mais clara e menos genérica
- [x] lint, build e teste focado aprovados

## Dependencias

- Task 041 - done

## Resultado da execucao

- o dashboard profissional deixou de usar copies genericas e widgets pouco uteis
- a home passou a enfatizar pacientes, planejamentos, adesao e prioridades operacionais
- os paineis foram reorganizados para destacar foco da semana, distribuicao de uso e atalhos reais do trabalho

## Contexto utilizado

### Mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`
- `tasks/000-index.md`, esta task, `tasks/slices/019-referencia-shell-dashboard-ambiental-web.md`
- `.agents/state/handoffs/TASK-041.md`

### Sob demanda

- imagem enviada pelo usuario no chat
- `front-end/docs/ai/ARCHITECTURE.md`, `CODE_STYLE.md`, `ACCESSIBILITY.md`
- `front-end/src/pages/Main/ShellHome/index.tsx`
- `front-end/src/pages/Main/ShellHome/styles.module.css`
- `front-end/src/pages/Main/ShellHome/index.test.tsx`

### Contexto evitado

- `contracts/openapi.yaml` por nao haver mudanca de integracao
- backend, mobile e outras paginas do shell por nao fazerem parte deste refino

## Handoff

- `.agents/state/handoffs/TASK-053.md`

## Arquivos alterados

- `front-end/src/pages/Main/ShellHome/index.tsx`
- `front-end/src/pages/Main/ShellHome/styles.module.css`
- `front-end/src/pages/Main/ShellHome/index.test.tsx`
- `tasks/change-requests/053-refinar-dashboard-profissional-web.md`
- `tasks/slices/019-referencia-shell-dashboard-ambiental-web.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-053.md`

## Validacoes executadas

- `cd front-end && npm run lint` - ok
- `cd front-end && npm run build` - ok
- `cd front-end && npm run test -- ShellHome` - ok

## Pendencias pos-task

- nenhuma

## Status final

done

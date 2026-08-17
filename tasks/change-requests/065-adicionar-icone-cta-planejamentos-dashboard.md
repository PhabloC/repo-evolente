# Task 065 - Adicionar ícone ao CTA de planejamentos no dashboard

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

- nao se aplica; ajuste visual sem alteracao de integracao

## Modo de execucao

single-stack

## Slice vertical

- Slice 019 - Reproducao de shell dashboard por referencia externa
- `tasks/slices/019-referencia-shell-dashboard-ambiental-web.md`

## Referencia visual

### Tipo

feedback direto do usuario sobre consistencia visual do CTA de planejamentos

### Cobertura

- card "Foco da semana" em `/dashboard`
- CTA `Abrir planejamentos`

### Lacunas

- sem novo print de referencia
- decisao: adicionar apenas um icone coerente com os demais atalhos sem alterar layout ou copy

## Objetivo

Adicionar um ícone ao botão `Abrir planejamentos` para alinhá-lo visualmente aos outros CTAs do dashboard.

## Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/019-referencia-shell-dashboard-ambiental-web.md`
- `.agents/state/handoffs/TASK-064.md`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| UI web | feedback do usuario no chat | confirmar o ajuste visual pedido | sim |
| Front-end | `front-end/docs/ai/ACCESSIBILITY.md` | preservar nome acessivel e legibilidade do CTA | sim |
| Front-end | `front-end/src/pages/Main/ShellHome/index.tsx` | incluir o icone no CTA correto | sim |

## Orçamento de contexto

- baixo
- estrategia: alterar apenas o markup do CTA de planejamentos

## Criterios de conclusao

- [x] o CTA `Abrir planejamentos` exibe um ícone coerente com a linguagem visual atual
- [x] o texto e o destino do link permanecem inalterados
- [x] teste focado do `ShellHome` permanece aprovado

## Dependencias

- Task 064 - done

## Resultado da execucao

- o CTA `Abrir planejamentos` passou a exibir um ícone ao lado do texto
- o ajuste reaproveitou os ícones já usados na própria tela

## Contexto utilizado

### Mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`
- `tasks/000-index.md`, esta task, `tasks/slices/019-referencia-shell-dashboard-ambiental-web.md`
- `.agents/state/handoffs/TASK-064.md`

### Sob demanda

- feedback do usuario no chat
- `front-end/docs/ai/ACCESSIBILITY.md`
- `front-end/src/pages/Main/ShellHome/index.tsx`

### Contexto evitado

- `front-end/src/pages/Main/ShellHome/styles.module.css` por nao exigir novo ajuste de estilo
- `contracts/openapi.yaml` por nao haver integracao nova
- backend e mobile por estarem fora do escopo

## Handoff

- `.agents/state/handoffs/TASK-065.md`

## Arquivos alterados

- `front-end/src/pages/Main/ShellHome/index.tsx`
- `tasks/change-requests/065-adicionar-icone-cta-planejamentos-dashboard.md`
- `tasks/slices/019-referencia-shell-dashboard-ambiental-web.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-065.md`

## Validacoes executadas

- `cd front-end && npm run test -- ShellHome` - ok

## Pendencias pos-task

- nenhuma

## Status final

done

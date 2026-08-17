# Task 071 - Alinhar paginação de planejamentos com pacientes

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

- Slice 008 - Trilhas semanais e evolucao
- `tasks/slices/008-trilhas-semanais-evolucao.md`

## Referencia visual

### Stack de referencia visual

front-end

### Tipo de referencia visual

padrao ja consolidado na tabela de pacientes

### Fonte primaria visual

- `front-end/src/pages/Main/Patients/{index.tsx,styles.module.css}`

### Lacunas

- sem print dedicado; decisao: copiar o padrao visual compacto da paginação de `Pacientes` (setas com label sr-only, botoes menores, estado ativo azul)

## Objetivo

Deixar a paginação da página de planejamentos visualmente igual à da página de pacientes.

## Contexto mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`, `tasks/000-index.md`
- esta task, `tasks/slices/008-trilhas-semanais-evolucao.md`
- `.agents/state/handoffs/TASK-050.md`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| UI web | `front-end/src/pages/Main/Patients/{index.tsx,styles.module.css}` | espelhar markup e CSS da paginação | sim |
| UI web | `front-end/src/pages/Main/Plans/{index.tsx,styles.module.css,index.test.tsx}` | aplicar o alinhamento | sim |
| A11y | `front-end/docs/ai/ACCESSIBILITY.md` | preservar labels, nav e aria-live | sim |

## Orçamento de contexto

- baixo; restrito aos estilos e markup da barra de paginação

## Criterios de conclusao

- [x] estilos da paginação em `Plans` espelham `Patients` (tamanho, raio, cores, label sr-only, ativo)
- [x] comportamento e acessibilidade da paginação permanecem intactos
- [x] teste da página e lint/build do front-end aprovados

## Dependencias

- Task 046 - done
- Task 050 - done

## Resultado da execucao

- a paginação de `Planejamentos` passou a usar o mesmo visual compacto de `Pacientes`: botões menores, cantos levemente arredondados, estado ativo azul e rótulos Anterior/Próxima em sr-only
- markup e comportamento de paginação local (lotes de 10) foram preservados

## Contexto utilizado

### Mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`
- `tasks/000-index.md`, esta task, Slice 008, handoff `TASK-050`

### Sob demanda

- `front-end/src/pages/Main/Patients/{index.tsx,styles.module.css}`
- `front-end/src/pages/Main/Plans/{index.tsx,styles.module.css,index.test.tsx}`
- `front-end/docs/ai/ACCESSIBILITY.md`

## Handoff

- `.agents/state/handoffs/TASK-071.md`

## Arquivos alterados

- `front-end/src/pages/Main/Plans/styles.module.css`
- `front-end/src/pages/Main/Plans/index.tsx`
- `tasks/change-requests/071-alinhar-paginacao-planejamentos-com-pacientes.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-071.md`

## Validacoes executadas

- `npm run test -- src/pages/Main/Plans/index.test.tsx` — aprovado
- `npm run lint` — aprovado
- `npm run build` — aprovado

## Acessibilidade aplicada

- `nav` com `aria-label`
- botões Anterior/Próxima com `aria-label` e texto sr-only
- página ativa com `aria-current="page"`
- resumo com `aria-live="polite"`

## Pendencias pos-task

- nenhuma

## Status final

done

# Task 313 - Unificar componente global de tabelas web

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

- nao se aplica; refactor visual e estrutural sem alterar integracao

## Modo de execucao

single-stack

## Slice vertical

- Slice 017 - Redesign da interface interna web
- `tasks/slices/017-redesign-interface-interna-web.md`

## Referencia visual

### Tipo

feedback direto do usuario sobre consistencia visual

### Cobertura

- tabelas da area autenticada web
- layout geral da tabela
- cor e hierarquia do cabecalho

### Lacunas

- sem novo print; a tarefa e consolidar o padrao visual ja dominante da area interna em um componente compartilhado

## Objetivo

Fazer todas as tabelas da area autenticada web seguirem o mesmo design, concentrando layout e estilo de cabecalho no componente global `Table`.

## Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/017-redesign-interface-interna-web.md`
- `.agents/state/handoffs/TASK-312.md`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| UI web compartilhada | `front-end/docs/ai/{AGENTS.md,ARCHITECTURE.md,COMPONENT_REUSE.md,ACCESSIBILITY.md}` | decidir onde centralizar o padrao global | sim |
| Componente base | `front-end/src/ui/Table/{index.tsx,styles.module.css}` | consolidar layout, cabecalho e comportamento padrao | sim |
| Páginas com override visual | `front-end/src/pages/Main/{Patients,Plans,Reports}/**` | remover customizacoes locais de skin da tabela | sim |
| Tabelas administrativas | `front-end/src/pages/Main/{Admin,AdminUsers}/**` | validar compatibilidade com o padrao comum | sim |

## Orçamento de contexto

- baixo
- estrategia: limitar a execucao ao componente `Table` e as paginas com override direto de skin, sem reabrir outras telas ou regras de negocio

## Criterios de conclusao

- [x] existe um padrao visual unico de tabela centralizado em `front-end/src/ui/Table`
- [x] pacientes, planejamentos, relatorios e admin continuam renderizando suas tabelas corretamente
- [x] overrides locais de cor de cabecalho/layout da tabela foram removidos ou reduzidos ao minimo necessario
- [x] validacoes focadas passam

## Dependencias

- Task 048 - done
- Task 066 - done
- Task 088 - done
- Task 183 - done
- Task 297 - done

## Resultado da execucao

- o componente global `Table` passou a concentrar o layout visual comum, incluindo container, raio, fundo, sombra e cabecalho padronizado
- as paginas de pacientes, planejamentos e relatorios deixaram de aplicar skin propria no cabecalho da tabela
- foi adicionado um teste focado do `Table` para preservar o contrato basico compartilhado de renderizacao

## Contexto utilizado

### Mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/017-redesign-interface-interna-web.md`
- `.agents/state/handoffs/TASK-312.md`

### Sob demanda

- `front-end/docs/ai/AGENTS.md`
- `front-end/docs/ai/ARCHITECTURE.md`
- `front-end/docs/ai/COMPONENT_REUSE.md`
- `front-end/docs/ai/ACCESSIBILITY.md`
- `front-end/src/ui/Table/{index.tsx,styles.module.css}`
- `front-end/src/pages/Main/{Patients,Plans,Reports}/**`
- `front-end/src/pages/Main/{Admin,AdminUsers}/**`

### Contexto evitado

- `contracts/openapi.yaml`, porque nao houve alteracao de contrato
- `backend/` e `mobile/`, porque o ajuste e exclusivo da camada web

## Handoff

- `.agents/state/handoffs/TASK-313.md`

## Arquivos alterados

- `front-end/src/ui/Table/index.test.tsx`
- `front-end/src/ui/Table/styles.module.css`
- `front-end/src/pages/Main/Patients/index.tsx`
- `front-end/src/pages/Main/Patients/styles.module.css`
- `front-end/src/pages/Main/Plans/index.tsx`
- `front-end/src/pages/Main/Plans/styles.module.css`
- `front-end/src/pages/Main/Reports/styles.module.css`
- `tasks/change-requests/313-unificar-componente-global-de-tabelas-web.md`
- `tasks/slices/017-redesign-interface-interna-web.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-313.md`

## Validacoes executadas

- `cd front-end && npm run test -- --run src/ui/Table/index.test.tsx src/pages/Main/Patients/index.test.tsx src/pages/Main/Plans/index.test.tsx` - ok
- `cd front-end && npx eslint src/ui/Table/index.tsx src/ui/Table/index.test.tsx src/pages/Main/Patients/index.tsx src/pages/Main/Plans/index.tsx` - ok
- `rg -n ":global\\(\\.table th\\)|\\.patientsTable|\\.plansTable|className=\\{styles\\.(patientsTable|plansTable)\\}" front-end/src` - sem ocorrencias

## Pendencias pos-task

- nenhuma

## Status final

done

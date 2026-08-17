# Handoff - Task 069

## Task

- identificador: 069
- título: Desacoplar dropdown da tabela de pacientes
- tipo: front
- modo de execução: single-stack
- status final: done

## Slice vertical

- identificador: Slice 018 - Fidelidade visual dashboard e pacientes web
- objetivo de negócio: impedir que o dropdown de ações quebre a tabela de pacientes
- entrega verificável: o menu abre fora do overflow da tabela

## Decisões preservadas

- decisão: renderizar o menu em portal no `body`
- motivo: o wrapper da tabela usa overflow e cortava o dropdown quando ele ficava dentro da linha
- impacto: o menu ficou desacoplado do fluxo da tabela e preservou a mesma interação

## Contexto utilizado

### Contexto mínimo lido

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- `tasks/change-requests/069-desacoplar-dropdown-tabela-pacientes.md`
- `tasks/slices/018-fidelidade-visual-dashboard-pacientes-web.md`
- `.agents/state/handoffs/TASK-068.md`

### Contexto sob demanda carregado

| Fonte | Gatilho | Uso |
|---|---|---|
| feedback do usuario no chat | UI web | confirmar o clipping do dropdown |
| `front-end/docs/ai/ACCESSIBILITY.md` | UI web | preservar acionamento/fechamento do menu |
| `front-end/src/pages/Main/Patients/{index.tsx,styles.module.css,index.test.tsx}` | implementacao atual | mover o menu para portal e validar |

### Contexto evitado

| Fonte | Motivo |
|---|---|
| `contracts/openapi.yaml` | sem alteracao de contrato |
| `backend/` | ajuste estritamente visual/comportamental de front |
| outras paginas do front-end | escopo restrito à tabela de pacientes |

## Resultado por stack

- front-end: dropdown da tabela desacoplado do overflow da tabela via portal
- backend: sem alteracoes
- mobile: sem alteracoes

## Arquivos alterados

- `front-end/src/pages/Main/Patients/index.tsx`
- `front-end/src/pages/Main/Patients/styles.module.css`
- `tasks/change-requests/069-desacoplar-dropdown-tabela-pacientes.md`
- `tasks/slices/018-fidelidade-visual-dashboard-pacientes-web.md`
- `tasks/000-index.md`

## Validações executadas

- `cd front-end && npm run test -- --run src/pages/Main/Patients/index.test.tsx`: ok

## Pendências ou bloqueios

- nenhuma

## Próxima ação sugerida

- seguir apenas se houver ajuste fino no alinhamento horizontal/vertical do portal em telas menores

## Próximo contexto recomendado

- `front-end/src/pages/Main/Patients/index.tsx`
- `front-end/src/pages/Main/Patients/styles.module.css`
- `tasks/change-requests/069-desacoplar-dropdown-tabela-pacientes.md`

## Contexto que não deve ser carregado na próxima etapa

- `backend/src/`
- motivo: ajuste local da UI web

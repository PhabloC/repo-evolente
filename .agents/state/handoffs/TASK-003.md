# Handoff - Task 003

## Task

- identificador: 003
- título: Shell web React com tokens e rotas por perfil
- tipo: front
- modo de execução: single-stack
- status final: done

## Slice vertical

- identificador: Slice 001 - Fundacao e contrato base
- objetivo de negócio: Shell web
- entrega verificável: App web com shell (parcial do slice; mobile 004 pendente)

## Decisões preservadas

- decisão: tokens Evolente + Nunito no global.css
- motivo: DS Desktop
- impacto: tema claro bege, primary laranja, sidebar branca

- decisão: RoleGuard stub com roles master/profissional/responsavel
- motivo: critério da task; login fora de escopo
- impacto: rotas filtradas + `/sem-permissao` + preview role no header

- decisão: sidebar DS filtrada por role; responsável sem área clínica desktop
- motivo: DS §4 Perfis de acesso
- impacto: navigation.ts

## Contexto utilizado

### Contexto mínimo lido

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`
- `tasks/000-index.md`, `tasks/003-shell-web-react.md`
- `tasks/slices/001-fundacao-contrato-base.md`
- `.agents/state/handoffs/TASK-002.md`

### Contexto sob demanda carregado

| Fonte | Gatilho | Uso |
|---|---|---|
| `design-system/front/Design_System_Evolente_Desktop.md` | UI | tokens/sidebar |
| `front-end/docs/ai/ARCHITECTURE.md` | front | rotas/layout |
| `front-end/docs/ai/CODE_STYLE.md` | front | types/utils |
| `front-end/docs/ai/ACCESSIBILITY.md` | UI | a11y mínima |

### Contexto evitado

| Fonte | Motivo |
|---|---|
| `design-system/mobile/` | Task web |
| `contracts/openapi.yaml` | contrato n/a |
| backend docs | stack não envolvida |

## Resultado por stack

- front-end: shell concluído
- backend: n/a
- mobile: n/a

## Arquivos alterados

- shell/layout/tokens/routes em `front-end/src/**`
- task/index/slice/handoff

## Validações executadas

- lint/test/build: ok (3 tests)

## Pendências ou bloqueios

- shell mobile (Task 004)
- login real e dashboards de negócio

## Próxima ação sugerida

- Executar Task 004 (`tasks/004-shell-mobile-expo.md`)

## Próximo contexto recomendado

- `tasks/004-shell-mobile-expo.md`
- `tasks/slices/001-fundacao-contrato-base.md`
- `design-system/mobile/Design_System_Evolente_App_Mobile.md`
- `mobile/docs/ai/` conforme a Task 004 declarar

## Contexto que não deve ser carregado na próxima etapa

- fonte: `design-system/front/` e `front-end/docs/ai/`
- motivo: Task 004 é mobile; não inferir UI web no app

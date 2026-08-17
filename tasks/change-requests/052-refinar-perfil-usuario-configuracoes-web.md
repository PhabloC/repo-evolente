# Task 052 - Refinar design do perfil do usuario em configuracoes web

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

- Slice 017 - Redesign da interface interna web
- `tasks/slices/017-redesign-interface-interna-web.md`

## Referencia de design system

### Stack de referencia visual

front-end

### Tipo de referencia visual

artefato de design system

### Fonte primaria visual

- `design-system/front/Design_System_Evolente_Desktop.md`

### Regra de aderencia visual

- preservar linguagem clara, acolhedora e profissional da area autenticada
- reforcar hierarquia visual da tela de configuracoes com foco no perfil do usuario

## Objetivo

Melhorar o design da pagina de perfil em configuracoes para deixar a leitura da conta, do papel do usuario e das preferencias mais forte e mais organizada.

## Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/017-redesign-interface-interna-web.md`
- `.agents/state/handoffs/TASK-039.md`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| UI web | `design-system/front/Design_System_Evolente_Desktop.md` | definir a direção visual do refino | sim |
| Front-end | `front-end/docs/ai/ARCHITECTURE.md`, `CODE_STYLE.md`, `ACCESSIBILITY.md` | implementar a tela com acessibilidade e coerencia estrutural | sim |
| Implementacao atual | `front-end/src/pages/Main/Settings/index.tsx` e `front-end/src/pages/Main/Settings/styles.module.css` | aplicar o redesign no menor escopo possivel | sim |

## Orçamento de contexto

- baixo
- estrategia: limitar a mudanca ao modulo `Settings` e ao perfil do usuario dentro da rota existente

## Criterios de conclusao

- [x] perfil do usuario com hero e resumo mais claros
- [x] dados da conta e preferencias com hierarquia visual mais forte
- [x] lint e build aprovados

## Dependencias

- Task 039 - done

## Resultado da execucao

- configuracoes ganhou hero de perfil com status da conta, sinais de seguranca e resumo do papel do usuario
- dados da conta passaram a ser exibidos em cards de leitura rapida e uma trilha de atividade da conta
- preferencias foram reorganizadas em um bloco mais claro, com melhor contraste e resumo superior
- refinamento incremental posterior: o perfil do profissional foi enxugado para destacar apenas identidade, contato, acesso e preferencias operacionais, removendo foco em datas e blocos menos uteis

## Contexto utilizado

### Mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`
- `tasks/000-index.md`, esta task, `tasks/slices/017-redesign-interface-interna-web.md`
- `.agents/state/handoffs/TASK-039.md`

### Sob demanda

- `design-system/front/Design_System_Evolente_Desktop.md`
- `front-end/docs/ai/ARCHITECTURE.md`, `CODE_STYLE.md`, `ACCESSIBILITY.md`
- `front-end/src/pages/Main/Settings/index.tsx`
- `front-end/src/pages/Main/Settings/styles.module.css`
- `front-end/src/types/auth.ts`
- `front-end/src/utils/formatDateTime.ts`

### Contexto evitado

- `contracts/openapi.yaml` por nao haver mudanca de integracao
- backend, mobile e outras paginas do shell por nao fazerem parte deste refino

## Handoff

- `.agents/state/handoffs/TASK-052.md`

## Arquivos alterados

- `front-end/src/pages/Main/Settings/index.tsx`
- `front-end/src/pages/Main/Settings/styles.module.css`
- `tasks/change-requests/052-refinar-perfil-usuario-configuracoes-web.md`
- `tasks/slices/017-redesign-interface-interna-web.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-052.md`

## Validacoes executadas

- `cd front-end && npm run lint` - ok
- `cd front-end && npm run build` - ok

## Pendencias pos-task

- nenhuma

## Status final

done

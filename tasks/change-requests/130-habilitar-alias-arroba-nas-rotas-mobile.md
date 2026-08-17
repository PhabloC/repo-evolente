# Task 130 - Habilitar alias `@/` nas rotas do mobile

## Status

done

## Tipo

mobile

## Stacks envolvidos

- mobile

## Perfil do projeto

- stack web escolhida: front-end (React/Vite)
- mobile: sim

## Contrato

- nao se aplica (ajuste de infraestrutura local de imports e rotas)

## Modo de execucao

single-stack

## Slice vertical

- Slice 001 - Fundacao e contrato base
- `tasks/slices/001-fundacao-contrato-base.md`

## Referencia de design system

### Stack de referencia visual

mobile

### Tipo de referencia visual

nao se aplica

### Fonte primaria visual

- nao se aplica

## Restricao explicita do usuario

- Permitir o uso de `@` nas rotas do mobile

## Objetivo

Configurar o app mobile Expo para aceitar o alias `@/*` apontando para `./src/*` e aplicar esse alias nos arquivos centrais de rota e linking do app.

## Contexto minimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- `tasks/change-requests/130-habilitar-alias-arroba-nas-rotas-mobile.md`
- `tasks/slices/001-fundacao-contrato-base.md`
- `.agents/state/handoffs/TASK-129.md`

## Contexto sob demanda

- `mobile/docs/ai/ARCHITECTURE.md`
- `mobile/docs/ai/CODE_STYLE.md`
- `mobile/tsconfig.json`
- `mobile/src/routes/RootNavigator.tsx`
- `mobile/src/routes/params.ts`
- `mobile/src/config/linking.ts`
- `mobile/src/app/AppGate.tsx`
- `mobile/src/features/auth/screens/SignInScreen.tsx`
- `mobile/src/features/auth/screens/PasswordRecoveryScreen.tsx`
- `mobile/src/features/auth/screens/PasswordResetScreen.tsx`

## Orcamento de contexto

- ~10 fontes
- estrategia de reducao: limitar a mudanca ao alias `@/*` e aos imports ligados ao eixo `routes/linking`

## Criterios de aceite

- `mobile/tsconfig.json` declara `paths` para `@/* -> ./src/*`
- `RootNavigator`, `linking` e telas auth que dependem de `RootStackParamList` passam a importar via `@/`
- Nenhuma mudanca funcional na navegacao ou nos nomes das rotas

## Fora de escopo

- Refatorar todos os imports relativos do mobile
- Alterar nomes de telas, paths de deep link ou estrutura de navegacao
- Mudancas de contrato, UI ou comportamento

## Dependencias

- Task 004 (shell mobile Expo)
- Task 129 (refino recente no mobile; handoff de continuidade)

## Validacao esperada

- `npm run lint`
- `npm run typecheck`
- `npm run test`

## Resultado da execucao

- O mobile passou a declarar `@/*` em `tsconfig.json`, apontando para `./src/*` sem depender de `baseUrl`
- Os arquivos centrais de navegacao (`AppGate`, `linking`, `RootNavigator`) e as telas auth que dependem dos tipos de rota passaram a importar `RootStackParamList` e modulos relacionados via `@/`
- A estrutura e os nomes das rotas permaneceram inalterados

## Contexto utilizado

- Contexto minimo lido: `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`, `tasks/000-index.md`, esta task, `tasks/slices/001-fundacao-contrato-base.md` e handoff `TASK-129`
- Contexto sob demanda carregado: `mobile/docs/ai/ARCHITECTURE.md`, `CODE_STYLE.md`, `mobile/tsconfig.json`, `src/routes`, `src/config/linking.ts`, `AppGate` e telas auth ligadas ao tipo de rota
- Fonte externa consultada para reduzir risco: documentacao oficial do Expo sobre suporte automatico a `tsconfig paths` no CLI/Metro

## Handoff

- `.agents/state/handoffs/TASK-130.md`
- Decisoes preservadas: o alias foi restrito ao mobile e aplicado apenas ao eixo de rotas/linking; sem limpeza global de imports relativos
- Proximo contexto recomendado: `mobile/src/routes/` e `mobile/src/app/` se houver nova padronizacao de imports na stack

## Arquivos alterados

- `mobile/tsconfig.json`
- `mobile/src/app/AppGate.tsx`
- `mobile/src/config/linking.ts`
- `mobile/src/routes/RootNavigator.tsx`
- `mobile/src/features/auth/screens/SignInScreen.tsx`
- `mobile/src/features/auth/screens/PasswordRecoveryScreen.tsx`
- `mobile/src/features/auth/screens/PasswordResetScreen.tsx`
- `tasks/change-requests/130-habilitar-alias-arroba-nas-rotas-mobile.md`
- `tasks/slices/001-fundacao-contrato-base.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-130.md`

## Validacoes executadas

- `npm run lint` - ok
- `npm run typecheck` - ok
- `npm run test` - ok (11 suites, 22 testes)

## Pendencias pos-task

- Avaliar em outra task se vale expandir o alias `@/` para mais imports relativos longos fora do eixo de rotas

## Status final

done

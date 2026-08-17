# Task 004 - Shell mobile Expo com tokens e navegacao por perfil

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

- nao se aplica

## Modo de execucao

single-stack

## Referencia de design system

### Stack de referencia visual

mobile

### Tipo de referencia visual

artefato de design system

### Fonte primaria visual

- `design-system/mobile/Design_System_Evolente_App_Mobile.md`

### Regra de aderencia visual

- Tokens mobile; area responsavel calma; SEM gamificacao apesar do DS.

## Contexto de negocio

### Por que

Base do app para master e responsavel.

### O que

Shell Expo com tokens, navegacao e guards.

### Comportamento esperado

- Navigator por role
- Tokens aplicados

### Fora de escopo

- Auth completa
- Trilha
- Gamificacao

## Review da spec

- [x] Permissoes definidas ou `nao se aplica`
- [x] Casos de erro mapeados
- [x] Decisoes de negocio confirmadas como humanas
- [x] Criterios de aceite objetivos e verificaveis
- [x] Casos de borda considerados

### Evidencias da review

- Permissoes: master e responsavel; profissional nao e publico mobile
- Casos de erro: role sem navigator
- Decisoes humanas confirmadas: Stack web React/Vite; mobile sim; profissional multi-especialidade; inativar nao excluir; gamificacao fora
- Casos de borda: profissional no mobile — negar/orientar web

## Especificacao tecnica

### Deve

- Expo scaffold
- Distinguir master vs responsavel

### Nao deve

- nao adicionar novas dependencias sem autorizacao explicita nesta task
- nao desviar dos padroes estabelecidos sem justificativa registrada
- Medalhas/pontos
- Login crianca

## Entradas

- `design-system/mobile/Design_System_Evolente_App_Mobile.md`
- `mobile/docs/ai/ARCHITECTURE.md`
- `requirements/001-escopo-produto.md`

## Dependencias

- Task 001

## Slice vertical

### Identificador do slice

Slice 001 - Fundacao e contrato base

### Arquivo do slice

- `tasks/slices/001-fundacao-contrato-base.md`

### Objetivo de negócio

Shell mobile.

### Entrega verificável do slice

App com shell.

### Fora do slice

- Web

## Contexto mínimo

Sempre ler:

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/001-fundacao-contrato-base.md`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| UI mobile | `design-system/mobile/Design_System_Evolente_App_Mobile.md` | UI mobile | sim |
| Mobile | `mobile/docs/ai/ARCHITECTURE.md e CODE_STYLE.md` | mobile | sim |
| Requisitos | `requirements/001-escopo-produto.md e 002-regras-de-negocio.md` | regras | sim |

## Orçamento de contexto

- Risco medio (conflito DS)

## Criterios de conclusao

- Shell sobe
- Sem UI gamificacao

## Instrucoes de implementacao

- Documentar exclusao de gamificacao

## Validacao esperada

- npm run lint
- npm run typecheck
- npm run test

## Entregaveis esperados

- Shell mobile

## Riscos ou ambiguidades

- Conflito DS vs requisitos

## Resultado da execucao

Shell Expo Evolente com tokens do DS mobile, navigators por role (master/responsável), bloqueio de profissional e exclusão documentada de gamificação.

### Por stack

- mobile: tokens Evolente; `resolveMobileShell`; MasterShellNavigator; ResponsavelShellNavigator (tom calmo); UnsupportedRoleScreen; preview de role no SignIn; `SCOPE_EXCLUSIONS.md`

### Slice

- Slice 001 concluído: Tasks 001–004 done

### Decisoes tecnicas

- Público mobile: master + responsavel; profissional → orientar web
- Sem login de criança; sem medalhas/conquistas
- Tab bar custom sem nova dependência `@react-navigation/bottom-tabs`
- Nunito documentado como alvo; fonte do sistema nesta task (sem nova dep de fontes)
- Amarelo do DS só como token semântico, sem UI de recompensa

### Trade-offs

- Conflito DS (gamificação/UI criança) vs requisitos: prevalece requisito
- Auth completa permanece stub/demo

### Contrato

- nao se aplica

### Referencia visual

- Fonte: `design-system/mobile/Design_System_Evolente_App_Mobile.md`
- Tokens e área responsável calma aplicados; gamificação explicitamente excluída

## Contexto utilizado

### Contexto minimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`, `tasks/000-index.md`, esta task, slice 001, handoff Task 003

### Contexto sob demanda carregado

- `design-system/mobile/Design_System_Evolente_App_Mobile.md`
- `mobile/docs/ai/ARCHITECTURE.md`, `CODE_STYLE.md`
- `requirements/001-escopo-produto.md`, trechos de `002-regras-de-negocio.md`

### Contexto nao carregado

- design-system/front, front-end docs, openapi (n/a)

## Handoff

- `.agents/state/handoffs/TASK-004.md`
- Slice 001 fechado; próxima execução conforme backlog (ex.: autenticação / Task 005)

## Arquivos alterados

- `mobile/src/shared/theme/tokens.ts`
- `mobile/src/shared/types/role.ts`
- `mobile/src/shared/utils/resolveMobileShell.ts`
- `mobile/src/shared/utils/resolveMobileShell.test.ts`
- `mobile/src/shared/components/ShellTabBar/**`
- `mobile/src/shared/components/Button/**`
- `mobile/src/shared/components/AppText/**`
- `mobile/src/features/auth/**` (session/role/sign-in preview)
- `mobile/src/features/shell/**`
- `mobile/src/routes/**`
- `mobile/src/config/linking.ts`
- `mobile/docs/ai/SCOPE_EXCLUSIONS.md`
- `mobile/src/features/home/components/styles.ts`
- `tasks/004-shell-mobile-expo.md`
- `tasks/000-index.md`
- `tasks/slices/001-fundacao-contrato-base.md`
- `.agents/state/handoffs/TASK-004.md`

## Validacoes executadas

- `npm run lint` — ok
- `npm run typecheck` — ok
- `npm run test` — 3 passed

## Aderencia ao design system

- Fonte primaria: `design-system/mobile/Design_System_Evolente_App_Mobile.md`
- Tipo: artefato documental
- Evidencias: paleta Evolente, área responsável calma, tabs inferiores, alvos ≥48px
- Desvio documentado: exclusão de gamificação/UI criança (requisito prevalece) em `mobile/docs/ai/SCOPE_EXCLUSIONS.md`
- Lacuna: Nunito não carregado (sem dep autorizada)

## Pendencias pos-task

- Auth completa (slice autenticação)
- Trilha/notificações reais
- Carregar Nunito quando houver autorização de dependência
- Próxima task do backlog após Slice 001

## Status final

done

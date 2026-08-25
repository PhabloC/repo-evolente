# Handoff - Task 621

## Task

- identificador: `621`
- título: Cadastro de filho no perfil do responsável mobile
- tipo: mobile
- modo de execução: single-stack
- status final: done

## Slice vertical

- Slice 055 — cadastro de filho no perfil mobile
- status: done

## Decisões preservadas

- O cadastro no app exige os mesmos dados e anamnese do contrato existente; não altera backend nem OpenAPI.
- O CTA aparece tanto para o primeiro filho quanto para filhos adicionais.
- Depois de criar, o filho é persistido como seleção ativa e os caches de filhos/perfil são atualizados.

## Contexto efetivamente usado

- Task/Slice, handoffs 560/561, contrato de children, design system mobile, perfil do responsável, feature children, rotas e componentes compartilhados.

## Arquivos alterados

- Feature `mobile/src/features/children` (tipo, service, mutation e tela de criação)
- Perfil do responsável e rotas mobile
- Task 621, Slice 055, índice e este handoff

## Validações executadas

- TypeScript e lint do escopo passaram.
- Testes de children: 3 suítes / 7 testes passaram.

## Pendências ou bloqueios

- Nenhuma.

## Próximo contexto recomendado

- Nenhum, salvo nova mudança no fluxo de filhos mobile.

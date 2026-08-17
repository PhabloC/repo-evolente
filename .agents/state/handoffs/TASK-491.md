# Handoff - Task 491

## Task

- identificador: TASK-491
- título: Limpar sessão de perfil não suportado no boot mobile
- tipo: mobile
- modo de execução: single-stack
- status final: done

## Slice vertical

- identificador: Slice 002 - Autenticacao e recuperacao de senha
- objetivo de negócio: login e recuperação de senha
- entrega verificável: boot com papel sem shell mobile abre login

## Decisões preservadas

- decisão: `restoreSession` limpa storage e retorna null se `resolveMobileShell(role) === 'unsupported'`
- motivo: evitar sticky em `UnsupportedRole` ao reabrir o app
- impacto: próximo cold start com sessão profissional antiga cai no login

- decisão: `signIn` não persiste sessão de papel unsupported (ainda retorna a sessão em memória para a tela de aviso)
- motivo: login profissional pode informar "use a web", mas não sobrevive ao reboot
- impacto: master/responsável continuam persistindo normalmente

## Contexto utilizado

### Contexto mínimo lido

- `AGENTS.md`
- `tasks/000-index.md`
- `tasks/change-requests/491-limpar-sessao-perfil-nao-suportado-no-boot-mobile.md`
- `tasks/slices/002-autenticacao.md`

### Contexto sob demanda carregado

| Fonte | Gatilho | Uso |
|---|---|---|
| `mobile/src/features/auth/services/authService.ts` | restore/login | implementação |
| `mobile/src/shared/utils/resolveMobileShell.ts` | regra de papéis | checagem unsupported |
| `authService.test.ts` | aceite | cobertura |

### Contexto evitado

- design-system completo, backend, front-end web

## Arquivos alterados

- `mobile/src/features/auth/services/authService.ts`
- `mobile/src/features/auth/services/authService.test.ts`
- `tasks/change-requests/491-*.md`
- `tasks/000-index.md`
- `tasks/slices/002-autenticacao.md`

## Validações executadas

- `npm test -- --testPathPattern=authService.test --no-coverage` — pass

## Pendências

- Usuário precisa fazer cold start / reload do app para limpar a sessão já gravada

## Próxima ação sugerida

- Abrir o app de novo e confirmar tela de login; entrar com master ou responsável

## Próximo contexto recomendado

- nenhum; fluxo encerrado

## Contexto que não deve ser carregado

- slices de jogos, design-system completo, OpenAPI

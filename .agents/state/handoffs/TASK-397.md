# Handoff - Task 397

## Task

- identificador: 397
- titulo: Vincular foto do profissional na aba de usuários web
- tipo: front
- modo de execucao: single-stack
- status final: done

## Slice vertical

- identificador: Slice 027 - Fotos de perfil em bucket
- objetivo de negocio: refletir também a foto do profissional na tabela administrativa de vínculos
- entrega verificavel: a coluna `Profissional` da aba `Pacientes` exibe a foto real quando `professional.avatarUrl` existir
- status do slice: done

## Decisoes preservadas

- a árvore admin já trazia `professional.avatarUrl`; a mudança ficou restrita ao front-end
- `PatientRow` passou a carregar `professionalAvatarUrl` sem criar tipo compartilhado novo
- a célula `Profissional` mantém o fallback por inicial quando não houver foto

## Contexto utilizado

### Contexto minimo lido

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- `tasks/change-requests/397-vincular-foto-profissional-na-aba-usuarios-web.md`
- `tasks/slices/027-fotos-de-perfil-em-bucket.md`
- `.agents/state/handoffs/TASK-193.md`
- `.agents/state/handoffs/TASK-331.md`
- `.agents/state/handoffs/TASK-332.md`

### Contexto sob demanda carregado

| Fonte | Gatilho | Uso |
|---|---|---|
| `front-end/docs/ai/{AGENTS.md,ARCHITECTURE.md,COMPONENT_REUSE.md,ACCESSIBILITY.md}` | stack front com UI | orientar implementação |
| `front-end/src/pages/Main/AdminUsers/**` | página usuários | ligar avatar do profissional, estilos e testes |

## Resultado por stack

- front-end: a aba `Pacientes` agora exibe a foto real do profissional vinculado na coluna `Profissional`

## Arquivos alterados

- `front-end/src/pages/Main/AdminUsers/index.tsx`
- `front-end/src/pages/Main/AdminUsers/styles.module.css`
- `front-end/src/pages/Main/AdminUsers/index.test.tsx`
- `tasks/change-requests/397-vincular-foto-profissional-na-aba-usuarios-web.md`
- `tasks/slices/027-fotos-de-perfil-em-bucket.md`
- `tasks/000-index.md`

## Validacoes executadas

- `cd front-end && npm run test -- --run src/pages/Main/AdminUsers/index.test.tsx`: ok
- `cd front-end && npx eslint src/pages/Main/AdminUsers/index.tsx src/pages/Main/AdminUsers/index.test.tsx`: ok

## Pendencias ou bloqueios

- nenhuma

## Proxima acao sugerida

- seguir só se quiser propagar o mesmo vínculo de foto para outras tabelas administrativas que ainda usem fallback textual

## Proximo contexto recomendado

- `front-end/src/pages/Main/AdminUsers/index.tsx`
- `front-end/src/pages/Main/AdminUsers/index.test.tsx`

# Handoff - Task 561

## Task

- identificador: `561`
- título: Mobile: selecionar o filho após o login
- tipo: mobile
- modo de execução: single-stack
- status final: done

## Slice vertical

- identificador: Slice 051
- objetivo de negócio: escolher o filho gerenciado no app após o login
- entrega verificável: seleção obrigatória antes do shell; empty state sem trilha
- status do slice: done

## Decisões preservadas

- Sempre mostra a seleção (também com 1 filho); nunca auto-seleciona
- Persistência AsyncStorage por `userId`; relogin restaura se o filho ainda existir
- Troca no perfil usa `forceSelect` para não reaplicar o id persistido
- 0 filhos: empty state na web; o tab shell não monta
- Trilha/relatórios/home leem o `childId` da store, não `children[0]`

## Contexto utilizado

### Contexto mínimo lido

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`, `tasks/000-index.md`
- `tasks/change-requests/561-seletor-filho-pos-login-mobile.md`
- `tasks/slices/051-seletor-filho-mobile.md`
- `mobile/docs/ai/AGENTS.md`, `ARCHITECTURE.md`, `MOBILE_PATTERNS.md`
- `.agents/state/handoffs/TASK-560.md`

### Contexto sob demanda carregado

| Fonte | Gatilho | Uso |
|---|---|---|
| DS mobile | UI | cards, empty, toque |
| shell/profile/rotas | gate | pós-login |
| `GET /guardians/me/children` | lista | childrenService |
| trailService | binding | childId |

### Contexto evitado

| Fonte | Motivo |
|---|---|
| wizard web | Slice 050 |
| jogos | fora de escopo |

## Resultado por stack

- mobile: seletor + binding do filho
- front-end / backend: não alterados

## Arquivos alterados

- `mobile/src/features/children/**`
- rotas, trilha, home, perfil, relatórios do responsável

## Validações executadas

- eslint arquivos da task: passou
- jest children: 14 passaram
- tsc: erros pré-existentes fora desta task

## Pendências ou bloqueios

- nenhuma da 561

## Próxima ação sugerida

- lote 556–561 encerrado; só seguir se houver nova task da raiz

## Próximo contexto recomendado

- nenhum obrigatório

## Contexto que não deve ser carregado na próxima etapa

- wizard web de filho
- dashboard profissional
- jogos

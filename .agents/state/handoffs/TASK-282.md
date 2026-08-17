# Handoff - Task 282

## Task

- identificador: 282
- título: Alinhar cards da pagina de avisos ao estilo do card da home mobile
- tipo: mobile
- modo de execução: single-stack
- status final: done

## Slice vertical

- identificador: 010
- objetivo de negócio: home/perfil/notificacoes do responsavel
- entrega verificável: cards de resumo e vazio da página de avisos no estilo HomeActionCard

## Decisões preservadas

- decisão: reutilizar `HomeActionCard` no resumo rápido e no estado vazio
- motivo: mesmo estilo da home (sombra no card, pastilha, status, tipografia)
- impacto: lista de itens individuais permanece com layout próprio

## Contexto utilizado

### Contexto mínimo lido

- task 282, handoff 281, slice 010, índice

### Contexto sob demanda carregado

| Fonte | Gatilho | Uso |
|---|---|---|
| `ResponsavelNotificationsScreen.tsx` | cards da página | troca para HomeActionCard |
| `screens/styles.ts` | limpeza | remover estilos órfãos |
| `HomeActionCard` | referencia | reuso |

### Contexto evitado

| Fonte | Motivo |
|---|---|
| requirements/contracts/outras stacks | não se aplica |

## Resultado por stack

- mobile: dois cards da página de avisos alinhados ao card da home

## Arquivos alterados

- `mobile/src/features/shell/screens/ResponsavelNotificationsScreen.tsx`
- `mobile/src/features/shell/screens/styles.ts`
- task/index/slice/handoff 282

## Validações executadas

- validação: visual no device após reload

## Pendências ou bloqueios

- nenhuma

## Próxima ação sugerida

- se quiser a lista de avisos também no HomeActionCard, abrir nova task

## Próximo contexto recomendado

- `ResponsavelNotificationsScreen.tsx`
- `.agents/state/handoffs/TASK-282.md`

## Contexto que não deve ser carregado na próxima etapa

- fonte: requirements, contracts, web/backend
- motivo: refino visual local

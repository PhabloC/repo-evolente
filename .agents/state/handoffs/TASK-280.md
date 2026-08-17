# Handoff - Task 280

## Task

- identificador: 280
- título: Corrigir sombra quadrada e bg trilha no card de avisos home mobile
- tipo: mobile
- modo de execução: single-stack
- status final: done

## Slice vertical

- identificador: 010
- objetivo de negócio: home/perfil/notificacoes do responsavel
- entrega verificável: sombra arredondada + `trilha.webp` visível sem esticar o card

## Decisões preservadas

- decisão: host de sombra é um `View` externo; `Pressable` só envolve o card clipado
- motivo: elevation no `Pressable` gerava bloco quadrado no Android
- impacto: sombra acompanha o radius

- decisão: elevation 5 e blur mais suave
- motivo: elevation alta reforçava a sombra em placa
- impacto: profundidade sem bloco duro

- decisão: carimbo `trilha.webp` 168x168, `contain`, opacidade 0.7 à esquerda
- motivo: 112px/0.45 sumia; fill 100% esticava o card
- impacto: ilustração visível sem distorcer o layout

## Contexto utilizado

### Contexto mínimo lido

- task 280, handoff 279, slice 010, índice

### Contexto sob demanda carregado

| Fonte | Gatilho | Uso |
|---|---|---|
| `HomeActionCard/index.tsx` | estrutura sombra | View host + Pressable interno |
| `HomeActionCard/styles.ts` | shadow/bg size | elevation e carimbo |
| `ResponsavelHomeScreen.tsx` | opacidade | 0.7 |

### Contexto evitado

| Fonte | Motivo |
|---|---|
| requirements/contracts/outras stacks | não se aplica |

## Resultado por stack

- mobile: sombra e bg do card de avisos corrigidos

## Arquivos alterados

- `mobile/src/features/shell/components/HomeActionCard/index.tsx`
- `mobile/src/features/shell/components/HomeActionCard/styles.ts`
- `mobile/src/features/shell/screens/ResponsavelHomeScreen.tsx`
- task/index/slice/handoff 280

## Validações executadas

- validação: visual no device após reload (confirmação do usuário)

## Pendências ou bloqueios

- confirmar tamanho/opacidade do carimbo no device

## Próxima ação sugerida

- se a sombra ainda parecer quadrada no Android, reduzir elevation para 3–4

## Próximo contexto recomendado

- `HomeActionCard/styles.ts`
- `.agents/state/handoffs/TASK-280.md`

## Contexto que não deve ser carregado na próxima etapa

- fonte: requirements, contracts, web/backend
- motivo: refino visual local

# Handoff - Task 279

## Task

- identificador: 279
- título: Reduzir tamanho do bg trilha no card de avisos home mobile
- tipo: mobile
- modo de execução: single-stack
- status final: done

## Slice vertical

- identificador: 010
- objetivo de negócio: home/perfil/notificacoes do responsavel
- entrega verificável: bg `trilha.webp` menor, sem esticar o card

## Decisões preservadas

- decisão: imagem 112x112, `contain`, ancorada à esquerda/inferior; sem scrim full-bleed
- motivo: o fill 100% + cover/stretch esticava a composição do card
- impacto: card volta ao tamanho natural; ilustração vira carimbo decorativo

- decisão: opacidade do bg na home em 0.45
- motivo: asset escuro em carimbo pequeno; opacidade total formava bloco preto forte
- impacto: trilha visível sem dominar o card

## Contexto utilizado

### Contexto mínimo lido

- task 279, handoff 278, slice 010, índice

### Contexto sob demanda carregado

| Fonte | Gatilho | Uso |
|---|---|---|
| `HomeActionCard/styles.ts` | tamanho do bg | 112x112 + posição |
| `HomeActionCard/index.tsx` | remoção do scrim | contain sem overlay |
| `ResponsavelHomeScreen.tsx` | opacidade | 0.45 |

### Contexto evitado

| Fonte | Motivo |
|---|---|
| requirements/contracts/outras stacks | não se aplica |

## Resultado por stack

- mobile: bg menor no card de avisos

## Arquivos alterados

- `mobile/src/features/shell/components/HomeActionCard/index.tsx`
- `mobile/src/features/shell/components/HomeActionCard/styles.ts`
- `mobile/src/features/shell/screens/ResponsavelHomeScreen.tsx`
- task/index/slice/handoff 279

## Validações executadas

- validação: visual no device após reload (confirmação do usuário)

## Pendências ou bloqueios

- ajustar tamanho se 112px ainda estiver grande/pequeno

## Próxima ação sugerida

- se pedir outro tamanho, só mexer em `backgroundImage` width/height

## Próximo contexto recomendado

- `HomeActionCard/styles.ts`
- `.agents/state/handoffs/TASK-279.md`

## Contexto que não deve ser carregado na próxima etapa

- fonte: requirements, contracts, web/backend
- motivo: refino visual local

# Handoff - Task 281

## Task

- identificador: 281
- título: Remover bg trilha e mover sombra para o card de avisos home mobile
- tipo: mobile
- modo de execução: single-stack
- status final: done

## Slice vertical

- identificador: 010
- objetivo de negócio: home/perfil/notificacoes do responsavel
- entrega verificável: card de avisos sem bg de imagem e com sombra no próprio card

## Decisões preservadas

- decisão: removido suporte a `backgroundImageSource` / `backgroundImageOpacity` do `HomeActionCard`
- motivo: usuário pediu remoção do background
- impacto: card volta a fundo sólido branco

- decisão: sombra no próprio card (`Pressable`/`View` com `styles.card` + `styles.cardShadow`); wrapper pai removido
- motivo: pedido explícito do usuário
- impacto: sem host externo de sombra

## Contexto utilizado

### Contexto mínimo lido

- task 281, handoff 280, slice 010, índice

### Contexto sob demanda carregado

| Fonte | Gatilho | Uso |
|---|---|---|
| `HomeActionCard/*` | limpeza bg + sombra | implementação |
| `ResponsavelHomeScreen.tsx` | remover props/require | home |

### Contexto evitado

| Fonte | Motivo |
|---|---|
| requirements/contracts/outras stacks | não se aplica |

## Resultado por stack

- mobile: card de avisos sem bg imagem; sombra no card

## Arquivos alterados

- `mobile/src/features/shell/components/HomeActionCard/index.tsx`
- `mobile/src/features/shell/components/HomeActionCard/styles.ts`
- `mobile/src/features/shell/screens/ResponsavelHomeScreen.tsx`
- task/index/slice/handoff 281

## Validações executadas

- validação: visual no device após reload

## Pendências ou bloqueios

- nenhuma

## Próxima ação sugerida

- se a sombra no Android voltar quadrada, revisar elevation no próprio card

## Próximo contexto recomendado

- `HomeActionCard/styles.ts`
- `.agents/state/handoffs/TASK-281.md`

## Contexto que não deve ser carregado na próxima etapa

- fonte: requirements, contracts, web/backend
- motivo: refino visual local

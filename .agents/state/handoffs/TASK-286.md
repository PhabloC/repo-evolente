# Handoff - Task 286

## Task

- identificador: 286
- título: Refinar card da crianca no perfil mobile
- tipo: mobile
- modo de execução: single-stack
- status final: done

## Slice vertical

- identificador: 010

## Decisões preservadas

- decisão: removido o cabeçalho agregado "Criança / 1 vinculada / toque..."
- motivo: pedido do usuário (print anexado)
- impacto: cada criança é um `HomeActionCard` independente

- decisão: nascimento com `Calendar`; código em linha abaixo com `Hash`
- motivo: pedido visual do usuário
- impacto: metadados no mesmo padrão do card do responsável

## Contexto utilizado

- print anexado, `ResponsavelProfileScreen.tsx`, handoff 285

## Arquivos alterados

- `ResponsavelProfileScreen.tsx`
- `screens/styles.ts`
- task/index/slice/handoff 286

## Validações executadas

- visual no device após reload

## Pendências ou bloqueios

- nenhuma

## Próxima ação sugerida

- nenhuma

## Próximo contexto recomendado

- `.agents/state/handoffs/TASK-286.md`

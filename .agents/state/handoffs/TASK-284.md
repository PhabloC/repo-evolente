# Handoff - Task 284

## Task

- identificador: 284
- título: Alinhar cards da pagina de perfil ao estilo do card da home mobile
- tipo: mobile
- modo de execução: single-stack
- status final: done

## Slice vertical

- identificador: 010

## Decisões preservadas

- decisão: reutilizar `HomeActionCard` nos dois cards do perfil
- motivo: mesmo estilo da home (sombra no card, pastilha, status, CTA)
- impacto: avatar com inicial do responsável substituído pela pastilha com ícone `User`

- decisão: lista de crianças fica como `children` do card "Criança"
- motivo: preservar navegação de edição por item
- impacto: card externo sem `onPress`; cada linha continua pressionável

## Contexto utilizado

- `ResponsavelProfileScreen.tsx`
- `HomeActionCard`
- `screens/styles.ts`
- handoff 283

## Arquivos alterados

- `mobile/src/features/shell/screens/ResponsavelProfileScreen.tsx`
- `mobile/src/features/shell/screens/styles.ts`
- task/index/slice/handoff 284

## Validações executadas

- visual no device após reload

## Pendências ou bloqueios

- nenhuma

## Próxima ação sugerida

- nenhuma

## Próximo contexto recomendado

- `.agents/state/handoffs/TASK-284.md`

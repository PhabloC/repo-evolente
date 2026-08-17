# Handoff - Task 287

## Task

- identificador: 287
- título: Foto de perfil nos cards de responsavel e crianca no perfil mobile
- tipo: mobile
- modo de execução: single-stack
- status final: done

## Slice vertical

- identificador: 010

## Decisões preservadas

- decisão: prop `leading` no `HomeActionCard` para avatar customizado
- motivo: foto de perfil não cabe no ícone Lucide/`imageSource` 24px
- impacto: cards da home de avisos continuam com ícone/imagem decorativa

- decisão: responsável usa foto ou inicial provisória (padrão `HomeHeader`)
- decisão: criança usa `ChildAvatar` (foto ou default por sexo)

## Contexto utilizado

- `ChildAvatar`, `HomeHeader` avatar, `HomeActionCard`, perfil screen

## Arquivos alterados

- `HomeActionCard/*`
- `ResponsavelProfileScreen.tsx`
- `screens/styles.ts`
- task/index/slice/handoff 287

## Validações executadas

- visual no device após reload

## Pendências ou bloqueios

- nenhuma

## Próxima ação sugerida

- nenhuma

## Próximo contexto recomendado

- `.agents/state/handoffs/TASK-287.md`

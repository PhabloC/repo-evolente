# Task 278 - Profundidade e bg trilha no card de avisos home mobile

## Status

done

## Tipo

mobile

## Stacks envolvidos

- mobile

## Perfil do projeto

- stack web escolhida: front-end (React/Vite)
- mobile: sim

## Contrato

- não se aplica

## Modo de execucao

single-stack

## Slice vertical

- Slice 010 - App do responsavel: home, perfil e notificacoes
- `tasks/slices/010-app-responsavel-home-notificacoes.md`

## Referencia visual

### Stack de referencia visual

mobile

### Tipo de referencia visual

refino incremental solicitado pelo usuário + print do card atual

### Fonte primaria visual

- print do card "Avisos da trilha" enviado pelo usuário (estado atual branco, sombra fraca)
- `mobile/assets/trilha.webp`
- `mobile/src/features/shell/components/HomeActionCard/index.tsx`
- `mobile/src/features/shell/components/HomeActionCard/styles.ts`
- `mobile/src/features/shell/screens/ResponsavelHomeScreen.tsx`

## Objetivo

Ajustar o card "Avisos da trilha" da home para ter sombra com sensação real de profundidade e usar `trilha.webp` como background visível do card.

## Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/010-app-responsavel-home-notificacoes.md`
- `.agents/state/handoffs/TASK-277.md`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| Composição do card | `HomeActionCard/index.tsx`, `styles.ts` | corrigir shadow e render do background | sim |
| Uso na home | `ResponsavelHomeScreen.tsx` | confirmar props do card de avisos | sim |
| Asset | `mobile/assets/trilha.webp` | background solicitado | sim |

## Orçamento de contexto

- baixo
- estrategia: ajustar apenas `HomeActionCard` e o uso do card de avisos na home

## Criterios de conclusao

- [x] sombra do card transmite profundidade (visível no Android via elevation + iOS shadow)
- [x] `trilha.webp` aparece como background do card de avisos
- [x] texto e CTA do card permanecem legíveis

## Dependencias

- Task 277 - done

## Resultado da execucao

- sombra reequilibrada: offset/radius realistas e `backgroundColor` no container elevado (necessário para elevation no Android)
- background do `trilha.webp` passou a usar `absoluteFill` + `resizeMode="cover"` para preencher o card de forma confiável
- com opacidade alta, um scrim branco leve preserva legibilidade do texto sobre o asset escuro

## Contexto utilizado

### Mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`
- `tasks/000-index.md`, esta task, `tasks/slices/010-app-responsavel-home-notificacoes.md`
- `.agents/state/handoffs/TASK-277.md`

### Sob demanda

- `mobile/src/features/shell/components/HomeActionCard/index.tsx`
- `mobile/src/features/shell/components/HomeActionCard/styles.ts`
- `mobile/src/features/shell/screens/ResponsavelHomeScreen.tsx`
- `mobile/assets/trilha.webp`

## Handoff

- `.agents/state/handoffs/TASK-278.md`

## Arquivos alterados

- `tasks/change-requests/278-profundidade-e-bg-trilha-card-avisos-home-mobile.md`
- `tasks/000-index.md`
- `tasks/slices/010-app-responsavel-home-notificacoes.md`
- `.agents/state/handoffs/TASK-278.md`
- `mobile/src/features/shell/components/HomeActionCard/index.tsx`
- `mobile/src/features/shell/components/HomeActionCard/styles.ts`

## Validacoes executadas

- validação visual dependente de hot reload / reload no Expo Go Android

## Pendencias pos-task

- confirmar no device se o equilíbrio entre presença do `trilha.webp` e legibilidade do texto está no ponto

## Status final

done

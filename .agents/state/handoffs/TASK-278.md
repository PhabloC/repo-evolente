# Handoff - Task 278

## Task

- identificador: 278
- título: Profundidade e bg trilha no card de avisos home mobile
- tipo: mobile
- modo de execução: single-stack
- status final: done

## Slice vertical

- identificador: 010
- objetivo de negócio: home/perfil/notificacoes do responsavel
- entrega verificável: card "Avisos da trilha" com profundidade e bg `trilha.webp`

## Decisões preservadas

- decisão: sombra com offset ~10 e elevation 12, com `backgroundColor` no container elevado
- motivo: offset 80 tornava a sombra quase invisível; Android precisa de fundo no view com elevation
- impacto: profundidade visível sem pontas estranhas

- decisão: `trilha.webp` em `cover` + `absoluteFill`, com scrim branco leve quando opacidade >= 0.5
- motivo: asset é claro sobre preto; sem scrim o texto escuro perde contraste
- impacto: fundo ilustrado visível e CTA/título legíveis

## Contexto utilizado

### Contexto mínimo lido

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- `tasks/change-requests/278-profundidade-e-bg-trilha-card-avisos-home-mobile.md`
- `tasks/slices/010-app-responsavel-home-notificacoes.md`
- `.agents/state/handoffs/TASK-277.md`

### Contexto sob demanda carregado

| Fonte | Gatilho | Uso |
|---|---|---|
| `HomeActionCard/index.tsx` | composição do bg | render do background + scrim |
| `HomeActionCard/styles.ts` | sombra e fill | profundidade e absoluteFill |
| `ResponsavelHomeScreen.tsx` | props do card | confirmar `trilha.webp` e opacity 1 |
| `mobile/assets/trilha.webp` | asset solicitado | background do card |

### Contexto evitado

| Fonte | Motivo |
|---|---|
| `requirements/` | não se aplica |
| `contracts/openapi.yaml` | sem mudança de API |
| `front-end/`, `backend/` | stack não envolvida |

## Resultado por stack

- front-end ou next-js: não se aplica
- backend: não se aplica
- mobile: card de avisos com sombra profunda e bg `trilha.webp`

## Arquivos alterados

- `mobile/src/features/shell/components/HomeActionCard/index.tsx`
- `mobile/src/features/shell/components/HomeActionCard/styles.ts`
- `tasks/change-requests/278-profundidade-e-bg-trilha-card-avisos-home-mobile.md`
- `tasks/000-index.md`
- `tasks/slices/010-app-responsavel-home-notificacoes.md`
- `.agents/state/handoffs/TASK-278.md`

## Validações executadas

- validação: visual no device via Expo Go (pendente confirmação do usuário após reload)

## Pendências ou bloqueios

- confirmar no app se o scrim/opacidade do fundo está no ponto desejado

## Próxima ação sugerida

- se o usuário pedir mais/menos presença do bg ou mais/menos sombra, ajustar só esses tokens no `HomeActionCard`

## Próximo contexto recomendado

- `HomeActionCard/styles.ts`
- `HomeActionCard/index.tsx`
- `.agents/state/handoffs/TASK-278.md`

## Contexto que não deve ser carregado na próxima etapa

- fonte: `requirements/`, `contracts/`, stacks web/backend
- motivo: refino visual local do card

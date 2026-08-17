# Handoff - Task 351

## Task

- identificador: 351
- título: Refinar botões e resumo da semana na trilha web
- tipo: front
- modo de execução: single-stack
- status final: done

## Slice vertical

- identificador: Slice 017 - Redesign interface interna web
- objetivo de negócio: reforçar a hierarquia visual da navegação da trilha e do resumo semanal
- entrega verificável: CTAs azuis na trilha e período da semana destacado em badge

## Decisões preservadas

- decisão: manter a estrutura do card da semana e trocar apenas a apresentação visual dos CTAs e do texto de período
- motivo: o problema reportado era de hierarquia visual, não de fluxo ou comportamento
- impacto: a navegação e a lógica da semana permanecem iguais, com leitura mais clara

## Contexto utilizado

### Contexto mínimo lido

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- `tasks/change-requests/351-refinar-botoes-e-resumo-da-semana-na-trilha-web.md`
- `tasks/slices/017-redesign-interface-interna-web.md`
- `.agents/state/handoffs/TASK-349.md`

### Contexto sob demanda carregado

| Fonte | Gatilho | Uso |
|---|---|---|
| `front-end/docs/ai/ACCESSIBILITY.md` | UI web | preservar contraste e foco dos novos botões |
| `front-end/docs/ai/CODE_STYLE.md` | UI web | manter consistência de implementação |
| `front-end/src/pages/Main/Plans/PatientTrail/index.tsx` | trilha | aplicar os CTAs azuis e refinar a copy semanal |
| `front-end/src/pages/Main/Plans/styles.module.css` | estilos locais | criar as variações visuais específicas da trilha |
| `front-end/src/pages/Main/Plans/PatientTrail/index.test.tsx` | validação | confirmar estabilidade da tela |

### Contexto evitado

| Fonte | Motivo |
|---|---|
| `contracts/openapi.yaml` | sem mudança de contrato |
| `backend/` | sem mudança de API |
| outras páginas de planejamentos | ajuste isolado à trilha do paciente |

## Resultado por stack

- front-end: trilha com CTAs azuis consistentes e resumo semanal mais legível
- backend: nao se aplica
- mobile: nao se aplica

## Arquivos alterados

- `front-end/src/pages/Main/Plans/PatientTrail/index.tsx`
- `front-end/src/pages/Main/Plans/styles.module.css`
- `tasks/change-requests/351-refinar-botoes-e-resumo-da-semana-na-trilha-web.md`
- `tasks/slices/017-redesign-interface-interna-web.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-351.md`

## Validações executadas

- `cd front-end && npm test -- --run src/pages/Main/Plans/PatientTrail/index.test.tsx` - ok
- `cd front-end && npx eslint src/pages/Main/Plans/PatientTrail/index.tsx src/pages/Main/Plans/PatientTrail/index.test.tsx` - ok
- `cd front-end && npx eslint src/pages/Main/Plans/styles.module.css` - aviso esperado; CSS ignorado pela configuração atual

## Pendências ou bloqueios

- nenhuma

## Próxima ação sugerida

- validar visualmente se o mesmo azul deve ser reaplicado a outros botões secundários da área de planejamentos

## Próximo contexto recomendado

- `front-end/src/pages/Main/Plans/PatientTrail/index.tsx`
- `front-end/src/pages/Main/Plans/styles.module.css`

## Contexto que não deve ser carregado na próxima etapa

- fonte: `backend/`, `contracts/openapi.yaml`, outras páginas de planejamentos
- motivo: a mudança foi isolada ao visual da trilha

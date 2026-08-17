# Handoff - Task 316

## Task

- identificador: 316
- titulo: Extrair variant info do botão e aplicar no Baixar de relatórios
- tipo: front
- modo de execucao: single-stack
- status final: done

## Slice vertical

- identificador: Slice 011 - Relatorios de evolucao
- objetivo de negocio: alinhar o CTA `Baixar` ao design system e consolidar reuso no botão global
- entrega verificavel: a ação `Baixar` usa um variant reutilizável azul baseado em `Confianca` e a rota `/relatorios` continua funcional

## Decisoes preservadas

- a cor oficial adotada para o variant foi `Azul Confianca` (`#2978BB`), conforme o design system desktop
- o refinamento saiu da página `Reports` e virou variant global `info` no `ui/Button`
- a página de relatórios passou a apenas consumir `variant="info"`, mantendo o alinhamento já resolvido da coluna `Ações`

## Contexto utilizado

### Contexto minimo lido

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- `tasks/change-requests/316-extrair-variant-info-do-botao-e-aplicar-no-baixar-relatorios.md`
- `tasks/slices/011-relatorios-evolucao.md`
- `.agents/state/handoffs/TASK-315.md`

### Contexto sob demanda carregado

| Fonte | Gatilho | Uso |
|---|---|---|
| `design-system/front/Design_System_Evolente_Desktop.md` | aderência visual | confirmar o azul `Confianca` e o direcionamento de CTA |
| `front-end/docs/ai/{AGENTS.md,ARCHITECTURE.md,ACCESSIBILITY.md,COMPONENT_REUSE.md}` | ajuste de primitiva compartilhada | manter coerência estrutural, semântica e de reuso |
| `front-end/src/ui/Button/{index.tsx,styles.module.css}` | novo variant global | expor `variant="info"` no botão compartilhado |
| `front-end/src/pages/Main/Reports/{index.tsx,styles.module.css}` | migração do consumidor | aplicar o variant e remover a skin local |

### Contexto evitado

| Fonte | Motivo |
|---|---|
| `backend/` | sem mudança funcional ou de API |
| `contracts/openapi.yaml` | sem alteração de contrato |

## Resultado por stack

- front-end: variant global `info` criado no `Button` e aplicado ao CTA `Baixar`
- backend: sem alterações
- mobile: sem alterações

## Arquivos alterados

- `front-end/src/ui/Button/index.tsx`
- `front-end/src/ui/Button/styles.module.css`
- `front-end/src/pages/Main/Reports/index.tsx`
- `front-end/src/pages/Main/Reports/styles.module.css`
- `tasks/change-requests/316-extrair-variant-info-do-botao-e-aplicar-no-baixar-relatorios.md`
- `tasks/slices/011-relatorios-evolucao.md`
- `tasks/000-index.md`

## Validacoes executadas

- `cd front-end && npx eslint src/ui/Button/index.tsx src/pages/Main/Reports/index.tsx`: ok
- `cd front-end && npm run build`: ok

## Pendencias ou bloqueios

- nenhuma

## Proxima acao sugerida

- reutilizar o variant `info` em outras ações informativas da interface apenas quando o design system exigir a mesma semântica visual

## Proximo contexto recomendado

- `front-end/src/ui/Button/index.tsx`
- `front-end/src/ui/Button/styles.module.css`
- `front-end/src/pages/Main/Reports/index.tsx`

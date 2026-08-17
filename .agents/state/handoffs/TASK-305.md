# Handoff - Task 305

## Task

- identificador: 305
- titulo: Evitar deslocamento do subtítulo ao abrir busca web
- tipo: front
- modo de execucao: single-stack
- status final: done

## Slice vertical

- identificador: Slice 017 - Redesign da interface interna web
- objetivo de negocio: manter o header estável ao abrir a busca compartilhada
- entrega verificavel: o subtítulo da página deixa de ser empurrado quando a busca abre

## Decisoes preservadas

- a solução reservou a largura máxima da área de busca no desktop em vez de reposicionar o campo de forma absoluta
- o comportamento recente da busca permaneceu intacto: foco automático, input estável e fechamento por botão dedicado
- o ajuste foi mantido no CSS do header compartilhado, evitando alterações nas páginas consumidoras

## Contexto utilizado

### Contexto minimo lido

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- `tasks/change-requests/305-evitar-deslocamento-do-subtitulo-ao-abrir-busca-web.md`
- `tasks/slices/017-redesign-interface-interna-web.md`
- `.agents/state/handoffs/TASK-304.md`

### Contexto sob demanda carregado

| Fonte | Gatilho | Uso |
|---|---|---|
| `front-end/docs/ai/ACCESSIBILITY.md` | UI web | preservar semântica e foco da busca |
| `front-end/docs/ai/COMPONENT_REUSE.md` | layout compartilhado | limitar a mudança ao header |
| `front-end/src/layout/Header/{index.tsx,styles.module.css,index.test.tsx}` | regressão do header | estabilizar a largura do bloco de busca |
| `front-end/src/pages/Main/Patients/index.test.tsx` | regressão leve | confirmar integridade de uma rota interna após o ajuste |

### Contexto evitado

| Fonte | Motivo |
|---|---|
| `contracts/openapi.yaml` | sem alteração de contrato |
| `backend/` | sem mudança funcional |
| `mobile/` | escopo exclusivo da web |

## Resultado por stack

- front-end: header estável ao abrir a busca, sem empurrar o subtítulo
- backend: sem alteracoes
- mobile: sem alteracoes

## Arquivos alterados

- `front-end/src/layout/Header/styles.module.css`
- `tasks/change-requests/305-evitar-deslocamento-do-subtitulo-ao-abrir-busca-web.md`
- `tasks/slices/017-redesign-interface-interna-web.md`
- `tasks/000-index.md`

## Validacoes executadas

- `cd front-end && npm run test -- --run src/layout/Header/index.test.tsx src/pages/Main/Patients/index.test.tsx`: ok
- `cd front-end && npx eslint src/layout/Header/index.tsx src/layout/Header/index.test.tsx`: ok

## Pendencias ou bloqueios

- nenhuma

## Proxima acao sugerida

- seguir apenas se houver pedido para tornar a busca funcional com resultados reais

## Proximo contexto recomendado

- `front-end/src/layout/Header/styles.module.css`
- `front-end/src/layout/Header/index.tsx`
- `front-end/src/layout/Header/index.test.tsx`

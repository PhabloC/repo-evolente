# Handoff - Task 298

## Task

- identificador: 298
- titulo: Corrigir busca expansível no header web
- tipo: front
- modo de execucao: single-stack
- status final: done

## Slice vertical

- identificador: Slice 017 - Redesign da interface interna web
- objetivo de negocio: remover a friccao da busca expansivel no header compartilhado
- entrega verificavel: a lupa abre a busca, o clique no campo nao recolhe o componente e o fechamento acontece por um icone dedicado

## Decisoes preservadas

- o `input` deixou de ficar aninhado dentro do botao da lupa para corrigir semantica e comportamento
- a lupa passou a apenas abrir a busca; o fechamento agora acontece em um botao separado com icone `X`
- o foco vai automaticamente para o campo ao abrir, mantendo acessibilidade e fluidez operacional

## Contexto utilizado

### Contexto minimo lido

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- `tasks/change-requests/298-corrigir-busca-expansivel-no-header-web.md`
- `tasks/slices/017-redesign-interface-interna-web.md`
- `.agents/state/handoffs/TASK-297.md`

### Contexto sob demanda carregado

| Fonte | Gatilho | Uso |
|---|---|---|
| `front-end/docs/ai/ACCESSIBILITY.md` | interacao de UI | garantir foco, semântica e acionamento por teclado |
| `front-end/docs/ai/COMPONENT_REUSE.md` | componente compartilhado | limitar a mudança ao header |
| `front-end/src/layout/Header/{index.tsx,styles.module.css,index.test.tsx}` | busca expansível | corrigir estrutura, estilo e cobertura |
| `front-end/src/pages/Main/Patients/index.test.tsx` | regressão leve | validar que a área de pacientes segue íntegra após a mudança no layout |

### Contexto evitado

| Fonte | Motivo |
|---|---|
| `contracts/openapi.yaml` | sem alteração de contrato |
| `backend/` | sem mudança funcional |
| `mobile/` | escopo exclusivo da web |

## Resultado por stack

- front-end: busca expansível do header corrigida com botão dedicado de fechar
- backend: sem alteracoes
- mobile: sem alteracoes

## Arquivos alterados

- `front-end/src/layout/Header/index.tsx`
- `front-end/src/layout/Header/styles.module.css`
- `front-end/src/layout/Header/index.test.tsx`
- `tasks/change-requests/298-corrigir-busca-expansivel-no-header-web.md`
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

- `front-end/src/layout/Header/index.tsx`
- `front-end/src/layout/Header/styles.module.css`
- `front-end/src/layout/Header/index.test.tsx`

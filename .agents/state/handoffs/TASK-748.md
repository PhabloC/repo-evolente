# Handoff - Task 748

## Task

- identificador: TASK-748
- título: Contato na política de privacidade web
- tipo: front
- modo de execução: single-stack
- status final: done

## Slice vertical

- identificador: Slice 062
- objetivo de negócio: contato do titular na política de privacidade
- entrega verificável: e-mail e celular na seção “Como solicitar”

## Decisões preservadas

- decisão: canais na seção 11, com `mailto:` e `tel:+5538984058324`
- motivo: a política já concentrava pedidos nessa seção e só citava “e-mail de suporte”
- impacto: a data vigente passou para 29 de setembro de 2026; o celular 38-984058324 aparece como (38) 98405-8324

## Contexto utilizado

### Contexto mínimo lido

- `AGENTS.md`
- `GUIDE.md` (índice de governança; a execução não precisou de regra extra)
- `.agents/context-map.md`
- `tasks/000-index.md`
- `tasks/change-requests/748-contato-politica-privacidade-web.md`
- `tasks/slices/062-contato-politica-privacidade-web.md`

### Contexto sob demanda carregado

| Fonte | Gatilho | Uso |
|---|---|---|
| `front-end/src/pages/Public/PrivacyPolicy/` | página pública da política | incluir os contatos |
| `front-end/docs/ai/ACCESSIBILITY.md` | links novos | foco visível e nome do link igual ao valor |

### Contexto evitado

| Fonte | Motivo |
|---|---|
| `mobile/`, `backend/`, `contracts/openapi.yaml` | não se aplica a esta task |

## Resultado por stack

- front-end: seção “Como solicitar” com e-mail e celular
- backend: não envolvido
- mobile: não envolvido

## Arquivos alterados

- `front-end/src/pages/Public/PrivacyPolicy/content.ts`
- `front-end/src/pages/Public/PrivacyPolicy/index.tsx`
- `front-end/src/pages/Public/PrivacyPolicy/styles.module.css`

## Validações executadas

- página pública `/politica-de-privacidade`: contatos visíveis e links com `mailto` e `tel`

## Pendências ou bloqueios

- nenhuma

## Próxima ação sugerida

- nenhuma

## Próximo contexto recomendado

- `front-end/src/pages/Public/PrivacyPolicy/content.ts` se o canal de contato mudar de novo

## Contexto que não deve ser carregado na próxima etapa

- fonte: histórico das tasks de layout e jogos
- motivo: não altera a política de privacidade

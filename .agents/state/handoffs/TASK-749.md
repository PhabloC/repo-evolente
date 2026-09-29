# Handoff - Task 749

## Task

- identificador: TASK-749
- título: Remover o bloco de pagamento da política de privacidade
- tipo: front
- modo de execução: single-stack
- status final: done

## Slice vertical

- identificador: Slice 062
- objetivo de negócio: política de privacidade pública coerente com o pedido atual
- entrega verificável: sem o bloco “Pagamento” em “Dados que coletamos”

## Decisões preservadas

- decisão: remover só o subtítulo “Pagamento” e o parágrafo de Asaas, cartão e PIX
- motivo: o pedido nomeou essa parte da política
- impacto: menções pontuais a assinatura e Asaas em finalidades, compartilhamento, transferência e retenção continuam

## Contexto utilizado

### Contexto mínimo lido

- `tasks/change-requests/749-remover-pagamento-politica-privacidade.md`
- `front-end/src/pages/Public/PrivacyPolicy/content.ts`

### Contexto sob demanda carregado

| Fonte | Gatilho | Uso |
|---|---|---|
| nenhuma extra | remoção localizada | — |

### Contexto evitado

| Fonte | Motivo |
|---|---|
| `mobile/`, `backend/`, `contracts/` | não se aplica |

## Resultado por stack

- front-end: bloco “Pagamento” removido
- backend: não envolvido
- mobile: não envolvido

## Arquivos alterados

- `front-end/src/pages/Public/PrivacyPolicy/content.ts`

## Validações executadas

- `/politica-de-privacidade` sem o subtítulo “Pagamento”

## Pendências ou bloqueios

- nenhuma

## Próxima ação sugerida

- nenhuma

## Próximo contexto recomendado

- `front-end/src/pages/Public/PrivacyPolicy/content.ts`

## Contexto que não deve ser carregado na próxima etapa

- fonte: tasks de layout e jogos
- motivo: não alteram esta página

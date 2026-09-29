# Handoff - Task 750

## Task

- identificador: TASK-750
- título: Retirar Asaas da política de privacidade
- tipo: front
- modo de execução: single-stack
- status final: done

## Slice vertical

- identificador: Slice 062
- objetivo de negócio: política sem as frases de Asaas pedidas
- entrega verificável: sem o item de cartão/PIX e sem Asaas na seção 7

## Decisões preservadas

- decisão: remover o bullet do Asaas e a frase “O Asaas opera no Brasil”
- motivo: pedido explícito dessas duas partes
- impacto: a seção 7 segue com OneSignal e região da mídia

## Contexto utilizado

### Contexto mínimo lido

- `front-end/src/pages/Public/PrivacyPolicy/content.ts`

### Contexto sob demanda carregado

| Fonte | Gatilho | Uso |
|---|---|---|
| nenhuma extra | edição localizada | — |

### Contexto evitado

| Fonte | Motivo |
|---|---|
| `mobile/`, `backend/`, `contracts/` | não se aplica |

## Resultado por stack

- front-end: duas frases do Asaas removidas
- backend: não envolvido
- mobile: não envolvido

## Arquivos alterados

- `front-end/src/pages/Public/PrivacyPolicy/content.ts`

## Validações executadas

- `/politica-de-privacidade` sem Asaas

## Pendências ou bloqueios

- nenhuma

## Próxima ação sugerida

- nenhuma

## Próximo contexto recomendado

- `front-end/src/pages/Public/PrivacyPolicy/content.ts`

## Contexto que não deve ser carregado na próxima etapa

- fonte: tasks de layout e jogos
- motivo: não alteram esta página

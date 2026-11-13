# Handoff - Task 811

## Task

- identificador: 811
- título: Botão falar com o suporte na assinatura web
- tipo: front
- modo de execução: single-stack
- status final: done

## Slice vertical

- identificador: 005
- objetivo de negócio: pagamento e gate de assinatura
- entrega verificável: CTA mailto no gate `/assinatura`

## Decisões preservadas

- decisão: usar `<a href="mailto:evolenteapp@gmail.com">` com visual de botão secundário, não `Button` com `onClick`
- motivo: leitor de tela e teclado tratam como link de e-mail; teste valida `href`
- impacto: constante em `constants/support.ts`; política de privacidade continua com e-mail próprio

## Contexto utilizado

### Contexto mínimo lido

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- `tasks/change-requests/811-botao-falar-com-suporte-assinatura-web.md`
- `tasks/slices/005-assinatura-liberacao-acesso.md`

### Contexto sob demanda carregado

| Fonte | Gatilho | Uso |
|---|---|---|
| `front-end/src/pages/Auth/SubscriptionGate/` | UI do gate | inserir CTA |
| `front-end/docs/ai/ACCESSIBILITY.md` | a11y | link focável |
| `front-end/src/ui/Button/styles.module.css` | visual | espelhar secondary |

### Contexto evitado

| Fonte | Motivo |
|---|---|
| `requirements/` | não se aplica |
| `contracts/openapi.yaml` | sem API |
| `mobile/` | fora de escopo |
| `PrivacyPolicy` | e-mail diferente; não misturar |

## Resultado por stack

- front-end: CTA suporte no gate
- backend: n/a
- mobile: n/a

## Arquivos alterados

- `front-end/src/constants/support.ts`
- `front-end/src/pages/Auth/SubscriptionGate/index.tsx`
- `front-end/src/pages/Auth/SubscriptionGate/styles.module.css`
- `front-end/src/pages/Auth/SubscriptionGate/index.test.tsx`

## Validações executadas

- validação: Vitest SubscriptionGate — 5 passed

## Pendências ou bloqueios

- item: nenhuma

## Próxima ação sugerida

- Nenhuma; task concluída.

## Próximo contexto recomendado

- Só `SubscriptionGate` e `constants/support.ts` se precisar ajustar o e-mail.

## Contexto que não deve ser carregado na próxima etapa

- fonte: backend, mobile, OpenAPI, política de privacidade
- motivo: fora do escopo deste CTA

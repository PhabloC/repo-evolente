# Task 811 - Botão falar com o suporte na assinatura web

## Status

done

## Tipo

front

## Stacks envolvidos

- front-end

## Perfil do projeto

- stack web escolhida: front-end (React/Vite)
- mobile: sim (fora de escopo desta task)

## Contrato

- n/a (apenas link `mailto:` no cliente; sem API)

## Modo de execucao

single-stack

## Slice vertical

- Slice 005 - Assinatura e liberação de acesso
- `tasks/slices/005-assinatura-liberacao-acesso.md`

## Objetivo

Na página de assinatura (`/assinatura`), oferecer um botão "Falar com o suporte" que abre o cliente de e-mail com destino `evolenteapp@gmail.com`.

## Escopo

- Adicionar CTA visível na tela de assinatura (gate).
- Abrir `mailto:evolenteapp@gmail.com` ao acionar o botão.
- Manter o restante do fluxo de login/pagamento inalterado.

## Fora de escopo

- Mobile
- Backend / OpenAPI
- Chat in-app, formulário de ticket ou troca de e-mail da política de privacidade
- Redesign do gate

## Referencia de design system

### Stack de referencia visual

front-end

### Tipo de referencia visual

artefato de design system

### Fonte primaria visual

- `design-system/front/Design_System_Evolente_Desktop.md` — apenas se o CTA exigir componente novo; preferir reutilizar `Button` e padrões já usados em `SubscriptionGate`

### Regra de aderencia visual

- Sem print deste estado. Reutilizar botão secundário/ghost e ícone Lucide já adotados no gate.

## Origem da solicitacao

Pedido direto: na página de assinatura, botão para falar com o suporte enviando e-mail para `evolenteapp@gmail.com`.

## Comportamento esperado

- Em qualquer estado do gate (login, pending, awaiting-payment, error), o usuário vê "Falar com o suporte".
- Ao clicar, o navegador abre o cliente de e-mail com destinatário `evolenteapp@gmail.com`.
- O fluxo de pagamento e o link "Voltar ao login" continuam iguais.

## Criterios de aceite

- [x] Botão "Falar com o suporte" visível em `/assinatura`
- [x] Ação abre `mailto:evolenteapp@gmail.com`
- [x] Sem alteração de API, mobile ou política de privacidade
- [x] Teste do gate cobre a presença do CTA e o `href`/`mailto`

## Contexto mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`
- `tasks/000-index.md`
- este arquivo
- `tasks/slices/005-assinatura-liberacao-acesso.md`

## Contexto sob demanda

| Gatilho | Fonte | Decisão |
|---|---|---|
| UI do gate | `front-end/src/pages/Auth/SubscriptionGate/` | inserir CTA |
| A11y web | `front-end/docs/ai/ACCESSIBILITY.md` | link/`mailto` acionável por teclado |
| Padrão de botão | `front-end/src/ui/Button/` | visual secundário em `<a>` |

## Orçamento de contexto

baixo — uma página auth; sem DS amplo, sem OpenAPI, sem mobile

## Estrategia de reducao

- Não reler requirements nem DS completo
- Não alterar política de privacidade (e-mail diferente)
- Não tocar backend/mobile

## Dependencias

- Task 013 / gate de assinatura — done

## Resultado da execucao

- CTA "Falar com o suporte" no rodapé do gate `/assinatura`, com `mailto:evolenteapp@gmail.com`.
- Constante compartilhada em `front-end/src/constants/support.ts`.
- Teste do gate valida presença e `href`.

## Contexto utilizado

- Contexto mínimo da task + `SubscriptionGate` + `ACCESSIBILITY.md` (link focável) + estilos secundários do `Button`.

## Handoff

- `.agents/state/handoffs/TASK-811.md`

## Arquivos alterados

- `front-end/src/constants/support.ts`
- `front-end/src/pages/Auth/SubscriptionGate/index.tsx`
- `front-end/src/pages/Auth/SubscriptionGate/styles.module.css`
- `front-end/src/pages/Auth/SubscriptionGate/index.test.tsx`
- `tasks/change-requests/811-botao-falar-com-suporte-assinatura-web.md`
- `tasks/slices/005-assinatura-liberacao-acesso.md`
- `tasks/000-index.md`

## Validacoes executadas

- Vitest `SubscriptionGate/index.test.tsx`: 5 passed
- Acessibilidade: CTA como `<a href="mailto:…">` focável, texto legível sem depender só do ícone, `focus-visible`

## Pendencias pos-task

- Nenhuma

## Status final

done

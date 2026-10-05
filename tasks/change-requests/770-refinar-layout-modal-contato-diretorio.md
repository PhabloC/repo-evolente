# Task 770 - Refinar layout do modal de contato do diretório

## Status

done

## Tipo

front

## Stacks envolvidos

- front-end

## Perfil do projeto

- stack web escolhida: front-end (React/Vite)
- mobile: sim

## Contrato

- Reaproveita `ProfessionalDirectoryItem` (sem mudança de API)

## Modo de execucao

single-stack

## Slice vertical

- Slice 067 — `tasks/slices/067-modal-contato-profissional-diretorio.md`

## Referencia de design system

- Stack de referência visual: front-end
- Tipo: UI existente do modal + pedido visual humano (print)
- Fonte primária: `front-end/src/pages/Main/Guardian/Professionals/`
- Lacuna: print mostra layout atual; pedido é refinar botões, ícone e densidade de informação

## Origem da solicitacao

Pedido humano: modal mais bonito; botões lado a lado; ícone do WhatsApp; mais informações do profissional.

## Comportamento esperado

- Modal exibe nome, avatar, tipo de atuação, especialidades, registro, cidade, clínica (quando houver) e telefone.
- Ações WhatsApp e Fechar na mesma linha.
- Botão WhatsApp usa o ícone da marca (SVG).
- Sem telefone: mensagem e só Fechar.

## Fora de escopo

- Mobile
- Alterar API/contrato
- Alterar cards da listagem

## Criterios de aceite

- [x] Modal mostra campos públicos disponíveis do profissional.
- [x] Botões WhatsApp e Fechar lado a lado no desktop/tablet.
- [x] Ícone do WhatsApp no CTA.
- [x] Teste da página cobre infos e link.
- [x] Lint/testes focados passam.

## Contexto mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`, `tasks/000-index.md`
- esta task, Slice 067, handoff 761

## Contexto sob demanda

| Gatilho | Fonte | Decisão | Obrigatório? |
|---|---|---|---|
| UI modal | Professionals page/styles | layout | sim |
| A11y | `front-end/docs/ai/ACCESSIBILITY.md` | botões/ícone | sim |

## Orçamento de contexto

- baixo

## Resultado da execucao

- Modal com avatar, badge de atuação, chips de especialidade e grade de detalhes.
- Ações WhatsApp (ícone da marca) e Fechar lado a lado.

## Contexto utilizado

- Página Professionals, styles, Modal/Button, ACCESSIBILITY.md.

## Handoff

- `.agents/state/handoffs/TASK-770.md`

## Arquivos alterados

- `front-end/src/components/WhatsAppIcon.tsx`
- `front-end/src/pages/Main/Guardian/Professionals/index.tsx(+test)`
- `front-end/src/pages/Main/Guardian/styles.module.css`

## Validacoes executadas

- vitest Professionals — 2 testes ok
- eslint arquivos do modal — ok

## Acessibilidade

- Ícone WhatsApp com `aria-hidden`.
- Labels de detalhe com ícones decorativos.
- Botões/link focáveis; Fechar permanece disponível.

## Pendencias pos-task

- Conferência visual no browser autenticado.

## Status final

done

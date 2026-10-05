# Task 768 - Filtro por área no diretório de profissionais (web)

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

- Depende da Task 767: `GET /professionals?specialty=`

## Modo de execucao

single-stack

## Slice vertical

- Slice 063 — `tasks/slices/063-diretorio-profissionais-responsavel-web.md`

## Referencia de design system

- Stack de referência visual: front-end
- Tipo: artefato de design system + UI existente do diretório
- Fonte primária: `design-system/front/Design_System_Evolente_Desktop.md`
- Fontes adjacentes: `front-end/src/pages/Main/Guardian/Professionals/`
- Lacuna: sem prints do filtro — reutilizar toolbar/tokens; não inventar linguagem visual nova

## Origem da solicitacao

Pedido humano: no diretório de profissionais, adicionar filtro pela área do profissional.

## Comportamento esperado

- Na página `/profissionais`, ao lado da busca, um seletor **Área** com opção “Todas as áreas” e áreas usuais (fonoaudiologia, psicologia, terapia ocupacional, fisioterapia, psicopedagogia).
- A seleção envia `specialty` na listagem; combina com a busca por nome.
- Empty state considera o filtro ativo.
- Campo com label visível e nome acessível.

## Fora de escopo

- Mobile
- API (Task 767)
- Cadastro de novas especialidades

## Criterios de aceite

- [x] Seletor de área visível na toolbar do diretório.
- [x] Hook/serviço envia `specialty` quando uma área está selecionada.
- [x] Empty/loading/erro continuam coerentes.
- [x] Teste da página cobre mudança do filtro.
- [x] Lint/testes focados passam.

## Contexto mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`, `tasks/000-index.md`
- esta task, Slice 063 e handoff da Task 767

## Contexto sob demanda

| Gatilho | Fonte | Decisão | Obrigatório? |
|---|---|---|---|
| UI diretório | `front-end/src/pages/Main/Guardian/Professionals/` | posicionar o select | sim |
| Hook/serviço | `useProfessionalsDirectory` + `professionalService` | query `specialty` | sim |
| A11y | `front-end/docs/ai/ACCESSIBILITY.md` | label do filtro | sim |

## Orçamento de contexto

- baixo

## Estratégia de redução

- Não reabrir Filhos, modal de WhatsApp nem cadastro profissional.

## Resultado da execucao

- Toolbar de `/profissionais` com Busca + Área; hook envia `specialty`.
- Empty state considera busca e área.

## Contexto utilizado

- Página Professionals, hook/serviço, ACCESSIBILITY.md (label visível).

## Handoff

- `.agents/state/handoffs/TASK-768.md`

## Arquivos alterados

- `front-end/src/constants/professionalAreas.ts`
- `front-end/src/types/professional.ts`
- `front-end/src/services/professionals/professionalService.ts`
- `front-end/src/hooks/useProfessionalsDirectory.ts`
- `front-end/src/pages/Main/Guardian/Professionals/index.tsx`
- `front-end/src/pages/Main/Guardian/Professionals/index.test.tsx`
- `front-end/src/pages/Main/Guardian/styles.module.css`

## Validacoes executadas

- `npx vitest run src/pages/Main/Guardian/Professionals/index.test.tsx --pool=threads` — 2 testes ok
- eslint nos arquivos da página/hook/serviço — ok

## Acessibilidade

- Select com `label` visível associado via `htmlFor`.
- Busca com `label` visível e `aria-label`.
- Empty state em texto, não só por ausência de cards.

## Pendencias pos-task

- Verificação visual autenticada no browser (depende de sessão do responsável).

## Status final

done

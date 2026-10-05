# Task 769 - Opções de área a partir das especialidades cadastradas

## Status

done

## Tipo

shared

## Stacks envolvidos

- contracts
- backend
- front-end

## Perfil do projeto

- stack web escolhida: front-end (React/Vite)
- mobile: sim

## Contrato

- `GET /professionals`
- `ProfessionalDirectoryListResponse.availableSpecialties`

## Modo de execucao

cross-stack

## Slice vertical

- Slice 063 — `tasks/slices/063-diretorio-profissionais-responsavel-web.md`

## Referencia de design system

- Stack de referência visual: front-end
- Tipo: UI existente do diretório
- Fonte primária: `front-end/src/pages/Main/Guardian/Professionals/`
- Lacuna: sem prints; manter o select atual, só mudar a origem das opções

## Origem da solicitacao

Pedido humano: o filtro de área deve vir das especialidades já cadastradas, não de lista fixa.

## Objetivo

O seletor de área em `/profissionais` lista somente especialidades de profissionais elegíveis no diretório.

## Dependências

- Task 767 e 768

## Comportamento esperado

- A listagem devolve `availableSpecialties`: valores únicos das especialidades dos profissionais ativos com acesso, **antes** dos filtros de busca/área (para o select não sumir ao filtrar).
- Deduplicação sem acento/caixa; ordenação pt-BR.
- O front remove o catálogo fixo e preenche o select com essa lista.
- Combina com a query `specialty` já existente.

## Fora de escopo

- Mobile
- Alterar o cadastro (especialidade continua texto livre)
- Enum rígido no contrato de registro

## Criterios de aceite

- [x] OpenAPI declara `availableSpecialties`.
- [x] Backend devolve especialidades únicas dos elegíveis.
- [x] Select da web usa essa lista.
- [x] Testes backend e da página cobrem o comportamento.
- [x] Lint/testes focados passam.

## Contexto mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`, `tasks/000-index.md`
- esta task, Slice 063, handoffs 767/768

## Contexto sob demanda

| Gatilho | Fonte | Decisão | Obrigatório? |
|---|---|---|---|
| Contrato | `contracts/openapi.yaml` (schema do diretório) | campo novo | sim |
| API | `professionals.service` | extração única | sim |
| UI | página Professionals + hook | opções do select | sim |
| A11y | `front-end/docs/ai/ACCESSIBILITY.md` | select com label | sim |

## Orçamento de contexto

- baixo

## Estratégia de redução

- Não reabrir cadastro profissional nem modal de WhatsApp.

## Resultado da execucao

- `GET /professionals` inclui `availableSpecialties` dos profissionais elegíveis, independente do filtro atual.
- O select de Área usa essa lista; catálogo fixo removido.

## Contexto utilizado

- OpenAPI do diretório, professionals.service, página/hook, ACCESSIBILITY.md.

## Handoff

- `.agents/state/handoffs/TASK-769.md`

## Arquivos alterados

- `contracts/openapi.yaml`
- `backend/src/modules/professionals/professionals.service.ts(+spec)`
- `backend/src/modules/professionals/utils/specialty-filter.util.ts(+spec)`
- `front-end/src/types/professional.ts`
- `front-end/src/hooks/useProfessionalsDirectory.ts`
- `front-end/src/pages/Main/Guardian/Professionals/index.tsx(+test)`
- removido `front-end/src/constants/professionalAreas.ts`

## Validacoes executadas

- jest professionals + specialty-filter — 12 testes ok
- vitest Professionals — 2 testes ok

## Acessibilidade

- Select continua com label visível “Área”.
- Opções anunciadas pelo texto cadastrado da especialidade.

## Pendencias pos-task

- Verificação visual autenticada no browser.

## Status final

done

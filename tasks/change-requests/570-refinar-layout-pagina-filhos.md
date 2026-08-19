# Task 570 - Refinar layout da página Filhos

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

Não se aplica.

## Modo de execucao

single-stack

## Slice vertical

### Identificador do slice

Slice 050 - Área web do responsável e cadastro de filhos

### Arquivo do slice

- `tasks/slices/050-area-web-responsavel-multiplos-filhos.md`

## Referencia de design system

- Stack de referência visual: front-end.
- Tipo: refinamento de layout solicitado pelo usuário.
- Fonte: página Filhos, estilos locais do responsável e componentes de cards existentes.

## Origem da solicitacao

Pedido humano: melhorar o layout da página Filhos, que possui muito espaço em branco sem conteúdo.

## Comportamento esperado

- Com filhos cadastrados, página apresenta contexto da família e perfis em composição mais preenchida e legível.
- CTA do header permanece o único acesso de cadastro nessa tela.
- Empty state e links aos perfis permanecem.

## Fora de escopo

- Alterar dados dos filhos, cadastro, dashboard ou APIs.

## Criterios de aceite

- [ ] Lista de filhos não fica visualmente isolada em uma grande área vazia.
- [ ] Cards continuam navegando ao perfil individual.
- [ ] Empty state e responsividade são preservados.
- [ ] Lint focado passa.

## Contexto mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`, `tasks/000-index.md`
- esta task, Slice 050 e `.agents/state/handoffs/TASK-569.md`

## Contexto sob demanda

| Gatilho | Fonte | Decisão | Obrigatório? |
|---|---|---|---|
| Estrutura | página Filhos e estilos locais | criar composição informativa sem duplicar CTA | sim |
| Componentes | Avatar e cards existentes | manter links e identidade dos filhos | sim |
| UI | `front-end/docs/ai/ACCESSIBILITY.md` | hierarquia semântica e foco | sim |

## Orçamento de contexto

- baixo
- estratégia de redução: restringir à página Filhos e estilos locais.

## Dependencias

- Task 569 - Reduzir espaço entre CTA e ícones do header (done)

## Resultado da execucao

A página Filhos ganhou um resumo da família com contagem de perfis, explicação do acesso individual e uma seção dedicada à listagem. Os cards ficam visualmente mais presentes, com altura mínima e feedback de hover, evitando que a tela pareça vazia mesmo com poucos filhos. O CTA continua exclusivamente no header e os cartões preservam seus links de perfil.

## Contexto utilizado

- Contexto mínimo: governança raiz, índice, esta task, Slice 050, handoff Task 569 e acessibilidade.
- Sob demanda: página Filhos, Avatar, estilos locais e estrutura dos cards.

## Handoff

`.agents/state/handoffs/TASK-570.md`

## Arquivos alterados

- `front-end/src/pages/Main/Guardian/Children/index.tsx`
- `front-end/src/pages/Main/Guardian/styles.module.css`
- esta task, Slice 050, índice e handoff da Task 570

## Validacoes executadas

- prettier: ok.
- eslint focado: ok.
- `git diff --check`: ok (somente avisos CRLF preexistentes).

## Pendencias pos-task

- Nenhuma.

## Status final

done

# Task 401 - Atualizar abas e objetivo da biblioteca web

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

nao se aplica

## Modo de execucao

single-stack

## Referencia de design system

### Stack de referencia visual

front-end

### Tipo de referencia visual

ajuste funcional orientado por referência enviada no chat

### Fonte primaria visual

- `design-system/front/Design_System_Evolente_Desktop.md`
- referência visual enviada no chat em 5 de agosto de 2026 para a seção `Conteúdos`

### Regra de aderencia visual

- preservar a estrutura atual da biblioteca web
- substituir as abas da seção `Conteúdos` pelas nove áreas informadas pelo usuário
- exibir o objetivo da aba ativa logo abaixo das tabs, sem abrir nova navegação ou modal

## Contexto de negocio

### Por que

A seção `Conteúdos` precisava refletir as áreas terapêuticas definidas pelo usuário, com leitura imediata do objetivo de cada aba.

### O que

Atualizar as tabs da biblioteca para `Articulação`, `Cognição`, `Atenção`, `Vocabulário`, `Leitura e Escrita`, `Frases`, `Socioemocionais`, `Fluência` e `Diálogo`, mostrando também a descrição da aba selecionada.

### Comportamento esperado

- a aba ativa começa em `Articulação`
- ao clicar em outra aba, a descrição abaixo das tabs troca junto com a seleção
- o acervo editorial exibido na biblioteca acompanha o agrupamento funcional da aba ativa

### Fora de escopo

- mudanças no backend ou no contrato de conteúdos
- criação de novas categorias persistidas na API
- alterações no modal de criação/edição de conteúdo

## Slice vertical

### Identificador do slice

Slice 017 - Redesign interface interna web

### Arquivo do slice

- `tasks/slices/017-redesign-interface-interna-web.md`

## Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/017-redesign-interface-interna-web.md`
- `.agents/state/handoffs/TASK-393.md`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| Ajuste das tabs | `front-end/src/pages/Main/Library/index.tsx` | trocar tabs, mapeamento e descrição da aba ativa | sim |
| Ajuste visual local | `front-end/src/pages/Main/Library/styles.module.css` | acomodar o bloco de objetivo abaixo das tabs | sim |
| Regressão da página | `front-end/src/pages/Main/Library/index.test.tsx` | validar troca de abas e descrição ativa | sim |
| Acessibilidade web | `front-end/docs/ai/ACCESSIBILITY.md` | manter semântica de tabs e painel ativo | sim |

## Orçamento de contexto

- baixo
- estrategia de reducao: limitar a execução à página `Library` e ao teste focado da própria página

## Criterios de conclusao

- [x] as tabs da seção `Conteúdos` usam exatamente as nove labels enviadas pelo usuário
- [x] a descrição da aba ativa aparece logo abaixo das tabs
- [x] a troca de aba atualiza a descrição renderizada
- [x] o teste focado da biblioteca cobre a troca de abas

## Dependencias

- Task 356
- Task 393

## Resultado da execucao

- a seção `Conteúdos` da biblioteca passou a renderizar as nove abas pedidas pelo usuário
- a aba ativa agora expõe um bloco textual com o objetivo correspondente
- a filtragem visível do acervo editorial foi ajustada por agrupamentos locais, sem exigir mudança de contrato na API
- o catálogo jogável permaneceu disponível no topo, preservando o comportamento já validado da página

## Contexto utilizado

### Mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`
- `tasks/000-index.md`, esta task, `tasks/slices/017-redesign-interface-interna-web.md`
- `.agents/state/handoffs/TASK-393.md`

### Sob demanda

- `front-end/src/pages/Main/Library/index.tsx`
- `front-end/src/pages/Main/Library/styles.module.css`
- `front-end/src/pages/Main/Library/index.test.tsx`
- `front-end/docs/ai/ACCESSIBILITY.md`

### Contexto evitado

- `backend/` por não haver alteração de API
- outras páginas do módulo `Main`

## Handoff

- `.agents/state/handoffs/TASK-401.md`

## Arquivos alterados

- `front-end/src/pages/Main/Library/index.tsx`
- `front-end/src/pages/Main/Library/styles.module.css`
- `front-end/src/pages/Main/Library/index.test.tsx`
- `tasks/change-requests/401-atualizar-abas-e-objetivo-da-biblioteca-web.md`
- `tasks/slices/017-redesign-interface-interna-web.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-401.md`

## Validacoes executadas

- `cd front-end && npm test -- --run src/pages/Main/Library/index.test.tsx` - ok

## Pendencias pos-task

- nenhuma

## Status final

done

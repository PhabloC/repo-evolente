# Task 166 - Acoes hover nos cards de jogo da biblioteca

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

- `contracts/openapi.yaml#/paths` contents

## Modo de execucao

single-stack

## Referencia de design system

### Stack de referencia visual

front-end

### Tipo de referencia visual

artefato de design system

### Fonte primaria visual

- `design-system/front/Design_System_Evolente_Desktop.md`

### Regra de aderencia visual

- Os cards de jogo devem continuar integrados à biblioteca atual, apenas com overlay de ações no hover.

## Contexto de negocio

### Por que

O master precisa gerenciar o jogo diretamente pelo card da biblioteca, sem depender da tabela inferior para encontrar ações.

### O que

Adicionar overlay escurecido com ações de visualizar, editar e inativar nos cards de jogo, usando ícones Lucide, e remover os jogos da tabela abaixo.

### Comportamento esperado

- Hover no card escurece o preview
- Aparecem ações por ícone: visualizar, editar e inativar/reativar
- Jogos deixam de aparecer na tabela abaixo
- Conteúdos não-jogo continuam na tabela

### Fora de escopo

- Mudanças no backend
- Novos jogos
- Mudanças na execução mobile

## Review da spec

- [x] Permissoes definidas ou `nao se aplica`
- [x] Casos de erro mapeados
- [x] Decisoes de negocio confirmadas como humanas
- [x] Criterios de aceite objetivos e verificaveis
- [x] Casos de borda considerados

### Evidencias da review

- Permissoes: master age no card; profissional segue leitura
- Casos de erro: card inativo; ação de visualizar; ausência de outros conteúdos na tabela
- Decisoes humanas confirmadas: ícones Lucide; overlay no hover; remover jogos da tabela
- Casos de borda: teclado/foco nos ícones; card em modo read-only

## Especificacao tecnica

### Deve

- escurecer o card no hover/focus
- mostrar ações com ícones Lucide
- suportar visualizar separado de editar
- remover itens `game` da tabela inferior

### Nao deve

- nao remover a seção de cards
- nao quebrar a edição já existente
- nao reintroduzir criação via UI

## Entradas

- `design-system/front/Design_System_Evolente_Desktop.md`
- `front-end/docs/ai/`

## Dependencias

- Task 165

## Slice vertical

### Identificador do slice

Slice 029 - Catalogo inicial de jogos terapeuticos

### Arquivo do slice

- `tasks/slices/029-catalogo-inicial-jogos-terapeuticos.md`

### Objetivo de negócio

Endurecer a gestão visual do primeiro jogo dentro da biblioteca.

### Entrega verificável do slice

Card do jogo com ações diretas no hover e tabela sem duplicação dos jogos.

### Fora do slice

- Backend e mobile

## Contexto mínimo

Sempre ler:

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/029-catalogo-inicial-jogos-terapeuticos.md`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| UI web | `design-system/front/Design_System_Evolente_Desktop.md` | card/overlay | sim |
| Front-end | `front-end/docs/ai/ARCHITECTURE.md e CODE_STYLE.md e ACCESSIBILITY.md` | implementação web | sim |

## Orçamento de contexto

- Risco baixo
- Estrategia de reducao: restringir a mudança à rota `/biblioteca` e aos testes dessa página

## Criterios de conclusao

- Hover/focus exibe overlay e ações por ícone
- Visualizar e editar funcionam
- Jogos não aparecem mais na tabela inferior
- Testes da biblioteca atualizados e passando

## Instrucoes de implementacao

- Preferir ação de visualizar em modal read-only reaproveitando o modal atual
- Garantir acessibilidade de teclado para os ícones

## Validacao esperada

- `npm run lint`
- `npm run build`
- `npx vitest run src/pages/Main/Library/index.test.tsx`

## Entregaveis esperados

- overlay de ações nos cards de jogo
- modo de visualização read-only
- tabela sem itens de jogo

## Riscos ou ambiguidades

- o ícone de inativar pode ser reaproveitado também para reativar, desde que o nome acessível reflita a ação real

## Execucao

- overlay escurecido aplicado aos cards de jogo do master com ações por ícone via Lucide
- modal atual reaproveitado em dois modos: visualização read-only e edição
- tabela inferior ajustada para exibir apenas conteúdos não-jogo
- testes da biblioteca alinhados ao comportamento novo dos cards e do modal

## Validacao executada

- `npm run lint` — ok
- `npm run build` — ok
- `npx vitest run src/pages/Main/Library/index.test.tsx` — ok

# Task 164 - Remover criacao de conteudo na biblioteca web

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

- A biblioteca deve continuar no padrão visual atual, apenas sem CTA e fluxo de criação.

## Contexto de negocio

### Por que

A criação de jogos e conteúdos passará a ser feita diretamente no código, então a biblioteca do master não deve mais expor o fluxo de “Novo conteúdo”.

### O que

Remover da biblioteca web a função de criação de conteúdo, preservando listagem, edição e ativação/inativação do catálogo pelo master.

### Comportamento esperado

- O botão “Novo conteúdo” deixa de existir
- O modal de criação deixa de estar acessível pela UI
- O master continua podendo editar e inativar/ativar conteúdos existentes
- O profissional continua em modo leitura

### Fora de escopo

- Mudanças no backend
- Mudanças no contrato
- Execução mobile dos jogos
- Nova ferramenta de autoria fora da biblioteca

## Review da spec

- [x] Permissoes definidas ou `nao se aplica`
- [x] Casos de erro mapeados
- [x] Decisoes de negocio confirmadas como humanas
- [x] Criterios de aceite objetivos e verificaveis
- [x] Casos de borda considerados

### Evidencias da review

- Permissoes: master ainda muta itens existentes; profissional segue read-only
- Casos de erro: biblioteca vazia; edição de conteúdo existente; item inativo
- Decisoes humanas confirmadas: criação de jogos/conteúdos sai da UI e vai para código
- Casos de borda: não sobrar caminho residual de create no modal/estado

## Especificacao tecnica

### Deve

- remover CTA de criação da tela `/biblioteca`
- remover da page o fluxo de `createContent`
- manter edição e toggle de status funcionando

### Nao deve

- nao quebrar leitura do profissional
- nao remover edição do master
- nao alterar payloads ou contratos da API

## Entradas

- `design-system/front/Design_System_Evolente_Desktop.md`
- `front-end/docs/ai/`
- `contracts/openapi.yaml`

## Dependencias

- Task 015
- Task 157

## Slice vertical

### Identificador do slice

Slice 006 - Catalogo

### Arquivo do slice

- `tasks/slices/006-catalogo-conteudos-master.md`

### Objetivo de negócio

Ajustar o catálogo master ao novo fluxo editorial sem remover gestão dos itens existentes.

### Entrega verificável do slice

Biblioteca web sem criação via UI, mantendo edição e status.

### Fora do slice

- Mobile

## Contexto mínimo

Sempre ler:

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/006-catalogo-conteudos-master.md`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| UI web | `design-system/front/Design_System_Evolente_Desktop.md` | preservar biblioteca | sim |
| Front-end | `front-end/docs/ai/ARCHITECTURE.md e CODE_STYLE.md e ACCESSIBILITY.md` | implementação web | sim |
| API | `contracts/openapi.yaml` | confirmar que a mudança é só de UI | sim |

## Orçamento de contexto

- Risco baixo
- Estrategia de reducao: limitar a mudança à rota `/biblioteca` e aos testes dessa página

## Criterios de conclusao

- CTA “Novo conteúdo” removido da biblioteca
- Fluxo de criação não mais acessível pela tela
- Edição e status continuam funcionando
- Testes atualizados e passando

## Instrucoes de implementacao

- Preferir remoção do fluxo na page antes de refatorar estruturas compartilhadas
- Manter o modal apenas no papel ainda necessário para edição

## Validacao esperada

- `npm run lint`
- `npm run test`
- `npm run build`

## Entregaveis esperados

- ajustes na página da biblioteca
- testes da biblioteca atualizados

## Riscos ou ambiguidades

- a service `createContent` pode continuar existindo fora da UI; isso só deve ser removido se ficar realmente órfão ou conflitar com lint

## Resultado da execucao

### Resumo por stack

- **front-end**: a biblioteca do master deixou de expor o CTA e o fluxo de criação de conteúdo; a rota `/biblioteca` agora permite apenas listar, editar e inativar/reativar conteúdos existentes.

### Relação com o slice

- Slice 006 permaneceu concluído, agora ajustado ao novo fluxo editorial em que a criação de conteúdos/jogos acontece em código, não pela UI da biblioteca.

### Decisões técnicas

- Remoção do botão `Novo conteúdo` da `LibraryPage`.
- Remoção da branch de `createContent` e do estado de `create` na page.
- Simplificação do `ContentFormModal` para papel exclusivo de edição.
- Preservação de `updateContent` e `uploadContentMedia` para itens já existentes.

### Trade-offs

- A função `createContent` continua disponível no service porque a task exigia apenas remover o fluxo da UI; não houve limpeza além do escopo necessário.
- O modal continua existindo, mas agora só abre para editar conteúdo existente.

### Contrato

- Sem alterações no `contracts/openapi.yaml`; a mudança é exclusivamente de interface.

## Contexto utilizado

### Contexto mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`
- `tasks/000-index.md`, esta task, `tasks/slices/006-catalogo-conteudos-master.md`
- `.agents/state/handoffs/TASK-015.md`
- `.agents/state/handoffs/TASK-157.md`

### Contexto sob demanda

| Fonte | Gatilho | Uso |
|---|---|---|
| `design-system/front/Design_System_Evolente_Desktop.md` | UI web | preservar layout, tabela, filtros e ações da biblioteca |
| `front-end/docs/ai/ARCHITECTURE.md`, `CODE_STYLE.md`, `ACCESSIBILITY.md` | implementação web | manter organização e acessibilidade da tela |
| `contracts/openapi.yaml` | API | confirmar que a mudança não exigia alteração de contrato |

### Contexto evitado

- `design-system/mobile/`, `mobile/docs/ai/` e `backend/docs/ai/` não foram carregados porque a task é single-stack front-end.

## Handoff

- Caminho: `.agents/state/handoffs/TASK-164.md`
- Próximo contexto recomendado: reutilizar a task 164 e o handoff se a biblioteca ganhar nova política editorial ou nova UI de gestão.

## Arquivos alterados

### Front-end

- `front-end/src/pages/Main/Library/index.tsx`
- `front-end/src/pages/Main/Library/ContentFormModal.tsx`
- `front-end/src/pages/Main/Library/index.test.tsx`

### Governança

- `tasks/change-requests/164-remover-criacao-de-conteudo-na-biblioteca-web.md`
- `tasks/slices/006-catalogo-conteudos-master.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-164.md`

## Validacoes executadas

- `cd front-end && npm run lint` — ok
- `cd front-end && npm run build` — ok
- `cd front-end && npx vitest run src/pages/Main/Library/index.test.tsx` — ok
- `cd front-end && npm run test` — **falhou por timeout pré-existente fora do escopo** em `src/pages/Auth/RegisterProfessional/index.test.tsx` (`renders stepped flow and clinic fields on atuação step`) na sexta-feira, 24 de julho de 2026

## Aderencia ao design system

- A biblioteca manteve o mesmo padrão de filtros no topo, tabela/lista limpa e ações no fim; apenas o CTA de criação foi removido.

## Acessibilidade aplicada

- A remoção do CTA não afetou a semântica da tela.
- O modal de edição manteve labels, erro textual e controles acionáveis por teclado.
- O feedback de sucesso/erro da biblioteca foi preservado.

## Pendencias pos-task

- Nenhuma bloqueante para a biblioteca.
- Se o produto quiser remover também a capacidade de criação por outras superfícies, isso deve virar nova task.
- A suite completa do `front-end` ainda tem falha pré-existente em `RegisterProfessional`, fora deste escopo.

## Status final

done

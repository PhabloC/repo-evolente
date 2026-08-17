# Task 326 - Excluir conteúdos da biblioteca master

## Status

done

## Tipo

shared

## Stacks envolvidos

- front-end
- backend

## Perfil do projeto

- stack web escolhida: front-end (React/Vite)
- mobile: sim

## Contrato

- `contracts/openapi.yaml#/paths/~1contents~1{contentId}`

## Modo de execucao

cross-stack

## Referencia de design system

### Stack de referencia visual

front-end

### Tipo de referencia visual

artefato de design system

### Fonte primaria visual

- `design-system/front/Design_System_Evolente_Desktop.md`

### Regra de aderencia visual

- A tabela da biblioteca deve expor a lixeira como ação destrutiva compacta, com confirmação explícita em modal.

## Contexto de negocio

### Por que

O master precisa excluir conteúdos do catálogo diretamente pela biblioteca.

### O que

Adicionar exclusão real de conteúdos no catálogo web, com lixeira na tabela, modal de confirmação e endpoint dedicado no backend.

### Comportamento esperado

- o master vê ação de excluir por ícone de lixeira
- a exclusão exige confirmação explícita
- o backend remove o conteúdo e a mídia do storage
- conteúdos já usados em trilhas ou evolução não podem ser excluídos

### Fora de escopo

- exclusão em lote
- restauração após exclusão
- mudanças mobile

## Review da spec

- [x] Permissoes definidas ou `nao se aplica`
- [x] Casos de erro mapeados
- [x] Decisoes de negocio confirmadas como humanas
- [x] Criterios de aceite objetivos e verificaveis
- [x] Casos de borda considerados

### Evidencias da review

- Permissões: apenas `master` pode excluir
- Casos de erro: conteúdo inexistente, conteúdo em uso, falha ao remover mídia
- Decisão humana confirmada: esta CR reabre a regra anterior de “inativar, não excluir”
- Casos de borda: item com mídia no bucket e item já referenciado por trilha/evolução

## Especificacao tecnica

### Deve

- adicionar `DELETE /contents/{id}` no contrato e backend
- remover mídia do storage quando existir
- impedir exclusão de conteúdo em uso por trilhas ou evolução
- adicionar ação de lixeira na tabela da biblioteca
- confirmar exclusão em modal destrutivo

### Nao deve

- nao excluir conteúdo em uso
- nao quebrar o fluxo existente de edição e inativação
- nao apagar mídia sem remover o registro correspondente

## Entradas

- `contracts/openapi.yaml`
- `front-end/src/pages/Main/Library/`
- `backend/src/modules/contents/`

## Dependencias

- Task 324
- Task 325
- Task 159
- Task 160

## Slice vertical

### Identificador do slice

Slice 006 - Catalogo

### Arquivo do slice

- `tasks/slices/006-catalogo-conteudos-master.md`

### Objetivo de negocio

Permitir limpeza real do catálogo pelo master sem corromper conteúdos já usados no produto.

### Entrega verificavel do slice

Master exclui conteúdo não utilizado pela biblioteca web; itens em uso são bloqueados com mensagem clara.

### Fora do slice

- Mobile

## Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/006-catalogo-conteudos-master.md`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| UI web | `front-end/docs/ai/ACCESSIBILITY.md e CODE_STYLE.md` | modal e ações icon-only | sim |
| API | `contracts/openapi.yaml` | novo delete de contents | sim |
| Backend | `backend/src/modules/contents/` | regra de exclusão e storage | sim |

## Orçamento de contexto

- Risco médio
- Estratégia de redução: limitar a mudança ao módulo de contents e à biblioteca web, com checagem de uso apenas em trilhas/evolução

## Criterios de conclusao

- lixeira disponível na tabela da biblioteca
- modal confirma exclusão
- conteúdo sem uso é excluído
- conteúdo em uso é bloqueado com erro claro
- testes do backend e da biblioteca cobrindo o fluxo

## Validacao esperada

- `cd backend && npm run test -- contents.service.spec.ts`
- `cd front-end && npx vitest run src/pages/Main/Library/index.test.tsx`

## Entregaveis esperados

- contrato atualizado
- endpoint de exclusão
- ação de lixeira na biblioteca
- testes atualizados

## Resultado da execucao

### Resumo por stack

- **backend**: o módulo de conteúdos ganhou `DELETE /contents/{id}`, remove a mídia do storage quando existir e bloqueia exclusão de conteúdo já usado em trilhas ou no histórico de evolução.
- **front-end**: a tabela da biblioteca ganhou lixeira icon-only com confirmação explícita em modal destrutivo.

### Relação com o slice

- O Slice 006 passou a permitir exclusão real de conteúdos pelo master, substituindo a restrição anterior de apenas inativar, com trava de segurança para itens em uso.

### Decisões técnicas

- A exclusão só é permitida para `master`.
- O backend conta referências em `trail_items` e `evolution_records` antes de excluir.
- Se houver mídia associada, o arquivo é removido do storage antes do delete do registro.
- A lixeira da tabela reutiliza o padrão de modal destrutivo já adotado em relatórios.

### Trade-offs

- O bloqueio de exclusão ficou restrito a trilhas e evolução, que são os vínculos operacionais críticos do catálogo nesta fase.
- Não houve restauração, soft delete separado nem exclusão em lote.

### Contrato

- Novo endpoint: `DELETE /contents/{contentId}` com `204` em sucesso e `400` para conteúdo em uso.

## Contexto utilizado

### Contexto mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`
- `tasks/000-index.md`, esta task e `tasks/slices/006-catalogo-conteudos-master.md`

### Contexto sob demanda

| Fonte | Gatilho | Uso |
|---|---|---|
| `contracts/openapi.yaml` | novo delete de contents | contrato da exclusão |
| `backend/src/modules/contents/` | regra de negócio | endpoint, service, repository e testes |
| `front-end/src/pages/Main/Library/` | UI web | lixeira na tabela, modal e teste |
| `front-end/docs/ai/ACCESSIBILITY.md` | modal/ícones | nomes acessíveis e confirmação explícita |

### Contexto evitado

- `mobile/` e outras áreas do backend não envolvidas diretamente no catálogo

## Handoff

- Caminho: `.agents/state/handoffs/TASK-326.md`
- Próximo contexto recomendado: reutilizar esta task se o produto pedir restauração, exclusão em lote ou bloqueios adicionais por dependências futuras.

## Arquivos alterados

### Backend

- `backend/src/modules/contents/contents.controller.ts`
- `backend/src/modules/contents/contents.repository.ts`
- `backend/src/modules/contents/contents.in-memory.repository.ts`
- `backend/src/modules/contents/contents.typeorm.repository.ts`
- `backend/src/modules/contents/contents.service.ts`
- `backend/src/modules/contents/contents.service.spec.ts`

### Front-end

- `front-end/src/services/contents/contentService.ts`
- `front-end/src/pages/Main/Library/index.tsx`
- `front-end/src/pages/Main/Library/styles.module.css`
- `front-end/src/pages/Main/Library/index.test.tsx`

### Governança

- `contracts/openapi.yaml`
- `tasks/change-requests/326-excluir-conteudos-da-biblioteca-master.md`
- `tasks/slices/006-catalogo-conteudos-master.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-326.md`

## Validacoes executadas

- `cd backend && npm run test -- contents.service.spec.ts` — ok em **quarta-feira, 29 de julho de 2026**
- `cd front-end && npx vitest run src/pages/Main/Library/index.test.tsx` — ok em **quarta-feira, 29 de julho de 2026**

## Acessibilidade aplicada

- A lixeira usa `button` semântico com `aria-label`.
- O modal destrutivo mantém ações claras de cancelar e confirmar exclusão.
- O fluxo de confirmação continua acionável por teclado.

## Pendencias pos-task

- Se o produto quiser restaurar conteúdo excluído, isso exige nova task e política de retenção.
- Se surgirem novas dependências do catálogo fora de trilhas/evolução, o bloqueio de exclusão deve ser ampliado.

## Status final

done

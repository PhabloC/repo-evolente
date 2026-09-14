## Status

done

## Título

Remover margem lateral das capas nos cards de atividades mobile

## Tipo

mobile

## Stacks envolvidos

- mobile

## Perfil do projeto

- stack web escolhida: front-end (React/Vite)
- mobile: sim

## Contrato

Não se aplica.

## Modo de execução

single-stack

## Slice vertical

`tasks/slices/047-trilha-self-serve-responsavel-mobile.md`

## Objetivo

Fazer a capa ocupar toda a largura visual do topo do card de atividade na Biblioteca mobile, eliminando a sobra lateral observada.

## Entrega verificável

A imagem da capa encosta nas laterais internas do card, preservando o conteúdo textual e as ações existentes.

## Fora de escopo

- Alterar dados, navegação ou permissões da Biblioteca.
- Alterar o layout de outras telas ou cards.

## Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- `tasks/slices/047-trilha-self-serve-responsavel-mobile.md`
- `mobile/src/features/trail/screens/TrailLibraryPane.tsx`
- `mobile/src/features/trail/screens/styles.ts`
- `mobile/src/features/admin/contents/components/ContentCoverThumb/styles.ts`

## Contexto sob demanda

- `design-system/mobile/Design_System_Evolente_App_Mobile.md`: validar preservação do padrão visual mobile.
- `mobile/src/features/admin/contents/components/ContentCoverThumb/index.tsx`: confirmar o comportamento de largura da imagem.

## Orçamento de contexto

Baixo; carregar somente os arquivos do card e validação focada da stack mobile.

## Dependências

- Slice 047 concluído.

## Status final

done

## Resultado da execucao

A capa dos cards da Biblioteca mobile passou a remover o padding interno de 4px do componente compartilhado, encostando nas laterais sem alterar o corpo textual nem as ações.

## Contexto utilizado

- Contexto mínimo: task 680, Slice 047 e índice do backlog.
- Contexto sob demanda: `mobile/src/features/trail/screens/styles.ts` e `ContentCoverThumb`.

## Handoff

Refinamento visual concluído na capa dos cards da Biblioteca. Retomar por `mobile/src/features/trail/screens/styles.ts` caso seja necessário validar outros breakpoints.

## Arquivos alterados

- `mobile/src/features/trail/screens/styles.ts`
- `mobile/src/features/admin/contents/components/ContentCoverThumb/styles.ts`
- `tasks/change-requests/680-remover-margem-lateral-capas-cards-mobile.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-680.md`

## Validacoes executadas

- `cd mobile && npm run typecheck` — falhou por erros preexistentes em arquivos administrativos, autenticação, jogos e tipos compartilhados; nenhuma ocorrência aponta para a alteração de margem.

## Pendencias pos-task

- Corrigir os erros globais preexistentes do typecheck em tasks separadas.

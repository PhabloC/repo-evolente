# Task 382 - Propagar description do conteúdo para o vídeo mobile

## Status

done

## Tipo

mobile

## Stacks envolvidos

- mobile

## Perfil do projeto

- stack web escolhida: front-end (React/Vite)
- mobile: sim

## Contrato

não se aplica

## Modo de execução

single-stack

## Slice vertical

- Slice 008 - Trilhas semanais e evolução
- `tasks/slices/008-trilhas-semanais-evolucao.md`

## Referência visual

- mobile; card de detalhes do vídeo já existente e correção funcional pedida na conversa

## Objetivo

Usar a descrição real do conteúdo no card de vídeo, propagando o campo `description` já existente na origem dos dados para o modelo mobile da trilha.

## Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/008-trilhas-semanais-evolucao.md`
- `.agents/state/handoffs/TASK-381.md`

## Contexto sob demanda

| Gatilho | Fonte | Uso | Obrigatório? |
|---|---|---|---|
| Modelo mobile | `mobile/src/features/trail/types/trail.ts`, `mobile/src/features/trail/adapters/adaptDayTrail.ts` | adicionar e adaptar `description` | sim |
| Fonte de dados mobile | `mobile/src/features/trail/services/trailService.ts` | alinhar demos e leitura local com o novo campo | sim |
| UI mobile | `mobile/src/features/trail/screens/TrailActivityScreen.tsx` | usar a descrição correta no card de vídeo | sim |

## Orçamento de contexto

- baixo
- estratégia: alteração concentrada no modelo/adapter/service/screen do fluxo de trilha mobile

## Critérios de conclusão

- [x] descrição do vídeo usa `content.description` quando disponível
- [x] objetivo continua usando `therapeuticObjective`
- [x] `npm run typecheck` segue sem diagnósticos

## Resultado da execucao

- o modelo mobile da trilha passou a aceitar e adaptar o campo `description` do conteúdo
- o card de vídeo agora usa `content.description` e só cai para `title` quando a descrição não vier preenchida
- os dados demo do vídeo `Bico de Peixe` foram alinhados com a descrição e o objetivo corretos
- a tipagem foi mantida compatível com fixtures antigos do mobile, deixando `description` opcional no tipo e normalizando para `null` no adapter

## Contexto utilizado

- contexto mínimo: `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`, `tasks/000-index.md`, esta task, Slice 008 e handoff `TASK-381`
- contexto sob demanda: `mobile/src/features/trail/types/trail.ts`, `mobile/src/features/trail/adapters/adaptDayTrail.ts`, `mobile/src/features/trail/services/trailService.ts`, `mobile/src/features/trail/screens/TrailActivityScreen.tsx`
- referência adicional de consistência: busca local mostrou que backend e web já expõem `description` no domínio de conteúdos
- contexto evitado: alterações no backend e na web, porque a correção necessária estava apenas no consumo mobile

## Handoff

- `.agents/state/handoffs/TASK-382.md`

## Arquivos alterados

- `mobile/src/features/trail/types/trail.ts`
- `mobile/src/features/trail/adapters/adaptDayTrail.ts`
- `mobile/src/features/trail/services/trailService.ts`
- `mobile/src/features/trail/screens/TrailActivityScreen.tsx`
- esta task, slice, índice e handoff

## Validacoes executadas

- `cd mobile && npm run typecheck` — executado sem diagnósticos

## Pendencias pos-task

- nenhuma

## Status final

done

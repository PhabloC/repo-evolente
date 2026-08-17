# Task 460 - Melhorar prévia sem capa no modal Nova atividade

## Status

done

## Tipo

front

## Stacks envolvidos

- front-end

## Contrato

- nao se aplica; apenas copy/visual da prévia lateral

## Modo de execucao

single-stack

## Slice vertical

- `tasks/slices/006-catalogo-conteudos-master.md`

## Referencia visual

- Stack de referência visual: front-end
- print do estado vazio da capa no chat (modal Nova atividade)
- fonte primaria documental: `design-system/front/Design_System_Evolente_Desktop.md` (biblioteca), sob demanda

## Contexto mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`
- `tasks/000-index.md`
- este arquivo
- `tasks/slices/006-catalogo-conteudos-master.md`
- handoff `TASK-459` (layout atual do modal)

## Contexto sob demanda

- `front-end/src/pages/Main/Library/ContentFormModal.tsx` — bloco `contentEditCoverFallback`
- `front-end/src/pages/Main/Library/styles.module.css` — classes da capa
- `front-end/docs/ai/ACCESSIBILITY.md` — checklist mínimo de UI
- `design-system/front/Design_System_Evolente_Desktop.md` — somente se precisar alinhar tom visual

## Orçamento de contexto

- baixo; alteração local de empty state
- estratégia de redução: não carregar backend, mobile, openapi nem requirements

## Objetivo

Substituir o empty state "Sem capa ainda" da prévia lateral do modal de nova/edição de atividade por conteúdo mais claro e útil, alinhado ao fato de que áudio/vídeo não têm capa própria na biblioteca.

## Criterios de conclusao

- [x] copy deixa de sugerir capa pendente/faltando para áudio/vídeo
- [x] hierarquia visual da prévia vazia melhorada (ícone + título + apoio)
- [x] texto varia por tipo de mídia (áudio/vídeo/jogo)
- [x] fluxo create/edit/view e upload de arquivo preservados

## Dependencias

- Task 459 (layout do modal) — done

## Resultado da execucao

- Empty state passa a ser prévia tipada (`Atividade de áudio` / `Atividade de vídeo` / nome do jogo)
- Hint explicando que a biblioteca usa o tipo da mídia (áudio/vídeo) ou prévia ilustrada (jogo)
- Ícone em badge + título + apoio; `aria-label` no bloco decorativo

## Contexto utilizado

- contexto mínimo da task
- `ContentFormModal.tsx` + CSS da capa
- `ACCESSIBILITY.md` (alt decorativo, aria-label, aria-hidden no ícone)
- DS documental não carregado (ajuste local de copy/hierarquia)

## Handoff

- `.agents/state/handoffs/TASK-460.md`

## Arquivos alterados

- `front-end/src/pages/Main/Library/ContentFormModal.tsx`
- `front-end/src/pages/Main/Library/styles.module.css`
- `tasks/change-requests/460-melhorar-previa-capa-modal-nova-atividade.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-460.md`

## Validacoes executadas

- revisão visual do markup/CSS do fallback
- acessibilidade: texto não depende só do ícone; `role="img"` + `aria-label`

## Pendencias pos-task

- nenhuma

## Status final

done

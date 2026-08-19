# Task 573 - Remover card de acesso à plataforma do perfil do responsável

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

- não aplicável; alteração local de interface.

## Modo de execucao

single-stack

## Slice vertical

- Slice 050 — `tasks/slices/050-area-web-responsavel-multiplos-filhos.md`

## Referência visual

- tipo: solicitação visual do usuário (cartão anexado nesta conversa).
- escopo: remover somente o cartão “Acesso à plataforma” da página de perfil/configurações do responsável.

## Contexto mínimo

- Governança raiz, índice, esta task, Slice 050 e handoff Task 572.

## Contexto sob demanda

- `front-end/src/pages/Main/Settings/index.tsx` para remover o cartão alvo;
- `front-end/src/pages/Main/Settings/index.test.tsx`, se existir, para adequar a cobertura;
- `front-end/docs/ai/ACCESSIBILITY.md` para preservar a semântica após remover conteúdo.

## Orçamento de contexto

- baixo; limitar ao componente de configurações e ao teste focado.

## Estratégia de redução

- não alterar a rota de download, o perfil profissional ou qualquer outro card das configurações.

## Dependências

- Task 572 (done)

## Resultado da execucao

- Removido o cartão “Acesso à plataforma” do perfil/configurações, incluindo o texto de acompanhamento e o link de download do aplicativo.
- O status de acesso, os dados cadastrais, a assinatura e a rota de download permanecem inalterados.

## Contexto utilizado

- `front-end/src/pages/Main/Settings/index.tsx`
- `front-end/src/pages/Main/Settings/styles.module.css`
- `front-end/docs/ai/ACCESSIBILITY.md`

## Handoff

- `.agents/state/handoffs/TASK-573.md`

## Arquivos alterados

- `front-end/src/pages/Main/Settings/index.tsx`
- `front-end/src/pages/Main/Settings/styles.module.css`
- Rastreabilidade da task, Slice 050, índice e handoff.

## Validacoes executadas

- `npx eslint src/pages/Main/Settings/index.tsx --max-warnings=0` — ok.
- `git diff --check` — ok.
- Não há teste focado para este módulo.

## Pendencias pos-task

- Nenhuma.

## Status final

done

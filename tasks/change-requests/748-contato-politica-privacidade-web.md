# Task 748 - Contato na política de privacidade web

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

## Modo de execução

single-stack

## Slice vertical

- Slice 062 — `tasks/slices/062-contato-politica-privacidade-web.md`

## Objetivo

Publicar e-mail e celular de contato na política de privacidade web.

## Dependências

Nenhuma.

## Contexto mínimo

- esta task
- `front-end/src/pages/Public/PrivacyPolicy/content.ts`
- `front-end/src/pages/Public/PrivacyPolicy/index.tsx`
- `front-end/src/pages/Public/PrivacyPolicy/styles.module.css`

## Contexto sob demanda

| Gatilho | Fonte | Uso |
|---|---|---|
| Links e foco | `front-end/docs/ai/ACCESSIBILITY.md` | manter nome acessível e foco visível nos contatos |

## Orçamento de contexto

- baixo
- estratégia: alterar só a página pública de privacidade.

## Critérios de aceite

- [x] A seção “Como solicitar” lista o e-mail taliviasilva@gmail.com.
- [x] A mesma seção lista o celular (38) 98405-8324.
- [x] Os dois canais são links (e-mail e ligação).
- [x] A data da política passa para 29 de setembro de 2026.

## Fora de escopo

- app mobile
- formulário de pedido de privacidade

## Resultado da execucao

A seção 11 passa a oferecer e-mail e celular clicáveis. A data no topo da política foi atualizada para 29 de setembro de 2026. O celular informado como 38-984058324 aparece como (38) 98405-8324.

## Contexto utilizado

- contexto mínimo da task
- trechos de links e foco em `front-end/docs/ai/ACCESSIBILITY.md`

## Handoff

- `.agents/state/handoffs/TASK-748.md`

## Arquivos alterados

- `front-end/src/pages/Public/PrivacyPolicy/content.ts`
- `front-end/src/pages/Public/PrivacyPolicy/index.tsx`
- `front-end/src/pages/Public/PrivacyPolicy/styles.module.css`
- `tasks/slices/062-contato-politica-privacidade-web.md`
- `tasks/000-index.md`

## Validacoes executadas

- revisão da página `/politica-de-privacidade` no navegador, incluindo os links de e-mail e telefone

## Pendencias pos-task

- nenhuma

## Status final

done

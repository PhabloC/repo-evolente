# Task 139 - Aplicar selo com icone nos heroes mobile

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

- nao se aplica

## Modo de execucao

single-stack

## Slice vertical

- Slice 022 - Linguagem visual do print aplicada as telas mobile
- `tasks/slices/022-linguagem-visual-print-telas-mobile.md`

## Referencia de design system

### Stack de referencia visual

mobile

### Tipo de referencia visual

print enviado em conversa

### Fonte primaria visual

- referencia visual do selo no hero com icone e label em caps

## Restricao explicita do usuario

- Aplicar o selo no formato do print e repetir o padrao nas outras paginas
- Na pagina de atividades, usar icone de estrela

## Objetivo

Substituir o texto solto do eyebrow dos heroes por um selo visual com icone, mantendo coerencia entre home, atividades, perfil e avisos.

## Contexto minimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- `tasks/change-requests/139-aplicar-selo-com-icone-nos-heroes-mobile.md`
- `tasks/slices/022-linguagem-visual-print-telas-mobile.md`
- `.agents/state/handoffs/TASK-138.md`

## Contexto sob demanda

- `mobile/src/shared/components/`
- heroes em `mobile/src/features/shell/` e `mobile/src/features/trail/`

## Orcamento de contexto

- ~8 fontes
- estrategia de reducao: criar um componente compartilhado e aplicar apenas nos heroes existentes

## Criterios de aceite

- Os heroes usam selo com icone no lugar do eyebrow em texto simples
- O padrao visual fica consistente entre as paginas
- As telas de atividades usam icone de estrela no selo

## Fora de escopo

- Alterar copy principal dos heroes
- Mudar layout dos cards fora da faixa do selo

## Dependencias

- Task 138

## Validacao esperada

- `npm run lint`
- `npm run typecheck`
- `npm run test`

## Resultado da execucao

- Foi criado um componente compartilhado de selo para os heroes com fundo translúcido, icone e label uppercase
- Home, perfil, avisos e as duas telas de atividades passaram a usar o mesmo padrao
- As telas de atividades receberam icone de estrela conforme solicitado

## Handoff

- `.agents/state/handoffs/TASK-139.md`

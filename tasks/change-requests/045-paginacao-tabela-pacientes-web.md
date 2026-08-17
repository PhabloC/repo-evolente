# Task 045 - Paginação na tabela de pacientes web

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

- nao se aplica; usar os dados ja retornados pela listagem atual sem alterar API

## Modo de execucao

single-stack

## Slice vertical

- Slice 007 - Gestao de pacientes do profissional
- `tasks/slices/007-gestao-pacientes-profissional.md`

## Referencia visual

### Tipo

ajuste incremental solicitado no chat

### Cobertura

- rodape da tabela com controles de pagina
- manutencao do visual atual da tela de pacientes

### Lacunas

- sem print dedicado para paginação
- decisao: aplicar paginação discreta e coerente com os botões e filtros já refinados na tela

## Objetivo

Adicionar paginação na tabela da página de pacientes para reduzir densidade visual e melhorar navegação em listas maiores.

## Contexto mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`, `tasks/000-index.md`
- esta task, Slice 007 e `.agents/state/handoffs/TASK-044.md`

## Contexto sob demanda

- `front-end/docs/ai/AGENTS.md`
- `front-end/docs/ai/ACCESSIBILITY.md`
- `front-end/src/pages/Main/Patients/{index.tsx,index.test.tsx,styles.module.css}`
- `front-end/src/ui/Table/index.tsx`
- `front-end/src/types/{patient.ts,guardian.ts}`

## Orçamento de contexto

- baixo; limitado à listagem web de pacientes e ao componente de tabela usado por ela

## Criterios de conclusao

- [x] tabela de pacientes exibe paginação funcional no front-end
- [x] troca de busca ou filtro reseta para a primeira página
- [x] pagina atual permanece válida quando o total de resultados muda
- [x] controles são acionáveis por teclado e com estado atual visível
- [x] lint e testes da tela aprovados

## Resultado da execucao

- a listagem de pacientes passou a paginar localmente em lotes de 10 itens
- o rodape da tabela ganhou resumo de faixa exibida e botões de navegação por página
- a tabela compartilhada recebeu `className` opcional para permitir customização local sem afetar outros módulos
- a página ganhou teste cobrindo a troca entre páginas

## Contexto utilizado

- fontes globais, Slice 007, handoff 044, docs locais de front/acessibilidade, tipos de paciente/guardian, página de pacientes e `ui/Table`

## Handoff

- `.agents/state/handoffs/TASK-045.md`

## Arquivos alterados

- `front-end/src/pages/Main/Patients/{index.tsx,index.test.tsx,styles.module.css}`
- `front-end/src/ui/Table/index.tsx`
- task, slice, índice e handoff

## Validacoes executadas

- `cd front-end && npm run lint`
- `cd front-end && npm run test -- --run src/pages/Main/Patients/index.test.tsx`

## Pendencias pos-task

- nenhuma

## Status final

done

## Dependencias

- Task 017 - done
- Task 044 - done

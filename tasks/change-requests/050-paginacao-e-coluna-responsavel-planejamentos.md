# Task 050 - Paginação e coluna de responsável na tabela de planejamentos

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

- nao se aplica; reaproveitar o payload atual de `GET /patients`

## Modo de execucao

single-stack

## Slice vertical

- Slice 008 - Trilhas semanais e evolucao
- `tasks/slices/008-trilhas-semanais-evolucao.md`

## Referencia visual

### Stack de referencia visual

front-end

### Tipo de referencia visual

artefato de design system + padrao ja consolidado na tabela de pacientes

### Fonte primaria visual

- `design-system/front/Design_System_Evolente_Desktop.md`
- `front-end/src/pages/Main/Patients/{index.tsx,styles.module.css}`

### Lacunas

- sem print dedicado para a tabela de planejamentos com paginação e responsável
- decisao: reutilizar o padrão visual discreto já aplicado em `Pacientes`, preservando a customização existente da Task 048

## Objetivo

Adicionar paginação local na tabela da página de planejamentos e expor a coluna de responsável usando o dado já retornado pela listagem de pacientes.

## Contexto mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`, `tasks/000-index.md`
- esta task, `tasks/slices/008-trilhas-semanais-evolucao.md` e handoffs `TASK-048` e `TASK-046`

## Contexto sob demanda

- `design-system/front/Design_System_Evolente_Desktop.md`
- `front-end/docs/ai/{AGENTS.md,ACCESSIBILITY.md}`
- `front-end/src/pages/Main/Plans/{index.tsx,styles.module.css,index.test.tsx}`
- `front-end/src/pages/Main/Patients/index.tsx`
- `front-end/src/types/patient.ts`
- `front-end/src/ui/Table/index.tsx`

## Orçamento de contexto

- baixo; restrito à listagem da página de planejamentos e ao padrão já existente em pacientes

## Criterios de conclusao

- [x] tabela de planejamentos exibe coluna `Responsável`
- [x] tabela de planejamentos pagina localmente em lotes consistentes
- [x] navegação de páginas funciona por teclado e mantém feedback textual do intervalo exibido
- [x] lint, teste da página e build aprovados

## Resultado da execucao

- a listagem de pacientes da página `Planejamentos` passou a exibir a coluna `Responsável` com dado real já presente no payload
- a tabela agora pagina localmente em lotes de 10 pacientes, com resumo textual e navegação por páginas
- o visual da paginação segue o padrão compacto já usado em `Pacientes`, sem desfazer os refinamentos visuais da Task 048
- o botão `Montar trilha` teve o `box-shadow` alinhado ao shadow base dos botões de ação do fluxo, reduzindo contraste excessivo
- foi adicionado teste de tela cobrindo a coluna nova e a troca de páginas

## Contexto utilizado

- fontes globais, Slice 008, handoffs 046 e 048, docs locais de front/acessibilidade, página de planejamentos, página de pacientes, tipos de paciente e `ui/Table`

## Handoff

- `.agents/state/handoffs/TASK-050.md`

## Arquivos alterados

- `front-end/src/pages/Main/Plans/{index.tsx,styles.module.css,index.test.tsx}`
- `tasks/change-requests/050-paginacao-e-coluna-responsavel-planejamentos.md`
- `tasks/slices/008-trilhas-semanais-evolucao.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-050.md`

## Validacoes executadas

- `cd front-end && npm run lint`
- `cd front-end && npm run test -- --run src/pages/Main/Plans/index.test.tsx`
- `cd front-end && npm run build`

## Pendencias pos-task

- nenhuma

## Status final

done

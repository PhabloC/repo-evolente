# Task 397 - Vincular foto do profissional na aba de usuários web

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

- nao se aplica; a árvore admin já expõe `professional.avatarUrl` via `AdminUser`

## Modo de execucao

single-stack

## Referencia de design system

### Stack de referencia visual

- front-end

### Tipo de referencia visual

artefato documental

### Fonte primaria visual

- `design-system/front/Design_System_Evolente_Desktop.md`

### Regra de aderencia visual

- preservar a composição atual da aba `Pacientes` da página `/usuarios`, apenas vinculando a foto real do profissional na coluna `Profissional` e mantendo o fallback textual existente

## Contexto de negocio

### Por que

Na aba `Pacientes` da página de usuários, o profissional vinculado ainda aparecia só com inicial, mesmo quando já possuía foto de perfil cadastrada.

### O que

Ligar `professional.avatarUrl` já disponível na árvore admin à coluna `Profissional` da aba `Pacientes`.

### Comportamento esperado

1. paciente vinculado a profissional com foto exibe a imagem real na coluna `Profissional`
2. profissional sem foto continua com fallback por inicial já usado nessa célula
3. a tabela mantém a hierarquia visual e acessibilidade atuais

### Fora de escopo

- mudanças de backend ou contrato
- upload/remoção de foto
- redesign da tabela de usuários

## Slice vertical

### Identificador do slice

Slice 027 - Fotos de perfil em bucket

### Arquivo do slice

- `tasks/slices/027-fotos-de-perfil-em-bucket.md`

## Dependencias

- Task 193 - done
- Task 331 - done
- Task 332 - done

## Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/027-fotos-de-perfil-em-bucket.md`
- `.agents/state/handoffs/TASK-193.md`
- `.agents/state/handoffs/TASK-331.md`
- `.agents/state/handoffs/TASK-332.md`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| Stack front com UI | `front-end/docs/ai/{AGENTS.md,ARCHITECTURE.md,COMPONENT_REUSE.md,ACCESSIBILITY.md}` | orientar estrutura, reuso e a11y | sim |
| Página usuários | `front-end/src/pages/Main/AdminUsers/**` | ligar `professional.avatarUrl` e ajustar a célula/tipos locais/testes | sim |

## Orçamento de contexto

- Risco baixo
- Estratégia: limitar a mudança à modelagem local de `PatientRow`, à célula da coluna `Profissional` e aos testes da página

## Criterios de conclusao

- coluna `Profissional` da aba `Pacientes` usa foto real quando `professional.avatarUrl` existir
- fallback por inicial permanece quando a foto não existir
- testes da página cobrem os dois cenários

## Validacao esperada

- `cd front-end && npm run test -- --run src/pages/Main/AdminUsers/index.test.tsx`
- `cd front-end && npx eslint src/pages/Main/AdminUsers/index.tsx src/pages/Main/AdminUsers/index.test.tsx`

## Resultado da execucao

### Resumo por stack

- **front-end**: a aba `Pacientes` da página `/usuarios` passou a renderizar a foto real do profissional vinculado na coluna `Profissional`, com fallback por inicial preservado

### Relação com o slice

- estende o Slice 027 para cobrir o último ponto restante da tabela administrativa de vínculos que ainda não refletia a foto do profissional

### Decisões técnicas

- `PatientRow` passou a carregar `professionalAvatarUrl` a partir de `node.professional.avatarUrl`
- a célula `Profissional` reutiliza a mesma estrutura visual existente, trocando apenas o conteúdo do avatar para imagem quando disponível
- o `alt` da imagem foi mantido explícito para preservar nome acessível no cenário com foto

### Trade-offs

- a foto do profissional foi ligada apenas na aba `Pacientes`; o modal de pacientes vinculados não precisou mudar porque não renderiza a identidade do profissional

## Contexto utilizado

### Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/027-fotos-de-perfil-em-bucket.md`
- `.agents/state/handoffs/TASK-193.md`
- `.agents/state/handoffs/TASK-331.md`
- `.agents/state/handoffs/TASK-332.md`

### Contexto sob demanda

| Fonte | Gatilho | Uso |
|---|---|---|
| `front-end/docs/ai/{AGENTS.md,ARCHITECTURE.md,COMPONENT_REUSE.md,ACCESSIBILITY.md}` | stack front com UI | orientar estrutura, reuso e acessibilidade |
| `front-end/src/pages/Main/AdminUsers/**` | página usuários | ligar `professional.avatarUrl`, ajustar estilos e atualizar testes |

## Handoff

- Caminho: `.agents/state/handoffs/TASK-397.md`

## Arquivos alterados

- `front-end/src/pages/Main/AdminUsers/index.tsx`
- `front-end/src/pages/Main/AdminUsers/styles.module.css`
- `front-end/src/pages/Main/AdminUsers/index.test.tsx`
- `tasks/change-requests/397-vincular-foto-profissional-na-aba-usuarios-web.md`
- `tasks/slices/027-fotos-de-perfil-em-bucket.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-397.md`

## Validacoes executadas

- `cd front-end && npm run test -- --run src/pages/Main/AdminUsers/index.test.tsx` — ok
- `cd front-end && npx eslint src/pages/Main/AdminUsers/index.tsx src/pages/Main/AdminUsers/index.test.tsx` — ok

## Pendencias pos-task

- nenhuma

## Status final

done

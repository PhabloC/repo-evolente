# Task 352 - Remover gradientes dos botões do sistema web

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

nao se aplica

## Modo de execucao

single-stack

## Referencia de design system

### Stack de referencia visual

front-end

### Tipo de referencia visual

ajuste visual global orientado por decisão do usuário no chat

### Fonte primaria visual

- `design-system/front/Design_System_Evolente_Desktop.md`

### Regra de aderencia visual

- preservar as cores e a hierarquia dos botões atuais, removendo apenas o uso de gradientes dos controles interativos

## Contexto de negocio

### Por que

O usuário pediu padronização visual para que os botões do sistema usem cores sólidas em vez de gradientes.

### O que

Remover gradientes dos estilos de botões compartilhados e dos principais overrides locais de CTA no front-end.

### Comportamento esperado

- botões do componente base não usam gradiente
- CTAs operacionais com estilos locais não usam gradiente
- paginações ativas e botões de ação mantêm contraste e hierarquia, mas com fundo sólido

### Fora de escopo

- remoção de gradientes de cards, hero sections, tabelas ou superfícies que não sejam botões
- refatoração ampla de tokens visuais do shell
- mudanças no mobile ou no backend

## Slice vertical

### Identificador do slice

Slice 017 - Redesign interface interna web

### Arquivo do slice

- `tasks/slices/017-redesign-interface-interna-web.md`

## Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/017-redesign-interface-interna-web.md`
- `.agents/state/handoffs/TASK-351.md`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| UI web | `front-end/docs/ai/ACCESSIBILITY.md`, `CODE_STYLE.md` | preservar contraste, foco e consistência visual | sim |
| Botão base | `front-end/src/ui/Button/styles.module.css` | remover gradiente do variant compartilhado `info` | sim |
| CTA compartilhado | `front-end/src/components/PageActionButton/styles.module.css` | remover gradiente do botão reutilizado entre páginas | sim |
| Controles do shell | `front-end/src/layout/Header/styles.module.css` | remover gradiente residual do botão de notificação | sim |
| CTAs locais | `front-end/src/pages/Main/ShellHome/styles.module.css`, `Admin/styles.module.css`, `Patients/styles.module.css`, `Plans/styles.module.css`, `Reports/styles.module.css`, `Library/styles.module.css` | remover gradientes dos botões e paginações ativas que ainda os forçavam localmente | sim |
| Testes focados | `front-end/src/layout/Header/index.test.tsx`, `front-end/src/pages/Main/ShellHome/index.test.tsx`, `front-end/src/pages/Main/Plans/PatientTrail/index.test.tsx` | validar estabilidade do shell e páginas com CTAs alterados | sim |

## Orçamento de contexto

- medio
- estrategia de reducao: atacar apenas estilos explicitamente ligados a botões e CTAs, sem reabrir superfícies não interativas que também usam gradiente

## Criterios de conclusao

- [x] componente base de botão não mantém gradientes residuais
- [x] `PageActionButton` e botão de notificação do header ficam com fundos sólidos
- [x] paginações ativas e CTAs locais de dashboard, pacientes, trilha, relatórios, admin e biblioteca deixam de usar gradiente
- [x] testes focados das áreas tocadas passam

## Dependencias

- Task 297
- Task 347
- Task 348
- Task 349
- Task 351

## Resultado da execucao

- o variant `info` do `ui/Button` passou a usar fundo sólido
- `PageActionButton`, botão de notificação do header e principais CTAs/estados ativos locais migraram para fundos sólidos
- paginações ativas, CTA de sugestão na trilha, CTA primário do dashboard, botão de confirmação perigosa em relatórios e botões de preview interativo na biblioteca deixaram de usar gradiente

## Contexto utilizado

### Mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`
- `tasks/000-index.md`, esta task, `tasks/slices/017-redesign-interface-interna-web.md`
- `.agents/state/handoffs/TASK-351.md`

### Sob demanda

- `front-end/docs/ai/ACCESSIBILITY.md`
- `front-end/docs/ai/CODE_STYLE.md`
- `front-end/src/ui/Button/styles.module.css`
- `front-end/src/components/PageActionButton/styles.module.css`
- `front-end/src/layout/Header/styles.module.css`
- `front-end/src/pages/Main/ShellHome/styles.module.css`
- `front-end/src/pages/Main/Admin/styles.module.css`
- `front-end/src/pages/Main/Patients/styles.module.css`
- `front-end/src/pages/Main/Plans/styles.module.css`
- `front-end/src/pages/Main/Reports/styles.module.css`
- `front-end/src/pages/Main/Library/styles.module.css`
- `front-end/src/layout/Header/index.test.tsx`
- `front-end/src/pages/Main/ShellHome/index.test.tsx`
- `front-end/src/pages/Main/Plans/PatientTrail/index.test.tsx`

### Contexto evitado

- `backend/` por nao haver mudança de API
- `mobile/` por nao fazer parte do escopo pedido
- arquivos de cards e superfícies não interativas que usam gradiente, por estarem fora do pedido

## Handoff

- `.agents/state/handoffs/TASK-352.md`

## Arquivos alterados

- `front-end/src/ui/Button/styles.module.css`
- `front-end/src/components/PageActionButton/styles.module.css`
- `front-end/src/layout/Header/styles.module.css`
- `front-end/src/pages/Main/ShellHome/styles.module.css`
- `front-end/src/pages/Main/Admin/styles.module.css`
- `front-end/src/pages/Main/Patients/styles.module.css`
- `front-end/src/pages/Main/Plans/styles.module.css`
- `front-end/src/pages/Main/Reports/styles.module.css`
- `front-end/src/pages/Main/Library/styles.module.css`
- `tasks/change-requests/352-remover-gradientes-dos-botoes-do-sistema-web.md`
- `tasks/slices/017-redesign-interface-interna-web.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-352.md`

## Validacoes executadas

- `cd front-end && npm test -- --run src/pages/Main/Plans/PatientTrail/index.test.tsx src/layout/Header/index.test.tsx src/pages/Main/ShellHome/index.test.tsx` - ok
- `cd front-end && npx eslint src/ui/Button/styles.module.css src/components/PageActionButton/styles.module.css src/layout/Header/styles.module.css src/pages/Main/ShellHome/styles.module.css src/pages/Main/Admin/styles.module.css src/pages/Main/Patients/styles.module.css src/pages/Main/Plans/styles.module.css src/pages/Main/Reports/styles.module.css src/pages/Main/Library/styles.module.css` - apenas avisos esperados; arquivos CSS ignorados pela configuração atual do ESLint

## Pendencias pos-task

- validar visualmente outras telas menos usadas para decidir se a mesma padronização deve alcançar superfícies interativas que não usam o componente `Button`

## Status final

done

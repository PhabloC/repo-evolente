# Task 333 - Refinar feedback e máscara no criar usuário master web

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

- nao se aplica

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

- preservar a linguagem visual já consolidada da página de usuários, elevando a hierarquia do feedback de sucesso e mantendo o modal de criação consistente com os demais formulários do produto

## Contexto de negocio

### Por que

O feedback “Usuário master ... criado.” está visualmente fraco para um evento importante e o campo de telefone do modal ainda não aplica máscara durante a digitação.

### O que

Transformar o feedback de sucesso em um bloco visual mais claro na página de usuários e aplicar máscara no telefone do modal de criação de usuário master.

### Comportamento esperado

1. após criar usuário master, o feedback aparece em um bloco de sucesso com melhor destaque visual
2. o telefone do modal é mascarado durante a digitação no padrão `(11) 99999-9999`
3. o submit continua enviando o telefone normalizado, sem máscara

### Fora de escopo

- alterações de contrato ou backend
- mudanças no fluxo de criação além do feedback e da máscara

## Slice vertical

### Identificador do slice

Slice 017 - Redesign da interface interna web

### Arquivo do slice

- `tasks/slices/017-redesign-interface-interna-web.md`

## Dependencias

- Task 155 - done
- Task 258 - done
- Task 183 - done
- Task 332 - done

## Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/017-redesign-interface-interna-web.md`
- `.agents/state/handoffs/TASK-258.md`
- `.agents/state/handoffs/TASK-332.md`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| Página usuários | `front-end/src/pages/Main/AdminUsers/**` | refinar feedback visual local | sim |
| Modal de criação | `front-end/src/pages/Main/AdminUsers/CreateMasterUserModal.tsx` | aplicar máscara no telefone | sim |
| Workspace admin | `front-end/src/pages/Main/Admin/useAdminWorkspace.tsx` | preservar origem do feedback | sim |
| Util de telefone | `front-end/src/utils/phone.ts` | reutilizar máscara e normalização | sim |
| Testes da página | `front-end/src/pages/Main/AdminUsers/index.test.tsx` | validar feedback e máscara | sim |

## Orçamento de contexto

- Risco baixo
- Estratégia: restringir a mudança à página `AdminUsers`, ao modal de criação e ao util de telefone já existente

## Criterios de conclusao

- feedback de sucesso da criação fica visualmente mais forte
- telefone do modal é mascarado durante a digitação
- submit continua enviando telefone sem máscara
- testes da página passam

## Validacao esperada

- `cd front-end && npm run test -- --run src/pages/Main/AdminUsers/index.test.tsx`

## Resultado da execucao

### Resumo por stack

- **front-end**: a página de usuários passou a exibir um banner de sucesso mais forte após a criação de usuário master, e o modal agora mascara o telefone durante a digitação.

### Relação com o slice

- refina incrementalmente a experiência operacional da página de usuários dentro do Slice 017, sem alterar contrato, backend ou fluxos vizinhos.

### Decisões técnicas

- o `actionMessage` continuou sendo produzido no `useAdminWorkspace`, mas a página `AdminUsers` passou a renderizá-lo em um banner visual local em vez do texto simples do `AdminFeedback`
- o campo de telefone do modal passou a reutilizar `formatPhone` via `setValue`, preservando o envio normalizado já entregue na Task 258
- o caso de teste de telefone inválido foi ajustado para refletir o novo comportamento da máscara em campo opcional

### Trade-offs

- o novo banner local melhora especificamente a página de usuários; outras páginas do módulo admin continuam usando o feedback textual padrão de `AdminFeedback`

## Contexto utilizado

### Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/017-redesign-interface-interna-web.md`
- `.agents/state/handoffs/TASK-258.md`
- `.agents/state/handoffs/TASK-332.md`

### Contexto sob demanda

| Fonte | Gatilho | Uso |
|---|---|---|
| `front-end/src/pages/Main/AdminUsers/**` | refino local da página | banner de sucesso e estilos |
| `front-end/src/pages/Main/AdminUsers/CreateMasterUserModal.tsx` | máscara do telefone | onChange mascarado |
| `front-end/src/pages/Main/Admin/useAdminWorkspace.tsx` | origem do feedback | manter emissão do `actionMessage` |
| `front-end/src/utils/phone.ts` | máscara e normalização | reaproveitar `formatPhone` |
| `front-end/src/pages/Main/AdminUsers/index.test.tsx` | cobertura | validar banner e máscara |

## Handoff

- Caminho: `.agents/state/handoffs/TASK-333.md`

## Arquivos alterados

- `front-end/src/pages/Main/AdminUsers/index.tsx`
- `front-end/src/pages/Main/AdminUsers/CreateMasterUserModal.tsx`
- `front-end/src/pages/Main/AdminUsers/index.test.tsx`
- `front-end/src/pages/Main/AdminUsers/styles.module.css`
- `tasks/change-requests/333-refinar-feedback-e-mascara-no-criar-usuario-master-web.md`
- `tasks/slices/017-redesign-interface-interna-web.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-333.md`

## Validacoes executadas

- `cd front-end && npm run test -- --run src/pages/Main/AdminUsers/index.test.tsx` — ok

## Pendencias pos-task

- nenhuma bloqueante

## Status final

done

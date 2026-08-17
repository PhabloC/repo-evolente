# Task 082 - Refinar card de profissionais e vínculos no admin web

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

- nao se aplica; ajuste visual sem alterar payloads, regras ou integracoes

## Modo de execucao

single-stack

## Slice vertical

- Slice 017 - Redesign da interface interna web
- `tasks/slices/017-redesign-interface-interna-web.md`

## Referencia visual

### Stack de referencia visual

front-end

### Tipo de referencia visual

print de tela enviado no chat

### Fonte primaria visual

- trecho da seção `Profissionais e vínculos` mostrado no chat
- `front-end/src/pages/Main/Admin/sections.tsx`

### Lacunas

- o print cobre apenas um estado do card; decisao: melhorar hierarquia visual do bloco mantendo a estrutura de dados e estados atuais

## Objetivo

Melhorar o design do card de profissionais e vínculos no admin para dar mais hierarquia ao profissional, ao paciente vinculado e aos badges laterais.

## Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/017-redesign-interface-interna-web.md`
- `.agents/state/handoffs/TASK-081.md`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| UI web | `front-end/src/pages/Main/Admin/sections.tsx` | reestruturar o bloco visual de profissionais e pacientes | sim |
| Estilos locais | `front-end/src/pages/Main/Admin/styles.module.css` | aplicar o novo layout, espaçamentos e estados visuais | sim |
| Acessibilidade | `front-end/docs/ai/ACCESSIBILITY.md` | validar contraste, semântica e legibilidade do ajuste | sim |

## Orçamento de contexto

- baixo
- estrategia: limitar a mudança à seção `Profissionais e vínculos`, sem reabrir a tabela de usuários nem hooks de dados

## Criterios de conclusao

- [x] card do profissional com hierarquia visual mais forte
- [x] paciente vinculado com leitura mais clara de nome, código e status
- [x] badges laterais integrados ao layout sem aparência de conteúdo solto
- [x] lint e build do front-end aprovados

## Dependencias

- Task 077 - done
- Task 081 - done

## Resultado da execucao

- o bloco do profissional ganhou avatar com iniciais, tipografia mais forte e um badge de contagem melhor integrado ao cabeçalho
- cada paciente vinculado passou a ser renderizado como subcard interno, com separação clara entre nome, código e status
- o layout foi mantido responsivo sem alterar a estrutura de dados nem a lógica da tela

## Contexto utilizado

### Mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`
- `tasks/000-index.md`, esta task, `tasks/slices/017-redesign-interface-interna-web.md`
- `.agents/state/handoffs/TASK-081.md`

### Sob demanda

- `front-end/AGENTS.md`
- `front-end/docs/ai/AGENTS.md`
- `front-end/docs/ai/ACCESSIBILITY.md`
- `design-system/README.md`
- `front-end/src/pages/Main/Admin/sections.tsx`
- `front-end/src/pages/Main/Admin/styles.module.css`

### Contexto evitado

- hooks de workspace, backend, contrato OpenAPI e demais rotas do admin por nao participarem deste ajuste local de UI

## Handoff

- `.agents/state/handoffs/TASK-082.md`

## Arquivos alterados

- `front-end/src/pages/Main/Admin/sections.tsx`
- `front-end/src/pages/Main/Admin/styles.module.css`
- `tasks/change-requests/082-refinar-card-profissionais-vinculos-admin-web.md`
- `tasks/slices/017-redesign-interface-interna-web.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-082.md`

## Validacoes executadas

- `cd front-end && npm run lint` - ok
- `cd front-end && npm run build` - ok

## Pendencias pos-task

- nenhuma

## Status final

done

# Task 398 - Avatar redondo do profissional na aba pacientes de usuários web

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

- preservar a composição atual da aba `Pacientes`, ajustando apenas o raio do avatar do profissional para seguir o padrão circular já usado em outros pontos da página de usuários

## Contexto de negocio

### Por que

Depois de ligar a foto real do profissional na coluna `Profissional`, o avatar dessa célula ainda estava com cantos arredondados em vez de formato circular.

### O que

Ajustar o avatar do profissional na aba `Pacientes` da página `/usuarios` para borda totalmente redonda.

### Comportamento esperado

1. com foto, a imagem do profissional aparece em moldura circular
2. sem foto, o fallback por inicial continua no mesmo formato circular

### Fora de escopo

- mudanças de backend ou contrato
- redesign da tabela
- alterações em outros módulos

## Slice vertical

### Identificador do slice

Slice 027 - Fotos de perfil em bucket

### Arquivo do slice

- `tasks/slices/027-fotos-de-perfil-em-bucket.md`

## Dependencias

- Task 397 - done

## Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/027-fotos-de-perfil-em-bucket.md`
- `.agents/state/handoffs/TASK-397.md`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| Stack front com UI | `front-end/docs/ai/{AGENTS.md,ARCHITECTURE.md,COMPONENT_REUSE.md,ACCESSIBILITY.md}` | validar aderência estrutural e visual | sim |
| Estilo da página | `front-end/src/pages/Main/AdminUsers/styles.module.css` | ajustar o raio do avatar do profissional | sim |

## Orçamento de contexto

- Risco baixo
- Estratégia: alterar apenas a classe `professionalAvatar`, sem reabrir renderização, tipos ou contrato

## Criterios de conclusao

- avatar do profissional na aba `Pacientes` fica circular
- fallback por inicial preserva o mesmo formato

## Validacao esperada

- `cd front-end && npm run test -- --run src/pages/Main/AdminUsers/index.test.tsx`

## Resultado da execucao

### Resumo por stack

- **front-end**: o avatar do profissional na coluna `Profissional` da aba `Pacientes` passou de `8px` para formato circular

### Relação com o slice

- refina a apresentação visual de um ponto já coberto pelo Slice 027, sem alterar dados nem integração

### Decisões técnicas

- o ajuste ficou restrito à classe `professionalAvatar`
- a imagem e o fallback textual continuam compartilhando a mesma moldura circular

## Contexto utilizado

### Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/027-fotos-de-perfil-em-bucket.md`
- `.agents/state/handoffs/TASK-397.md`

### Contexto sob demanda

| Fonte | Gatilho | Uso |
|---|---|---|
| `front-end/docs/ai/{AGENTS.md,ARCHITECTURE.md,COMPONENT_REUSE.md,ACCESSIBILITY.md}` | stack front com UI | confirmar aderência do ajuste |
| `front-end/src/pages/Main/AdminUsers/styles.module.css` | estilo da página | tornar o avatar circular |

## Handoff

- Caminho: `.agents/state/handoffs/TASK-398.md`

## Arquivos alterados

- `front-end/src/pages/Main/AdminUsers/styles.module.css`
- `tasks/change-requests/398-avatar-redondo-profissional-aba-pacientes-usuarios-web.md`
- `tasks/slices/027-fotos-de-perfil-em-bucket.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-398.md`

## Validacoes executadas

- `cd front-end && npm run test -- --run src/pages/Main/AdminUsers/index.test.tsx` — ok

## Pendencias pos-task

- nenhuma

## Status final

done

# Task 027 - Lucide React como biblioteca padrao de icones web

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

front-end

### Tipo de referencia visual

artefato de design system

### Fonte primaria visual

- `design-system/front/Design_System_Evolente_Desktop.md` (tom visual; icones Lucide)

## Origem da solicitacao

Pedido do usuario para adotar Lucide React como biblioteca padrao de icones.

## Objetivo

Instalar `lucide-react`, documentar como padrao no front-end e migrar os SVGs inline existentes (Login).

## Escopo

- Adicionar dependencia `lucide-react` (autorizada nesta task)
- Documentar em `front-end/docs/ai/CODE_STYLE.md` (e ACCESSIBILITY se couber)
- Substituir SVGs da LoginPage por icones Lucide
- Validar lint/test/build

## Fora de escopo

- Mobile / outras libs de icone
- Refator amplo de UI nao relacionada

## Dependencias

- Task 026 (login visual) — done

## Slice vertical

### Identificador do slice

Slice 013 - Lucide React como padrao de icones (web)

### Arquivo do slice

- `tasks/slices/013-lucide-icones-web.md`

## Contexto mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/013-lucide-icones-web.md`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatorio? |
|---|---|---|---|
| Padrao front | `front-end/docs/ai/CODE_STYLE.md` | documentar regra | sim |
| A11y icones | `front-end/docs/ai/ACCESSIBILITY.md` | botoes so-icone | sim |
| Migracao | `front-end/src/pages/Auth/Login/index.tsx` | trocar SVGs | sim |

## Orçamento de contexto

- Risco: baixo
- Estrategia: nao carregar mobile/backend/openapi

## Criterios de conclusao

- [x] `lucide-react` no package.json
- [x] Regra de padrao documentada
- [x] Login sem SVG inline de icone
- [x] lint/test/build ok

## Instrucoes de implementacao

1. `npm install lucide-react` em `front-end`
2. Documentar: import nomeado; `aria-hidden` em icones decorativos; `aria-label` em botoes so-icone; tamanho via `size` prop
3. Migrar Login: Mail, Lock, Eye/EyeOff, Users, CalendarCheck, BarChart3, Shield, Headphones
4. Manter classes CSS existentes nos icones

## Validacao esperada

- `cd front-end && npm run lint`
- `cd front-end && npm run test -- --run src/pages/Auth/Login`
- `cd front-end && npm run build`

## Entregaveis esperados

- Dependencia + docs + Login migrada + handoff TASK-027

## Resultado da execucao

### Resumo por stack

- **front-end**: `lucide-react` instalado; padrao documentado; Login migrada para Lucide.

### Relação com o slice

- Slice 013 concluído.

### Decisões técnicas

- Dependencia autorizada nesta task.
- Icones Login: Users, CalendarCheck, BarChart3, Mail, Lock, Eye/EyeOff, Shield, Headphones.
- SVG custom permanece apenas para logos de marca (webp).

### Trade-offs

- Migracao limitada a Login (unico uso de SVG inline de icone).

## Contexto utilizado

### Contexto mínimo

- AGENTS, GUIDE, context-map, index, esta task, slice 013

### Contexto sob demanda

| Fonte | Gatilho | Uso |
|---|---|---|
| CODE_STYLE | padrao | secao Icones |
| ACCESSIBILITY | a11y | nota lucide |
| LoginPage | migracao | troca SVGs |

### Evitado

- mobile/, backend/, openapi

## Handoff

- Caminho: `.agents/state/handoffs/TASK-027.md`

## Arquivos alterados

- `front-end/package.json` / `package-lock.json`
- `front-end/src/pages/Auth/Login/index.tsx`
- `front-end/docs/ai/CODE_STYLE.md`
- `front-end/docs/ai/ACCESSIBILITY.md`
- `tasks/change-requests/027-lucide-icones-web.md`
- `tasks/slices/013-lucide-icones-web.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-027.md`

## Validacoes executadas

- lint ok
- test Login ok
- build ok

## Pendencias pos-task

- Nenhuma obrigatoria; novas telas devem usar Lucide

## Status final

done

# Task 083 - Estruturar central de relatórios do master web

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

- nao se aplica; ajuste de UX e conteudo na rota administrativa sem criar nova integracao

## Modo de execucao

single-stack

## Slice vertical

- Slice 017 - Redesign da interface interna web
- `tasks/slices/017-redesign-interface-interna-web.md`

## Referencia visual

### Stack de referencia visual

front-end

### Tipo de referencia visual

artefato documental + direcionamento funcional do projeto

### Fonte primaria visual

- `design-system/front/Design_System_Evolente_Desktop.md`
- `requirements/001-escopo-produto.md`
- `requirements/002-regras-de-negocio.md`
- `front-end/src/pages/Main/AdminReports/index.tsx`

### Lacunas

- nao existe fonte administrativa dedicada para relatórios do master nesta fase
- decisao: estruturar a tela como central operacional do que o master deve acompanhar, sem simular dados inexistentes

## Objetivo

Transformar a rota de relatórios do master em uma central útil de leitura operacional, com os relatórios ideais do projeto, prioridades, filtros recomendados e orientação de exportação.

## Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/017-redesign-interface-interna-web.md`
- `.agents/state/handoffs/TASK-082.md`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| Domínio de relatórios | `requirements/001-escopo-produto.md`, `requirements/002-regras-de-negocio.md` | confirmar o papel do master e o ciclo de geração/compartilhamento | sim |
| UI web | `design-system/front/Design_System_Evolente_Desktop.md` | compor cards, hierarquia e estados da central | sim |
| Stack front-end | `front-end/docs/ai/{AGENTS.md,ACCESSIBILITY.md}` | garantir estrutura, contraste e semântica da nova página | sim |
| Implementação atual | `front-end/src/pages/Main/AdminReports/index.tsx` | substituir o placeholder por uma central operacional real | sim |

## Orçamento de contexto

- baixo
- estrategia: limitar a execução à rota `AdminReports`, sem abrir backend ou contratos não usados na tela

## Criterios de conclusao

- [x] a rota deixa de ser placeholder e passa a comunicar claramente os relatórios ideais do master
- [x] a tela organiza prioridades, recortes e exportações de forma operacional
- [x] a página registra com transparência os gaps de fonte administrativa dedicada
- [x] lint e build do front-end aprovados

## Dependencias

- Task 043 - done
- Task 047 - done

## Resultado da execucao

- a rota administrativa de relatórios deixou de ser um placeholder e virou uma central operacional para o perfil master
- a tela passou a organizar leituras prioritárias, catálogo ideal de relatórios, recortes recomendados e exportações úteis ao projeto
- o conteúdo deixa explícito que o fluxo clínico de geração e compartilhamento já existe, mas a consolidação administrativa dedicada ainda depende de fonte própria

## Contexto utilizado

### Mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`
- `tasks/000-index.md`, esta task, `tasks/slices/017-redesign-interface-interna-web.md`
- `.agents/state/handoffs/TASK-082.md`

### Sob demanda

- `requirements/001-escopo-produto.md`
- `requirements/002-regras-de-negocio.md`
- `design-system/front/Design_System_Evolente_Desktop.md`
- `front-end/docs/ai/AGENTS.md`
- `front-end/docs/ai/ACCESSIBILITY.md`
- `front-end/src/pages/Main/Reports/index.tsx`
- `front-end/src/pages/Main/AdminReports/index.tsx`

### Contexto evitado

- backend, contrato OpenAPI e hooks de dados administrativos por nao haver integração nova nesta entrega

## Handoff

- `.agents/state/handoffs/TASK-083.md`

## Arquivos alterados

- `front-end/src/pages/Main/AdminReports/index.tsx`
- `front-end/src/pages/Main/AdminReports/styles.module.css`
- `tasks/change-requests/083-estruturar-central-relatorios-master-web.md`
- `tasks/slices/017-redesign-interface-interna-web.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-083.md`

## Validacoes executadas

- `cd front-end && npm run lint` - ok
- `cd front-end && npm run build` - ok

## Pendencias pos-task

- nenhuma

## Status final

done

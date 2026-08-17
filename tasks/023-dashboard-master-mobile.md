# Task 023 - Dashboard master mobile

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

- `contracts/openapi.yaml#/paths` admin

## Modo de execucao

single-stack

## Referencia de design system

### Stack de referencia visual

mobile

### Tipo de referencia visual

artefato de design system

### Fonte primaria visual

- `design-system/mobile/Design_System_Evolente_App_Mobile.md`

### Regra de aderencia visual

- Admin operacional mobile; nao infantil; sem gamificacao.

## Contexto de negocio

### Por que

Master no app.

### O que

MVP: metricas, usuarios, inativar; logs se couber.

### Comportamento esperado

- Metricas
- Inativar
- Listas

### Fora de escopo

- CRUD conteudos completo

## Review da spec

- [x] Permissoes definidas ou `nao se aplica`
- [x] Casos de erro mapeados
- [x] Decisoes de negocio confirmadas como humanas
- [x] Criterios de aceite objetivos e verificaveis
- [x] Casos de borda considerados

### Evidencias da review

- Permissoes: master
- Casos de erro: 403; rede
- Decisoes humanas confirmadas: Stack web React/Vite; mobile sim; profissional multi-especialidade; inativar nao excluir; gamificacao fora
- Casos de borda: paginacao

## Especificacao tecnica

### Deve

- Paridade essencial

### Nao deve

- nao adicionar novas dependencias sem autorizacao explicita nesta task
- nao desviar dos padroes estabelecidos sem justificativa registrada
- Fluxo crianca

## Entradas

- `design-system/mobile/Design_System_Evolente_App_Mobile.md`
- `mobile/docs/ai/`
- `requirements/001-escopo-produto.md`

## Dependencias

- Task 021

## Slice vertical

### Identificador do slice

Slice 009 - Admin master

### Arquivo do slice

- `tasks/slices/009-administracao-master.md`

### Objetivo de negócio

Admin mobile.

### Entrega verificável do slice

App master operacional.

### Fora do slice

- Web

## Contexto mínimo

Sempre ler:

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/009-administracao-master.md`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| UI mobile | `design-system/mobile/Design_System_Evolente_App_Mobile.md` | UI mobile | sim |
| Mobile | `mobile/docs/ai/ARCHITECTURE.md e CODE_STYLE.md` | mobile | sim |
| API | `contracts/openapi.yaml` | API | sim |
| Requisitos | `requirements/001-escopo-produto.md e 002-regras-de-negocio.md` | regras | sim |

## Orçamento de contexto

- Risco alto — MVP metricas+usuarios

## Criterios de conclusao

- Metricas e inativar
- Sem gamificacao

## Instrucoes de implementacao

- Reduzir escopo se estourar

## Validacao esperada

- npm run lint
- npm run typecheck
- npm run test

## Entregaveis esperados

- Dashboard master mobile

## Riscos ou ambiguidades

- Paridade ampla

## Resultado da execucao

MVP admin no shell master:

- Aba **Início**: métricas (`GET /admin/metrics`) + logs recentes (`GET /admin/audit-logs`)
- Aba **Usuários**: lista + inativar/reativar (`GET/PATCH /users`) com bloqueio de auto-inativação
- Abas Conteúdos/Config permanecem placeholder (CRUD catálogo fora do escopo)
- Modo demo quando `useDemoData`/sem API
- Tom operacional (sem gamificação/fluxo criança) — desvio do DS mobile infantil documentado

## Contexto utilizado

### Contexto mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`
- `tasks/000-index.md`, esta task, `tasks/slices/009-administracao-master.md`
- `.agents/state/handoffs/TASK-022.md`

### Contexto sob demanda

| Fonte | Gatilho | Uso |
|---|---|---|
| DS mobile | UI | tom operacional; desvio gamificação |
| openapi admin/users | API | integração |
| mobile ARCHITECTURE | mobile | feature admin |
| requirements 001 | regras | capacidades master |

### Contexto não carregado

- front-end pages Admin (só contrato)
- CRUD conteúdos

## Handoff

- `.agents/state/handoffs/TASK-023.md`

## Arquivos alterados

- `mobile/src/features/admin/**`
- `mobile/src/features/shell/navigators/MasterShellNavigator.tsx`
- `mobile/src/shared/components/Button/index.tsx` (`disabled`)
- task/index/slice/handoff

## Validacoes executadas

- `npm run lint` ok
- `npm run typecheck` ok
- `npm run test` ok (8 testes)

## Aderencia ao design system

- Fonte: DS mobile
- **Desvio:** DS enfatiza ludicidade/criança/medalhas; requisitos e task mandam admin operacional sem gamificação — prevalece requisito
- A11y: loading/erro, `accessibilityLiveRegion` no feedback, `accessibilityState.disabled` no botão

## Pendencias pos-task

- Nenhuma do Slice 009
- Próximas: Task 024 (home/notificações responsável) ou 025 conforme index

## Status final

done

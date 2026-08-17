# Slice 009 - Administracao master

## Status

done

## Objetivo de negocio

Metricas, usuarios (criar/editar/inativar/permissoes), planos, logs e pacientes por profissional (web+mobile).

## Entrega verificavel

Admin completa sem exclusao; metricas e logs; mobile com capacidades essenciais.

## Fora de escopo

- Exclusao definitiva
- Catalogo (slice 006)
- Gamificacao

## Perfil do projeto

- stack web escolhida: front-end (React/Vite)
- mobile: sim

## Stacks envolvidas

- front-end
- backend
- mobile

## Contrato

- `contracts/openapi.yaml#/paths` de admin

## Referencia visual por stack

### Web

- tipo: artefato de design system
- fonte primaria: `design-system/front/Design_System_Evolente_Desktop.md` (dashboard master)

### Mobile

- tipo: artefato de design system
- fonte primaria: `design-system/mobile/Design_System_Evolente_App_Mobile.md` (adaptacao operacional)

## Permissoes e atores

- Apenas master

## Casos de erro e borda

- 403
- Inativar a si mesmo
- Filtros vazios

## Decisoes humanas confirmadas

- Stack web: React/Vite; Mobile: sim; Profissional multi-especialidade; Inativar (nao excluir); Gamificacao/jogos fora do escopo

## Premissas adotadas

- Gateway, valores e push a definir — abstrair
- DS documental governa tokens; sem prints nesta fase
- Conflito DS mobile (gamificacao/UI crianca) vs requisitos — prevalece requisito

## Tasks relacionadas

- `tasks/021-api-admin-master.md` - API admin
- `tasks/022-dashboard-master-web.md` - Dashboard web
- `tasks/023-dashboard-master-mobile.md` - Dashboard mobile
- `tasks/change-requests/484-hardening-dashboard-master-mobile-assinaturas-logs.md` - hardening do dashboard master mobile para assinaturas e logs — **done**
- `tasks/change-requests/447-adicionar-graficos-dashboard-master-web.md` - gráficos operacionais no dashboard master — **done**
- `tasks/change-requests/490-hardening-admin-logs-e-lookups-backend.md` - hardening dos lookups e da exportação PDF de logs no backend — **done**

## Dependencias do slice

- Slices 002 e 005

## Contexto minimo recomendado

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- este slice

## Contexto sob demanda recomendado

| Gatilho | Fonte | Quando carregar | Obrigatorio? |
|---|---|---|---|
| Requisitos | `requirements/001-escopo-produto.md`, `requirements/002-regras-de-negocio.md` | regras do slice | sim |
| UI web | `design-system/front/Design_System_Evolente_Desktop.md` | UI web | sim se UI web |
| UI mobile | `design-system/mobile/Design_System_Evolente_App_Mobile.md` | UI mobile | sim se UI mobile |
| API | `contracts/openapi.yaml` | API | sim se API |
| Front-end | `front-end/docs/ai/` | front envolvido | sim se front |
| Backend | `backend/docs/ai/` | back envolvido | sim se back |
| Mobile | `mobile/docs/ai/` | mobile envolvido | sim se mobile |

## Risco de contexto

- alto
- estrategia: carregar apenas secoes/paths citados nas tasks

## Observacoes de rastreabilidade

- Sem conflitos adicionais alem das premissas.
- Task 021 (API), Task 022 (web) e Task 023 (mobile MVP) concluidas.
- Mobile: metricas + usuarios/inativar + logs curtos; catalogo permanece na web.

## Status final

done

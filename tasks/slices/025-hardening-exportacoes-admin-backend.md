# Slice 025 - Hardening de exportacoes e consultas admin no backend

## Status

done

## Objetivo de negocio

Endurecer as exportacoes administrativas do master e reduzir riscos de degradacao nas consultas internas do modulo admin, preservando o contrato funcional ja consumido pela web.

## Entrega verificavel

- exportacao CSV administrativa de logs transmite o arquivo em stream incremental paginado, sem carregar todos os registros em memoria
- serializacao CSV trata `Date` explicitamente
- exportacao de profissionais tolera `linkedAt` ausente/invalido sem erro de runtime
- composicao da arvore profissional e da exportacao evita N+1 de criancas e usa leitura paginada de profissionais no backend

## Fora de escopo

- redesign ou ajuste de UI web/mobile
- novos filtros funcionais na central admin
- mudancas de permissao do master
- refatoracao ampla de todos os repositorios do backend

## Perfil do projeto

- stack web escolhida: front-end (React/Vite)
- mobile: sim

## Stacks envolvidas

- backend

## Contrato

- `contracts/openapi.yaml#/paths/~1admin~1professionals-tree`
- `contracts/openapi.yaml#/paths/~1admin~1reports~1professionals~1export`
- `contracts/openapi.yaml#/paths/~1admin~1reports~1audit-logs~1export`

## Referencia visual por stack

### Backend

- tipo: nao se aplica
- fonte primaria: nao se aplica

## Permissoes e atores

- master

## Casos de erro e borda

- `linkedAt` nulo, indefinido ou serializado como string
- objeto `Date` enviado diretamente para o utilitario CSV
- exportacao de logs com volume alto o suficiente para pressionar heap quando o CSV eh montado integralmente
- base com muitos profissionais/vinculos causando fan-out excessivo

## Decisoes humanas confirmadas

- o code review em `ajustes_backend.md` deve virar change request adicional antes da implementacao
- a task deve preservar compatibilidade do consumo atual do front sempre que possivel

## Tasks relacionadas

- `tasks/021-api-admin-master.md` - API admin master — **done**
- `tasks/change-requests/085-exportacoes-csv-relatorios-master-web-e-api.md` - Exportacoes CSV admin — **done**
- `tasks/change-requests/089-corrigir-page-size-users-nos-logs-admin-web.md` - Hardening de paginação auxiliar nos logs web — **done**
- `tasks/change-requests/151-hardening-exportacoes-admin-backend.md` - Hardening de exportacoes e consultas admin no backend — **done**
- `tasks/change-requests/455-exportacoes-csv-laranja-e-pdf-relatorios-admin.md` - CSV/PDF com logo nos exports admin — **done**

## Dependencias do slice

- Slices 009 e 017

## Contexto minimo recomendado

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- este slice
- `tasks/change-requests/151-hardening-exportacoes-admin-backend.md`

## Contexto sob demanda recomendado

| Gatilho | Fonte | Quando carregar | Obrigatorio? |
|---|---|---|---|
| Contrato admin | `contracts/openapi.yaml` | validar compatibilidade das rotas admin impactadas | sim |
| Modulo admin | `backend/src/modules/admin/*` | implementar hardening de exportacao/consulta | sim |
| Usuarios paginados | `backend/src/modules/users/*` | reduzir carga ao buscar profissionais para exportacao | sim |
| Guardioes/criancas | `backend/src/modules/guardians/*` | evitar N+1 na resolucao de criancas vinculadas | sim |
| Guias locais | `backend/docs/ai/ARCHITECTURE.md`, `CODE_STYLE.md`, `QA.md` | manter estrutura e validacao corretas | sim |
| Handoffs existentes | `.agents/state/handoffs/TASK-021.md`, `.agents/state/handoffs/TASK-085.md` | reaproveitar decisoes de admin e exportacoes | sim |

## Risco de contexto

- medio
- estrategia: restringir a admin, users e guardians; sem reabrir front-end nem modulo clinico

## Status final

done

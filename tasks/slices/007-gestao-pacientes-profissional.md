# Slice 007 - Gestao de pacientes do profissional

## Status

done

## Objetivo de negocio

Listar, vincular por codigo, editar e inativar pacientes sob gestao, com anamnese.

## Entrega verificavel

Arvore isolada por vinculo; codigo unico; inativacao; sem exclusao.

## Fora de escopo

- Montagem de trilha
- Relatorios
- Pacientes de outros profissionais

## Perfil do projeto

- stack web escolhida: front-end (React/Vite)
- mobile: sim

## Stacks envolvidas

- front-end
- backend

## Contrato

- `contracts/openapi.yaml#/paths` de patients

## Referencia visual por stack

### Web

- tipo: artefato de design system
- fonte primaria: `design-system/front/Design_System_Evolente_Desktop.md` (pacientes)

### Mobile

- tipo: artefato de design system
- fonte primaria: `nao se aplica`

## Permissoes e atores

- Profissional com assinatura
- Isolamento por vinculo

## Casos de erro e borda

- Codigo inexistente
- Ja vinculado (premissa mono-vinculo)
- 403 cross-tenant

## Decisoes humanas confirmadas

- Stack web: React/Vite; Mobile: sim; Profissional multi-especialidade; Inativar (nao excluir); Gamificacao/jogos fora do escopo

## Premissas adotadas

- Gateway, valores e push a definir — abstrair
- DS documental governa tokens; sem prints nesta fase
- Conflito DS mobile (gamificacao/UI crianca) vs requisitos — prevalece requisito

## Tasks relacionadas

- `tasks/016-api-pacientes-profissional.md` - API pacientes
- `tasks/017-dashboard-profissional-pacientes-web.md` - UI pacientes
- `tasks/change-requests/045-paginacao-tabela-pacientes-web.md` - paginação na tabela de pacientes web
- `tasks/change-requests/046-coluna-responsavel-e-refino-paginacao-pacientes.md` - coluna de responsável e refino da paginação
- `tasks/change-requests/051-refinar-perfil-paciente-web.md` - refino visual incremental da página de perfil do paciente
- `tasks/change-requests/555-grafico-evolucao-diaria-perfil-paciente.md` - grafico diario individual no perfil da crianca — **done**
- `tasks/change-requests/074-corrigir-data-local-e-buscas-redundantes-em-pacientes.md` - correcoes pontuais de data local e menu de ações
- `tasks/change-requests/394-recarregar-progressos-descartados-pela-paginacao-de-pacientes-web.md` - progresso deixa de ficar preso em carregando ao paginar

## Dependencias do slice

- Slices 003, 004 e 005

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

- medio
- estrategia: carregar apenas secoes/paths citados nas tasks

## Observacoes de rastreabilidade

- Premissa: um paciente por profissional ate confirmacao contraria.
- Task 016 (API) e Task 017 (UI web) concluidas.
- Task 045 refinou a listagem web com paginação local sem alterar contrato de API.
- Task 046 expôs o responsável na listagem de pacientes e refinou a barra de paginação.
- Task 051 reorganizou visualmente o perfil do paciente com hero, painel lateral de vínculo e anamnese mais legível.
- Task 074 corrigiu timezone em datas puras e limpou buscas redundantes no portal de ações.
- Slice 007 fechado; trilha fica no Slice 008.
- Task 394 reabriu o slice apenas para corrigir o descarte de progressos em voo na paginação: o guard virou por geração de dados e os resultados por paciente passam a ser sempre aplicados.
- Task 555 adiciona o grafico diario individual no perfil da crianca, reusando trails/progress e o componente da Task 554.

## Status final

done

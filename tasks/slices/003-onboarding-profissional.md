# Slice 003 - Onboarding do profissional

## Status

done

## Objetivo de negocio

Permitir cadastro de profissional (individual ou clinica) e redirecionar ao pagamento antes do acesso completo.

## Entrega verificavel

Profissional cria conta e e enviado ao fluxo de assinatura sem acesso liberado.

## Fora de escopo

- Pagamento efetivo
- Gestao de pacientes
- Criacao de conteudos

## Perfil do projeto

- stack web escolhida: front-end (React/Vite)
- mobile: sim

## Stacks envolvidas

- front-end
- backend

## Contrato

- `contracts/openapi.yaml#/paths` de registro profissional

## Referencia visual por stack

### Web

- tipo: artefato de design system
- fonte primaria: `design-system/front/Design_System_Evolente_Desktop.md` (registro)

### Mobile

- tipo: artefato de design system
- fonte primaria: `nao se aplica`

## Permissoes e atores

- Visitante criando conta profissional

## Casos de erro e borda

- E-mail duplicado
- Campos de clinica ausentes
- Validacao de especialidade

## Decisoes humanas confirmadas

- Stack web: React/Vite; Mobile: sim; Profissional multi-especialidade; Inativar (nao excluir); Gamificacao/jogos fora do escopo

## Premissas adotadas

- Gateway, valores e push a definir — abstrair
- DS documental governa tokens; sem prints nesta fase
- Conflito DS mobile (gamificacao/UI crianca) vs requisitos — prevalece requisito

## Tasks relacionadas

- `tasks/008-api-cadastro-profissional.md` - API cadastro
- `tasks/009-fluxo-cadastro-profissional-web.md` - Fluxo web

## Dependencias do slice

- Slice 002

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

- baixo
- estrategia: carregar apenas secoes/paths citados nas tasks

## Observacoes de rastreabilidade

- API cadastro: Task 008 done
- Fluxo web: Task 009 done (redirect gate `/assinatura` sem liberar dashboard)
- Pagamento efetivo permanece no Slice 005

## Progresso das tasks relacionadas

- `tasks/008-api-cadastro-profissional.md` — done
- `tasks/009-fluxo-cadastro-profissional-web.md` — done

## Status final

done

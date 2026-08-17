# Slice 004 - Onboarding responsavel, crianca e anamnese

## Status

done

## Objetivo de negocio

Cadastro multi-etapa do responsavel e da crianca, anamnese, codigo unico e personalizacao pela pergunta 6.

## Entrega verificavel

Responsavel autenticavel, crianca com codigo unico, anamnese persistida e trilha sugerida pelas areas marcadas.

## Fora de escopo

- Pagamento
- Execucao mobile
- Montagem manual pelo profissional

## Perfil do projeto

- stack web escolhida: front-end (React/Vite)
- mobile: sim

## Stacks envolvidas

- front-end
- backend

## Contrato

- `contracts/openapi.yaml#/paths` de registro responsavel/crianca/anamnese

## Referencia visual por stack

### Web

- tipo: artefato de design system
- fonte primaria: `design-system/front/Design_System_Evolente_Desktop.md` (registro multi-etapa)

### Mobile

- tipo: artefato de design system
- fonte primaria: `nao se aplica`

## Permissoes e atores

- Visitante responsavel
- Crianca sem login

## Casos de erro e borda

- Menoridade
- CPF invalido
- Anamnese incompleta
- Pergunta 6 vazia

## Decisoes humanas confirmadas

- Stack web: React/Vite; Mobile: sim; Profissional multi-especialidade; Inativar (nao excluir); Gamificacao/jogos fora do escopo

## Premissas adotadas

- Gateway, valores e push a definir — abstrair
- DS documental governa tokens; sem prints nesta fase
- Conflito DS mobile (gamificacao/UI crianca) vs requisitos — prevalece requisito

## Tasks relacionadas

- `tasks/010-api-cadastro-responsavel-anamnese.md` - API cadastro+anamnese
- `tasks/011-fluxo-cadastro-responsavel-web.md` - Wizard web

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

- medio
- estrategia: carregar apenas secoes/paths citados nas tasks

## Observacoes de rastreabilidade

- Personalizacao usa pergunta 6; pode nascer vazia se catalogo ainda nao existir.
- API cadastro+anamnese entregue na Task 010 (`POST /guardians/register`).
- Wizard web entregue na Task 011 (`/cadastro/responsavel` → `/assinatura` com `patientCode`).

## Progresso das tasks relacionadas

- `tasks/010-api-cadastro-responsavel-anamnese.md` — done
- `tasks/011-fluxo-cadastro-responsavel-web.md` — done

## Status final

done

# Slice 005 - Assinatura e liberacao de acesso

## Status

done

## Objetivo de negocio

Exigir pagamento apos cadastro e liberar acesso completo somente apos confirmacao.

## Entrega verificavel

Sem assinatura ativa fica no gate; com assinatura acessa o restante.

## Fora de escopo

- Gateway/valores definitivos
- Gestao avancada de planos (slice 009)

## Perfil do projeto

- stack web escolhida: front-end (React/Vite)
- mobile: sim

## Stacks envolvidas

- front-end
- backend

## Contrato

- `contracts/openapi.yaml#/paths` de subscription

## Referencia visual por stack

### Web

- tipo: artefato de design system
- fonte primaria: `design-system/front/Design_System_Evolente_Desktop.md` (assinatura)

### Mobile

- tipo: artefato de design system
- fonte primaria: `nao se aplica`

## Permissoes e atores

- Profissional e responsavel
- Master isento (premissa)

## Casos de erro e borda

- Pagamento recusado/pendente
- Confirmacao ausente
- Acesso pago sem assinatura

## Decisoes humanas confirmadas

- Stack web: React/Vite; Mobile: sim; Profissional multi-especialidade; Inativar (nao excluir); Gamificacao/jogos fora do escopo

## Premissas adotadas

- Gateway, valores e push a definir — abstrair
- DS documental governa tokens; sem prints nesta fase
- Conflito DS mobile (gamificacao/UI crianca) vs requisitos — prevalece requisito

## Tasks relacionadas

- `tasks/012-api-assinatura-gate.md` - API gate
- `tasks/013-tela-pagamento-web.md` - Tela pagamento

## Dependencias do slice

- Slices 003 e 004

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

- Gateway e valores a definir: abstracao + fake provider.
- Slice 049 mantém o gate de pagamento após o cadastro só do responsável; o destino pós-`accessGranted` na web deixa de ser `/baixar-app` (Slice 050).
- API gate entregue na Task 012.
- UI gate entregue na Task 013 (`/assinatura`, login no gate, fake pay, CTA app para responsável).
- Gateway Asaas + regras de ciclo: Slice 039 (`tasks/slices/039-gateway-asaas-assinatura.md`) — não reabre este slice.

## Progresso das tasks relacionadas

- `tasks/012-api-assinatura-gate.md` — done
- `tasks/013-tela-pagamento-web.md` — done

## Status final

done

# Slice 055 - Cadastro de filho no perfil mobile

## Status

done

## Objetivo de negocio

Permitir que o responsável com assinatura ativa cadastre um filho diretamente pelo perfil do aplicativo, sem depender da área web.

## Entrega verificavel

- O perfil do responsável oferece a ação `Cadastrar filho`, inclusive no estado sem filhos.
- O app coleta dados da criança e a anamnese obrigatória e envia `POST /guardians/me/children`.
- Ao concluir, atualiza a lista, seleciona o novo filho e retorna ao perfil com confirmação.

## Fora de escopo

- Alterar contrato ou backend.
- Edição da anamnese, pagamento, trilha semanal e cadastro no fluxo público.

## Stacks envolvidas

- mobile

## Contrato

- `POST /guardians/me/children`
- `GET /guardians/me/children`

## Dependencias

- Slice 050 (contrato de criação de filho) — done
- Slice 051 (seleção persistida do filho) — done

## Referencia visual

- `design-system/mobile/Design_System_Evolente_App_Mobile.md` para formulários, cards e feedbacks.
- Lacuna: não há print do cadastro de filho no app; reutilizar a linguagem visual e componentes existentes do perfil, sem inferir o layout web.

## Contexto minimo recomendado

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`, `tasks/000-index.md`
- esta slice e Task 621

## Contexto sob demanda recomendado

| Gatilho | Fonte | Uso |
|---|---|---|
| Formulário mobile | `mobile/src/features/profile/**`, `mobile/src/shared/components/**` | rota e componentes reutilizáveis |
| Criação | `mobile/src/features/children/**` | service, query e seleção |
| Payload | `contracts/openapi.yaml` (`CreateGuardianChildRequest`) | validação e DTO |
| UI | Design system mobile | aderência visual |

## Status final

done

## Tasks relacionadas

- Task 621 — done (`tasks/change-requests/621-cadastro-filho-perfil-responsavel-mobile.md`)
- Task 622 — done (`tasks/change-requests/622-cta-cadastro-filho-seletor-mobile.md`)
- Task 623 — done (`tasks/change-requests/623-refinar-formulario-cadastro-filho-mobile.md`)

# Slice 047 - Trilha self-serve do responsável no mobile

## Status

done

## Atualizações relacionadas

- `tasks/change-requests/577-claymorphism-cards-trilha-mobile.md` — **done** (cards da Trilha com acabamento claymorphism).

## Objetivo de negocio

Permitir que o responsável, sem vínculo com profissional, monte e personalize a trilha semanal no mobile (biblioteca, dia a dia e geração pela anamnese), mantendo o modo execução quando houver vínculo profissional.

## Entrega verificavel

- Sem vínculo: empty state com gerar/biblioteca/começar do zero; editar dias; biblioteca; suggest anamnese
- Com vínculo: responsável também pode montar/editar (Task 506)
- Área Trilha com sub-abas **Trilhas** | **Biblioteca** (Task 503)

## Fora de escopo

- Atividade custom (upload)
- Profissional editar no mobile
- Responsável editar trilha do profissional

## Perfil do projeto

- stack web escolhida: front-end (React/Vite)
- mobile: sim

## Stacks envolvidas

- contracts
- backend
- mobile

## Contrato

- `contracts/openapi.yaml` — trails create/suggest/replace; WeeklyTrail.professionalUserId nullable; Child.hasActiveProfessionalLink

## Referencia visual por stack

### Mobile

- tipo: artefato de design system + pedido de estrutura self-serve
- fonte: `design-system/mobile/Design_System_Evolente_App_Mobile.md`

## Permissoes e atores

- Responsável da criança: pode montar/editar/sugerir a trilha (com ou sem vínculo)
- Com vínculo ativo **e** trilha existente: aviso de confirmação antes de gerar/alterar (Task 508)
- Profissional: montagem web inalterada
- Chip de autoria: `professionalUserId` indica se a semana foi criada pelo profissional

## Tasks relacionadas

- `tasks/change-requests/500-contrato-trilha-self-serve-responsavel.md`
- `tasks/change-requests/501-backend-trilha-self-serve-responsavel.md`
- `tasks/change-requests/502-mobile-trilha-self-serve-ui.md`
- `tasks/change-requests/503-mobile-abas-trilhas-biblioteca.md`
- `tasks/change-requests/504-mobile-icones-subabas-trilhas-biblioteca.md`
- `tasks/change-requests/505-mobile-refinar-ui-biblioteca-trilha.md`
- `tasks/change-requests/506-permitir-responsavel-montar-trilha.md`
- `tasks/change-requests/507-mobile-cards-biblioteca-estilo-master.md`
- `tasks/change-requests/508-aviso-trilha-propria-com-vinculo.md`
- `tasks/change-requests/548-demo-mobile-persistir-add-remove-trilha.md`
- `tasks/change-requests/551-patch-trilha-responsavel-canmanage.md` — done (PATCH status alinhado a `canManage`)

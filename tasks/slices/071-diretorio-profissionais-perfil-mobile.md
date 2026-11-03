# Slice 071 - Diretório de profissionais no perfil mobile do responsável

## Status

done

## Objetivo de negócio

Permitir que o responsável descubra profissionais cadastrados na Evolente a partir do perfil do app, no mesmo fluxo já existente na web.

## Entrega verificável

- No perfil do responsável há um card **Encontrar profissionais**.
- O card abre uma tela autenticada que lista profissionais via `GET /professionals`.
- A listagem cobre busca, seções Próximos/Outros, loading, erro, empty e contato por WhatsApp quando houver telefone.
- O vínculo continua pelo código da criança; a tela não solicita vínculo.

## Fora de escopo

- Alterar backend, OpenAPI ou a página web `/profissionais`
- Criar ou aprovar vínculo a partir do diretório
- Expor e-mail, CPF, CNPJ ou dados sensíveis
- Chat, agendamento ou mensagens in-app
- Página pública sem login

## Decisões confirmadas

- Entrada no mobile: card no perfil (não na home).
- Reutilizar o contrato já entregue no Slice 063 (`GET /professionals`).
- Linguagem visual: cards, tokens e hero do perfil/relatórios mobile; não copiar o layout desktop.
- Sem print específico desta tela.

## Perfil do projeto

- stack web escolhida: front-end (React/Vite)
- mobile: sim

## Stacks envolvidas

- mobile

## Contrato

- `GET /professionals` (já existente; papel responsável autenticado)

## Referência visual por stack

### Mobile

- tipo: artefato de design system
- fonte primária: `design-system/mobile/Design_System_Evolente_App_Mobile.md`
- fontes adjacentes: `HomeActionCard`, perfil do responsável, tela de relatórios
- lacuna: sem print do diretório; reutilizar cards/tokens existentes

### Web

- tipo: não se aplica (comportamento já entregue no Slice 063)

## Tasks relacionadas

- `tasks/change-requests/791-card-encontrar-profissionais-perfil-mobile.md`
- `tasks/change-requests/751-api-diretorio-profissionais-responsavel.md`
- `tasks/change-requests/752-pagina-encontrar-profissionais-web.md`

## Progresso

- Task 791 — done

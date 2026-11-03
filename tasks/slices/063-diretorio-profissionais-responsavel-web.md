# Slice 063 - Diretório de profissionais para o responsável (web)

## Status

done

## Objetivo de negócio

Permitir que o responsável descubra profissionais cadastrados na Evolente a partir da área de Filhos na web, sem depender apenas do vínculo iniciado pelo profissional via código.

## Entrega verificável

- Na sidebar do responsável há o item **Profissionais**, que abre o diretório.
- O item navega para uma página que lista profissionais cadastrados e elegíveis no sistema.
- A listagem consome um endpoint autenticado do contrato OpenAPI, com campos públicos seguros.
- Empty state, loading e erro ficam cobertos na página.

## Fora de escopo

- App mobile
- Solicitar ou criar vínculo a partir do diretório (continua o fluxo por código + aprovação do Slice 053)
- Expor e-mail pessoal, CPF, CNPJ ou dados sensíveis do profissional
- Chat, agendamento ou mensagens entre responsável e profissional
- Página pública (sem login) de profissionais
- Alterar o fluxo de cadastro do profissional

## Decisões confirmadas (a validar na revisão humana)

- O acesso fica na sidebar do responsável (item **Profissionais** → `/profissionais`), não no cabeçalho de Filhos.
- A página de destino é autenticada e restrita ao papel `responsavel` com `accessGranted`.
- Só entram profissionais com conta `active`, perfil completo e `accessGranted=true`.
- Campos exibidos: nome, avatar, especialidades, registro profissional (quando houver), tipo de prática e nome da clínica (quando houver).
- Busca simples por nome ou especialidade faz parte do slice.
- O vínculo permanece iniciado pelo profissional via código da criança; o diretório é só descoberta.

## Premissas adotadas

- Não há prints específicos desta tela; reutilizar shell, cards e tokens da área web do responsável.
- Telefone da clínica pode aparecer quando `practiceType=clinica`; telefone/e-mail pessoais do usuário profissional não.
- Paginação mínima (page/pageSize) no contrato para evitar listagens monolíticas.

## Perfil do projeto

- stack web escolhida: front-end (React/Vite)
- mobile: sim (fora deste slice)

## Stacks envolvidas

- contracts
- backend
- front-end

## Contrato

- `GET /professionals` (novo; papel responsável autenticado)
- Schemas de item/listagem do diretório

## Referência visual por stack

### Web

- tipo: artefato de design system
- fonte primária: `design-system/front/Design_System_Evolente_Desktop.md`
- fontes adjacentes: `front-end/src/pages/Main/Guardian/Children/`, shell `MainLayout`, cards da área do responsável
- lacuna: sem prints do diretório; não inventar produto visual novo

### Mobile

- tipo: não se aplica

## Tasks relacionadas

- `tasks/change-requests/751-api-diretorio-profissionais-responsavel.md`
- `tasks/change-requests/752-pagina-encontrar-profissionais-web.md`
- `tasks/change-requests/793-mover-encontrar-profissionais-sidebar-web.md`
- `tasks/change-requests/767-api-filtro-area-diretorio-profissionais.md`
- `tasks/change-requests/768-ui-filtro-area-diretorio-profissionais.md`
- `tasks/change-requests/769-opcoes-area-especialidades-cadastradas.md`
- `tasks/change-requests/771-paginacao-diretorio-profissionais.md`

## Progresso

- Task 751 — done
- Task 752 — done
- Task 753 — done (layout dos botões do cabeçalho Filhos)
- Task 754 — done (ícones no topo, CTAs embaixo)
- Task 767 — done (filtro por área, API)
- Task 768 — done (filtro por área, web)
- Task 769 — done (opções do filtro pelas especialidades cadastradas)
- Task 771 — done (paginação independente)
- Task 793 — done (item na sidebar; botão removido de Filhos)

## Contexto mínimo recomendado

- esta slice
- `tasks/000-index.md`
- página Filhos e rotas do responsável
- trecho de profissionais no OpenAPI

## Risco de contexto

médio — exige contrato + API + UI, mas o escopo é só listagem/descoberta

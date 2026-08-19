# Slice 049 - Cadastro público só do responsável

## Status

done

## Objetivo de negocio

O visitante cadastra apenas a conta do responsável e segue para o pagamento. Criança e anamnese saem do fluxo público.

## Entrega verificavel

- `POST /guardians/register` cria só o responsável, com `accessGranted=false`
- Wizard web `/cadastro/responsavel` pede só dados do responsável e cai em `/assinatura`
- Conta autenticável após o cadastro, mas o acesso completo continua bloqueado até o pagamento

## Fora de escopo

- Cadastro de filho (Slice 050)
- Área web autenticada do responsável (Slice 050)
- Seletor de filho no mobile (Slice 051)
- Mudança de preço, gateway ou ciclo de assinatura
- Fluxo do profissional `POST /patients` (continua criando responsável + criança + anamnese)

## Perfil do projeto

- stack web escolhida: front-end (React/Vite)
- mobile: sim

## Stacks envolvidas

- contracts
- backend
- front-end

## Contrato

- `contracts/openapi.yaml#/paths/~1guardians~1register`
- `contracts/openapi.yaml#/paths/~1guardians~1me~1children` (POST novo, usado pelo Slice 050)

## Referencia visual por stack

### Web

- tipo: artefato de design system
- fonte primaria: `design-system/front/Design_System_Evolente_Desktop.md` (auth, wizard, estados)
- lacuna: sem prints novos do cadastro só do responsável; reutilizar o wizard atual sem as etapas de criança/anamnese

### Mobile

- tipo: nao se aplica

## Permissoes e atores

- Visitante responsável (endpoint público)
- Criança continua sem login

## Casos de erro e borda

- Menoridade do responsável
- CPF/e-mail já cadastrados
- Senha fraca
- Pagamento recusado/pendente (já coberto pelo Slice 005/039)
- Contas antigas com filho criado no register atômico continuam válidas

## Decisoes humanas confirmadas

- Cadastro público tem apenas o responsável
- Ao finalizar o cadastro, o responsável cai no pagamento
- Stack web: React/Vite; mobile: sim

## Premissas adotadas

- Assinatura permanece **por conta do responsável**, não por filho
- Parentesco deixa de ser obrigatório no cadastro público (não há criança ainda); passa a ser campo do filho no Slice 050
- `POST /patients` do profissional **não** muda neste slice
- Sem limite de filhos declarado; não aplicar teto

## Tasks relacionadas

- `tasks/change-requests/556-contrato-cadastro-responsavel-sem-filho.md`
- `tasks/change-requests/557-api-cadastro-responsavel-e-filhos.md`
- `tasks/change-requests/558-wizard-cadastro-so-responsavel-web.md`

## Dependencias do slice

- Slice 004 (histórico do wizard atômico; este slice o substitui no fluxo público)
- Slice 005 / 039 (pagamento e gate)

## Contexto minimo recomendado

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- este slice

## Contexto sob demanda recomendado

| Gatilho | Fonte | Quando carregar | Obrigatorio? |
|---|---|---|---|
| Requisitos | `requirements/001-escopo-produto.md`, `requirements/002-regras-de-negocio.md` | atualizar fluxo do responsável | sim |
| API | `contracts/openapi.yaml` paths `/guardians/register` e schemas Guardian/Child | contrato | sim |
| UI web | `design-system/front/Design_System_Evolente_Desktop.md` | wizard | sim se UI |
| Front | `front-end/src/pages/Auth/RegisterGuardian/**` | wizard | sim se front |
| Back | `backend/src/modules/guardians/**` | register | sim se back |

## Risco de contexto

- medio
- estrategia: não reabrir o Slice 004 inteiro; alterar só o fluxo público e o contrato do register

## Observacoes de rastreabilidade

- Substitui o comportamento público das Tasks 010/011 sem reabrir o Slice 004 como `in_progress`.
- O POST de filho autenticado nasce no contrato deste slice, mas a UI fica no Slice 050.
- Task 556 (contrato + requirements) done.

## Progresso das tasks relacionadas

- Task 556 — done
- Task 557 — done
- Task 558 — done

## Status final

done

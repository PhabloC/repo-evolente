# Slice 051 - Seletor de filho no mobile

## Status

done

## Objetivo de negocio

No app, depois do login, o responsável escolhe qual filho vai gerenciar. Home, trilha, perfil e avisos passam a operar no filho selecionado.

## Entrega verificavel

- Após login com papel `responsavel` e `accessGranted`, a próxima tela é a seleção de filho
- Com 2+ filhos, a escolha é obrigatória antes do shell
- Com 1 filho, ainda mostra a seleção (decisão humana: “qual filho você vai gerenciar”)
- Com 0 filhos, empty state orienta cadastrar na web; não entra no shell da trilha
- Dá para trocar o filho depois, sem novo login

## Fora de escopo

- Cadastro de filho no mobile
- Área web do responsável (Slice 050)
- Alterar jogos, trilha self-serve ou avisos além de filtrar pelo `childId` selecionado
- Login da criança

## Perfil do projeto

- stack web escolhida: front-end (React/Vite)
- mobile: sim

## Stacks envolvidas

- mobile

## Contrato

- `GET /guardians/me/children` (já existe)
- endpoints de trilha/perfil/relatórios já parametrizados por `childId` / `patientId`

## Referencia visual por stack

### Mobile

- tipo: artefato de design system
- fonte primaria: `design-system/mobile/Design_System_Evolente_App_Mobile.md` (área do responsável, cards, estados)
- fonte adjacente: `design-system/mobile/prints/home-responsavel-referencia.png` (linguagem da home, não layout da seleção)
- lacuna: **não há print** da tela de seleção de filho; registrar a lacuna e usar cards/avatar já existentes no perfil (`ChildAvatar`), sem inventar um visual de outro produto

### Web

- tipo: nao se aplica

## Permissoes e atores

- Responsável autenticado com assinatura
- Sem `accessGranted`: permanece no fluxo de assinatura já existente no mobile

## Casos de erro e borda

- Lista vazia
- Falha ao carregar filhos
- Sessão expirada
- Filho selecionado some/inativado: voltar à seleção
- Conta antiga com um único filho

## Decisoes humanas confirmadas

- No mobile, a próxima tela após o login é selecionar qual filho gerenciar
- Cada filho tem trilha e perfil individuais

## Premissas adotadas

- A seleção persiste no storage local até o responsável trocar ou sair
- Cadastro de novo filho não entra no mobile neste slice (empty state aponta para a web)
- Home/trilha/perfil/avisos já existentes passam a ler o `childId` selecionado em vez de assumir o primeiro da lista
- Tasks 240/241 (copy no singular “Criança”) devem ser revistas para o filho selecionado, sem reabrir o visual da home

## Tasks relacionadas

- `tasks/change-requests/561-seletor-filho-pos-login-mobile.md`

## Dependencias do slice

- Slice 049 (conta pode existir sem filho)
- Slice 010 (shell do responsável)
- Slice 047 (trilha por criança)

## Contexto minimo recomendado

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- este slice

## Contexto sob demanda recomendado

| Gatilho | Fonte | Quando carregar | Obrigatorio? |
|---|---|---|---|
| UI mobile | `design-system/mobile/Design_System_Evolente_App_Mobile.md` | tela seleção | sim |
| Print adjacente | `design-system/mobile/prints/home-responsavel-referencia.png` | linguagem visual | nao |
| API | `GET /guardians/me/children` | lista | sim |
| Shell atual | `mobile/src/features/shell/**`, perfil, trilha | encaixe pós-seleção | sim |

## Risco de contexto

- baixo/medio
- estrategia: uma tela nova + persistência do `childId`; não redesenhar a home

## Observacoes de rastreabilidade

- `GET /guardians/me/children` já existe; o app hoje assume um filho (copy singular nas Tasks 240/241).

## Progresso das tasks relacionadas

- Task 561 — done

## Status final

done

## Correcoes posteriores

- Task 589 - done (cache de filhos isolado por responsável).

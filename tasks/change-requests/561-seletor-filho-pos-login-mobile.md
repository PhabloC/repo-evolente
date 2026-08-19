# Task 561 - Mobile: selecionar o filho após o login

## Status

done

## Tipo

mobile

## Stacks envolvidos

- mobile

## Perfil do projeto

- stack web escolhida: front-end (React/Vite)
- mobile: sim

## Contrato

- `GET /guardians/me/children`

## Modo de execucao

single-stack

## Referencia de design system

### Stack de referencia visual

mobile

### Tipo de referencia visual

artefato de design system

### Fonte primaria visual

- `design-system/mobile/Design_System_Evolente_App_Mobile.md`
- adjacente: `design-system/mobile/prints/home-responsavel-referencia.png` (tom da área do responsável, não o layout da seleção)

### Regra de aderencia visual

- Tela nova sem print: usar cards, avatar da criança (`ChildAvatar`) e tokens já da home/perfil
- Não importar UI web
- Registrar lacuna do print da seleção

## Contexto de negocio

### Por que

O app assume um filho (copy no singular). Com vários filhos, o responsável precisa escolher quem gerenciar.

### O que

Depois do login, mostrar a seleção de filho; persistir a escolha; home, trilha, perfil e avisos usam esse `childId`.

### Comportamento esperado

- Login `responsavel` + `accessGranted` → tela “Qual filho você vai gerenciar?”
- Lista todos os filhos (nome, avatar, código)
- 0 filhos: empty state dizendo para cadastrar na web; sem entrar no tab shell
- 1 ou mais: seleção explícita (também com um filho só)
- Ação para trocar de filho a partir do perfil ou de um atalho no shell, voltando à seleção
- Persistência local da escolha até logout ou troca
- Se o filho persistido não existir mais, volta à seleção

### Fora de escopo

- Cadastrar filho no app
- Alterar visual da home além de amarrar o filho selecionado
- Web

## Slice vertical

### Identificador do slice

Slice 051 - Seletor de filho no mobile

### Arquivo do slice

- `tasks/slices/051-seletor-filho-mobile.md`

## Permissoes

- Responsável com assinatura
- Sem pagamento: fluxo de gate já existente no mobile

## Casos de erro mapeados

- Loading / erro da lista
- Lista vazia
- Filho persistido inválido
- Sessão expirada

## Decisoes humanas confirmadas

- Após o login no app, a próxima tela é selecionar o filho

## Premissas adotadas pela IA

- Persistência em storage local (mesmo mecanismo de sessão já usado no app)
- Cadastro de filho continua só na web neste planejamento
- Copy das Tasks 240/241 (singular) passa a refletir o filho selecionado, sem reabrir o layout da home

## Criterios de aceite

- [x] Pós-login mostra a seleção antes da home
- [x] Trilha/perfil/home usam o `childId` escolhido
- [x] Dá para trocar de filho sem novo login
- [x] Empty state sem filhos não abre a trilha
- [x] Lint, typecheck e testes da seleção ok
- [x] Acessibilidade: lista selecionável, estado vazio anunciado

## Casos de borda

- Um filho
- Vários filhos
- Zero filhos
- Relogin com escolha anterior válida

## Contexto mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`, `tasks/000-index.md`
- esta task, Slice 051, Task 557
- `mobile/docs/ai/ACCESSIBILITY.md` (se existir; senão `mobile/docs/ai/AGENTS.md`)

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| DS mobile | `design-system/mobile/Design_System_Evolente_App_Mobile.md` | tela | sim |
| Shell | `mobile/src/features/shell/**`, rotas pós-auth | encaixe | sim |
| Children API | client de `GET /guardians/me/children` já no app | lista | sim |
| Perfil | `mobile/src/features/profile/**` | troca de filho | sim |

## Orçamento de contexto

- medio
- estrategia de reducao: não reabrir jogos nem self-serve da trilha; só seleção + binding do `childId`

## Dependencias

- Task 557 (conta pode não ter filhos; lista já existia, mas o register novo precisa estar estável)

## Resultado da execucao

### Resumo por stack

- **mobile**: após login de responsável, o app mostra “Qual filho você vai gerenciar?” antes do tab shell. A escolha persiste por `userId` no AsyncStorage. Home, trilha e relatórios usam o `childId` selecionado. Sem filhos, empty state aponta para a web e o shell da trilha não abre. Troca de filho no perfil, sem novo login.

### Relação com o slice

- Fecha o Slice 051.

### Decisões técnicas

- Feature `children`: storage, store, query, tela e regras puras de view state.
- Gate no `RootNavigator`: sem `selectedChildId` válido (ou com `forceSelect`) só existe `SelectChild`.
- Um filho ainda exige toque explícito; não há auto-seleção.
- Relogin restaura a escolha persistida se o filho ainda existir; filho inválido volta à seleção.
- `GET /guardians/me/children` reutilizado; trilha deixa de assumir `items[0]`.

### Relação com o contrato

- Consome `GET /guardians/me/children` já existente. Sem path novo.

### Relação com a referência visual

- Cards, avatar (`ChildAvatar`) e tokens da área do responsável.
- Lacuna: sem print da seleção; header laranja + lista de cards, sem importar UI web.

## Contexto utilizado

### Contexto mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`, `tasks/000-index.md`
- esta task, Slice 051, handoff 560
- `mobile/docs/ai/AGENTS.md`, `ARCHITECTURE.md`, `MOBILE_PATTERNS.md` (não há `ACCESSIBILITY.md` local)

### Contexto sob demanda

| Fonte | Gatilho | Uso |
|---|---|---|
| DS mobile | tela | paleta, cards, empty, alvos 44px |
| `RootNavigator`, shell, profile | encaixe | gate e troca |
| `GET /guardians/me/children` | lista | `childrenService` |
| `trailService` | binding | `childId` nas trilhas |

### Evitado

- cadastro de filho no app
- jogos / self-serve da trilha além do `childId`
- web

## Handoff

- Caminho: `.agents/state/handoffs/TASK-561.md`
- Próximo contexto: nenhum obrigatório neste lote; o fluxo 556–561 está fechado

## Arquivos alterados

- `mobile/src/features/children/**`
- `mobile/src/routes/RootNavigator.tsx`
- `mobile/src/routes/params.ts`
- `mobile/src/config/linking.ts`
- `mobile/src/features/trail/services/trailService.ts`
- `mobile/src/features/trail/hooks/useTrailToday.ts`
- `mobile/src/features/shell/screens/ResponsavelHomeScreen.tsx`
- `mobile/src/features/shell/screens/ResponsavelProfileScreen.tsx`
- `mobile/src/features/shell/screens/GuardianReportsScreen.tsx`
- `tasks/change-requests/561-seletor-filho-pos-login-mobile.md`
- `tasks/slices/051-seletor-filho-mobile.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-561.md`

## Validacoes executadas

- eslint dos arquivos alterados — passou
- jest `src/features/children` — 14 testes passaram
- `tsc --noEmit` — falhas **pré-existentes** (admin, auth, jogos, trail library); nenhum erro nos arquivos desta task

## Qualidade estrutural

- Tipos em `features/children/types/`
- Utils em `features/children/utils/` e `storage/`
- Store Zustand para escolha compartilhada
- Pendência residual: a tela de seleção reusa `ChildAvatar` e `HomeActionCard` do shell (pedido da task)

## Aderencia ao design system

- Fonte: `design-system/mobile/Design_System_Evolente_App_Mobile.md` (artefato)
- Print adjacente da home usado só como tom, não como layout da seleção
- Lacuna registrada: sem print da tela de seleção

## Acessibilidade aplicada

- Cards da lista com `accessibilityRole="button"` e nome (filho + código)
- Empty state com `accessibilityLiveRegion="polite"` e `accessibilityRole="text"`
- Loading com `accessibilityLabel`
- Alvos de toque via cards existentes da área do responsável

## Pendencias pos-task

- Nenhuma desta task. `tsc` global do mobile continua com erros antigos fora do escopo.

## Status final

done

# Task 095 - Lucide React Native como biblioteca padrao de icones mobile

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

- nao se aplica

## Modo de execucao

single-stack

## Referencia de design system

### Stack de referencia visual

mobile

### Tipo de referencia visual

artefato de design system

### Fonte primaria visual

- `design-system/mobile/Design_System_Evolente_App_Mobile.md` (tom visual; icones nao padronizados hoje)

## Origem da solicitacao

Pedido do usuario para adotar a biblioteca de icones Lucide no mobile, espelhando o padrao ja adotado na web (Task 027 / Slice 013).

## Objetivo

Instalar `lucide-react-native` (com peer `react-native-svg`), documentar como padrao no mobile e migrar os icones ad-hoc da auth (email, lock, eye).

## Escopo

- Adicionar dependencias `lucide-react-native` e `react-native-svg` (autorizadas nesta task)
- Documentar em `mobile/docs/ai/CODE_STYLE.md`
- Substituir icones View-based em `AuthFieldIcon` e `PasswordVisibilityIcon` por Lucide
- Validar lint/typecheck/test

## Fora de escopo

- Front-end / outras libs de icone
- Refator amplo de UI nao relacionada
- Migrar assets de marca (logo, ilustracoes) para Lucide

## Dependencias

- Task 094 (login mobile fiel ao print) — done
- Task 027 (precedente web Lucide) — done (referencia de padrao, nao bloqueante de codigo)

## Slice vertical

### Identificador do slice

Slice 020 - Lucide como padrao de icones (mobile)

### Arquivo do slice

- `tasks/slices/020-lucide-icones-mobile.md`

## Contexto mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/020-lucide-icones-mobile.md`
- `.agents/state/handoffs/TASK-094.md` (quando existir)

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatorio? |
|---|---|---|---|
| Padrao mobile | `mobile/docs/ai/CODE_STYLE.md` | documentar regra | sim |
| Migracao auth | `mobile/src/features/auth/components/AuthFieldIcon.tsx` | trocar icones | sim |
| Migracao auth | `mobile/src/features/auth/components/PasswordVisibilityIcon.tsx` | trocar icones | sim |
| Dependencias | `mobile/package.json` | instalar libs | sim |

## Orçamento de contexto

- Risco: baixo
- Estrategia: nao carregar front-end/backend/openapi; nao recarregar print de login salvo se icones afetarem layout de forma critica

## Criterios de conclusao

- [x] `lucide-react-native` e `react-native-svg` no package.json
- [x] Regra de padrao documentada em CODE_STYLE
- [x] AuthFieldIcon / PasswordVisibilityIcon sem Views ad-hoc de icone
- [x] lint/typecheck/test ok

## Instrucoes de implementacao

1. Em `mobile`, instalar com Expo: `npx expo install react-native-svg lucide-react-native`
2. Documentar: import nomeado de `lucide-react-native`; icones decorativos com `accessibilityElementsHidden` / `importantForAccessibility="no-hide-descendants"`; controles so-icone com `accessibilityLabel`; tamanho via prop `size`; `strokeWidth` tipico 2; cor via `color` e tokens do tema
3. Migrar: Mail, Lock, Eye / EyeOff
4. Simplificar styles dos componentes de icone (wrapper minimo se necessario)
5. Nao misturar com `lucide-react` (web)

## Validacao esperada

- `cd mobile && npm run lint`
- `cd mobile && npm run typecheck`
- `cd mobile && npm run test`

## Entregaveis esperados

- Dependencia + docs + icones auth migrados + handoff TASK-095

## Resultado da execucao

### Resumo por stack

- **mobile**: `lucide-react-native` e `react-native-svg` instalados; padrao documentado em CODE_STYLE; icones da auth migrados para Mail/Lock/Eye/EyeOff.

### Relação com o slice

- Slice 020 concluído.

### Decisões técnicas

- Dependencias autorizadas nesta task via `npx expo install`.
- Icones auth: Mail, Lock, Eye (senha oculta), EyeOff (senha visivel).
- Controles so-icone continuam com `accessibilityLabel` no Pressable; icones decorativos marcados como hidden para a11y.
- Assets de marca (logo, ilustracoes) permanecem fora do Lucide.

### Trade-offs

- Migracao limitada aos icones ad-hoc da auth (unico uso atual de Views como icone).

## Contexto utilizado

### Contexto mínimo

- AGENTS, GUIDE, context-map, index, esta task, slice 020, handoff TASK-094

### Contexto sob demanda

| Fonte | Gatilho | Uso |
|---|---|---|
| CODE_STYLE | padrao | secao Icones |
| AuthFieldIcon / PasswordVisibilityIcon | migracao | troca Views → Lucide |
| package.json | deps | instalacao Expo |

### Evitado

- front-end/, backend/, openapi, print de login (layout nao alterado alem dos glifos)

## Handoff

- Caminho: `.agents/state/handoffs/TASK-095.md`

## Arquivos alterados

- `mobile/package.json` / `mobile/package-lock.json`
- `mobile/src/features/auth/components/AuthFieldIcon.tsx`
- `mobile/src/features/auth/components/AuthFieldIcon.styles.ts`
- `mobile/src/features/auth/components/PasswordVisibilityIcon.tsx`
- `mobile/src/features/auth/components/PasswordVisibilityIcon.styles.ts`
- `mobile/docs/ai/CODE_STYLE.md`
- `tasks/change-requests/095-lucide-icones-mobile.md`
- `tasks/slices/020-lucide-icones-mobile.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-095.md`

## Validacoes executadas

- lint ok
- typecheck ok
- test ok

## Pendencias pos-task

- Nenhuma obrigatoria; novas telas mobile devem usar Lucide

## Status final

done

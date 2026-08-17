# Handoff - Task 095

## Task

- identificador: 095
- título: Lucide React Native como biblioteca padrao de icones mobile
- tipo: mobile
- modo de execução: single-stack
- status final: done

## Slice vertical

- identificador: Slice 020 - Lucide como padrao de icones (mobile)
- objetivo de negócio: padronizar icones mobile com Lucide, alinhado ao padrao web
- entrega verificável: deps instaladas, regra em CODE_STYLE, icones auth migrados
- status do slice: done

## Decisões preservadas

- decisão: usar `lucide-react-native` + peer `react-native-svg` (via Expo)
- motivo: equivalente oficial da Lucide no React Native; ja padronizado na web com `lucide-react`
- impacto: novas telas devem importar de `lucide-react-native`, nunca de `lucide-react`

- decisão: migrar apenas AuthFieldIcon e PasswordVisibilityIcon
- motivo: unicos icones ad-hoc View-based na auth
- impacto: styles dos wrappers reduzidos a container 24x24

- decisão: Eye quando senha oculta; EyeOff quando senha visivel
- motivo: convencao padrao de toggle de senha
- impacto: Pressable ja possui accessibilityLabel; icone fica decorativo

## Contexto utilizado

### Contexto mínimo lido

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`
- `tasks/000-index.md`, `tasks/change-requests/095-lucide-icones-mobile.md`
- `tasks/slices/020-lucide-icones-mobile.md`
- `.agents/state/handoffs/TASK-094.md`

### Contexto sob demanda carregado

| Fonte | Gatilho | Uso |
|---|---|---|
| `mobile/docs/ai/CODE_STYLE.md` | padrao | secao Icones |
| `AuthFieldIcon` / `PasswordVisibilityIcon` | migracao | troca para Lucide |
| `mobile/package.json` | deps | instalacao |

### Contexto evitado

| Fonte | Motivo |
|---|---|
| front-end / openapi / backend | task estritamente mobile |
| print de login | layout nao exigiu reabrir fidelidade visual |

## Resultado por stack

- mobile: Lucide adotado como padrao; auth migrada; lint/typecheck/test ok

## Arquivos alterados

- `mobile/package.json`, `mobile/package-lock.json`
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

- `npm run lint` ok
- `npm run typecheck` ok
- `npm run test` ok

## Pendencias

- Nenhuma

## Proxima acao sugerida

- Em novas telas mobile, preferir icones Lucide nomeados com tokens de cor do tema

## Proximo contexto recomendado

- Task/tela mobile que precise de novos icones
- Evitar: front-end Lucide, openapi, backend

## Contexto que nao deve ser carregado

- `lucide-react` / docs do front-end para implementar icones mobile
- OpenAPI / backend

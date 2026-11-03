# Handoff - Task 789

## Task

- identificador: 789
- título: Versão sempre visível no login mobile
- tipo: mobile
- modo de execução: single-stack
- status final: done

## Slice vertical

- identificador: Slice 002
- objetivo de negócio: versão da build sempre visível no login
- entrega verificável: rodapé reservado; conteúdo acima sobe

## Decisões preservadas

- decisão: versão fora do `loginForm`, footer `flexShrink: 0`
- motivo: o cluster do formulário + CTA estourava e o canvas cortava o overflow
- impacto: se faltar altura, corta hero/nuvem, não a versão

- decisão: `paddingBottom` com `insets.bottom` (mín. 8)
- motivo: `Screen` só aplica safe area em top/left/right
- impacto: versão fica acima da home indicator

## Contexto utilizado

### Contexto mínimo lido

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`
- `tasks/000-index.md`, Task 789, Slice 002

### Contexto sob demanda carregado

| Fonte | Gatilho | Uso |
|---|---|---|
| `SignInScreen.tsx` / `styles.ts` | layout | rodapé e compactação |
| `Screen/index.tsx` | safe area | edge bottom ausente |
| `TASK-788.md` | overflow após CTA | causa |

### Contexto evitado

| Fonte | Motivo |
|---|---|
| front-end / backend / OpenAPI | sem mudança |

## Resultado por stack

- mobile: versão fixa no rodapé do login

## Arquivos alterados

- `mobile/src/features/auth/screens/SignInScreen.tsx`
- `mobile/src/features/auth/screens/styles.ts`
- task 789, índice, slice 002, este handoff

## Validações executadas

- eslint dos arquivos do login — passou

## Pendências ou bloqueios

- conferir no Expo que a versão não some atrás da barra do sistema

## Próxima ação sugerida

- recarregar o login no aparelho/emulador

## Próximo contexto recomendado

- `mobile/src/features/auth/screens/SignInScreen.tsx`

## Contexto que não deve ser carregado na próxima etapa

- fonte: Asaas / contrato
- motivo: fora desta task

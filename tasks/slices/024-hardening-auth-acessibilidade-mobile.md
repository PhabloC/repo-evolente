# Slice 024 - Hardening de auth, storage e acessibilidade mobile

## Status

done

## Objetivo de negocio

Endurecer comportamentos de sessao e armazenamento local do app mobile e melhorar a leitura por tecnologias assistivas nos principais cards da home, sem alterar o fluxo funcional do produto.

## Entrega verificavel

- `TextField` compartilhado aceita `ref` para permitir foco programatico entre campos de auth
- Storages locais de biometria e sessao tratam falhas e preservam compatibilidade com chaves antigas
- Cards e atalhos da home anunciam descricao e badges por leitor de tela
- `app.json` deixa de declarar `expo-status-bar` como plugin invalido

## Fora de escopo

- Mudancas visuais amplas no auth ou na home
- Novos fluxos de navegacao
- Alteracoes em backend ou contrato OpenAPI
- Refatoracao geral de todos os storages/components compartilhados

## Perfil do projeto

- stack web escolhida: front-end (React/Vite)
- mobile: sim

## Stacks envolvidas

- mobile

## Contrato

- nao se aplica

## Referencia visual por stack

### Mobile

- tipo: continuidade de interface existente
- fonte primaria: componentes e telas mobile ja consolidados nas slices 021, 022 e 023

## Permissoes e atores

- master e responsavel no mobile

## Casos de erro e borda

- Falha de `AsyncStorage` por indisponibilidade/permissao
- Sessao legada salva na chave antiga do `SecureStore`
- Campo de senha sem foco programatico ao avancar pelo teclado
- Leitor de tela anunciar apenas o titulo/rotulo e omitir badges e descricoes
- Resolucao de config Expo falhar por plugin declarado incorretamente

## Decisoes humanas confirmadas

- O code review em `ajustes_mobile.md` deve ser tratado como change request adicional antes da implementacao
- Compatibilidade de sessao existente deve ser preservada durante a migracao de chave

## Tasks relacionadas

- `tasks/change-requests/121-login-biometrico-mobile.md` - Login biometrico mobile — **done**
- `tasks/change-requests/123-home-responsavel-fiel-ao-print-referencia.md` - Home do responsavel fiel ao print — **done**
- `tasks/change-requests/127-refresh-automatico-sessao-mobile.md` - Refresh automatico da sessao no mobile — **done**
- `tasks/change-requests/149-eliminar-faixa-branca-nav-bar-android-abaixo-da-tabbar-mobile.md` - Ajuste recente de configuracao/app shell — **done**
- `tasks/change-requests/150-hardening-auth-acessibilidade-mobile.md` - Hardening de auth, storage e acessibilidade mobile — **done**

## Dependencias do slice

- Slices 021, 022 e 023

## Contexto minimo recomendado

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- este slice
- `tasks/change-requests/150-hardening-auth-acessibilidade-mobile.md`

## Contexto sob demanda recomendado

| Gatilho | Fonte | Quando carregar | Obrigatorio? |
|---|---|---|---|
| Componentes auth compartilhados | `mobile/src/shared/components/TextField/*` | implementar `forwardRef` sem quebrar API publica | sim |
| Storage local de auth | `mobile/src/features/auth/storage/biometricPreferenceStorage.ts`, `mobile/src/shared/storage/secureStorage.ts` | endurecer falhas e migracao de chave | sim |
| Home mobile com UI | `mobile/src/features/shell/components/HomeActionCard/*`, `mobile/src/features/shell/components/HomeShortcutTile/*` | enriquecer labels de acessibilidade | sim |
| Config Expo | `mobile/app.json` | remover plugin invalido | sim |
| Padroes locais da stack | `mobile/docs/ai/ARCHITECTURE.md`, `mobile/docs/ai/CODE_STYLE.md`, `mobile/docs/ai/COMPONENT_REUSE.md`, `mobile/docs/ai/QA.md` | garantir organizacao e validacao | sim |
| Handoffs recentes | `.agents/state/handoffs/TASK-127.md`, `.agents/state/handoffs/TASK-149.md` | reaproveitar decisoes de sessao e config | sim |

## Risco de contexto

- baixo
- estrategia: restringir a componentes compartilhados, storages de auth, cards da home e `app.json`, sem reabrir telas/fluxos completos

## Status final

done

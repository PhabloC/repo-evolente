# Slice 021 - Login biometrico mobile

## Status

done

## Objetivo de negocio

Permitir que o responsavel/master ative login por biometria (digital/Face ID) apos o primeiro login com senha e, nas proximas sessoes, entre com biometria ou senha.

## Entrega verificavel

- Apos login com senha bem-sucedido, o app oferece ativar biometria quando o dispositivo suportar
- Com biometria ativa e sessao salva, o usuario pode desbloquear o acesso via prompt biometrico
- Login com e-mail/senha continua disponivel como fallback
- Logout limpa a sessao local e a preferencia de biometria

## Fora de escopo

- Alteracoes no backend ou contrato OpenAPI
- Login biometrico na web
- Cadastro de conta
- Troca de usuario sem logout explicito

## Perfil do projeto

- stack web escolhida: front-end (React/Vite)
- mobile: sim

## Stacks envolvidas

- mobile

## Contrato

- nao se aplica (biometria destrava tokens locais ja persistidos; nao ha endpoint novo)

## Referencia visual por stack

### Mobile

- tipo: artefato de design system
- fonte primaria: `design-system/mobile/Design_System_Evolente_App_Mobile.md` (login/acesso)
- UI adicional: prompt nativo do sistema + oferta pos-login (Alert/modal) + CTA de biometria na tela de login, alinhados ao shell auth existente

## Permissoes e atores

- master e responsavel no mobile

## Casos de erro e borda

- Dispositivo sem hardware biometrico
- Biometria nao cadastrada no sistema
- Usuario recusa ativar biometria
- Falha/cancelamento do prompt biometrico
- Sessao expirada/invalida apos unlock biometrico
- Logout limpa tokens e preferencia

## Decisoes humanas confirmadas

- Fluxo padrao mobile: oferta apos login com senha; depois biometria ou senha
- Sem mudanca de API: tokens permanecem no SecureStore

## Tasks relacionadas

- Task 121 - Login com biometria (digital/Face ID) no mobile

## Contexto minimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- este slice
- `tasks/change-requests/121-login-biometrico-mobile.md`

## Contexto sob demanda

- `design-system/mobile/Design_System_Evolente_App_Mobile.md`
- `mobile/docs/ai/AGENTS.md`
- `mobile/docs/ai/ARCHITECTURE.md`
- `mobile/docs/ai/CODE_STYLE.md`
- `mobile/docs/ai/QA.md`
- `mobile/src/features/auth/`
- `mobile/src/shared/storage/secureStorage.ts`
- `mobile/src/app/AppGate.tsx`
- `.agents/state/handoffs/TASK-120.md`

## Orcamento de contexto

- 12 fontes
- estrategia de reducao: restringir ao fluxo de sessao/login mobile; nao reabrir visual amplo do auth nem outras stacks

## Risco de contexto

- medio — toca boot da sessao (AppGate) e tela de login; manter mudancas locais a auth/storage

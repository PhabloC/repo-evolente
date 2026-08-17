# Task 121 - Login com biometria (digital/Face ID) no mobile

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

- nao se aplica (biometria destrava sessao local no SecureStore; sem endpoint novo)

## Modo de execucao

single-stack

## Slice vertical

- Slice 021 - Login biometrico mobile
- `tasks/slices/021-login-biometrico-mobile.md`

## Objetivo

Implementar o fluxo padrao de biometria no mobile: apos login com senha, oferecer cadastro da digital/Face ID; nas proximas aberturas, permitir entrar com biometria ou com e-mail/senha.

## Contexto minimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- `tasks/change-requests/121-login-biometrico-mobile.md`
- `tasks/slices/021-login-biometrico-mobile.md`

## Contexto sob demanda

- `design-system/mobile/Design_System_Evolente_App_Mobile.md`
- `mobile/docs/ai/AGENTS.md`
- `mobile/docs/ai/ARCHITECTURE.md`
- `mobile/docs/ai/CODE_STYLE.md`
- `mobile/docs/ai/QA.md`
- `.agents/state/handoffs/TASK-120.md`
- `mobile/src/features/auth/services/authService.ts`
- `mobile/src/features/auth/hooks/useSignInForm.ts`
- `mobile/src/features/auth/screens/SignInScreen.tsx`
- `mobile/src/features/auth/store/useSessionStore.ts`
- `mobile/src/shared/storage/secureStorage.ts`
- `mobile/src/app/AppGate.tsx`
- `mobile/app.json` (ou `app.config.*`)

## Orcamento de contexto

- 14 fontes
- estrategia de reducao: limitar a sessao, preferencia biometrica e UI minima no SignIn; nao reabrir layout/copy do auth

## Criterios de aceite

- Instalar e integrar `expo-local-authentication`
- Declarar permissao iOS de Face ID quando necessario
- Apos login com senha, se o dispositivo tiver biometria disponivel e a preferencia ainda nao estiver ativa, perguntar se deseja ativar
- Preferencia e sessao persistidas de forma segura (SecureStore)
- Com biometria ativa e sessao salva, o boot nao autentica automaticamente: o usuario desbloqueia via biometria ou senha
- CTA de biometria na tela de login quando disponivel
- Fallback para e-mail/senha em falha, cancelamento ou indisponibilidade
- Logout limpa sessao e preferencia de biometria
- Cobertura de testes unitarios do servico/preferencia biometrica

## Dependencias

- Task 007 (auth mobile)
- Task 120 (API local auth)

## Fora de escopo

- Backend/OpenAPI
- Web
- Configuracao de biometria em tela de perfil (pode ser CR futuro)

## Resultado da execucao

- Integrado `expo-local-authentication` com plugin e `NSFaceIDUsageDescription`
- Apos login com senha, Alert oferece ativar biometria quando o hardware estiver disponivel
- Preferencia biométrica persistida no SecureStore; sessao continua no SecureStore existente
- Com biometria ativa, AppGate nao hidrata a sessao automaticamente e monta a navegacao apenas apos a splash encerrar; unlock via prompt/CTA ou senha
- Logout limpa sessao e preferencia biométrica
- Testes unitarios para storage e regras do biometricService

## Contexto utilizado

- Contexto minimo lido: `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`, `tasks/000-index.md`, esta task e `tasks/slices/021-login-biometrico-mobile.md`
- Contexto sob demanda carregado: docs AI mobile (Architecture/Code Style), fluxo auth mobile, SecureStore, AppGate, `app.json`
- Fontes evitadas: `requirements/`, `contracts/openapi.yaml`, stacks web/backend, redesign visual amplo do auth
- Reducao de escopo: UI minima (Alert nativo + botao ghost) sem reabrir layout do login

## Handoff

- `.agents/state/handoffs/TASK-121.md`
- Decisoes preservadas: biometria so destrava tokens locais; oferta unica pos-login; boot com lock biometrico; logout limpa preferencia
- Proximo contexto recomendado: `biometricService.ts` / `useBiometricSignIn.ts` se houver toggle em perfil

## Arquivos alterados

- `mobile/package.json`
- `mobile/package-lock.json`
- `mobile/app.json`
- `mobile/src/app/AppGate.tsx`
- `mobile/src/features/auth/services/authService.ts`
- `mobile/src/features/auth/services/biometricService.ts`
- `mobile/src/features/auth/services/biometricService.test.ts`
- `mobile/src/features/auth/storage/biometricPreferenceStorage.ts`
- `mobile/src/features/auth/storage/biometricPreferenceStorage.test.ts`
- `mobile/src/features/auth/hooks/useBiometricSignIn.ts`
- `mobile/src/features/auth/hooks/useSignInForm.ts`
- `mobile/src/features/auth/components/SignInForm.tsx`
- `mobile/src/features/auth/components/styles.ts`
- `mobile/src/features/auth/screens/SignInScreen.tsx`
- `tasks/change-requests/121-login-biometrico-mobile.md`
- `tasks/slices/021-login-biometrico-mobile.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-121.md`

## Validacoes executadas

- eslint em `src/features/auth/**` e `src/app/AppGate.tsx` - ok
- `npm run typecheck` - ok
- `npm run test` - ok

## Pendencias pos-task

- Validar Face ID/digital em dispositivo fisico
- Toggle de biometria em perfil permanece como CR futuro

## Status final

done

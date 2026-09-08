# Slice 012 - Login visual e acesso livre (web)

## Status

done

## Objetivo de negocio

Alinhar a pagina de login web ao print de referencia e permitir exploracao da plataforma sem exigir autenticacao real nesta fase.

## Entrega verificavel

- Pagina `/login` visualmente aderente ao print desktop.
- Logos em `front-end/src/assets/` aplicadas na UI.
- Navegacao na area principal sem obrigar login (bypass temporario de guards).

## Fora de escopo

- Alterar API de autenticacao
- Redesign de recovery/reset/cadastro
- Mobile
- Remover fluxo de login real (manter formulario funcional)

## Perfil do projeto

- stack web escolhida: front-end (React/Vite)
- mobile: sim (fora deste slice)

## Stacks envolvidas

- front-end

## Contrato

- nao se aplica (sem mudanca de contrato)

## Referencia visual por stack

### Web

- tipo: prints de telas
- fonte primaria: `design-system/front/prints/login-desktop.png`
- apoio: `design-system/front/Design_System_Evolente_Desktop.md` (tokens/cores)
- assets: `front-end/src/assets/logo-wordmark.webp`, `front-end/src/assets/logo-seal.webp`

### Telas/estados cobertos pelo print

- Login desktop: layout split (branding + card), formulario, lembrar-me, esqueci senha, CTAs Entrar/Criar conta, footer de confianca

### Lacunas do print

- Sem estado de erro/loading
- Sem variante mobile
- Sem mascote em asset dedicado (decoracao CSS; mascote omitido)

## Tasks relacionadas

- Task 026 (CR) - Login visual e acesso livre web — **done**
- Task 634 (CR) - Login web mobile apenas com formulário — **done**
- Task 635 (CR) - Login web mobile manter cabeçalho do card — **done**

## Contexto mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`
- `tasks/000-index.md`
- este slice
- task 026

## Contexto sob demanda

- print + DS desktop
- `front-end/docs/ai/` (ARCHITECTURE, CODE_STYLE, ACCESSIBILITY)
- codigo atual de Login/AuthLayout/guards

## Risco de contexto

baixo — UI single-stack, um print, sem API

## Resultado

- Entrega web concluida na Task 026.
- Bypass de guards e temporario e documentado no handoff.
- **Atualizacao:** bypass revertido na Task 029 / Slice 015 (auth obrigatoria).
- **Atualizacao:** Task 426 — fundo `capa-tela-login.webp` no login via prop `coverBackground` do AuthLayout.
- **Atualizacao:** Task 427 — efeito de vidro (blur + verniz) sobre a capa do login.
- **Atualizacao:** Task 634 concluiu a variante responsiva do login web, mantendo apenas o formulário em telas de até 560px.
- **Atualizacao:** Task 635 preserva o cabeçalho e a superfície do card conforme a referência mobile enviada.

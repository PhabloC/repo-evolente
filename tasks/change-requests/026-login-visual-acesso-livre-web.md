# Task 026 - Login visual e acesso livre web

## Status

done

## Tipo

front

## Stacks envolvidos

- front-end

## Perfil do projeto

- stack web escolhida: front-end (React/Vite)
- mobile: sim

## Contrato

- nao se aplica

## Modo de execucao

single-stack

## Referencia de design system

### Stack de referencia visual

front-end

### Tipo de referencia visual

prints de telas

### Fonte primaria visual

- `design-system/front/prints/login-desktop.png`

### Fontes de apoio

- `design-system/front/Design_System_Evolente_Desktop.md` (paleta/tipografia)
- `front-end/src/assets/Vector.webp` (wordmark Evolente)
- `front-end/src/assets/Circular logos container.webp` (selo circular do card)

### Regra de aderencia visual

- Layout split: branding a esquerda + card de login a direita (desktop).
- Fundo bege com formas decorativas coloridas.
- Card branco arredondado: selo circular, titulo "Acesse sua conta", e-mail/senha com icones, lembrar-me, esqueci senha, Entrar (rosa), separador "ou", Criar conta (outline rosa).
- Footer de confianca (LGPD/seguranca/suporte).
- Usar logos ja presentes em `front-end/src/assets/`.
- Em mobile, empilhar branding + card sem quebrar usabilidade.

### Telas/estados governados pelo print

- Login desktop (estado default)

### Lacunas do print

- Erro/loading: manter padroes atuais de feedback
- Sem mascote em asset: decoracao CSS ou omitir
- "Criar conta": mapear para fluxo existente (profissional/responsavel) sem inventar tela nova

## Origem da solicitacao

Pedido do usuario para deixar a pagina de login bem parecida ao print enviado, usando logos ja adicionadas em assets, e permitir acesso livre sem precisar realizar login.

## Objetivo

Redesenhar `/login` conforme o print e liberar navegacao na area principal sem autenticacao obrigatoria (bypass temporario).

## Escopo

- Redesign da pagina de Login (e layout dedicado se necessario, sem quebrar AuthLayout das demais telas auth).
- Aplicar logos dos assets.
- Bypass de `PrivateRoutes`/`RoleGuard` para acesso livre a area principal (sessao guest local ou guards permissivos), documentado como temporario.
- Manter formulario de login real funcional (API) quando o usuario optar por autenticar.
- Atualizar testes da LoginPage.

## Fora de escopo

- Backend/API
- Mobile
- Redesign de recovery, reset, cadastros e gate de assinatura
- Remover endpoints de auth

## Entradas

- `design-system/front/prints/login-desktop.png`
- `design-system/front/Design_System_Evolente_Desktop.md`
- `front-end/src/assets/*`
- `front-end/docs/ai/ARCHITECTURE.md`, `CODE_STYLE.md`, `ACCESSIBILITY.md`
- codigo: `front-end/src/pages/Auth/Login/**`, guards, AuthLayout

## Dependencias

- Task 006 (telas auth web) — done

## Slice vertical

### Identificador do slice

Slice 012 - Login visual e acesso livre (web)

### Arquivo do slice

- `tasks/slices/012-login-visual-acesso-livre.md`

### Objetivo de negocio

Login web aderente ao print + exploracao sem auth obrigatoria.

### Entrega verificavel do slice

UI de login alinhada ao print; area principal acessivel sem login.

### Fora do slice

- Mobile, API, demais telas auth

## Contexto mínimo

Sempre ler:

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/012-login-visual-acesso-livre.md`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatorio? |
|---|---|---|---|
| UI login | `design-system/front/prints/login-desktop.png` | redesenhar layout | sim |
| Tokens/cores | `design-system/front/Design_System_Evolente_Desktop.md` | mapear paleta | sim |
| Logos | `front-end/src/assets/` | aplicar wordmark/selo | sim |
| Padroes front | `front-end/docs/ai/ARCHITECTURE.md`, `CODE_STYLE.md`, `ACCESSIBILITY.md` | implementar | sim |
| Guards atuais | `PrivateRoutes`, `RoleGuard`, `authStore` | bypass acesso livre | sim |

## Orçamento de contexto

- Fontes obrigatorias estimadas: 8
- Fontes sob demanda estimadas: 5
- Risco: baixo
- Estrategia de reducao: nao carregar mobile, backend, openapi, requirements; nao redesenhar outras telas auth

## Criterios de conclusao

- [x] `/login` visualmente proxima do print (layout, logos, card, CTAs, footer)
- [x] Logos dos assets utilizadas
- [x] Area principal acessivel sem autenticacao
- [x] Login real continua disponivel via formulario
- [x] Testes da LoginPage atualizados e passando
- [x] lint/build/test ok no front-end

## Instrucoes de implementacao

1. Criar layout dedicado da landing de login (nao alterar AuthLayout das outras telas auth, salvo extracao compartilhada minima).
2. Montar coluna de branding (logo Vector, tagline, headline com "voz" em destaque, texto, 3 feature cards) + card (selo circular, form, acoes).
3. Formas decorativas via CSS; mascote apenas se houver asset — nao inventar dependencia.
4. "Criar conta": CTA primario outline; pode abrir escolha profissional/responsavel ou linkar ao cadastro profissional com link secundario ao responsavel — registrar decisao no handoff.
5. Acesso livre: permitir Outlet em PrivateRoutes sem sessao e relaxar RoleGuard quando nao autenticado (ou sessao guest `profissional` local marcada como guest). Preferir abordagem explicita e reversivel.
6. Atualizar testes.

## Validacao esperada

- `cd front-end && npm run lint`
- `cd front-end && npm run test -- --run src/pages/Auth/Login`
- `cd front-end && npm run build`

## Entregaveis esperados

- Pagina Login redesenhada
- Bypass de acesso livre documentado
- Testes atualizados
- Handoff `.agents/state/handoffs/TASK-026.md`

## Riscos ou ambiguidades

- Print nao cobre mobile — empilhar com bom senso
- "Criar conta" unico no print vs dois cadastros no produto
- Bypass e temporario e nao substitui auth de producao

## Resultado da execucao

### Resumo por stack

- **front-end**: `/login` redesenhada como landing split (branding + card) aderente ao print; logos `logo-wordmark.webp` e `logo-seal.webp`; acesso livre via bypass em `PrivateRoutes`/`RoleGuard` + nav guest como profissional; login real mantido.

### Relação com o slice

- Slice 012 concluído nesta task.

### Decisões técnicas

- Layout dedicado na LoginPage (AuthLayout das demais telas auth intacto).
- Assets renomeados para nomes sem espaço (`logo-wordmark.webp`, `logo-seal.webp`).
- "Criar conta" → cadastro profissional; link secundário para responsável.
- Bypass: sem sessão, `PrivateRoutes` e `RoleGuard` liberam Outlet; sidebar guest usa itens do perfil profissional.
- Mascote do print omitido (sem asset); formas decorativas em CSS.
- CTA "explorar o dashboard" no card para descoberta do acesso livre.

### Trade-offs

- Bypass temporário reduz segurança de rotas — reversível removendo os early-returns.
- Botão Entrar usa override rosa via CSS (print) sobre token primary laranja do DS.

### Contrato

- nao se aplica

### Referência visual

- Print `design-system/front/prints/login-desktop.png` + tokens DS desktop.

## Contexto utilizado

### Contexto mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`
- `tasks/000-index.md`, esta task, `tasks/slices/012-login-visual-acesso-livre.md`

### Contexto sob demanda

| Fonte | Gatilho | Uso |
|---|---|---|
| print login-desktop | UI | layout/copy/CTAs |
| DS Desktop | tokens | cores/tipografia |
| assets logos | branding | wordmark + selo |
| ARCHITECTURE/CODE_STYLE | front | estrutura |
| Login/guards/nav | implementacao | redesign + bypass |

### Evitado

- mobile/, backend/, openapi, requirements, outras telas auth

## Handoff

- Caminho: `.agents/state/handoffs/TASK-026.md`
- Decisões: layout dedicado; bypass guards; Criar conta → profissional
- Próximo contexto: reverter bypass quando auth de producao for obrigatoria; opcional mascote asset
- Pendências: mascote; reativar guards em producao

## Arquivos alterados

### raiz / governanca

- `tasks/change-requests/026-login-visual-acesso-livre-web.md`
- `tasks/slices/012-login-visual-acesso-livre.md`
- `tasks/000-index.md`
- `design-system/front/prints/login-desktop.png`
- `.agents/state/handoffs/TASK-026.md`

### front-end

- `front-end/src/pages/Auth/Login/index.tsx`
- `front-end/src/pages/Auth/Login/styles.module.css`
- `front-end/src/pages/Auth/Login/index.test.tsx`
- `front-end/src/routes/PrivateRoutes.tsx`
- `front-end/src/routes/RoleGuard.tsx`
- `front-end/src/constants/navigation.ts`
- `front-end/src/assets/logo-wordmark.webp` (renomeado de Vector.webp)
- `front-end/src/assets/logo-seal.webp` (renomeado de Circular logos container.webp)

## Validacoes executadas

- `npm run test -- --run src/pages/Auth/Login` — ok
- `npm run lint` — ok
- `npm run build` — ok

## Pendencias pos-task

- Reverter bypass de guards antes de producao
- Asset do mascote (opcional) se quiser paridade total com o print
- Mobile auth visual permanece no DS mobile (fora de escopo)

## Status final

done

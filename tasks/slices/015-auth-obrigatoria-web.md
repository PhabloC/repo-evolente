# Slice 015 - Autenticacao obrigatoria web

## Status

done

## Objetivo de negocio

Exigir login com e-mail e senha para acessar a area principal da web, encerrando o bypass temporario de acesso livre.

## Entrega verificavel

- Rotas privadas redirecionam para `/login` sem sessao autenticada.
- RoleGuard volta a exigir perfil autenticado.
- CTA/hint de "explorar sem entrar" removido da LoginPage.
- Sidebar deixa de expor navegacao guest como profissional.

## Fora de escopo

- Backend/API (login real ja existe)
- Mobile
- Redesign visual do login
- Alterar fluxo de cadastro ou recovery

## Perfil do projeto

- stack web escolhida: front-end (React/Vite)
- mobile: sim (fora deste slice)

## Stacks envolvidas

- front-end

## Contrato

- nao se aplica (sem mudanca de contrato; consome auth existente)

## Referencia visual por stack

### Web

- tipo: nao se aplica (sem mudanca visual estrutural; apenas remocao de hint de acesso livre)
- fonte primaria: layout de login ja estabelecido (Slice 012 / Task 026)

## Tasks relacionadas

- Task 029 (CR) - Reativar autenticacao obrigatoria web — **done**

## Dependencias do slice

- Slice 012 (bypass introduzido na Task 026)
- Slice 002 (auth funcional)

## Contexto minimo recomendado

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`
- `tasks/000-index.md`
- este slice
- task 029
- handoff Task 026

## Contexto sob demanda recomendado

| Gatilho | Fonte | Quando carregar | Obrigatorio? |
|---|---|---|---|
| Bypass atual | `PrivateRoutes`, `RoleGuard`, `navigation`, LoginPage | reverter | sim |
| Padroes front | `front-end/docs/ai/ARCHITECTURE.md`, `CODE_STYLE.md` | implementar | sim |
| A11y | `front-end/docs/ai/ACCESSIBILITY.md` | se UI alterar | sim se UI |

## Risco de contexto

baixo — single-stack, reversoes localizadas, sem API

## Observacoes de rastreabilidade

- Pendencia documentada no indice e no handoff da Task 026: reverter bypass antes de producao.
- Este slice fecha essa pendencia.

## Resultado

- Entrega web concluida na Task 029.
- Bypass de guards revertido; autenticacao obrigatoria restaurada.

## Status final

done

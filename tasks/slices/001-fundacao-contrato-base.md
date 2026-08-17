# Slice 001 - Fundacao e contrato base

## Status

done

## Objetivo de negocio

Estabelecer contrato OpenAPI inicial, modelos de identidade/papeis e shells das apps web e mobile alinhados ao design system.

## Entrega verificavel

Existe contrato base com paths de auth/usuarios/papeis; backend com fundacao de auth/roles; web e mobile com shell, tokens e rotas protegidas por perfil.

## Fora de escopo

- Cadastro completo
- Pagamento
- Trilhas
- Dashboards de negocio

## Perfil do projeto

- stack web escolhida: front-end (React/Vite)
- mobile: sim

## Stacks envolvidas

- front-end
- backend
- mobile

## Contrato

- `contracts/openapi.yaml` (paths base de auth, users, roles)

## Referencia visual por stack

### Web

- tipo: artefato de design system
- fonte primaria: `design-system/front/Design_System_Evolente_Desktop.md` (tokens, tipografia, estados)

### Mobile

- tipo: artefato de design system
- fonte primaria: `design-system/mobile/Design_System_Evolente_App_Mobile.md` (tokens, tipografia, estados)

## Permissoes e atores

- Master, profissional, responsavel como papeis
- Paciente/crianca sem login proprio

## Casos de erro e borda

- Contrato vazio atual deve ser preenchido sem inventar endpoints de dominio ainda nao planejados
- Shells nao liberam areas pagas sem gate futuro

## Decisoes humanas confirmadas

- Stack web: React/Vite; Mobile: sim; Profissional multi-especialidade; Inativar (nao excluir); Gamificacao/jogos fora do escopo

## Premissas adotadas

- Gateway, valores e push a definir — abstrair
- DS documental governa tokens; sem prints nesta fase
- Conflito DS mobile (gamificacao/UI crianca) vs requisitos — prevalece requisito

## Tasks relacionadas

- `tasks/001-contrato-openapi-base.md` - Contrato OpenAPI base
- `tasks/002-fundacao-backend-identidade.md` - Fundacao backend
- `tasks/003-shell-web-react.md` - Shell web
- `tasks/004-shell-mobile-expo.md` - Shell mobile
- `tasks/change-requests/049-gitignore-stacks-backend-front-end-mobile.md` - Gitignore local das stacks
- `tasks/change-requests/076-criar-readmes-operacionais-das-stacks.md` - READMEs operacionais de backend, front-end e mobile
- `tasks/change-requests/092-ajustar-execucao-web-expo-mobile.md` - Execucao web dedicada do Expo mobile
- `tasks/change-requests/130-habilitar-alias-arroba-nas-rotas-mobile.md` - Alias `@/` nas rotas do mobile

## Dependencias do slice

Nenhuma

## Contexto minimo recomendado

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- este slice

## Contexto sob demanda recomendado

| Gatilho | Fonte | Quando carregar | Obrigatorio? |
|---|---|---|---|
| Requisitos | `requirements/001-escopo-produto.md`, `requirements/002-regras-de-negocio.md` | regras do slice | sim |
| UI web | `design-system/front/Design_System_Evolente_Desktop.md` | UI web | sim se UI web |
| UI mobile | `design-system/mobile/Design_System_Evolente_App_Mobile.md` | UI mobile | sim se UI mobile |
| API | `contracts/openapi.yaml` | API | sim se API |
| Front-end | `front-end/docs/ai/` | front envolvido | sim se front |
| Backend | `backend/docs/ai/` | back envolvido | sim se back |
| Mobile | `mobile/docs/ai/` | mobile envolvido | sim se mobile |

## Risco de contexto

- medio
- estrategia: carregar apenas secoes/paths citados nas tasks

## Observacoes de rastreabilidade

- OpenAPI base (Task 001), identidade backend (Task 002), shell web (Task 003), shell mobile (Task 004).
- CR 049 adiciona higiene local de versionamento no backend sem reabrir escopo funcional do slice.
- CR 076 documentou operacionalmente as três stacks sem alterar escopo funcional.
- CR 092 dedicou porta fixa para a execucao web do Expo mobile, evitando colisao com a porta padrao do Metro sem reabrir escopo funcional do slice.
- CR 130 habilitou o alias `@/*` no mobile e o aplicou ao eixo de rotas/linking sem reabrir escopo funcional do slice.
- Gamificacao mobile excluida e documentada em `mobile/docs/ai/SCOPE_EXCLUSIONS.md`.

## Progresso das tasks relacionadas

- `tasks/001-contrato-openapi-base.md` — done
- `tasks/002-fundacao-backend-identidade.md` — done
- `tasks/003-shell-web-react.md` — done
- `tasks/004-shell-mobile-expo.md` — done
- `tasks/change-requests/049-gitignore-stacks-backend-front-end-mobile.md` — done
- `tasks/change-requests/076-criar-readmes-operacionais-das-stacks.md` — done
- `tasks/change-requests/092-ajustar-execucao-web-expo-mobile.md` — done
- `tasks/change-requests/130-habilitar-alias-arroba-nas-rotas-mobile.md` — done

## Status final

done

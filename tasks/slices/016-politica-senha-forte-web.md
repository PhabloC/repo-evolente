# Slice 016 - Politica de senha forte (web)

## Status

done

## Objetivo de negocio

Garantir que senhas criadas ou redefinidas na web cumpram politica minima de seguranca e que a redefinicao confirme a nova senha.

## Entrega verificavel

- Cadastro (profissional/responsavel) rejeita senha fraca com mensagem clara.
- Redefinicao de senha exige nova senha forte + confirmacao igual.
- Backend e contrato OpenAPI validam a mesma politica em create/reset.
- Login permanece com validacao minima de comprimento (nao bloqueia contas antigas).

## Fora de escopo

- Mobile
- Redesign visual das telas auth
- Forcar troca de senha em contas ja existentes
- Alterar fluxo de pedido de recovery (somente o reset)

## Perfil do projeto

- stack web escolhida: front-end (React/Vite)
- mobile: sim (fora deste slice)

## Stacks envolvidas

- front-end
- backend
- contracts (openapi)

## Contrato

- `contracts/openapi.yaml` — schemas de password em registro e PasswordResetRequest

## Referencia visual por stack

### Web

- tipo: nao se aplica (sem redesign; apenas validacao/mensagens de erro)
- fonte: telas auth existentes (Slice 014)

## Tasks relacionadas

- Task 030 (CR) - Politica de senha forte e confirmacao no reset — **done**
- Task 787 (CR) - Aviso quando senhas não coincidem no cadastro web — **done**

## Dependencias do slice

- Slice 002 (auth)
- Slice 003/004 (cadastros)
- Slice 014 (template auth)

## Contexto minimo recomendado

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`
- `tasks/000-index.md`
- este slice
- task 030

## Contexto sob demanda recomendado

| Gatilho | Fonte | Quando carregar | Obrigatorio? |
|---|---|---|---|
| Contrato password | `contracts/openapi.yaml` (schemas password) | alinhar pattern | sim |
| Forms auth | Register*, PasswordReset, AddPatient | aplicar schema | sim |
| DTOs back | create/register/password-reset DTOs | validar servidor | sim |

## Risco de contexto

baixo/medio — shared focado, paths concretos, sem mobile

## Resultado

- Entrega concluida na Task 030.
- Politica unica front/back/contrato; reset com confirmacao.
- Task 787: cadastro profissional e responsável também confirmam senha com aviso de divergência.

## Status final

done

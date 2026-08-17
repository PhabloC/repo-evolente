# Handoff - Task 030

## Task

- identificador: 030
- título: Politica de senha forte e confirmacao no reset
- tipo: shared
- modo de execução: cross-stack
- status final: done
- arquivo: `tasks/change-requests/030-politica-senha-forte-web.md`

## Slice vertical

- identificador: Slice 016 - Politica de senha forte (web)
- objetivo de negócio: senhas novas seguras + confirmacao no reset
- entrega verificável: cadastro/reset rejeitam senha fraca; reset exige confirmacao igual
- status do slice: done

## Decisões preservadas

- decisão: politica `>=8` + maiúscula + número + caractere especial (qualquer não alfanumérico)
- motivo: pedido do usuario
- impacto: utils/DTOs/OpenAPI alinhados; login permanece só com minLength 8

- decisão: util front `strongPasswordSchema` e decorator back `IsStrongPasswordField` + `assertStrongPassword` no UsersService
- motivo: validação client + server + defesa em create/update/reset
- impacto: fixtures de teste atualizadas para `SenhaForte1!` / `NovaSenha1!`

- decisão: PasswordReset já tinha nova + confirmar; reforçado com politica forte e igualdade
- motivo: escopo do pedido
- impacto: placeholders e schema atualizados

- decisão: mobile fora de escopo
- motivo: demanda focada em web/API
- impacto: app mobile pode precisar CR futura

## Contexto utilizado

### Contexto mínimo lido

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`
- `tasks/000-index.md`, CR-030, slice 016

### Contexto sob demanda carregado

| Fonte | Gatilho | Uso |
|---|---|---|
| openapi password schemas | contrato | pattern/description |
| Register*/PasswordReset/DTOs | implementacao | aplicar politica |
| password.util / forms | codigo | utils e validacao |

### Evitado

- mobile/, design-system, requirements

## Arquivos alterados

- front: `utils/password.ts`, Register*, PasswordReset, testes
- back: decorator, password.util, DTOs, users.service, specs
- `contracts/openapi.yaml`
- governanca: slice 016, CR-030, index, este handoff

## Validações executadas

- front: `password` tests, RegisterProfessional test, lint, build — ok
- back: jest auth|users|professionals|guardians — ok; lint — ok

## Pendências

- Mobile: aplicar mesma politica se desejado
- Contas antigas com senha fraca continuam logando (intencional)

## Próxima ação sugerida

- Validar manualmente cadastro e `/redefinir-senha` no browser

## Próximo contexto recomendado

- Handoff desta task

## Contexto que não deve ser carregado

- mobile/, design-system, requirements inteiros

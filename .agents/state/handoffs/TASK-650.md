# Handoff - Task 630

## Task

- identificador: `630`
- título: Multisseleção de motivo principal e comunicação na anamnese
- status final: done

## Slice vertical

- `tasks/slices/060-multisselecao-anamnese-filho.md`

## Decisões preservadas

- Ambos os campos são arrays no contrato e no JSON de respostas; escolhas antigas devem ser lidas como arrays de um item quando aplicável.
- Web e mobile usam controles checkbox; demais perguntas não foram alteradas.
- A mudança exigiu backend/OpenAPI apesar de a solicitação visual citar web e mobile, para não perder seleções no envio.

## Contexto utilizado

- Formulários de cadastro web/mobile, tipos/schema, DTO e serviço de guardians, relatório, OpenAPI, design systems e acessibilidade web.

## Arquivos alterados

- Front-end, mobile, backend, contrato, Task 630, Slice 060 e índice.

## Validações executadas

- Backend build e lint passaram.
- Typecheck direcionado web/mobile passou para os arquivos alterados; projetos completos mantêm erros preexistentes fora do escopo.
- `git diff --check` passou.

## Pendências ou bloqueios

- Nenhuma funcional; acompanhar os erros preexistentes de typecheck em futuras tasks de estabilidade.

## Próximo contexto recomendado

- Nenhum, salvo demanda de edição/reidratação da anamnese ou normalização de registros legados.


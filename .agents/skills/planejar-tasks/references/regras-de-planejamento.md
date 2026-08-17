# Regras de planejamento (raiz)

## Principio

Planejar o projeto inteiro em backlog unico, sem fragmentar por repositorio, usando progressive disclosure e vertical slices.

## Ordem de raciocinio

1. contexto mínimo da raiz
2. perfil do projeto: stack web e mobile
3. requisitos relevantes
4. referências visuais relevantes
5. review verificável da spec
6. identificação de jornadas/capacidades de negócio
7. decomposição em vertical slices
8. materialização de 1 arquivo por slice em `tasks/slices/`
9. contrato openapi necessário por slice
10. impacto shared
11. impacto front, back e mobile quando aplicável
12. contexto mínimo e contexto sob demanda por task
13. dependências cruzadas
14. estratégia incremental
15. risco de contexto excessivo

## Checklist minimo de cada task

- Tipo
- Stacks envolvidos
- Perfil do projeto quando impactar roteamento (`front-end` ou `next-js`; mobile `sim` ou `nao`)
- Contrato (quando aplicavel)
- Modo de execucao
- Slice vertical com caminho concreto para `tasks/slices/*.md`
- Contexto mínimo
- Contexto sob demanda
- Orçamento de contexto
- Fora do slice
- Dependencias
- Criterios verificaveis
- Fonte primaria visual em `design-system/front/` ou `design-system/mobile/` (quando houver UI)
- Tipo de referencia visual (`artefato documental`, `aplicacao-prototipo visual`, `prints de telas` ou `nao se aplica`)
- Permissoes impactadas ou `nao se aplica`
- Casos de erro e borda mapeados

## Review verificavel da spec

Antes de considerar o backlog planejado:

- confirmar permissoes e registrar evidencia na task
- mapear casos de erro e estados excepcionais relevantes
- separar decisao humana confirmada de premissa assumida
- escrever criterios de aceite observaveis e testaveis
- registrar casos de borda relevantes ou a ausencia deles

Planejamento incompleto deve virar risco, pendencia ou duvida explicita. Nao ocultar lacunas.

## Cobertura esperada

Quando aplicavel:

- fundacao tecnica
- contrato
- integracoes
- front-end React/Vite ou Next.js, conforme escolha do usuario
- backend
- mobile, somente quando confirmado
- seguranca
- testes
- observabilidade
- documentacao

## Qualidade

Cada slice deve existir como arquivo proprio em `tasks/slices/` e funcionar como agregado de negocio das tasks tecnicas relacionadas.

Um executor deve conseguir implementar sem reinterpretar o problema.

Uma task deve ser pequena o bastante para o executor implementá-la carregando apenas o contexto sob demanda declarado. Se a task exigir leitura ampla de múltiplos domínios, ela deve ser dividida antes da execução.

Nenhuma task deve listar docs de stacks não envolvidas apenas por disponibilidade no scaffold.

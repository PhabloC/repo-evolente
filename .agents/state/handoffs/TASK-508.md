# Handoff - Task 508

## Task

- identificador: 508
- título: Aviso ao criar trilha própria com vínculo e trilha existentes
- status final: done

## Decisões preservadas

- aviso só se `hasActiveProfessionalLink && trailId`
- sem vínculo: sem modal extra
- responsável continua podendo montar (Task 506)

## Arquivos alterados

- backend trails list + openapi + mobile confirm flows

## Validações executadas

- jest trails.service.spec 8 passed

## Pendências ou bloqueios

- nenhuma

## Próxima ação sugerida

- testar conta com vínculo+trilha e conta sem vínculo

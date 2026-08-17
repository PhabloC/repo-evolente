# Handoff - Task 506

## Task

- identificador: 506
- título: Permitir responsável montar trilha mesmo com vínculo
- status final: done

## Decisões preservadas

- responsável dono da criança sempre pode manage (`canManage: true`)
- vínculo profissional ativo não bloqueia mais edição
- chip de autoria usa `professionalUserId`, não `canManage`

## Arquivos alterados

- trails.service + spec, openapi, mobile trail types/UI

## Validações executadas

- jest trails.service.spec: 8 passed

## Pendências ou bloqueios

- nenhuma

## Próxima ação sugerida

- testar no app: Biblioteca + gerar anamnese com conta de responsável

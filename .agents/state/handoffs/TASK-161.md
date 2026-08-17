# Handoff - Task 161

## Task

- identificador: 161
- título: Mapear uso do bucket no projeto
- tipo: shared
- modo de execução: cross-stack
- status final: done

## Slice vertical

- identificador: Slice 006 - Catalogo
- objetivo de negócio: dar visibilidade operacional ao uso do bucket
- entrega verificável: documento raiz com usos atuais e recomendados do bucket
- status do slice: done

## Decisões preservadas

- decisão: documentar apenas o que está confirmado no código atual
- motivo: evitar planejar bucket com base em suposição
- impacto: avatar e anexos aparecem como candidatos futuros, não como uso existente

- decisão: manter a convenção `prefixo/.../original/...`
- motivo: alinhar novas pastas ao padrão já adotado em conteúdos
- impacto: futuras features de arquivo podem seguir a mesma estrutura

## Contexto utilizado

### Contexto mínimo lido

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`
- `tasks/000-index.md`, `tasks/change-requests/161-mapa-de-uso-do-bucket-no-projeto.md`
- `tasks/slices/006-catalogo-conteudos-master.md`
- `.agents/state/handoffs/TASK-160.md`

### Contexto sob demanda carregado

| Fonte | Gatilho | Uso |
|---|---|---|
| `contracts/openapi.yaml` | endpoints com arquivo | confirmar upload/download |
| `backend/src/modules/contents/**` | storage | confirmar mídia em bucket |
| `backend/src/modules/reports/**` | relatórios | confirmar persistência em banco |
| `backend/src/modules/admin/**` | exportações | confirmar geração em memória/stream |
| `backend/src/modules/users/**`, `guardians/**`, `professionals/**` | perfis | confirmar ausência de avatar |
| `mobile/src/features/shell/components/HomeHeader/**` | avatar mobile | confirmar iniciais sem upload |

## Resultado por stack

- backend: done
- front-end: done
- mobile: done

## Arquivos alterados

- `STORAGE_BUCKET_MAP.md`
- `tasks/change-requests/161-mapa-de-uso-do-bucket-no-projeto.md`
- `tasks/slices/006-catalogo-conteudos-master.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-161.md`

## Validações executadas

- busca por termos de arquivo/upload/anexo/avatar: ok
- revisão manual das entidades, services e contrato relevantes: ok

## Pendências ou bloqueios

- nenhuma bloqueante
- atualizar o documento quando avatar, anexos clínicos ou storage de relatórios forem implementados

## Próxima ação sugerida

- usar este mapa como base antes de criar upload de avatar ou anexos

## Próximo contexto recomendado

- tasks futuras de `avatars`, `attachments` ou migração de `reports` para storage

## Contexto que não deve ser carregado na próxima etapa

- fonte: design-system amplo
- motivo: esta decisão é de storage/domínio, não de UI

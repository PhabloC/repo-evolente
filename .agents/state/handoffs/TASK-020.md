# Handoff - Task 020

## Task

- identificador: 020
- título: Execução da trilha no app mobile
- tipo: mobile
- modo de execução: single-stack
- status final: done

## Slice vertical

- identificador: Slice 008 - Trilhas
- objetivo de negócio: Trilhas semanais + evolução
- entrega verificável: Trilha no app do responsável
- status do slice: done

## Decisões preservadas

- decisão: aba Trilha no shell do responsável + detalhe de atividade
- motivo: listar/abrir mídia/concluir sem gamificação
- impacto: Home aponta para a aba; sem tela de conquistas

- decisão: `GET /guardians/me/children` para obter `patientId`
- motivo: responsável não tinha endpoint para resolver a criança
- impacto: extensão mínima backend/OpenAPI além do escopo mobile puro

- decisão: `GET /contents` liberado para `responsavel` (somente active)
- motivo: itens da trilha só trazem `contentId`; mídia/título vêm do catálogo
- impacto: sem embed de content no TrailDetail nesta fase

- decisão: mídia via `expo-linking` (`openURL`)
- motivo: sem novas dependências de player
- impacto: fallback textual se URL indisponível

- decisão: desvio do DS mobile (gamificação)
- motivo: requisitos/task prevalecem
- impacto: feedback simples de conclusão apenas

## Contexto utilizado

### Contexto mínimo lido

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`
- `tasks/000-index.md`, `tasks/020-execucao-trilha-mobile.md`
- `tasks/slices/008-trilhas-semanais-evolucao.md`
- `.agents/state/handoffs/TASK-019.md`

### Contexto sob demanda carregado

| Fonte | Gatilho | Uso |
|---|---|---|
| DS mobile | UI | atividades; desvio gamificação |
| openapi | API | trails/progress/guardians/contents |
| mobile docs/ai | mobile | estrutura feature trail |

### Contexto evitado

| Fonte | Motivo |
|---|---|
| front-end / DS desktop | Task mobile |
| admin / push | fora do slice |

## Resultado por stack

- mobile: done
- backend: extensão mínima done (children + contents read)

## Arquivos alterados

- `mobile/src/features/trail/**`
- shell responsável (navigator + home)
- guardians `me/children` + contents roles
- `contracts/openapi.yaml`
- task/index/slice/handoff

## Validações executadas

- mobile lint/typecheck/test: ok
- backend lint + testes guardians/contents: ok

## Pendências ou bloqueios

- nenhuma do Slice 008

## Próxima ação sugerida

- Executar próxima task planned do index (ex.: Task 021 admin API, ou 023/024 conforme prioridade humana)

## Próximo contexto recomendado

- task escolhida + contrato/paths citados + docs da stack envolvida

## Contexto que não deve ser carregado na próxima etapa

- fonte: feature trail mobile completa
- motivo: Slice 008 fechado; só reabrir se regressão

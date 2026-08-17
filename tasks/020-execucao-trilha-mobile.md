# Task 020 - Execucao da trilha no app mobile

## Status

done

## Tipo

mobile

## Stacks envolvidos

- mobile

## Perfil do projeto

- stack web escolhida: front-end (React/Vite)
- mobile: sim

## Contrato

- `contracts/openapi.yaml#/paths` trails/progress
- Extensões mínimas para o fluxo mobile: `GET /guardians/me/children`, `GET /contents` (leitura active para responsavel)

## Modo de execucao

single-stack

## Referencia de design system

### Stack de referencia visual

mobile

### Tipo de referencia visual

artefato de design system

### Fonte primaria visual

- `design-system/mobile/Design_System_Evolente_App_Mobile.md`

### Regra de aderencia visual

- Atividades do dia DS; SEM medalhas/gamificacao.

## Contexto de negocio

### Por que

Executar atividades no app.

### O que

Listar, abrir midia, concluir com progresso.

### Comportamento esperado

- Lista
- Midia
- Concluir
- Feedback simples

### Fora de escopo

- Gamificacao
- Jogos
- Admin

## Review da spec

- [x] Permissoes definidas ou `nao se aplica`
- [x] Casos de erro mapeados
- [x] Decisoes de negocio confirmadas como humanas
- [x] Criterios de aceite objetivos e verificaveis
- [x] Casos de borda considerados

### Evidencias da review

- Permissoes: responsavel
- Casos de erro: rede; midia
- Decisoes humanas confirmadas: Stack web React/Vite; mobile sim; profissional multi-especialidade; inativar nao excluir; gamificacao fora
- Casos de borda: trilha vazia

## Especificacao tecnica

### Deve

- Feedback positivo simples ok

### Nao deve

- nao adicionar novas dependencias sem autorizacao explicita nesta task
- nao desviar dos padroes estabelecidos sem justificativa registrada
- Tela conquistas

## Entradas

- `design-system/mobile/Design_System_Evolente_App_Mobile.md`
- `mobile/docs/ai/`
- `requirements/001-escopo-produto.md`

## Dependencias

- Task 018

## Slice vertical

### Identificador do slice

Slice 008 - Trilhas

### Arquivo do slice

- `tasks/slices/008-trilhas-semanais-evolucao.md`

### Objetivo de negócio

Execucao mobile.

### Entrega verificável do slice

Trilha no app.

### Fora do slice

- Web

## Contexto mínimo

Sempre ler:

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/008-trilhas-semanais-evolucao.md`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| UI mobile | `design-system/mobile/Design_System_Evolente_App_Mobile.md` | UI mobile | sim |
| Mobile | `mobile/docs/ai/ARCHITECTURE.md e CODE_STYLE.md` | mobile | sim |
| API | `contracts/openapi.yaml` | API | sim |
| Requisitos | `requirements/001-escopo-produto.md e 002-regras-de-negocio.md` | regras | sim |

## Orçamento de contexto

- Risco alto

## Criterios de conclusao

- Concluir atualiza progresso
- Sem medalhas

## Instrucoes de implementacao

- Documentar desvio do DS gamificacao

## Validacao esperada

- npm run lint
- npm run typecheck
- npm run test

## Entregaveis esperados

- Fluxo trilha mobile

## Riscos ou ambiguidades

- DS vs requisitos

## Resultado da execucao

Fluxo de trilha do dia no app do responsável: aba **Trilha**, lista do dia, detalhe com abertura de mídia (`expo-linking`), conclusão via `POST /progress/completions` e feedback simples sem medalhas/pontos.

Lacuna de contrato resolvida com extensões mínimas no backend/OpenAPI: `GET /guardians/me/children` (resolver `patientId`) e leitura de `GET /contents` para `responsavel` (título/mídia das atividades). Modo demo preservado quando `useDemoData`/sem API.

## Contexto utilizado

### Contexto mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`
- `tasks/000-index.md`, esta task, `tasks/slices/008-trilhas-semanais-evolucao.md`
- `.agents/state/handoffs/TASK-019.md`

### Contexto sob demanda

| Fonte | Gatilho | Uso |
|---|---|---|
| DS mobile | UI | atividades do dia; desvio gamificação |
| openapi trails/progress/guardians/contents | API | payloads e papéis |
| mobile docs/ai (ARCHITECTURE/CODE_STYLE) | mobile | feature trail + shell |

### Contexto não carregado

- front-end / design-system front (fora do escopo mobile)
- admin / gamificação

## Handoff

- `.agents/state/handoffs/TASK-020.md`

## Arquivos alterados

### Mobile

- `mobile/src/features/trail/**` (types, utils, adapters, services, hooks, screens, testes)
- `mobile/src/features/shell/navigators/ResponsavelShellNavigator.tsx`
- `mobile/src/features/shell/screens/ResponsavelHomeScreen.tsx`

### Backend / contrato (extensão mínima para o fluxo)

- `backend/src/modules/guardians/guardians.controller.ts` (+ `GET me/children`)
- `backend/src/modules/guardians/guardians.service.ts` / repositories / module
- `backend/src/modules/contents/contents.controller.ts` (`responsavel` em GET)
- `contracts/openapi.yaml` (`/guardians/me/children`, descrição contents)

### Governança

- esta task, `tasks/000-index.md`, `tasks/slices/008-trilhas-semanais-evolucao.md`
- `.agents/state/handoffs/TASK-020.md`

## Validacoes executadas

- mobile: `npm run lint` ok; `npm run typecheck` ok; `npm run test` ok (7 testes)
- backend: `npm run lint` ok; testes guardians/contents ok (11 testes)

## Aderencia ao design system

- Fonte: `design-system/mobile/Design_System_Evolente_App_Mobile.md` (atividades do dia)
- **Desvio documentado:** DS cita gamificação/medalhas/conquistas; requisitos e task mandam **não** implementar. UI calma com feedback textual simples apenas.
- Mídia aberta via URL externa (`Linking`), sem player nativo novo (sem novas dependências).

### Acessibilidade (mobile)

- Estados de loading/erro/vazio
- `accessibilityLiveRegion` no feedback de conclusão
- Botões com labels claros; sem aninhamento Pressable+Button

## Pendencias pos-task

- Nenhuma bloqueante para o Slice 008
- Próximas tasks planejadas: 021+ (admin/home/notificações conforme index)

## Status final

done

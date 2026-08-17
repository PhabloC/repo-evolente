# Task 171 - Recalibrar tolerancia da escrita sem aceitar rabisco

## Status

done

## Tipo

shared

## Stacks envolvidos

- front-end
- mobile

## Perfil do projeto

- stack web escolhida: front-end (React/Vite)
- mobile: sim

## Contrato

nao se aplica

## Modo de execucao

cross-stack

## Slice vertical

- `tasks/slices/030-escrita-guiada-de-letras.md`

## Referencia de design system

### Web

- stack de referencia visual: front-end
- tipo de referencia visual: artefato de design system
- fonte primaria visual: `design-system/front/Design_System_Evolente_Desktop.md`

### Mobile

- stack de referencia visual: mobile
- tipo de referencia visual: artefato de design system
- fonte primaria visual: `design-system/mobile/Design_System_Evolente_App_Mobile.md`

### Regra de aderencia visual

- Sem mudança de UI; apenas recalibragem da heurística.

## Contexto de negocio

### Por que

Após a Task 170, a validação passou a aceitar qualquer rabisco. É preciso endurecer a comparação sem voltar a rejeitar letra torta de criança.

### O que

Recalibrar a heurística com limiares de média + percentil 90 e regra geométrica leve para `U` (topo aberto), mantendo bbox e amostragem por stroke da Task 170.

### Comportamento esperado

- `U`/`O` tortos e reconhecíveis passam
- scribble, zigue-zague e formas aleatórias falham
- círculo pode passar como `O`, mas não como `U`

### Fora de escopo

- integração de `$P`/`ndollar-js` ou TensorFlow.js
- mudança de UI

## Review da spec

- [x] Permissoes definidas ou `nao se aplica`
- [x] Casos de erro mapeados
- [x] Decisoes de negocio confirmadas como humanas
- [x] Criterios de aceite objetivos e verificaveis
- [x] Casos de borda considerados

### Evidencias da review

- Decisão humana: opção A (só recalibrar tolerância agora)
- Casos: letra torta vs rabisco vs círculo como `U`

## Especificacao tecnica

### Deve

- usar média e p90 das distâncias nearest-neighbor
- limiares calibrados (~0.15 média, ~0.25 p90)
- regra de topo aberto para `U`
- testes cobrindo aceite de `U` torto e rejeição de scribble

### Nao deve

- nao integrar biblioteca nova nesta task
- nao reabrir UI/contrato

## Entradas

- `front-end/src/pages/Main/Library/letterWritingGame.ts`
- `mobile/src/features/games/utils/alphabetWritingGame.ts`
- testes relacionados
- `.agents/state/handoffs/TASK-170.md`

## Dependencias

- Task 170

## Contexto mínimo

- `AGENTS.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/030-escrita-guiada-de-letras.md`
- `.agents/state/handoffs/TASK-170.md`

## Contexto sob demanda

| Gatilho | Fonte | Decisão/validação dependente | Obrigatorio? |
|---|---|---|---|
| recalibragem | utilitarios web/mobile de escrita | limiares e p90 | sim |
| regressão | testes unitarios | U torto vs scribble | sim |

## Orçamento de contexto

- baixo
- estrategia: só utilitarios e testes da escrita

## Criterios de aceite

- [x] `U` torto continua aceito
- [x] scribble/zigue-zague rejeitados
- [x] círculo não passa como `U`
- [x] testes web e mobile passam

## Ordem sugerida de execucao

1. Ajustar utilitario web
2. Alinhar mobile
3. Atualizar testes
4. Rodar checks

## Resultado da execucao

Recalibrada a heurística: média ≤ 0.15, p90 ≤ 0.25 e regra de topo aberto para `U`. Scribble e círculo deixam de passar como `U`; `U` torto e em dois traços continuam aceitos. Sem biblioteca nova (opção A).

## Contexto utilizado

- `tasks/change-requests/171-recalibrar-tolerancia-escrita-sem-aceitar-rabisco.md`
- `tasks/slices/030-escrita-guiada-de-letras.md`
- `.agents/state/handoffs/TASK-170.md`
- utilitarios e testes web/mobile de escrita

## Handoff

- handoff: `.agents/state/handoffs/TASK-171.md`
- proxima acao sugerida: smoke manual no preview; se ainda falhar demais/passar demais, considerar opção B (`$P`/`ndollar-js`)

## Arquivos alterados

- `front-end/src/pages/Main/Library/letterWritingGame.ts`
- `front-end/src/pages/Main/Library/letterWritingGame.test.ts`
- `mobile/src/features/games/utils/alphabetWritingGame.ts`
- `mobile/src/features/games/utils/alphabetWritingGame.test.ts`
- `tasks/change-requests/171-recalibrar-tolerancia-escrita-sem-aceitar-rabisco.md`
- `tasks/slices/030-escrita-guiada-de-letras.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-171.md`

## Validacoes executadas

- `cd front-end && npm run test -- src/pages/Main/Library/letterWritingGame.test.ts` — ok (8)
- `cd mobile && npm run test -- alphabetWritingGame.test.ts` — ok (10)

## Pendencias pos-task

- smoke manual no preview da biblioteca
- evolução futura opcional: opção B (`$P`/`ndollar-js`)

## Status final

done

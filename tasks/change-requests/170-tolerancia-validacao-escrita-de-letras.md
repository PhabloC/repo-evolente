# Task 170 - Tolerancia da validacao de escrita de letras

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

- Sem mudança visual de layout; apenas calibragem da heurística de validação da escrita.

## Contexto de negocio

### Por que

No preview da biblioteca (e potencialmente no jogo), letras escritas corretamente — em especial o `U` — são rejeitadas. Crianças escrevem de forma torta e a validação precisa ser tolerante.

### O que

Corrigir a heurística de validação da escrita guiada para aceitar traços imperfeitos sem exigir caligrafia perfeita, preservando rejeição de formas claramente distintas.

### Comportamento esperado

- um `U` reconhecível escrito de forma torta deve ser aceito
- traços com proporção estreita/larga ou lados irregulares ainda podem passar quando a forma geral for de `U`
- formas claramente diferentes (ex.: linha vertical pura vs `O`/`U`) continuam rejeitadas
- preview web e runtime mobile usam a mesma filosofia de tolerância

### Fora de escopo

- reconhecimento por IA
- expansão do alfabeto
- mudança de UI do jogo

## Review da spec

- [x] Permissoes definidas ou `nao se aplica`
- [x] Casos de erro mapeados
- [x] Decisoes de negocio confirmadas como humanas
- [x] Criterios de aceite objetivos e verificaveis
- [x] Casos de borda considerados

### Evidencias da review

- Permissoes: nao se aplica (ajuste de heurística local)
- Casos de erro: tentativa torta válida vs forma errada
- Decisao humana confirmada pelo pedido: aceitar escrita infantil imperfeita
- Casos de borda: `U` estreito, `U` torto, multiplos strokes, template normalizado em 0-1 no preview web

## Especificacao tecnica

### Deve

- corrigir normalização do bounding box no front-end (mínimo atual `1` distorce templates 0-1)
- amostrar strokes sem criar segmento fantasma entre traços
- aumentar levemente os limiares de distância para escrita infantil
- alinhar a mesma lógica no mobile
- cobrir com testes unitários (U torto aceito; forma distinta rejeitada)

### Nao deve

- nao alterar contrato/API
- nao exigir traço perfeito
- nao aceitar qualquer rabisco indiferente à letra

## Entradas

- `front-end/src/pages/Main/Library/letterWritingGame.ts`
- `mobile/src/features/games/utils/alphabetWritingGame.ts`
- `mobile/src/features/games/utils/alphabetWritingGame.test.ts`

## Dependencias

- Task 169

## Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/030-escrita-guiada-de-letras.md`

## Contexto sob demanda

| Gatilho | Fonte | Decisão/validação dependente | Obrigatorio? |
|---|---|---|---|
| bug de validação web | `front-end/src/pages/Main/Library/letterWritingGame.ts` | corrigir bbox e limiares | sim |
| paridade mobile | `mobile/src/features/games/utils/alphabetWritingGame.ts` | alinhar heurística | sim |
| regressão | testes existentes do mobile + novos testes web | garantir U torto aceito e O≠linha | sim |

## Orçamento de contexto

- baixo
- estrategia de reducao: tocar apenas nos utilitarios de validação e testes; nao reabrir UI, contrato ou bootstrap

## Criterios de aceite

- [x] `U` escrito de forma torta/estreita passa na validação web e mobile
- [x] bounding box do front-end nao distorce templates com coordenadas 0-1
- [x] múltiplos strokes nao geram segmento fantasma na amostragem
- [x] formas claramente distintas continuam rejeitadas
- [x] testes unitarios cobrindo o ajuste passam

## Ordem sugerida de execucao

1. Corrigir utilitario web
2. Alinhar utilitario mobile
3. Atualizar/criar testes
4. Rodar checks locais das stacks envolvidas

## Resultado da execucao

Causa raiz no preview web: `getBoundingBox` usava mínimo `1` para width/height, o que distorcia templates em coordenadas 0–1 e fazia até um `U` perfeito falhar. Ajustes: epsilon alinhado ao mobile, amostragem por stroke (sem segmento fantasma) e limiares mais tolerantes (0.28 / 0.30) para escrita infantil.

## Contexto utilizado

- `AGENTS.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- `tasks/change-requests/170-tolerancia-validacao-escrita-de-letras.md`
- `tasks/slices/030-escrita-guiada-de-letras.md`
- `front-end/src/pages/Main/Library/letterWritingGame.ts`
- `mobile/src/features/games/utils/alphabetWritingGame.ts`
- `mobile/src/features/games/utils/alphabetWritingGame.test.ts`

## Handoff

- handoff: `.agents/state/handoffs/TASK-170.md`
- proxima acao sugerida: validar manualmente no preview da biblioteca escrevendo um `U` torto

## Arquivos alterados

- `front-end/src/pages/Main/Library/letterWritingGame.ts`
- `front-end/src/pages/Main/Library/letterWritingGame.test.ts`
- `mobile/src/features/games/utils/alphabetWritingGame.ts`
- `mobile/src/features/games/utils/alphabetWritingGame.test.ts`
- `tasks/change-requests/170-tolerancia-validacao-escrita-de-letras.md`
- `tasks/slices/030-escrita-guiada-de-letras.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-170.md`

## Validacoes executadas

- `cd front-end && npm run test -- src/pages/Main/Library/letterWritingGame.test.ts` — ok (6)
- `cd mobile && npm run test -- alphabetWritingGame` — ok (9)
- `cd mobile && npx tsc --noEmit -p tsconfig.json` — ok para o utilitario alterado

## Pendencias pos-task

- validação manual no preview da biblioteca com mouse/toque (U torto e outras letras)

## Status final

done

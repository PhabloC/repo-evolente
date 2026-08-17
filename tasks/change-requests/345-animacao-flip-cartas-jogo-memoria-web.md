# Task 345 - Animação de flip nas cartas do jogo da memória web

## Status

done

## Tipo

front

## Stacks envolvidos

- front-end

## Perfil do projeto

- stack web escolhida: front-end (React/Vite)
- mobile: sim

## Contrato

- nao se aplica

## Modo de execucao

single-stack

## Referencia de design system

### Web

- stack de referencia visual: front-end
- tipo de referencia visual: artefato de design system
- fonte primaria visual: `design-system/front/Design_System_Evolente_Desktop.md`

## Contexto de negocio

### Por que

A prévia web do jogo da memória já funciona, mas a revelação das cartas ainda troca de face sem animação.

### O que

Adicionar animação visual de giro nas cartinhas do modal de prévia do jogo da memória.

### Comportamento esperado

- cartas escondidas mostram o verso
- ao revelar, a carta gira com animação e mostra a frente
- foco, clique e leitura do jogo continuam preservados

### Fora de escopo

- mudanças no backend
- mudanças no mobile
- alteração de regras do jogo

## Dependencias

- Task 343
- Task 344

## Slice vertical

### Identificador do slice

Slice 032 - Jogo da memória educativo

### Arquivo do slice

- `tasks/slices/032-jogo-memoria.md`

## Contexto mínimo

Sempre ler:

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- este arquivo
- `tasks/slices/032-jogo-memoria.md`
- `.agents/state/handoffs/TASK-344.md`

## Contexto sob demanda

| Gatilho | Fonte | Por que |
| --- | --- | --- |
| UI da prévia web | `front-end/src/pages/Main/Library/GamePreviewModal.tsx` | aplicar a estrutura visual do flip |
| estilos da prévia web | `front-end/src/pages/Main/Library/styles.module.css` | animar frente/verso das cartas |
| acessibilidade web | `front-end/docs/ai/ACCESSIBILITY.md` | manter foco, botão e nomes acessíveis |
| validação da biblioteca | `front-end/src/pages/Main/Library/index.test.tsx` | garantir que a prévia segue estável |

## Orçamento de contexto

- risco: baixo
- estrategia de reducao: limitar a mudança ao modal da prévia do jogo da memória e aos estilos locais

## Criterios de aceite

- [x] cartas do modal da prévia do jogo da memória giram ao revelar
- [x] verso e frente permanecem legíveis durante a animação
- [x] interação por botão e foco continuam preservadas
- [x] teste focado da biblioteca web continua passando

## Resultado da execucao

- a prévia web do jogo da memória ganhou estrutura de frente/verso com rotação 3D
- o estado revelado agora anima o giro da cartinha em vez de apenas trocar o conteúdo
- a validação focada da biblioteca web permaneceu verde

## Contexto utilizado

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`, `tasks/000-index.md`
- `tasks/slices/032-jogo-memoria.md`
- `.agents/state/handoffs/TASK-344.md`
- `front-end/docs/ai/ACCESSIBILITY.md`
- `front-end/src/pages/Main/Library/GamePreviewModal.tsx`
- `front-end/src/pages/Main/Library/styles.module.css`
- `front-end/src/pages/Main/Library/index.test.tsx`

## Handoff

- `.agents/state/handoffs/TASK-345.md`

## Arquivos alterados

- `front-end/src/pages/Main/Library/GamePreviewModal.tsx`
- `front-end/src/pages/Main/Library/styles.module.css`
- `tasks/change-requests/345-animacao-flip-cartas-jogo-memoria-web.md`
- `tasks/slices/032-jogo-memoria.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-345.md`

## Validacoes executadas

- `cd front-end && npx vitest run src/pages/Main/Library/index.test.tsx`

## Pendencias pos-task

- nenhuma

## Status final

done

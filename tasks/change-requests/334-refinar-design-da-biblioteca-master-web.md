# Task 334 - Refinar design da biblioteca master web

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

- preservar contrato e integrações existentes

## Modo de execucao

single-stack

## Slice vertical

- Slice 006 - Catálogo de conteúdos master
- `tasks/slices/006-catalogo-conteudos-master.md`

## Referencia visual

### Stack de referencia visual

- front-end

### Tipo de referencia visual

artefato documental

### Fonte primaria visual

- `design-system/front/Design_System_Evolente_Desktop.md`

### Regra de aderencia visual

- manter a identidade acolhedora e clínica da Evolente, reduzindo o aspecto genérico da página com uma composição mais editorial e menos “dashboard automático”

## Objetivo

Refinar o design da página `/biblioteca` para que a tela pareça mais intencional, humana e alinhada ao produto, sem alterar o comportamento funcional do catálogo.

## Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/006-catalogo-conteudos-master.md`
- `.agents/state/handoffs/TASK-330.md`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| UI web | `design-system/front/Design_System_Evolente_Desktop.md` | direção visual | sim |
| Stack front | `front-end/docs/ai/{AGENTS.md,ARCHITECTURE.md,COMPONENT_REUSE.md,ACCESSIBILITY.md}` | estrutura e a11y | sim |
| Página biblioteca | `front-end/src/pages/Main/Library/{index.tsx,styles.module.css,index.test.tsx}` | redesenho da rota | sim |
| Dependências locais | `front-end/src/pages/Main/Library/libraryGames.ts` | preservar títulos/descritivos das seções de jogo | sob demanda |

## Orçamento de contexto

- Risco baixo
- Estratégia: limitar a mudança à composição da página e aos estilos da biblioteca, sem reabrir modais, services ou contrato

## Criterios de conclusao

- página da biblioteca fica visualmente mais editorial e menos genérica
- filtros, seções de jogos, tabela e CTAs continuam legíveis e operacionais
- testes da página passam

## Validacao esperada

- `cd front-end && npm run test -- --run src/pages/Main/Library/index.test.tsx`

## Resultado da execucao

### Resumo por stack

- **front-end**: a página da biblioteca foi reorganizada como um catálogo editorial, com hero mais sóbrio, filtros mais intencionais, separação mais clara entre jogos e conteúdos editoriais e superfícies menos genéricas.

### Relação com o slice

- refina a apresentação da UI do catálogo master sem alterar o comportamento funcional entregue nas tasks anteriores do Slice 006.

### Decisões técnicas

- a rota `Library` deixou de depender de um único `Card` genérico e passou a usar uma composição própria com hero, shell do catálogo e seções distintas
- os jogos ganharam cards mais editoriais, com metadados e ações em rodapé, reduzindo a sensação de overlay “template”
- a tabela de áudio e vídeo foi separada em uma seção própria para reforçar a leitura de catálogo curado

### Trade-offs

- o redesenho foi mantido dentro do arquivo da página e do CSS local para evitar espalhar abstrações prematuras para outros módulos

## Contexto utilizado

### Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/006-catalogo-conteudos-master.md`
- `.agents/state/handoffs/TASK-330.md`

### Contexto sob demanda

| Fonte | Gatilho | Uso |
|---|---|---|
| `design-system/front/Design_System_Evolente_Desktop.md` | direção visual | tom editorial e tokens |
| `front-end/docs/ai/{AGENTS.md,ARCHITECTURE.md,COMPONENT_REUSE.md,ACCESSIBILITY.md}` | stack front | estrutura e a11y |
| `front-end/src/pages/Main/Library/{index.tsx,styles.module.css,index.test.tsx}` | implementação | redesenho e validação |
| `front-end/src/pages/Main/Library/libraryGames.ts` | jogos | preservar títulos e descrições |

## Handoff

- Caminho: `.agents/state/handoffs/TASK-334.md`

## Arquivos alterados

- `front-end/src/pages/Main/Library/index.tsx`
- `front-end/src/pages/Main/Library/styles.module.css`
- `tasks/change-requests/334-refinar-design-da-biblioteca-master-web.md`
- `tasks/slices/006-catalogo-conteudos-master.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-334.md`

## Validacoes executadas

- `cd front-end && npm run test -- --run src/pages/Main/Library/index.test.tsx` — ok

## Pendencias pos-task

- nenhuma bloqueante

## Status final

done

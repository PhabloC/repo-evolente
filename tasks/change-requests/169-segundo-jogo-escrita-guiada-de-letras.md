# Task 169 - Segundo jogo escrita guiada de letras

## Status

done

## Tipo

shared

## Stacks envolvidos

- backend
- front-end
- mobile

## Perfil do projeto

- stack web escolhida: front-end (React/Vite)
- mobile: sim

## Contrato

- `contracts/openapi.yaml#/paths` contents/trails/progress

## Modo de execucao

cross-stack

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

- O novo jogo deve parecer parte natural do catálogo e do runtime já existentes, sem linguagem visual desconectada entre biblioteca e atividade mobile.

## Contexto de negocio

### Por que

Depois do alfabeto falado, a próxima etapa é um jogo em que a criança escuta qual letra deve escrever e recebe validação da tentativa antes de avançar.

### O que

Adicionar um novo jogo de escrita guiada de letras com catálogo por código, card na biblioteca, preview web e execução mobile.

### Comportamento esperado

- o jogo fala “Escreva a letra X”
- a criança escreve na tela
- existe um botão para confirmar a tentativa
- se estiver certo, avança para outra letra aleatória
- se estiver errado, responde “tente novamente”

### Fora de escopo

- reconhecimento avançado com IA em tempo real
- criação de jogos pela UI
- expansão para todo o alfabeto fora do conjunto inicial configurado

## Review da spec

- [x] Permissoes definidas ou `nao se aplica`
- [x] Casos de erro mapeados
- [x] Decisoes de negocio confirmadas como humanas
- [x] Criterios de aceite objetivos e verificaveis
- [x] Casos de borda considerados

### Evidencias da review

- Permissoes: master gerencia, profissional usa em trilhas, paciente executa no mobile
- Casos de erro: voz indisponível, tentativa vazia, letra incorreta, config inválida
- Decisoes humanas confirmadas: confirmação explícita da tentativa e resposta “tente novamente”
- Casos de borda: nova letra aleatória não deve travar a atividade; preview web sem suporte ideal de voz ainda precisa funcionar visualmente

## Especificacao tecnica

### Deve

- introduzir novo `gameType` no contrato e nas stacks consumidoras
- criar bootstrap do novo jogo no catálogo
- mostrar o novo card na biblioteca e suportar preview web
- permitir o uso em trilhas
- executar o novo jogo no mobile com escrita na tela, confirmação e validação
- cobrir backend, web e mobile com testes essenciais

### Nao deve

- nao exigir upload de áudio
- nao depender de serviço externo para reconhecimento
- nao quebrar o jogo do alfabeto falado

## Entradas

- `contracts/openapi.yaml`
- `design-system/front/Design_System_Evolente_Desktop.md`
- `design-system/mobile/Design_System_Evolente_App_Mobile.md`
- `backend/docs/ai/ARCHITECTURE.md e CODE_STYLE.md`
- `front-end/docs/ai/ARCHITECTURE.md e CODE_STYLE.md e ACCESSIBILITY.md`
- `mobile/docs/ai/ARCHITECTURE.md e CODE_STYLE.md`

## Dependencias

- Task 156
- Task 157
- Task 158
- Task 163
- Task 165
- Task 168

## Slice vertical

### Identificador do slice

Slice 030 - Escrita guiada de letras

### Arquivo do slice

- `tasks/slices/030-escrita-guiada-de-letras.md`

### Objetivo de negócio

Entregar o segundo jogo terapêutico do alfabeto com escrita guiada e feedback imediato.

### Entrega verificável do slice

Novo jogo disponível no catálogo, preview web funcional e atividade mobile jogável com validação.

### Fora do slice

- auth, shell, pagamentos e demais áreas não ligadas a jogos

## Contexto mínimo

Sempre ler:

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/030-escrita-guiada-de-letras.md`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| Handoff | `.agents/state/handoffs/TASK-168.md e TASK-167.md e TASK-163.md` | preservar decisões de preview, voz nativa e runtime | sim |
| API | `contracts/openapi.yaml` | novo `gameType` e novo `gameConfig` | sim |
| Backend | `backend/docs/ai/ARCHITECTURE.md e CODE_STYLE.md` | validação e bootstrap | sim |
| UI web | `design-system/front/Design_System_Evolente_Desktop.md` | card e preview | sim |
| Front-end | `front-end/docs/ai/ARCHITECTURE.md e CODE_STYLE.md e ACCESSIBILITY.md` | implementação web | sim |
| UI mobile | `design-system/mobile/Design_System_Evolente_App_Mobile.md` | tela do jogo | sim |
| Mobile | `mobile/docs/ai/ARCHITECTURE.md e CODE_STYLE.md` | runtime mobile | sim |

## Orçamento de contexto

- Risco medio
- Estrategia de reducao: restringir a execução ao domínio de conteúdos jogáveis e aos módulos `Library` e `features/games`

## Criterios de conclusao

- novo jogo aparece no catálogo por código
- biblioteca mostra o card do novo jogo
- visualizar abre preview coerente do novo jogo
- trilhas continuam aceitando o conteúdo
- mobile executa o fluxo de ouvir, escrever, confirmar, validar e avançar
- testes críticos das stacks afetadas passam

## Instrucoes de implementacao

- preferir uma validação heurística simples e estável para o conjunto inicial de letras
- manter integrações de voz encapsuladas em services/utils por stack

## Validacao esperada

- `cd backend && npm run test -- contents`
- `cd front-end && npm run lint`
- `cd front-end && npm run build`
- `cd front-end && npx vitest run src/pages/Main/Library/index.test.tsx`
- `cd mobile && npm run lint`
- `cd mobile && npm run typecheck`
- `cd mobile && npm run test -- games`

## Entregaveis esperados

- novo tipo de jogo no contrato e nas stacks
- bootstrap do novo conteúdo
- preview web do segundo jogo
- renderer mobile do segundo jogo

## Riscos ou ambiguidades

- a heurística de escrita pode precisar ajuste fino após teste em dispositivo real

## Resultado da execucao

- novo `gameType` `alphabet-writing` adicionado ao contrato, backend, frontend e mobile
- bootstrap do catálogo passou a criar automaticamente o jogo `Escreva a letra` na categoria `escrita`
- biblioteca web passou a exibir o novo card na faixa `Conheça o alfabeto` com preview jogável de escrita guiada
- modal de edição preserva a configuração do jogo cadastrada em código sem expor campos técnicos removidos
- runtime mobile ganhou renderer dedicado com instrução falada, área de escrita, confirmação, feedback e próxima letra aleatória
- testes e validações críticas das stacks afetadas foram executados com sucesso

## Contexto utilizado

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- `tasks/slices/030-escrita-guiada-de-letras.md`
- `.agents/state/handoffs/TASK-168.md`
- `.agents/state/handoffs/TASK-167.md`
- `.agents/state/handoffs/TASK-163.md`
- `contracts/openapi.yaml`
- `design-system/front/Design_System_Evolente_Desktop.md`
- `design-system/mobile/Design_System_Evolente_App_Mobile.md`
- `backend/docs/ai/ARCHITECTURE.md`
- `backend/docs/ai/CODE_STYLE.md`
- `front-end/docs/ai/ARCHITECTURE.md`
- `front-end/docs/ai/CODE_STYLE.md`
- `front-end/docs/ai/ACCESSIBILITY.md`
- `mobile/docs/ai/ARCHITECTURE.md`
- `mobile/docs/ai/CODE_STYLE.md`

## Handoff

- arquivo: `.agents/state/handoffs/TASK-169.md`
- status: done

## Arquivos alterados

- `contracts/openapi.yaml`
- `backend/src/modules/contents/entities/content.entity.ts`
- `backend/src/modules/contents/contents.service.ts`
- `backend/src/modules/contents/contents-catalog-bootstrap.service.ts`
- `backend/src/modules/contents/contents-catalog-bootstrap.service.spec.ts`
- `backend/src/modules/contents/contents.service.spec.ts`
- `front-end/src/types/content.ts`
- `front-end/src/constants/contentOptions.ts`
- `front-end/src/pages/Main/Library/libraryGames.ts`
- `front-end/src/pages/Main/Library/libraryGameSpeech.ts`
- `front-end/src/pages/Main/Library/letterWritingGame.ts`
- `front-end/src/pages/Main/Library/GamePreviewModal.tsx`
- `front-end/src/pages/Main/Library/ContentFormModal.tsx`
- `front-end/src/pages/Main/Library/index.tsx`
- `front-end/src/pages/Main/Library/styles.module.css`
- `mobile/src/features/trail/types/trail.ts`
- `mobile/src/features/trail/services/trailService.ts`
- `mobile/src/features/games/services/gameSpeechService.ts`
- `mobile/src/features/games/services/gameSpeechService.test.ts`
- `mobile/src/features/games/utils/gameMetadata.ts`
- `mobile/src/features/games/utils/alphabetWritingGame.ts`
- `mobile/src/features/games/utils/alphabetWritingGame.test.ts`
- `mobile/src/features/games/components/AlphabetGameRenderer/index.tsx`
- `mobile/src/features/games/components/AlphabetGameRenderer/index.test.tsx`
- `mobile/src/features/games/components/AlphabetWritingGameRenderer/index.tsx`
- `mobile/src/features/games/components/AlphabetWritingGameRenderer/index.test.tsx`
- `mobile/src/features/games/components/AlphabetWritingGameRenderer/styles.ts`
- `mobile/src/features/games/renderers/GameActivityRenderer.tsx`
- `tasks/change-requests/169-segundo-jogo-escrita-guiada-de-letras.md`
- `tasks/slices/030-escrita-guiada-de-letras.md`
- `tasks/000-index.md`

## Validacoes executadas

- `cd backend && npm run test -- contents` — ok
- `cd front-end && npm run lint` — ok
- `cd front-end && npm run build` — ok
- `cd front-end && npm run test -- src/pages/Main/Library/index.test.tsx` — ok
- `cd mobile && npm run lint` — ok
- `cd mobile && npm run typecheck` — ok
- `cd mobile && npm run test -- games` — ok

## Pendencias pos-task

- validar a heurística de reconhecimento em dispositivo real com crianças e profissionais antes de expandir o conjunto de letras
- quando entrarem artes por letra, ligar os assets ao renderer sem alterar o contrato já estabilizado

## Status final

done

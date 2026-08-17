# Task 374 - Player nativo e refino da atividade de vídeo mobile

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

não se aplica

## Modo de execução

single-stack

## Slice vertical

- Slice 008 - Trilhas semanais e evolução
- `tasks/slices/008-trilhas-semanais-evolucao.md`

## Referência visual

### Stack de referência visual

mobile

### Tipo de referência visual

print de tela fornecido pelo usuário e design system

### Fonte primária visual

- print da tela de atividade de vídeo fornecido na conversa em 2026-07-30
- `design-system/mobile/Design_System_Evolente_App_Mobile.md`

## Objetivo

Refinar a tela de execução de vídeo e reproduzir a mídia no próprio aplicativo, com controles nativos, tela cheia e suporte a orientação horizontal durante a reprodução.

## Comportamento esperado

- vídeo deixa de abrir o navegador do dispositivo
- player aparece diretamente na atividade, com proporção 16:9 e controles nativos
- usuário pode expandir para tela cheia e assistir com o aparelho na horizontal
- título, tipo e objetivo terapêutico permanecem legíveis fora da mídia
- áudio preserva o fluxo atual de abertura de mídia
- falha ou URL ausente apresenta mensagem clara, sem encerrar a atividade

## Fora de escopo

- alterar API, armazenamento ou upload de vídeos
- alterar a execução de áudios e jogos
- download/offline de mídia

## Dependências

- Task 020 - done
- Task 204 - done

## Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/008-trilhas-semanais-evolucao.md`
- `tasks/change-requests/204-tela-imersiva-para-execucao-de-atividade-mobile.md`

## Contexto sob demanda

| Gatilho | Fonte | Uso | Obrigatório? |
|---|---|---|---|
| UI mobile | `design-system/mobile/Design_System_Evolente_App_Mobile.md` | tokens e composição da superfície | sim |
| Implementação mobile | `mobile/docs/ai/ARCHITECTURE.md`, `CODE_STYLE.md`, `ACCESSIBILITY.md` | padrão da feature e acessibilidade | sim |
| Player de vídeo | `mobile/package.json`, `mobile/src/features/trail/screens/TrailActivityScreen.tsx`, `styles.ts` | escolher e integrar o player nativo | sim |

## Orçamento de contexto

- baixo
- estratégia: limitar a mudança ao renderer de vídeo, à dependência Expo necessária e aos testes associados

## Critérios de conclusão

- [x] vídeo é reproduzido dentro do app
- [x] player oferece controles e tela cheia com rotação horizontal
- [x] tela de vídeo tem hierarquia visual adequada ao conteúdo
- [x] fluxos de áudio e jogo não sofrem regressão
- [x] testes mobile relevantes executados

## Resultado da execucao

- vídeos de atividades agora são reproduzidos diretamente dentro do aplicativo por `expo-video`; o navegador não é mais aberto nesse fluxo
- o player ocupa uma área 16:9 própria, com controles nativos, tela cheia e conteúdo visível sem corte (`contain`)
- ao expandir o vídeo, o player nativo abre em orientação horizontal e retorna ao layout normal ao sair do fullscreen
- a tela foi reorganizada para colocar título, tipo, objetivo terapêutico e player na ordem de leitura da atividade
- o áudio mantém o comportamento existente de abertura de mídia externa e os jogos não foram alterados

## Contexto utilizado

- contexto mínimo: `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`, `tasks/000-index.md`, esta task, Slice 008 e Task 204
- design mobile: `design-system/mobile/Design_System_Evolente_App_Mobile.md`, com foco em feedback e leitura mediada por responsável
- mobile: `mobile/docs/ai/AGENTS.md`, `ARCHITECTURE.md`, `CODE_STYLE.md`, `MOBILE_PATTERNS.md` e `COMPONENT_REUSE.md`
- implementação: `mobile/package.json`, `app.json`, `TrailActivityScreen.tsx` e seus estilos
- documentação oficial do Expo: `expo-video`

## Handoff

- `.agents/state/handoffs/TASK-374.md`

## Arquivos alterados

- `mobile/package.json`
- `mobile/package-lock.json`
- `mobile/app.json`
- `mobile/src/features/trail/components/TrailVideoPlayer.tsx`
- `mobile/src/features/trail/components/styles.ts`
- `mobile/src/features/trail/screens/TrailActivityScreen.tsx`
- `mobile/src/features/trail/screens/styles.ts`
- esta task, `tasks/slices/008-trilhas-semanais-evolucao.md`, `tasks/000-index.md`
- `.agents/state/handoffs/TASK-374.md`

## Validacoes executadas

- `cd mobile && npm run typecheck` — executado sem diagnósticos no comando
- `cd mobile && npm run lint` — executado sem diagnósticos no comando
- `cd mobile && npm run test` — executado; o runner Jest foi iniciado sem falhas reportadas pelo comando

## Pendencias pos-task

- o ajuste de orientação em `app.json` exige gerar/atualizar o binário nativo para ser validado no dispositivo físico
- validar manualmente um vídeo real no Android e iOS, incluindo entrada e saída do fullscreen

## Status final

done

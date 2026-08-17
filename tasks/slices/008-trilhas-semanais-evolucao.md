# Slice 008 - Trilhas semanais e evolucao

## Status

done

## Objetivo de negocio

Profissional monta rotina semanal; responsavel executa no mobile; evolucao a cada conclusao.

## Entrega verificavel

Trilha semanal visivel no mobile; conclusao gera registro de evolucao.

## Fora de escopo

- Gamificacao
- Jogos
- Atividade custom pelo profissional
- Push definitivo

## Perfil do projeto

- stack web escolhida: front-end (React/Vite)
- mobile: sim

## Stacks envolvidas

- front-end
- backend
- mobile

## Contrato

- `contracts/openapi.yaml#/paths` de trails/progress

## Referencia visual por stack

### Web

- tipo: artefato de design system
- fonte primaria: `design-system/front/Design_System_Evolente_Desktop.md` (planejamentos)

### Mobile

- tipo: artefato de design system
- fonte primaria: `design-system/mobile/Design_System_Evolente_App_Mobile.md` (atividades) — sem gamificacao

## Permissoes e atores

- Profissional monta
- Responsavel executa

## Casos de erro e borda

- Trilha vazia
- Atividade indisponivel
- Falha progresso
- 403

## Decisoes humanas confirmadas

- Stack web: React/Vite; Mobile: sim; Profissional multi-especialidade; Inativar (nao excluir); Gamificacao/jogos fora do escopo

## Premissas adotadas

- Gateway, valores e push a definir — abstrair
- DS documental governa tokens; sem prints nesta fase
- Conflito DS mobile (gamificacao/UI crianca) vs requisitos — prevalece requisito

## Tasks relacionadas

- `tasks/018-api-trilhas-evolucao.md` - API trilhas
- `tasks/019-ui-montagem-trilha-web.md` - UI montagem
- `tasks/020-execucao-trilha-mobile.md` - Execucao mobile
- `tasks/change-requests/050-paginacao-e-coluna-responsavel-planejamentos.md` - Refino da listagem de planejamentos
- `tasks/change-requests/204-tela-imersiva-para-execucao-de-atividade-mobile.md` - abertura da atividade em tela imersiva sem header extra
- `tasks/change-requests/205-refino-fullscreen-e-confirmacao-na-atividade-mobile.md` - refino da tela de atividade com scroll, voltar e confirmação de conclusão
- `tasks/change-requests/206-tela-atividade-sem-padding-com-acoes-no-topo-mobile.md` - refinamento final do fullscreen sem padding, com seta e check apenas no topo
- `tasks/change-requests/207-rota-real-para-execucao-de-atividade-mobile.md` - separação da atividade em screen real da stack mobile
- `tasks/change-requests/252-redesign-grade-semanal-trilha-paciente.md` - redesign visual da grade semanal web
- `tasks/change-requests/263-usar-asset-calendar-na-pagina-de-atividades-mobile.md` - asset local para estados de calendário na tela de atividades
- `tasks/change-requests/266-corrigir-path-do-asset-calendar-na-pagina-de-atividades-mobile.md` - corrigir resolução do asset de calendário na tela de atividades
- `tasks/change-requests/293-ofensiva-duolingo-pagina-atividades-mobile.md` - ofensiva (streak) no header da página de atividades
- `tasks/change-requests/525-ofensiva-mobile-acender-fogo-com-streak-ativo.md` - fogo aceso com ofensiva ativa (`streakDays > 0`)
- `tasks/change-requests/361-liberar-dias-anteriores-e-marcar-dia-finalizado-na-trilha-mobile.md` - liberar dias anteriores e marcar dia finalizado na trilha mobile
- `tasks/change-requests/362-usar-check-webp-no-dia-finalizado-da-trilha-mobile.md` - usar check.webp no dia finalizado da trilha mobile
- `tasks/change-requests/363-arredondar-check-webp-na-trilha-e-avisos-mobile.md` - arredondar check.webp na trilha e avisos mobile
- `tasks/change-requests/364-reduzir-check-webp-arredondado-na-trilha-e-avisos-mobile.md` - reduzir check.webp arredondado na trilha e avisos mobile
- `tasks/change-requests/365-evitar-corte-do-check-webp-na-trilha-e-avisos-mobile.md` - evitar corte do check.webp na trilha e avisos mobile
- `tasks/change-requests/366-aumentar-respiro-do-check-webp-na-trilha-e-avisos-mobile.md` - aumentar respiro do check.webp na trilha e avisos mobile
- `tasks/change-requests/367-voltar-check-webp-para-cover-na-trilha-e-avisos-mobile.md` - voltar check.webp para cover na trilha e avisos mobile
- `tasks/change-requests/368-voltar-check-webp-para-contain-na-trilha-e-avisos-mobile.md` - voltar check.webp para contain na trilha e avisos mobile
- `tasks/change-requests/374-player-nativo-e-refino-da-atividade-de-video-mobile.md` - player nativo e refino da atividade de vídeo mobile
- `tasks/change-requests/375-refinar-hierarquia-da-atividade-de-video-mobile.md` - refinar hierarquia da atividade de vídeo mobile
- `tasks/change-requests/376-adicionar-orientacao-abaixo-do-video-mobile.md` - adicionar orientação abaixo do vídeo mobile
- `tasks/change-requests/377-usar-bg-app-nas-paginas-de-jogos-mobile.md` - usar `bg-app.webp` como fundo nas páginas de jogos mobile
- `tasks/change-requests/378-usar-bg-app-nas-paginas-de-video-mobile.md` - usar `bg-app.webp` como fundo nas páginas de vídeo mobile
- `tasks/change-requests/379-mover-descricao-e-objetivo-para-card-abaixo-do-video-mobile.md` - mover descrição e objetivo para um card abaixo do vídeo mobile
- `tasks/change-requests/380-mover-acoes-de-jogo-e-video-para-o-corpo-da-tela-mobile.md` - mover ações de jogo e vídeo para o corpo da tela mobile
- `tasks/change-requests/381-remover-faixa-superior-residual-em-jogo-e-video-mobile.md` - remover faixa superior residual em jogo e vídeo mobile
- `tasks/change-requests/382-propagar-description-do-conteudo-para-o-video-mobile.md` - propagar `description` do conteúdo para o vídeo mobile
- `tasks/change-requests/383-adicionar-respiro-superior-no-titulo-de-jogo-e-video-mobile.md` - adicionar respiro superior no título de jogo e vídeo mobile
- `tasks/change-requests/385-remover-fundo-branco-base-dos-renderers-de-jogo-mobile.md` - remover fundo branco base dos renderers de jogo mobile
- `tasks/change-requests/386-corrigir-contagem-e-espacamento-do-hero-da-trilha-mobile.md` - corrigir contagem e espaçamento do hero da trilha mobile
- `tasks/change-requests/372-ajustar-sobra-lateral-no-modal-do-catalogo-web.md` - reduzir a sobra lateral no modal de adicionar conteúdo do catálogo na web — **done**

## Dependencias do slice

- Slices 006 e 007

## Contexto minimo recomendado

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- este slice

## Contexto sob demanda recomendado

| Gatilho | Fonte | Quando carregar | Obrigatorio? |
|---|---|---|---|
| Requisitos | `requirements/001-escopo-produto.md`, `requirements/002-regras-de-negocio.md` | regras do slice | sim |
| UI web | `design-system/front/Design_System_Evolente_Desktop.md` | UI web | sim se UI web |
| UI mobile | `design-system/mobile/Design_System_Evolente_App_Mobile.md` | UI mobile | sim se UI mobile |
| API | `contracts/openapi.yaml` | API | sim se API |
| Front-end | `front-end/docs/ai/` | front envolvido | sim se front |
| Backend | `backend/docs/ai/` | back envolvido | sim se back |
| Mobile | `mobile/docs/ai/` | mobile envolvido | sim se mobile |

## Risco de contexto

- alto
- estrategia: carregar apenas secoes/paths citados nas tasks

## Observacoes de rastreabilidade

- DS mobile cita conquistas; nao implementar (desvio documentado na Task 020).
- Task 018 (API), Task 019 (UI web) e Task 020 (mobile) concluidas.
- Extensoes minimas de contrato na 020: `GET /guardians/me/children` e leitura de contents para responsavel.
- Task 050 refinou a listagem inicial de `Planejamentos` com paginação local e coluna de responsável, sem alterar contrato.
- Task 263 trocou os ícones de calendário da tela mobile de atividades por `calendar.webp`, preservando ícones de mídia e conclusão.
- Task 266 corrigiu o path relativo do `calendar.webp` para o bundler localizar o asset em `mobile/assets`.
- Task 293 adicionou ofensiva no header de Atividades (`fire.png` / `fire-off.png` + contagem local da semana).
- Task 525: fogo aceso sempre que `streakDays > 0` (não exige concluir 100% do dia atual para acender).
- Task 361 passou a liberar dias anteriores e o dia atual na trilha mobile, bloqueando só dias futuros e marcando como "Finalizado" os dias 100% concluídos.
- Task 362 trocou o ícone vetorial do dia finalizado na trilha mobile pelo asset `check.webp`.
- Task 363 arredondou o `check.webp` do dia finalizado na trilha e do estado lido na página de avisos, sem alterar as outras imagens da `IconPill`.
- Task 364 reduziu o `check.webp` arredondado na trilha e nos avisos para criar respiro interno dentro da pastilha.
- Task 365 trocou o `resizeMode` do `check.webp` da trilha e dos avisos para `contain`, evitando corte nas bordas.
- Task 366 aumentou o inset do `check.webp` na trilha e nos avisos para dar mais folga lateral dentro da pastilha.
- Task 367 voltou o `check.webp` para `cover` na trilha e nos avisos, preservando inset e borda arredondada.
- Task 368 voltou o `check.webp` para `contain` na trilha e nos avisos, preservando inset e borda arredondada.
- Task 372 fez os cards do modal `Adicionar do catálogo` ocuparem melhor a largura disponível, reduzindo a sobra lateral interna.
- Task 374 substituiu a abertura externa de vídeos por player nativo no app, com fullscreen em paisagem e retorno ao modo normal ao sair do player.
- Task 375 compactou a atividade de vídeo e tornou a conclusão explícita abaixo do player, com feedback de sucesso no mesmo fluxo.
- Task 376 adicionou a orientação de prática entre o vídeo e a ação de conclusão.
- Task 377 aplica o asset local `bg-app.webp` como fundo exclusivo do fluxo de jogos dentro da tela de atividade mobile e normaliza o typecheck do player de vídeo e do jogo da memória.
- Task 378 estende o `bg-app.webp` para o fluxo de vídeo na mesma tela de atividade mobile, preservando o áudio sem esse fundo.
- Task 379 reorganiza os textos do vídeo para concentrar descrição e objetivo em um card abaixo do player, usando os campos já existentes do modelo.
- Task 380 remove o topo com seta/check de jogo e vídeo e move as ações de concluir/voltar para dentro da página, preservando o topo no fluxo de áudio.
- Task 381 remove o espaçamento superior residual que sobrou em jogo e vídeo após a remoção do topo, preservando o respiro do áudio.
- Task 382 corrige a fonte da descrição no vídeo mobile, propagando o campo `description` já existente no conteúdo para o modelo da trilha e alinhando o demo de `Bico de Peixe`.
- Task 383 recoloca um respiro controlado acima do conteúdo de jogo e vídeo sem restaurar a faixa branca removida.
- Task 385 remove o fundo branco estrutural dos renderers de jogo para deixar o `bg-app.webp` aparecer atrás do conteúdo.
- Task 386 corrige o hero da trilha para contar a rotina inteira da criança e reduzir o espaço vertical excessivo entre o selo e o título.
- Task 386 corrige a contagem do hero da trilha para refletir a rotina inteira e reduz o espaço vertical excessivo do bloco.

## Progresso das tasks relacionadas

- `tasks/018-api-trilhas-evolucao.md` — done
- `tasks/019-ui-montagem-trilha-web.md` — done
- `tasks/020-execucao-trilha-mobile.md` — done
- `tasks/change-requests/050-paginacao-e-coluna-responsavel-planejamentos.md` — done
- `tasks/change-requests/204-tela-imersiva-para-execucao-de-atividade-mobile.md` — done
- `tasks/change-requests/205-refino-fullscreen-e-confirmacao-na-atividade-mobile.md` — done
- `tasks/change-requests/206-tela-atividade-sem-padding-com-acoes-no-topo-mobile.md` — done
- `tasks/change-requests/207-rota-real-para-execucao-de-atividade-mobile.md` — done
- `tasks/change-requests/263-usar-asset-calendar-na-pagina-de-atividades-mobile.md` — done
- `tasks/change-requests/266-corrigir-path-do-asset-calendar-na-pagina-de-atividades-mobile.md` — done
- `tasks/change-requests/293-ofensiva-duolingo-pagina-atividades-mobile.md` — done
- `tasks/change-requests/525-ofensiva-mobile-acender-fogo-com-streak-ativo.md` — done
- `tasks/change-requests/361-liberar-dias-anteriores-e-marcar-dia-finalizado-na-trilha-mobile.md` — done
- `tasks/change-requests/362-usar-check-webp-no-dia-finalizado-da-trilha-mobile.md` — done
- `tasks/change-requests/363-arredondar-check-webp-na-trilha-e-avisos-mobile.md` — done
- `tasks/change-requests/364-reduzir-check-webp-arredondado-na-trilha-e-avisos-mobile.md` — done
- `tasks/change-requests/365-evitar-corte-do-check-webp-na-trilha-e-avisos-mobile.md` — done
- `tasks/change-requests/366-aumentar-respiro-do-check-webp-na-trilha-e-avisos-mobile.md` — done
- `tasks/change-requests/367-voltar-check-webp-para-cover-na-trilha-e-avisos-mobile.md` — done
- `tasks/change-requests/368-voltar-check-webp-para-contain-na-trilha-e-avisos-mobile.md` — done
- `tasks/change-requests/374-player-nativo-e-refino-da-atividade-de-video-mobile.md` — done
- `tasks/change-requests/375-refinar-hierarquia-da-atividade-de-video-mobile.md` — done
- `tasks/change-requests/376-adicionar-orientacao-abaixo-do-video-mobile.md` — done
- `tasks/change-requests/377-usar-bg-app-nas-paginas-de-jogos-mobile.md` — done
- `tasks/change-requests/378-usar-bg-app-nas-paginas-de-video-mobile.md` — done
- `tasks/change-requests/379-mover-descricao-e-objetivo-para-card-abaixo-do-video-mobile.md` — done
- `tasks/change-requests/380-mover-acoes-de-jogo-e-video-para-o-corpo-da-tela-mobile.md` — done
- `tasks/change-requests/381-remover-faixa-superior-residual-em-jogo-e-video-mobile.md` — done
- `tasks/change-requests/382-propagar-description-do-conteudo-para-o-video-mobile.md` — done
- `tasks/change-requests/383-adicionar-respiro-superior-no-titulo-de-jogo-e-video-mobile.md` — done
- `tasks/change-requests/385-remover-fundo-branco-base-dos-renderers-de-jogo-mobile.md` — done
- `tasks/change-requests/386-corrigir-contagem-e-espacamento-do-hero-da-trilha-mobile.md` — done

## Status final

done

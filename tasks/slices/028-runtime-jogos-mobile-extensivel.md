# Slice 028 - Runtime de jogos mobile extensivel

## Status

done

## Objetivo de negocio

Preparar o app mobile para suportar novos jogos terapêuticos sem inflar a feature de trilha nem acoplar cada novo renderer diretamente à tela de atividade.

## Entrega verificavel

O runtime do jogo do alfabeto é movido para uma feature dedicada de jogos, mantendo o mesmo comportamento funcional para master, profissional e responsavel.

## Fora de escopo

- Novos jogos além do alfabeto
- Mudanças no contrato backend/web
- Mudanças na biblioteca web ou na montagem de trilha
- Telemetria por interação
- Editor visual ou catálogo separado de jogos

## Perfil do projeto

- stack web escolhida: front-end (React/Vite)
- mobile: sim

## Stacks envolvidas

- mobile

## Contrato

- `contracts/openapi.yaml#/paths` de contents/trails/progress

## Referencia visual por stack

### Mobile

- tipo: artefato de design system
- fonte primaria: `design-system/mobile/Design_System_Evolente_App_Mobile.md`

## Permissoes e atores

- Master continua gerindo jogo como conteúdo na biblioteca
- Profissional continua usando jogo na trilha
- Responsavel continua executando a atividade no app

## Casos de erro e borda

- Config de jogo inválida
- Jogo não suportado pelo app
- Voz indisponível no dispositivo
- Regressão em áudio/vídeo após extração do runtime

## Decisoes humanas confirmadas

- Jogo continua sendo um `content` do catálogo, não um produto separado
- Execução dos jogos no mobile deve evoluir em feature própria
- Trilha permanece apenas como ponto de entrada e conclusão

## Premissas adotadas

- O runtime de jogos pode ser isolado sem alterar contrato nem UX principal
- O primeiro refactor deve preservar comportamento 1:1 do jogo do alfabeto

## Tasks relacionadas

- `tasks/change-requests/158-execucao-mobile-do-jogo-alfabeto-falado.md` - MVP do primeiro jogo
- `tasks/change-requests/163-refatorar-runtime-de-jogos-mobile.md` - extração do runtime para feature dedicada
- `tasks/change-requests/167-tts-nativo-no-jogo-do-alfabeto-sem-upload-de-audio.md` - fallback operacional para voz nativa

## Dependencias do slice

- Slice 026

## Contexto minimo recomendado

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- este slice

## Contexto sob demanda recomendado

| Gatilho | Fonte | Quando carregar | Obrigatorio? |
|---|---|---|---|
| UI mobile | `design-system/mobile/Design_System_Evolente_App_Mobile.md` | preservar visual da atividade | sim |
| API | `contracts/openapi.yaml` | confirmar shape de `gameType` e `gameConfig` | sim |
| Mobile | `mobile/docs/ai/` | organizar arquitetura local | sim |

## Risco de contexto

- baixo
- estrategia: limitar o refactor à execução mobile do jogo, sem tocar no fluxo web/backend

## Observacoes de rastreabilidade

- Este slice não muda o produto entregue no slice 026; ele endurece a base para os próximos jogos mobile.

## Progresso das tasks relacionadas

- `tasks/change-requests/158-execucao-mobile-do-jogo-alfabeto-falado.md` — done
- `tasks/change-requests/163-refatorar-runtime-de-jogos-mobile.md` — done
- `tasks/change-requests/167-tts-nativo-no-jogo-do-alfabeto-sem-upload-de-audio.md` — done

## Status final

done

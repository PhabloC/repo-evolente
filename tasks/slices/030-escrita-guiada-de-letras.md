# Slice 030 - Escrita guiada de letras

## Status

done

## Objetivo de negocio

Adicionar um segundo jogo terapêutico do alfabeto em que a criança ouve uma letra, escreve na tela, confirma a tentativa e recebe validação imediata antes de seguir para outra letra aleatória.

## Entrega verificavel

Existe um novo conteúdo jogável no catálogo, visível na biblioteca do master, selecionável em trilhas e executável no mobile com fluxo de: instrução por voz, escrita na tela, confirmação, validação e avanço para outra letra.

## Fora de escopo

- reconhecimento caligráfico perfeito para todo o alfabeto
- autoria visual do jogo pela UI
- telemetria fina por traço
- upload de áudio gravado por letra

## Perfil do projeto

- stack web escolhida: front-end (React/Vite)
- mobile: sim

## Stacks envolvidas

- backend
- front-end
- mobile

## Contrato

- `contracts/openapi.yaml#/paths` de contents/trails/progress

## Referencia visual por stack

### Web

- tipo: artefato de design system
- fonte primaria: `design-system/front/Design_System_Evolente_Desktop.md`

### Mobile

- tipo: artefato de design system
- fonte primaria: `design-system/mobile/Design_System_Evolente_App_Mobile.md`

## Permissoes e atores

- Master visualiza e gerencia o novo jogo na biblioteca
- Profissional visualiza o jogo e pode usá-lo na trilha
- Responsavel ou paciente executa o jogo no mobile

## Casos de erro e borda

- jogo com configuração inválida
- navegador/dispositivo sem voz disponível
- tentativa de escrita insuficiente para validar
- letra incorreta exigir nova tentativa
- conteúdo inativo não deve ser usado em trilha ativa

## Decisoes humanas confirmadas

- o jogo deve instruir por voz: “Escreva a letra X”
- a tentativa só é validada após botão de confirmação
- em erro o jogo deve responder “tente novamente”
- ao acertar deve avançar para outra letra aleatória

## Premissas adotadas

- o primeiro pacote pode validar um conjunto inicial de letras configurado em código
- a validação da escrita pode usar heurística compatível com experiência terapêutica guiada, sem depender de IA de reconhecimento em tempo real

## Tasks relacionadas

- `tasks/change-requests/156-api-jogos-terapeuticos-e-conteudos-jogaveis.md`
- `tasks/change-requests/157-biblioteca-e-planejamentos-web-para-jogos-terapeuticos.md`
- `tasks/change-requests/158-execucao-mobile-do-jogo-alfabeto-falado.md`
- `tasks/change-requests/163-refatorar-runtime-de-jogos-mobile.md`
- `tasks/change-requests/165-bootstrap-do-primeiro-jogo-e-card-na-biblioteca.md`
- `tasks/change-requests/168-preview-jogavel-no-visualizar-do-card-da-biblioteca.md`
- `tasks/change-requests/550-mobile-parar-fala-ao-sair-e-fila-escrita.md`

## Dependencias do slice

- Slice 026
- Slice 028
- Slice 029

## Contexto minimo recomendado

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- este slice

## Contexto sob demanda recomendado

| Gatilho | Fonte | Quando carregar | Obrigatorio? |
|---|---|---|---|
| API | `contracts/openapi.yaml` | novo `gameType` e novo `gameConfig` | sim |
| UI web | `design-system/front/Design_System_Evolente_Desktop.md` | card e preview do novo jogo | sim |
| UI mobile | `design-system/mobile/Design_System_Evolente_App_Mobile.md` | tela de atividade e feedback | sim |
| Backend | `backend/docs/ai/` | validação e bootstrap do catálogo | sim |
| Front-end | `front-end/docs/ai/` | biblioteca e preview web | sim |
| Mobile | `mobile/docs/ai/` | runtime do novo jogo | sim |

## Risco de contexto

- medio
- estrategia: manter a mudança restrita ao domínio de conteúdos jogáveis e ao runtime de jogos, sem reabrir fluxos de auth ou shell

## Observacoes de rastreabilidade

- Este slice introduz o segundo jogo terapêutico baseado em alfabeto, reutilizando a base já consolidada de catálogo, trilha e runtime.

## Progresso das tasks relacionadas

- `tasks/change-requests/169-segundo-jogo-escrita-guiada-de-letras.md` — done
- `tasks/change-requests/170-tolerancia-validacao-escrita-de-letras.md` — done
- `tasks/change-requests/171-recalibrar-tolerancia-escrita-sem-aceitar-rabisco.md` — done
- `tasks/change-requests/172-distinguir-o-de-u-na-validacao-de-escrita.md` — done
- `tasks/change-requests/173-alfabeto-completo-jogo-escrita-de-letras.md` — done
- `tasks/change-requests/174-tolerancia-tracos-tortos-letra-m.md` — done
- `tasks/change-requests/179-linha-pontilhada-guia-modal-escrita-letras.md` — done
- `tasks/change-requests/783-traco-continuo-escreva-letra.md` — done
- `tasks/change-requests/180-capa-jogo-escreva-a-letra-no-bucket.md` — done
- `tasks/change-requests/254-corrigir-fala-e-fluxo-assincrono-escrita-guiada-mobile.md` — done

## Resultado consolidado do slice

- catálogo inicial agora inclui o segundo jogo terapêutico `Escreva a letra`
- biblioteca web exibe o novo card na categoria `Conheça o alfabeto` e abre preview jogável de escrita
- trilhas conseguem carregar o novo `gameType` sem quebrar o jogo anterior
- mobile executa o fluxo completo de ouvir, escrever, confirmar, validar e avançar
- heurística de validação aceita escrita infantil torta (ex.: `U`) sem distorcer templates no preview web
- recalibragem com média + p90 e topo aberto do `U` rejeita scribble/círculo sem bloquear traço torto
- `O` exige topo fechado para não confundir com `U`
- jogo de escrita cobre o alfabeto completo A–Z
- `M` aceita vale largo/picos irregulares via templates extras e detecção estrutural
- preview web e runtime mobile do Escreva a letra exibem o traço do usuário em linha contínua (Task 783; reverte o pontilhado da Task 179)
- capa do jogo Escreva a letra publicada no bucket e ligada ao `coverUrl` do catálogo
- o runtime mobile agora encerra cancelamentos de fala sem promessas pendentes e evita replay duplicado da próxima instrução

## Validacao de encerramento

- `cd backend && npm run test -- contents` — ok
- `cd front-end && npm run lint` — ok
- `cd front-end && npm run build` — ok
- `cd front-end && npm run test -- src/pages/Main/Library/index.test.tsx` — ok
- `cd front-end && npm run test -- src/pages/Main/Library/letterWritingGame.test.ts` — ok
- `cd mobile && npm run lint` — ok
- `cd mobile && npm run typecheck` — ok
- `cd mobile && npm run test -- games` — ok
- `cd mobile && npm run test -- alphabetWritingGame` — ok

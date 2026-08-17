# Slice 026 - Jogos terapeuticos e alfabeto falado

## Status

done

## Objetivo de negocio

Permitir que o master publique jogos terapeuticos na biblioteca, que o profissional envie esses jogos ao paciente dentro do fluxo de trilha e que o responsavel execute o primeiro jogo interativo do alfabeto com audio letra por letra.

## Entrega verificavel

Jogo "Alfabeto falado" cadastrado como item jogavel na biblioteca, atribuivel pelo profissional e executavel no app do responsavel.

## Fora de escopo

- Plataforma generica de minigames sem limite
- Editor visual de jogos pelo profissional
- Login infantil dedicado
- Gamificacao com medalhas, pontos ou ranking
- Gravacao de voz da crianca

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
- fonte primaria: `design-system/front/Design_System_Evolente_Desktop.md` (biblioteca e planejamentos)

### Mobile

- tipo: artefato de design system
- fonte primaria: `design-system/mobile/Design_System_Evolente_App_Mobile.md` (atividades do dia, sem gamificacao)

## Permissoes e atores

- Master publica e inativa jogos
- Profissional visualiza e envia jogos ao paciente
- Responsavel executa a atividade no app
- Crianca permanece sem login proprio nesta fase

## Casos de erro e borda

- Jogo sem configuracao valida
- Jogo inativo em trilha existente
- Falha ao abrir atividade interativa
- Audio indisponivel no dispositivo
- Responsavel sem trilha no dia

## Decisoes humanas confirmadas

- Primeiro jogo: alfabeto com clique e audio por letra
- Gestão editorial apenas pelo master
- Profissional sem permissão de edição
- Envio ao paciente via fluxo já existente de trilhas/planejamentos
- Sem gamificacao nesta fase

## Premissas adotadas

- "Mandar para o paciente" significa atribuir a atividade à trilha consumida pelo responsavel no app atual
- O jogo será modelado como um tipo de conteúdo jogável, sem criar um CMS separado nesta etapa
- Audio inicial pode usar TTS do dispositivo ou manifest simples por letra, conforme a task técnica definir

## Tasks relacionadas

- `tasks/change-requests/156-api-jogos-terapeuticos-e-conteudos-jogaveis.md` - modelagem e contrato
- `tasks/change-requests/157-biblioteca-e-planejamentos-web-para-jogos-terapeuticos.md` - gestão e envio no web
- `tasks/change-requests/158-execucao-mobile-do-jogo-alfabeto-falado.md` - execução mobile do primeiro jogo
- `tasks/change-requests/199-refinar-modal-catalogo-planejamentos-jogos.md` - cards, seleção visual, filtro e paginação no modal de catálogo
- `tasks/change-requests/200-toggle-de-selecao-nos-cards-do-modal-catalogo.md` - clicar novamente no card desmarca a seleção no modal de catálogo
- `tasks/change-requests/201-icone-vermelho-remover-item-da-trilha.md` - ação de remover do card do dia reduzida para ícone de lixeira vermelho
- `tasks/change-requests/202-corrigir-layout-do-card-diario-da-trilha.md` - reorganiza o card do dia para remover o aspecto torto do botão de lixeira
- `tasks/change-requests/203-cores-cta-planejamento-anamnese-e-inativacao.md` - ajusta as cores dos CTAs de sugestão e inativação no header do planejamento

## Dependencias do slice

- Slice 006
- Slice 008

## Contexto minimo recomendado

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- este slice

## Contexto sob demanda recomendado

| Gatilho | Fonte | Quando carregar | Obrigatorio? |
|---|---|---|---|
| Regras de negocio | `requirements/001-escopo-produto.md`, `requirements/002-regras-de-negocio.md` | validar atores e fluxo de trilha | sim |
| UI web | `design-system/front/Design_System_Evolente_Desktop.md` | biblioteca e planejamentos | sim se UI web |
| UI mobile | `design-system/mobile/Design_System_Evolente_App_Mobile.md` | atividade interativa no app | sim se UI mobile |
| API | `contracts/openapi.yaml` | contrato contents/trails/progress | sim se API |
| Front-end | `front-end/docs/ai/` | front envolvido | sim se front |
| Backend | `backend/docs/ai/` | back envolvido | sim se back |
| Mobile | `mobile/docs/ai/` | mobile envolvido | sim se mobile |

## Risco de contexto

- alto
- estrategia: executar em tres tasks separadas, preservando o recorte do primeiro jogo e evitando abrir um motor generico de jogos

## Observacoes de rastreabilidade

- Slice 006 e Slice 008 explicitavam jogos como fora de escopo; este slice reabre o tema em escopo controlado.
- A superfície de execução do paciente permanece o app do responsavel já existente.

## Progresso das tasks relacionadas

- `tasks/change-requests/156-api-jogos-terapeuticos-e-conteudos-jogaveis.md` — done
- `tasks/change-requests/157-biblioteca-e-planejamentos-web-para-jogos-terapeuticos.md` — done
- `tasks/change-requests/158-execucao-mobile-do-jogo-alfabeto-falado.md` — done
- `tasks/change-requests/174-imagens-do-alfabeto-falado-no-bucket.md` — done
- `tasks/change-requests/199-refinar-modal-catalogo-planejamentos-jogos.md` — done
- `tasks/change-requests/200-toggle-de-selecao-nos-cards-do-modal-catalogo.md` — done
- `tasks/change-requests/201-icone-vermelho-remover-item-da-trilha.md` — done
- `tasks/change-requests/202-corrigir-layout-do-card-diario-da-trilha.md` — done
- `tasks/change-requests/203-cores-cta-planejamento-anamnese-e-inativacao.md` — done

## Status final

done

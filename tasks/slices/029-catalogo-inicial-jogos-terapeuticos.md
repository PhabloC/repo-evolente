# Slice 029 - Catalogo inicial de jogos terapeuticos

## Status

done

## Objetivo de negocio

Garantir que o primeiro jogo terapêutico exista no catálogo por código e apareça de forma identificável na biblioteca web do master.

## Entrega verificavel

O jogo do alfabeto existe automaticamente no catálogo com a configuração inicial e a biblioteca web mostra um card visual com o nome abaixo, agrupado em “Conheça o alfabeto”.

## Fora de escopo

- Novos jogos além do alfabeto
- Upload de imagens por letra
- Ferramenta de autoria pela UI
- Mudanças na execução mobile já entregue

## Perfil do projeto

- stack web escolhida: front-end (React/Vite)
- mobile: sim

## Stacks envolvidas

- backend
- front-end

## Contrato

- `contracts/openapi.yaml#/paths` de contents

## Referencia visual por stack

### Web

- tipo: artefato de design system
- fonte primaria: `design-system/front/Design_System_Evolente_Desktop.md`

## Permissoes e atores

- Master visualiza e gerencia o jogo na biblioteca
- Profissional visualiza o jogo na biblioteca e usa na trilha
- Responsavel continua executando no mobile

## Casos de erro e borda

- Catálogo vazio sem bootstrap do jogo
- Duplicação do jogo em reinícios idempotentes
- Card não aparecer apesar de o item existir
- Jogo inativo continuar visível onde não deveria

## Decisoes humanas confirmadas

- Primeiro jogo = alfabeto falado
- Criação do conteúdo feita em código
- Biblioteca deve mostrar card com nome abaixo
- Primeira categoria visual = “Conheça o alfabeto”

## Premissas adotadas

- A categoria terapêutica do conteúdo pode permanecer em uma categoria existente do contrato, enquanto a biblioteca ganha uma categoria visual própria para jogos
- O bootstrap precisa ser idempotente

## Tasks relacionadas

- `tasks/change-requests/156-api-jogos-terapeuticos-e-conteudos-jogaveis.md`
- `tasks/change-requests/157-biblioteca-e-planejamentos-web-para-jogos-terapeuticos.md`
- `tasks/change-requests/164-remover-criacao-de-conteudo-na-biblioteca-web.md`
- `tasks/change-requests/165-bootstrap-do-primeiro-jogo-e-card-na-biblioteca.md`
- `tasks/change-requests/166-acoes-hover-nos-cards-de-jogo-da-biblioteca.md`
- `tasks/change-requests/168-preview-jogavel-no-visualizar-do-card-da-biblioteca.md`
- `tasks/change-requests/175-ajustar-visual-modal-visualizar-jogo.md`
- `tasks/change-requests/176-remover-botao-fechar-rodape-modal-visualizar-jogo.md`
- `tasks/change-requests/198-visualizar-jogo-no-perfil-profissional-da-biblioteca.md`

## Dependencias do slice

- Slice 006
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
| API | `contracts/openapi.yaml` | confirmar shape do conteúdo jogável | sim |
| UI web | `design-system/front/Design_System_Evolente_Desktop.md` | biblioteca e card do jogo | sim |
| Backend | `backend/docs/ai/` | bootstrap do catálogo | sim se back |
| Front-end | `front-end/docs/ai/` | implementação da biblioteca | sim se front |

## Risco de contexto

- medio
- estrategia: limitar a mudança ao catálogo de conteúdos e à rota `/biblioteca`

## Observacoes de rastreabilidade

- Este slice complementa os slices 006 e 026 sem reabrir a execução mobile do jogo.

## Progresso das tasks relacionadas

- `tasks/change-requests/165-bootstrap-do-primeiro-jogo-e-card-na-biblioteca.md` — done
- `tasks/change-requests/166-acoes-hover-nos-cards-de-jogo-da-biblioteca.md` — done
- `tasks/change-requests/168-preview-jogavel-no-visualizar-do-card-da-biblioteca.md` — done
- `tasks/change-requests/175-ajustar-visual-modal-visualizar-jogo.md` — done
- `tasks/change-requests/176-remover-botao-fechar-rodape-modal-visualizar-jogo.md` — done
- `tasks/change-requests/198-visualizar-jogo-no-perfil-profissional-da-biblioteca.md` — done
- `tasks/change-requests/255-hardening-bootstrap-catalogo-jogos-backend.md` — done

## Resultado consolidado adicional

- o bootstrap do catálogo agora reaproveita fallback público consistente para assets S3 e protege a unicidade dos jogos por `gameType`

## Status final

done

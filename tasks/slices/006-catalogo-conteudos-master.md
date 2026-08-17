# Slice 006 - Catalogo de conteudos do master

## Status

done

## Objetivo de negocio

Master cria atividades audio/video com metadados; midia em storage.

## Entrega verificavel

Atividades publicadas com categoria/idade/dificuldade/objetivo; arquivos em storage.

## Fora de escopo

- Jogos
- Gamificacao
- Criacao pelo profissional

## Perfil do projeto

- stack web escolhida: front-end (React/Vite)
- mobile: sim

## Stacks envolvidas

- front-end
- backend

## Contrato

- `contracts/openapi.yaml#/paths` de contents

## Referencia visual por stack

### Web

- tipo: artefato de design system
- fonte primaria: `design-system/front/Design_System_Evolente_Desktop.md` (biblioteca)

### Mobile

- tipo: artefato de design system
- fonte primaria: `nao se aplica`

## Permissoes e atores

- Master write
- Profissional read

## Casos de erro e borda

- Upload invalido
- Falha storage
- Metadados ausentes

## Decisoes humanas confirmadas

- Stack web: React/Vite; Mobile: sim; Profissional multi-especialidade; Gamificacao/jogos fora do escopo

## Premissas adotadas

- Gateway, valores e push a definir — abstrair
- DS documental governa tokens; sem prints nesta fase
- Conflito DS mobile (gamificacao/UI crianca) vs requisitos — prevalece requisito

## Tasks relacionadas

- `tasks/014-api-conteudos-storage.md` - API+storage
- `tasks/015-ui-catalogo-master-web.md` - UI catalogo
- `tasks/change-requests/164-remover-criacao-de-conteudo-na-biblioteca-web.md` - ajuste editorial da biblioteca web
- `tasks/change-requests/324-reabrir-criacao-audio-video-na-biblioteca-master.md` - reabertura controlada da criação de audio/video na biblioteca web
- `tasks/change-requests/325-compactar-acoes-da-biblioteca-em-icones.md` - compactação das ações da tabela da biblioteca
- `tasks/change-requests/326-excluir-conteudos-da-biblioteca-master.md` - exclusão real de conteúdos com proteção para itens em uso
- `tasks/change-requests/327-adicionar-visualizacao-de-atividade-na-biblioteca-master.md` - visualização direta de atividades de áudio e vídeo pela tabela da biblioteca
- `tasks/change-requests/328-ajustar-acentuacao-e-badge-de-status-na-biblioteca.md` - refino textual e visual da tabela da biblioteca
- `tasks/change-requests/329-vincular-audios-gravados-no-alfabeto-falado.md` - vinculação de áudios gravados por letra no jogo Alfabeto falado
- `tasks/change-requests/330-deixar-botoes-de-acao-da-biblioteca-totalmente-redondos.md` - ajuste do shape circular das ações da tabela da biblioteca
- `tasks/change-requests/334-refinar-design-da-biblioteca-master-web.md` - refino editorial da composição visual da página da biblioteca
- `tasks/change-requests/335-refinar-metadados-dos-cards-da-biblioteca-web.md` - refino dos metadados dos cards da biblioteca em chips visuais
- `tasks/change-requests/336-reduzir-cards-dos-jogos-na-biblioteca-web.md` - redução da escala visual dos cards de jogo na biblioteca
- `tasks/change-requests/337-aproximar-cards-de-jogos-da-biblioteca-da-referencia-web.md` - aproximação dos cards de jogo da biblioteca ao card de referência enviado no chat
- `tasks/change-requests/338-corrigir-quebra-dos-cards-de-jogos-na-biblioteca-web.md` - correção da largura e da distribuição interna dos cards de jogo na biblioteca
- `tasks/change-requests/339-refinar-badges-dos-cards-de-jogo-na-biblioteca-web.md` - reposicionamento da badge principal e compactação dos chips de metadados nos cards de jogo
- `tasks/change-requests/340-adicionar-paginacao-na-tabela-da-biblioteca-web.md` - paginação local da tabela editorial de áudio e vídeo na biblioteca
- `tasks/change-requests/341-refinar-input-de-upload-da-biblioteca-web.md` - refino visual do controle de upload no modal da biblioteca
- `tasks/change-requests/342-encostar-capa-dos-jogos-nas-bordas-do-card.md` - ajuste do encaixe da capa dos jogos no card da biblioteca
- `tasks/change-requests/486-hardening-biblioteca-web-config-preview.md` - hardening da biblioteca web para configs mínimas válidas e preview sem resposta tardia — **done**
- `tasks/change-requests/159-storage-s3-compativel-minio-backend.md` - provider S3/MinIO real
- `tasks/change-requests/160-prefixo-de-ambiente-no-storage-de-conteudos.md` - organizacao das keys por ambiente
- `tasks/change-requests/161-mapa-de-uso-do-bucket-no-projeto.md` - inventario dos usos atuais e futuros do bucket

## Dependencias do slice

- Slice 001

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

- medio
- estrategia: carregar apenas secoes/paths citados nas tasks

## Observacoes de rastreabilidade

- API+storage entregue na Task 014.
- UI biblioteca entregue na Task 015 (`/biblioteca`).
- Task 164 remove o fluxo de criação da UI da biblioteca, preservando edição e status para itens existentes.
- Task 324 reabre a criação apenas para `audio` e `video`, mantendo jogos fora da autoria pela biblioteca.
- Task 325 compacta as ações da tabela da biblioteca para ícones.
- Task 326 reabre a política de exclusão do catálogo com endpoint dedicado e bloqueio de itens já em uso.
- Task 327 adiciona a visualização direta de atividades de áudio e vídeo pela tabela da biblioteca.
- Task 328 refina a acentuação dos labels e a badge de status da tabela da biblioteca.
- Task 329 vincula áudios gravados no bucket para letras específicas do jogo Alfabeto falado, com fallback nas letras restantes.
- Task 330 deixa os botões icon-only da tabela da biblioteca totalmente redondos.
- Task 334 refina a biblioteca como catálogo editorial mais sóbrio, separando hero, jogos e conteúdos editoriais.
- Task 335 transforma os metadados corridos dos cards da biblioteca em chips mais claros para categoria, dificuldade e faixa etária.
- Task 336 reduz a escala dos cards de jogo para deixar a biblioteca mais compacta e com leitura de catálogo.
- Task 337 aproxima os cards de jogo da biblioteca do print de referência, com capa alta, painel inferior e ações ancoradas no rodapé.
- Task 338 corrige a quebra dos cards de jogo com largura mínima maior e rodapé de ações estável.
- Task 339 reposiciona a badge principal antes do título e compacta os chips de categoria, dificuldade e faixa etária com ícones.
- Task 340 adiciona paginação local na tabela editorial de áudio e vídeo, com resumo de faixa visível e navegação compacta.
- Task 341 substitui o input de arquivo cru do modal da biblioteca por um controle composto mais claro e consistente com a UI editorial.
- Task 342 remove a moldura interna superior do card de jogo para a capa encostar nas laterais e no topo.
- Task 486 garante config mínima válida ao trocar o tipo de certos jogos na biblioteca web e impede resposta tardia de reabrir/substituir o preview.
- Task 159 reabre o slice apenas para substituir o adapter local por provider S3-compativel real em bucket público.
- Task 160 ajusta apenas o padrão das keys novas para prefixo por ambiente e pasta `original`.
- Task 161 documenta o mapa de uso do bucket no projeto sem alterar comportamento.
- Task 393: se o upload de mídia falhar após `createContent`, a biblioteca web remove a atividade recém-criada para não deixar órfã sem arquivo.

## Progresso das tasks relacionadas

- `tasks/014-api-conteudos-storage.md` — done
- `tasks/015-ui-catalogo-master-web.md` — done
- `tasks/change-requests/164-remover-criacao-de-conteudo-na-biblioteca-web.md` — done
- `tasks/change-requests/324-reabrir-criacao-audio-video-na-biblioteca-master.md` — done
- `tasks/change-requests/325-compactar-acoes-da-biblioteca-em-icones.md` — done
- `tasks/change-requests/326-excluir-conteudos-da-biblioteca-master.md` — done
- `tasks/change-requests/327-adicionar-visualizacao-de-atividade-na-biblioteca-master.md` — done
- `tasks/change-requests/328-ajustar-acentuacao-e-badge-de-status-na-biblioteca.md` — done
- `tasks/change-requests/329-vincular-audios-gravados-no-alfabeto-falado.md` — done
- `tasks/change-requests/330-deixar-botoes-de-acao-da-biblioteca-totalmente-redondos.md` — done
- `tasks/change-requests/334-refinar-design-da-biblioteca-master-web.md` — done
- `tasks/change-requests/335-refinar-metadados-dos-cards-da-biblioteca-web.md` — done
- `tasks/change-requests/336-reduzir-cards-dos-jogos-na-biblioteca-web.md` — done
- `tasks/change-requests/337-aproximar-cards-de-jogos-da-biblioteca-da-referencia-web.md` — done
- `tasks/change-requests/338-corrigir-quebra-dos-cards-de-jogos-na-biblioteca-web.md` — done
- `tasks/change-requests/339-refinar-badges-dos-cards-de-jogo-na-biblioteca-web.md` — done
- `tasks/change-requests/340-adicionar-paginacao-na-tabela-da-biblioteca-web.md` — done
- `tasks/change-requests/438-paginacao-e-cache-biblioteca-web.md` — done
- `tasks/change-requests/341-refinar-input-de-upload-da-biblioteca-web.md` — done
- `tasks/change-requests/342-encostar-capa-dos-jogos-nas-bordas-do-card.md` — done
- `tasks/change-requests/486-hardening-biblioteca-web-config-preview.md` — done
- `tasks/change-requests/159-storage-s3-compativel-minio-backend.md` — done
- `tasks/change-requests/160-prefixo-de-ambiente-no-storage-de-conteudos.md` — done
- `tasks/change-requests/161-mapa-de-uso-do-bucket-no-projeto.md` — done
- `tasks/change-requests/393-reverter-criacao-quando-upload-falhar-na-biblioteca-web.md` — done
- `tasks/change-requests/488-hardening-bootstrap-assets-jogos-backend.md` — done

## Status final

done

# Task 324 - Reabrir criacao de atividades audio e video na biblioteca master

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

- `contracts/openapi.yaml#/paths/~1contents`
- `contracts/openapi.yaml#/paths/~1contents~1{contentId}~1media`

## Modo de execucao

single-stack

## Referencia de design system

### Stack de referencia visual

front-end

### Tipo de referencia visual

artefato de design system

### Fonte primaria visual

- `design-system/front/Design_System_Evolente_Desktop.md`

### Regra de aderencia visual

- A biblioteca deve preservar o layout atual e reabrir apenas o fluxo de cadastro no modal do master.

## Contexto de negocio

### Por que

O master precisa voltar a cadastrar atividades de audio e video diretamente pela biblioteca web.

### O que

Reintroduzir na pagina `/biblioteca` uma opcao para o master criar atividades de audio e video com upload para o bucket, titulo, descricao, objetivo e categoria.

### Comportamento esperado

- O master volta a ver CTA de criacao na biblioteca
- O modal de criacao aceita apenas `audio` e `video`
- O modal permite informar titulo, descricao, objetivo terapeutico e categoria
- O modal permite anexar o arquivo de audio ou video para upload no bucket
- O profissional continua sem mutacoes na biblioteca

### Fora de escopo

- Criacao de jogos pela biblioteca
- Mudancas no runtime mobile
- Alteracoes de contrato ou backend sem necessidade comprovada

## Review da spec

- [x] Permissoes definidas ou `nao se aplica`
- [x] Casos de erro mapeados
- [x] Decisoes de negocio confirmadas como humanas
- [x] Criterios de aceite objetivos e verificaveis
- [x] Casos de borda considerados

### Evidencias da review

- Permissoes: master cria e edita; profissional segue read-only
- Casos de erro: arquivo ausente, tipo invalido, falha de upload, validacao incompleta
- Decisoes humanas confirmadas: escopo limitado a audio/video e categorias informadas pelo pedido
- Casos de borda: nao reabrir criacao de `game`; manter edicao dos itens existentes

## Especificacao tecnica

### Deve

- reintroduzir CTA de criacao apenas para `master`
- permitir cadastro de conteudos `audio` e `video`
- manter upload da midia pelo fluxo existente de bucket
- limitar a categoria a:
  - `linguagem`
  - `fala`
  - `atencao`
  - `memoria`
  - `raciocinio`
  - `emocoes`
  - `socializacao`
  - `leitura`
  - `escrita`
  - `matematica`
- manter edicao e status dos itens existentes

### Nao deve

- nao reabrir criacao de `game`
- nao quebrar a leitura do profissional
- nao alterar a infraestrutura de storage sem gatilho tecnico

## Entradas

- `design-system/front/Design_System_Evolente_Desktop.md`
- `front-end/docs/ai/`
- `contracts/openapi.yaml`

## Dependencias

- Task 015
- Task 164
- Task 159
- Task 160

## Slice vertical

### Identificador do slice

Slice 006 - Catalogo

### Arquivo do slice

- `tasks/slices/006-catalogo-conteudos-master.md`

### Objetivo de negocio

Reabrir o cadastro operacional de audio/video na biblioteca do master sem reintroduzir autoria de jogos.

### Entrega verificavel do slice

Biblioteca com criacao de audio/video para master e upload funcional no bucket.

### Fora do slice

- Mobile

## Contexto mínimo

Sempre ler:

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/006-catalogo-conteudos-master.md`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| UI web | `design-system/front/Design_System_Evolente_Desktop.md` | ajustar biblioteca/modal | sim |
| Front-end | `front-end/docs/ai/ARCHITECTURE.md e CODE_STYLE.md e ACCESSIBILITY.md` | implementação web | sim |
| API | `contracts/openapi.yaml` | confirmar payloads e upload existentes | sim |
| Handoff | `.agents/state/handoffs/TASK-164.md` | reaproveitar decisao que removeu create | sim |

## Orçamento de contexto

- Risco baixo
- Estrategia de reducao: limitar o trabalho a `/biblioteca`, modal de conteudo, testes da biblioteca e contrato de `contents`

## Criterios de conclusao

- Biblioteca volta a expor criacao para master
- Criacao aceita apenas audio/video
- Modal coleta titulo, descricao, objetivo terapeutico, categoria e arquivo
- Upload segue funcionando no bucket
- Testes da biblioteca atualizados

## Instrucoes de implementacao

- Reaproveitar o fluxo de create existente se ainda estiver disponivel no service
- Se o contrato exigir campos adicionais nao pedidos, registrar a decisao tecnica adotada na execucao
- Preservar o modal de edicao dos itens ja existentes

## Validacao esperada

- `npm run lint`
- `npx vitest run src/pages/Main/Library/index.test.tsx`
- `npm run build`

## Entregaveis esperados

- ajustes na biblioteca web
- modal de criacao atualizado
- testes da biblioteca atualizados

## Riscos ou ambiguidades

- o contrato atual de `contents` ainda pode exigir campos adicionais alem dos solicitados; se isso impedir simplificacao total do modal, a execucao deve documentar o fallback adotado sem abrir novo escopo

## Resultado da execucao

### Resumo por stack

- **front-end**: a biblioteca voltou a expor criacao para `master`, agora com CTA `Nova atividade`, modal em modo `create` restrito a `audio` e `video`, persistencia via `createContent` e upload no bucket via `uploadContentMedia`.

### Relação com o slice

- Slice 006 foi reaberto apenas para restaurar a criação operacional de áudio/vídeo na UI web, sem reintroduzir autoria de jogos.

### Decisões técnicas

- O CTA de criação foi recolocado no cabeçalho do card da biblioteca apenas para `master`.
- O `ContentFormModal` ganhou modo `create`, mantendo `edit` e `view`.
- No modo `create`, o seletor de tipo remove `game` e o upload do arquivo passa a ser obrigatório.
- O contrato ainda exige `ageMinYears`, `ageMaxYears` e `difficulty`; por isso esses campos foram mantidos no formulário para não quebrar a API nem assumir defaults arbitrários de produto.
- O fluxo de edição dos itens existentes permaneceu intacto, inclusive para jogos.

### Trade-offs

- O modal ficou focado no pedido de áudio/vídeo, mas não foi simplificado além do que o contrato atual permite.
- Não houve mudança em backend, storage ou OpenAPI porque a infraestrutura existente já cobre o caso.

### Contrato

- Reuso de `POST /contents` para metadados e `POST /contents/{contentId}/media` para upload da mídia.

### Referência visual

- Mantido o padrão atual da biblioteca web: card com header, filtros no topo, tabela/lista limpa e modal compartilhado com ícone, título e ações no rodapé.

## Contexto utilizado

### Contexto mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`
- `tasks/000-index.md`, esta task e `tasks/slices/006-catalogo-conteudos-master.md`

### Contexto sob demanda

| Fonte | Gatilho | Uso |
|---|---|---|
| `design-system/front/Design_System_Evolente_Desktop.md` | UI web | preservar estrutura visual da biblioteca e do modal |
| `front-end/docs/ai/ARCHITECTURE.md`, `CODE_STYLE.md`, `ACCESSIBILITY.md` | implementação web | manter organização, padrões e acessibilidade |
| `contracts/openapi.yaml` | API | confirmar payloads e upload já existentes |
| `.agents/state/handoffs/TASK-164.md` | histórico do slice | reaproveitar a decisão que tinha removido a criação |

### Contexto evitado

- `backend/docs/ai/` e `mobile/docs/ai/` não foram carregados porque a task ficou resolvida em `front-end`.

## Handoff

- Caminho: `.agents/state/handoffs/TASK-324.md`
- Próximo contexto recomendado: reutilizar a Task 324 e o handoff se houver pedido para simplificar o contrato da criação ou esconder idade/dificuldade via mudança de API.

## Arquivos alterados

### Front-end

- `front-end/src/pages/Main/Library/index.tsx`
- `front-end/src/pages/Main/Library/ContentFormModal.tsx`
- `front-end/src/pages/Main/Library/index.test.tsx`

### Governança

- `tasks/change-requests/324-reabrir-criacao-audio-video-na-biblioteca-master.md`
- `tasks/slices/006-catalogo-conteudos-master.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-324.md`

## Validacoes executadas

- `cd front-end && npx vitest run src/pages/Main/Library/index.test.tsx` — ok
- `cd front-end && npm run build` — ok
- `cd front-end && npm run lint` — **falhou por problema pré-existente fora do escopo** em `front-end/src/components/PatientAvatar/index.tsx` e `front-end/src/components/PatientAvatar/resolvePatientAvatarSource.ts` em **29 de julho de 2026**

## Aderencia ao design system

- A criação foi reintroduzida sem mudar a linguagem da página: o CTA fica no header do card, os filtros continuam no topo e o modal preserva o padrão branco, arredondado e com ações bem separadas.

## Acessibilidade aplicada

- O novo CTA usa `button` semântico.
- O modal continua com labels visíveis, `aria-busy`, mensagens de erro em texto e fechamento controlado.
- O teste cobre a abertura do modal e o envio do formulário no fluxo principal.

## Pendencias pos-task

- Se o produto quiser remover `idade` e `dificuldade` do modal, isso exigirá revisão de contrato/backend ou uma decisão explícita de defaults.
- O lint global do `front-end` continua bloqueado por erros prévios em `PatientAvatar`, fora desta task.

## Status final

done

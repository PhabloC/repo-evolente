# CR-008 - Refinamento do design system web e mobile

## Status

done

## Tipo

shared

## Stacks envolvidos

- raiz

## Contrato

- nao se aplica

## Modo de execucao

single-stack

## Perfil do projeto

- stack web escolhida: front-end (React/Vite)
- mobile: sim

## Referencia de design system

### Stack de referencia visual

multiplas stacks

### Tipo de referencia visual

artefato de design system

### Fonte primaria visual

- `design-system/front/Design_System_Evolente_Desktop.md`
- `design-system/mobile/Design_System_Evolente_App_Mobile.md`

### Regra de aderencia visual

- Preservar a identidade de marca compartilhada entre web e mobile.
- Reorganizar o conteudo para deixar diferencas de uso entre desktop e app mais explicitas.

## Origem da solicitacao

Pedido direto do usuario para reformular os documentos de design system do front e do mobile.

## Objetivo

Reescrever os documentos de design system web e mobile para torná-los mais claros, consistentes e prontos para consulta futura por produto, design e engenharia.

## Escopo

- Padronizar a estrutura editorial dos dois documentos.
- Remover HTML desnecessario e melhorar legibilidade em markdown.
- Tornar principios, componentes, estados e recomendacoes mais objetivos.
- Preservar a identidade visual e o posicionamento da marca Evolente.

## Fora de escopo

- Alterar requisitos de negocio.
- Implementar componentes nas stacks.
- Criar backlog adicional de produto.

## Entradas

- `design-system/front/Design_System_Evolente_Desktop.md`
- `design-system/mobile/Design_System_Evolente_App_Mobile.md`
- `tasks/000-index.md`

## Slice vertical

### Identificador do slice

Slice 008 - Refinamento do design system web e mobile

### Arquivo do slice

- `tasks/slices/008-refinamento-design-system-web-mobile.md`

### Objetivo de negocio

Melhorar a qualidade dos artefatos documentais que orientam a experiencia visual da Evolente em web e mobile.

### Entrega verificavel do slice

Os dois documentos passam a usar a mesma logica editorial, com secoes objetivas e diretrizes praticas por plataforma.

### Fora do slice

- Mudar implementacao de produto.
- Replanejar roadmap.

## Contexto mínimo

Sempre ler:

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/008-refinamento-design-system-web-mobile.md`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatorio? |
|---|---|---|---|
| Revisao documental web | `design-system/front/Design_System_Evolente_Desktop.md` | somente para reformular o design system desktop | sim |
| Revisao documental mobile | `design-system/mobile/Design_System_Evolente_App_Mobile.md` | somente para reformular o design system do app | sim |
| Processo/contexto | `.agents/references/context-engineering.md` | somente se houver duvida sobre escopo ou excesso de contexto | nao |

## Orçamento de contexto

- Fontes obrigatorias estimadas: 6
- Fontes sob demanda estimadas: 2
- Risco de contexto excessivo: baixo
- Estrategia para reduzir contexto: nao carregar requirements, contrato, handoffs antigos ou docs de stack porque a mudanca e puramente documental.

## Dependencias

- Nenhuma

## Criterios de conclusao

- Os dois arquivos usam markdown limpo e estrutura consistente.
- As diretrizes visuais ficam mais objetivas e consultaveis.
- `tasks/000-index.md` lista CR-008 como `done`.
- Handoff `TASK-008` criado.

## Instrucoes de implementacao

- Manter o escopo estritamente documental.
- Preservar a linguagem da marca e a diferenciacao entre desktop e mobile.
- Favorecer organizacao por secoes, listas e tabelas markdown simples.

## Validacao esperada

- Leitura final dos dois documentos reformulados.
- `rg --files tasks .agents/state/handoffs design-system`

## Entregaveis esperados

- Dois documentos de design system reformulados.
- Slice, task, indice e handoff atualizados.

## Riscos ou ambiguidades

- Sem bloqueios funcionais; o principal risco e apenas expandir o escopo para alem da documentacao.

## Resultado da execucao

- Os dois documentos foram reescritos em markdown limpo, com estrutura paralela entre web e mobile.
- A base visual da marca foi preservada e complementada com principios, tokens, componentes, estados e boas praticas mais acionaveis.
- O desktop ficou descrito como ambiente profissional e produtivo; o mobile, como experiencia guiada para crianca e responsavel.

## Contexto utilizado

- Contexto mínimo: `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`, `tasks/000-index.md`, esta task e o slice `008`.
- Contexto sob demanda: `design-system/front/Design_System_Evolente_Desktop.md` e `design-system/mobile/Design_System_Evolente_App_Mobile.md`.
- Contexto evitado: `requirements/`, `contracts/openapi.yaml`, docs locais de stack e handoffs anteriores, por nao serem necessarios para a reformulacao documental.

## Handoff

- `.agents/state/handoffs/TASK-008.md`

## Arquivos alterados

- `design-system/front/Design_System_Evolente_Desktop.md`
- `design-system/mobile/Design_System_Evolente_App_Mobile.md`
- `tasks/000-index.md`
- `tasks/slices/008-refinamento-design-system-web-mobile.md`
- `tasks/change-requests/008-refinamento-design-system-web-mobile.md`
- `.agents/state/handoffs/TASK-008.md`

## Validacoes executadas

- Revisao textual dos dois documentos reformulados: concluida.
- `rg --files tasks .agents/state/handoffs design-system`: executado.

## Pendencias pos-task

- Nenhuma.

## Status final

done

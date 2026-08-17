# Task 168 - Preview jogavel no visualizar do card da biblioteca

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

- `contracts/openapi.yaml#/paths` contents

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

- O preview deve parecer parte da biblioteca, sem abrir uma experiência paralela desconectada do card e dos modais existentes.

## Contexto de negocio

### Por que

O master precisa que o ícone de visualizar mostre o jogo em si, não apenas os metadados do conteúdo.

### O que

Trocar a ação de visualizar do card por uma prévia jogável do primeiro jogo do alfabeto dentro da biblioteca web.

### Comportamento esperado

- o ícone de olho abre um modal de preview do jogo
- o modal mostra as letras configuradas no conteúdo
- ao clicar em uma letra, a prévia responde como jogo e tenta falar a letra

### Fora de escopo

- novos jogos
- mudanças no backend
- substituição do fluxo mobile de execução

## Review da spec

- [x] Permissoes definidas ou `nao se aplica`
- [x] Casos de erro mapeados
- [x] Decisoes de negocio confirmadas como humanas
- [x] Criterios de aceite objetivos e verificaveis
- [x] Casos de borda considerados

### Evidencias da review

- Permissoes: preview fica no catálogo do master; profissional segue sem ações de gestão
- Casos de erro: navegador sem `speechSynthesis`; config de letras ausente; card inativo
- Decisoes humanas confirmadas: visualizar deve mostrar o jogo em si
- Casos de borda: foco por teclado dentro do modal; fallback textual quando a voz não estiver disponível

## Especificacao tecnica

### Deve

- substituir o modal read-only de metadados por preview jogável para conteúdos `game`
- manter edição separada em seu modal atual
- usar fala nativa do navegador quando disponível, sem upload de áudio
- cobrir a mudança com testes da biblioteca

### Nao deve

- nao mexer no contrato
- nao remover a confirmação de inativação
- nao criar engine genérica prematura para jogos web

## Entradas

- `design-system/front/Design_System_Evolente_Desktop.md`
- `front-end/docs/ai/ARCHITECTURE.md`
- `front-end/docs/ai/CODE_STYLE.md`
- `front-end/docs/ai/ACCESSIBILITY.md`

## Dependencias

- Task 166
- Task 167

## Slice vertical

### Identificador do slice

Slice 029 - Catalogo inicial de jogos terapeuticos

### Arquivo do slice

- `tasks/slices/029-catalogo-inicial-jogos-terapeuticos.md`

### Objetivo de negócio

Permitir que o master visualize o jogo real antes de editar ou distribuir.

### Entrega verificável do slice

O card do jogo abre uma prévia jogável no `visualizar`, mantendo edição e status separados.

### Fora do slice

- mobile e backend

## Contexto mínimo

Sempre ler:

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/029-catalogo-inicial-jogos-terapeuticos.md`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| UI web | `design-system/front/Design_System_Evolente_Desktop.md` | compor modal e preview | sim |
| Front-end | `front-end/docs/ai/ARCHITECTURE.md e CODE_STYLE.md e ACCESSIBILITY.md` | implementação web | sim |
| Handoff | `.agents/state/handoffs/TASK-166.md e TASK-167.md` | preservar decisões do card e do TTS | sim |

## Orçamento de contexto

- Risco baixo
- Estrategia de reducao: limitar a mudança ao módulo `Library`, sem tocar em planejamentos, contrato ou backend

## Criterios de conclusao

- visualizar abre uma prévia do jogo
- a prévia responde ao clique nas letras
- existe fallback quando a fala do navegador não estiver disponível
- testes da biblioteca atualizados e passando

## Instrucoes de implementacao

- preferir modal dedicado de preview em vez de sobrecarregar o modal de edição
- manter nomes acessíveis claros nas ações e nos botões das letras

## Validacao esperada

- `npm run lint`
- `npm run build`
- `npx vitest run src/pages/Main/Library/index.test.tsx`

## Entregaveis esperados

- modal de preview jogável
- integração de fala do navegador para a prévia web
- testes ajustados

## Riscos ou ambiguidades

- alguns navegadores podem bloquear ou variar a voz nativa; o preview precisa continuar útil visualmente mesmo sem áudio

## Resultado da execucao

### Resumo por stack

- **front-end**: a ação `visualizar` do card agora abre uma prévia jogável do alfabeto, com letras clicáveis e tentativa de fala usando a voz nativa do navegador.

### Relação com o slice

- Slice 029 foi expandido sem mexer em backend ou mobile: o catálogo do master agora consegue revisar o jogo real antes de editar ou distribuir.

### Decisões técnicas

- criação de um modal dedicado de preview em vez de reaproveitar o modal read-only de metadados
- extração da fala do navegador para utilitário local do módulo `Library`
- manutenção do modal de edição separado, sem misturar preview e formulário
- preservação de fallback textual quando a voz do navegador não estiver disponível

### Contrato

- sem alterações em `contracts/openapi.yaml`; a prévia usa apenas `gameType` e `gameConfig` já existentes

## Contexto utilizado

### Contexto mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`
- `tasks/000-index.md`, esta task, `tasks/slices/029-catalogo-inicial-jogos-terapeuticos.md`

### Contexto sob demanda

| Fonte | Gatilho | Uso |
|---|---|---|
| `.agents/state/handoffs/TASK-166.md` | continuidade do card | preservar overlay e ações do card |
| `.agents/state/handoffs/TASK-167.md` | continuidade da voz nativa | alinhar o preview web ao princípio de não exigir upload de áudio |
| `design-system/front/Design_System_Evolente_Desktop.md` | UI web | manter linguagem visual do modal e do card |
| `front-end/docs/ai/ARCHITECTURE.md` | implementação web | separar preview, utilitário de fala e página |
| `front-end/docs/ai/CODE_STYLE.md` | implementação web | manter contratos e helpers fora da page |
| `front-end/docs/ai/ACCESSIBILITY.md` | UI web | garantir foco, labels e feedback acessível |

### Contexto evitado

- `backend/docs/ai/`, `mobile/docs/ai/` e `contracts/openapi.yaml` inteiro não foram carregados além do estritamente necessário, porque a mudança é restrita ao módulo web da biblioteca

## Handoff

- Caminho: `.agents/state/handoffs/TASK-168.md`
- Próximo contexto recomendado: `front-end/src/pages/Main/Library/`

## Arquivos alterados

### Front-end

- `front-end/src/pages/Main/Library/index.tsx`
- `front-end/src/pages/Main/Library/GamePreviewModal.tsx`
- `front-end/src/pages/Main/Library/libraryGameSpeech.ts`
- `front-end/src/pages/Main/Library/styles.module.css`
- `front-end/src/pages/Main/Library/index.test.tsx`

### Governança

- `tasks/change-requests/168-preview-jogavel-no-visualizar-do-card-da-biblioteca.md`
- `tasks/slices/029-catalogo-inicial-jogos-terapeuticos.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-168.md`

## Validacoes executadas

- `cd front-end && npm run lint` — ok
- `cd front-end && npm run build` — ok
- `cd front-end && npx vitest run src/pages/Main/Library/index.test.tsx` — ok

## Aderencia ao design system

- a prévia mantém a linguagem acolhedora do desktop com card quente, pills suaves e modal integrado à biblioteca

## Acessibilidade aplicada

- botões de letra com `aria-label`
- feedback de fala em região `aria-live`
- foco mantido dentro do modal e retorno ao card ao fechar via infraestrutura do modal compartilhado

## Pendencias pos-task

- a qualidade e a disponibilidade da voz dependem do navegador e do sistema do usuário master
- se no futuro houver mais jogos web, o próximo passo é adicionar novos previews locais ao módulo sem criar engine genérica prematura

## Status final

done

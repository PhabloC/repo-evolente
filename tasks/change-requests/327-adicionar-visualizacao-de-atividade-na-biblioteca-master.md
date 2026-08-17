# Task 327 - Adicionar visualizacao de atividade na biblioteca master

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

- `nao se aplica`

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

- A tabela da biblioteca deve manter ações compactas por ícone e incluir visualização explícita antes de editar ou excluir.

## Contexto de negocio

### Por que

O master precisa conferir a atividade direto pela tabela antes de editar, inativar ou excluir.

### O que

Adicionar ação de visualizar com ícone de olho para conteúdos de áudio e vídeo na biblioteca.

### Comportamento esperado

- conteúdos de áudio e vídeo exibem ícone de olho na tabela
- o clique abre modal de visualização da atividade
- quando existir arquivo, o modal mostra player compatível com áudio ou vídeo
- quando não existir arquivo, o modal informa isso de forma clara

### Fora de escopo

- mudanças no backend
- alterações no fluxo de jogos
- download de mídia

## Dependencias

- Task 324
- Task 325
- Task 326

## Slice vertical

### Identificador do slice

Slice 006 - Catalogo

### Arquivo do slice

- `tasks/slices/006-catalogo-conteudos-master.md`

## Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/006-catalogo-conteudos-master.md`
- `.agents/state/handoffs/TASK-326.md`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| UI web | `front-end/src/pages/Main/Library/` | incluir olho na tabela e modal de visualização | sim |
| Acessibilidade | `front-end/docs/ai/ACCESSIBILITY.md` | manter ações icon-only com nome acessível e foco correto no modal | sim |

## Orçamento de contexto

- Risco baixo
- Estratégia de redução: limitar a mudança à biblioteca web, reaproveitando o estado de preview e sem tocar contrato ou backend

## Criterios de conclusao

- ícone de olho disponível na tabela para áudio e vídeo
- clique abre modal de visualização da atividade
- modal mostra player nativo quando houver mídia
- modal mostra mensagem clara quando não houver arquivo
- teste da biblioteca atualizado

## Validacao esperada

- `cd front-end && npx vitest run src/pages/Main/Library/index.test.tsx`

## Resultado da execucao

### Resumo por stack

- **front-end**: a tabela da biblioteca passou a exibir o ícone de olho para conteúdos de áudio e vídeo, abrindo um modal de visualização com player nativo ou aviso de ausência de arquivo.

### Relação com o slice

- O Slice 006 ficou mais operacional para o master ao permitir conferência imediata da atividade antes das demais ações do catálogo.

### Decisões técnicas

- o preview de jogos foi mantido no modal já existente
- áudio e vídeo ganharam modal próprio de visualização
- o botão de olho ficou icon-only com `aria-label`
- o modal reaproveita o componente global de modal para foco e fechamento por teclado

## Contexto utilizado

### Contexto mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`
- `tasks/000-index.md`, esta task, `tasks/slices/006-catalogo-conteudos-master.md`
- `.agents/state/handoffs/TASK-326.md`

### Contexto sob demanda

| Fonte | Gatilho | Uso |
|---|---|---|
| `front-end/src/pages/Main/Library/` | UI web | ação de visualizar e modal de mídia |
| `front-end/docs/ai/ACCESSIBILITY.md` | ícones e modal | nome acessível e foco do fluxo |

### Contexto evitado

- backend, mobile e contrato, por não haver alteração de integração

## Handoff

- Caminho: `.agents/state/handoffs/TASK-327.md`
- Próximo contexto recomendado: reutilizar esta task se o produto pedir download, compartilhamento ou analytics de visualização da mídia.

## Arquivos alterados

- `front-end/src/pages/Main/Library/index.tsx`
- `front-end/src/pages/Main/Library/index.test.tsx`
- `front-end/src/pages/Main/Library/MediaPreviewModal.tsx`
- `front-end/src/pages/Main/Library/styles.module.css`
- `tasks/change-requests/327-adicionar-visualizacao-de-atividade-na-biblioteca-master.md`
- `tasks/slices/006-catalogo-conteudos-master.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-327.md`

## Validacoes executadas

- `cd front-end && npx vitest run src/pages/Main/Library/index.test.tsx` — ok em **quarta-feira, 29 de julho de 2026**

## Acessibilidade aplicada

- botão de olho com `aria-label` descritivo
- modal com título claro e fechamento por teclado
- conteúdo de fallback em texto, sem depender apenas do player

## Pendencias pos-task

- sem pendências para visualização básica de áudio e vídeo
- download ou compartilhamento da mídia exigem nova task

## Status final

done

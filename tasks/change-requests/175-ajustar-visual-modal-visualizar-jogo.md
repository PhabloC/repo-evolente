# Task 175 - Ajustar visual do modal de visualizar jogo

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

- nao se aplica (ajuste visual local, sem mudanca de API)

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

- Manter a linguagem visual da biblioteca; aplicar apenas os refinamentos pedidos no modal de visualizar jogo.

## Contexto de negocio

### Por que

O modal de visualizar jogo precisa de polimento visual para ficar mais limpo e coerente com o restante da UI.

### O que

Ajustar botão fechar, ícones, card de prévia, fundo e barra de scroll do modal de visualizar jogo.

### Comportamento esperado

1. Botão X sem borda
2. Ícone ao lado do título “Visualizar jogo” vira `Dices`, com contorno 100% redondo
3. Card da “Prévia interativa” com borda em volta
4. Fundo do modal sem linear gradient
5. Barra de scroll da direita fica dentro do modal
6. Ícone do card de prévia interativa com borda 100% redonda

### Fora de escopo

- Mudanças de comportamento do preview jogável
- Backend e mobile
- Redesign de outros modais além do necessário no componente compartilhado `Modal`

## Review da spec

- [x] Permissoes definidas ou `nao se aplica`
- [x] Casos de erro mapeados
- [x] Decisoes de negocio confirmadas como humanas
- [x] Criterios de aceite objetivos e verificaveis
- [x] Casos de borda considerados

### Evidencias da review

- Permissoes: nao se aplica
- Casos de erro: nao se aplica
- Decisoes humanas: lista numerada fornecida pelo solicitante
- Casos de borda: modal compartilhado — mudanças estruturais de scroll/fundo/X devem preservar demais usos do `Modal`

## Especificacao tecnica

### Deve

- remover borda do botão fechar do modal
- trocar `headerIcon` do preview para Lucide `Dices`
- tornar o `iconBox` do título e o ícone do card de prévia totalmente redondos (`border-radius: 50%`)
- adicionar borda ao card da seção “Prévia interativa”
- remover gradient de fundo do modal em favor de fundo sólido
- garantir que o overflow/scroll fique contido dentro do raio do modal

### Nao deve

- nao alterar a lógica de fala/escrita do preview
- nao mudar contratos ou dados do jogo

## Entradas

- `front-end/src/ui/Modal/`
- `front-end/src/pages/Main/Library/GamePreviewModal.tsx`
- `front-end/src/pages/Main/Library/styles.module.css`

## Dependencias

- Task 168

## Slice vertical

### Identificador do slice

Slice 029 - Catalogo inicial de jogos terapeuticos

### Arquivo do slice

- `tasks/slices/029-catalogo-inicial-jogos-terapeuticos.md`

### Objetivo de negócio

Polir a superfície de visualização do jogo na biblioteca web.

### Entrega verificável do slice

Modal de visualizar jogo com os seis ajustes visuais solicitados.

### Fora do slice

- Novos jogos e mudanças mobile

## Contexto mínimo

Sempre ler:

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/029-catalogo-inicial-jogos-terapeuticos.md`
- `.agents/state/handoffs/TASK-168.md`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| UI web | `design-system/front/Design_System_Evolente_Desktop.md` | validar coerência visual | nao |
| Front-end | `front-end/docs/ai/CODE_STYLE.md` | se houver dúvida de estilo | nao |

## Orçamento de contexto

- Risco baixo
- Estrategia de reducao: restringir a `Modal` compartilhado e arquivos do preview na Library

## Criterios de conclusao

- X sem borda
- Ícone do título = Dices, redondo
- Card “Prévia interativa” com borda
- Fundo do modal sem linear-gradient
- Scrollbar contida dentro do modal
- Ícone do card de prévia 100% redondo

## Instrucoes de implementacao

- Preferir mudanças locais no preview; no `Modal` compartilhado, limitar ao necessário para X, fundo e scroll
- Usar Lucide `Dices`

## Validacao esperada

- `npm run lint`
- `npm run build`

## Entregaveis esperados

- visual do modal de visualizar jogo ajustado conforme lista

## Riscos ou ambiguidades

- Ajuste de scroll/fundo/X no `Modal` compartilhado impacta outros modais; aceito como alinhamento visual do componente base

## Resultado da execucao

- Botão X do `Modal` sem borda
- `headerIcon` do preview trocado para `Dices` e `iconBox` 100% redondo
- Card “Prévia interativa” com borda, padding e fundo sólido
- Fundo do modal em branco sólido (sem gradients)
- Scroll movido para o `body` do modal com `overflow: hidden` no container arredondado
- Ícone interno do card de prévia com `border-radius: 50%`

## Contexto utilizado

### Contexto mínimo lido

- `AGENTS.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/029-catalogo-inicial-jogos-terapeuticos.md`
- `.agents/state/handoffs/TASK-168.md`

### Contexto sob demanda carregado

| Fonte | Gatilho | Uso |
|---|---|---|
| `front-end/src/ui/Modal/` | scroll/fundo/X | ajuste do componente base |
| `front-end/src/pages/Main/Library/GamePreviewModal.tsx` | ícone Dices | header do preview |
| `front-end/src/pages/Main/Library/styles.module.css` | card/ícone prévia | borda e round |

## Handoff

- `.agents/state/handoffs/TASK-175.md`

## Arquivos alterados

- `front-end/src/ui/Modal/styles.module.css`
- `front-end/src/pages/Main/Library/GamePreviewModal.tsx`
- `front-end/src/pages/Main/Library/styles.module.css`
- `tasks/change-requests/175-ajustar-visual-modal-visualizar-jogo.md`
- `tasks/slices/029-catalogo-inicial-jogos-terapeuticos.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-175.md`

## Validacoes executadas

- `npm run lint` — ok
- `npm run build` — ok

## Pendencias pos-task

- nenhuma

## Status final

done

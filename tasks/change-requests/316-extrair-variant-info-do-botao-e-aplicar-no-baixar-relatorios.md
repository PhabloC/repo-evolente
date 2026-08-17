# Task 316 - Extrair variant info do botão e aplicar no Baixar de relatórios

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

- nao se aplica; ajuste visual e de reuso sem alterar integração

## Modo de execucao

single-stack

## Slice vertical

- Slice 011 - Relatorios de evolucao
- `tasks/slices/011-relatorios-evolucao.md`

## Referencia visual

### Stack de referencia visual

front-end

### Tipo de referencia visual

design system + feedback direto do usuario

### Fonte primaria visual

- `design-system/front/Design_System_Evolente_Desktop.md`
- `front-end/src/ui/Button/**`
- `front-end/src/pages/Main/Reports/**`

### Lacunas

- sem print novo; a mudança deve aderir explicitamente ao azul `Confianca` do design system e transformar o estilo local em variant reutilizável

## Objetivo

Usar explicitamente a paleta azul `Confianca` do design system no CTA `Baixar` da tabela de relatórios e extrair esse estilo para um `variant` reutilizável no componente global `Button`.

## Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/011-relatorios-evolucao.md`
- `.agents/state/handoffs/TASK-315.md`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| Design system | `design-system/front/Design_System_Evolente_Desktop.md` | alinhar o variant à paleta azul oficial | sim |
| UI web | `front-end/docs/ai/{AGENTS.md,ARCHITECTURE.md,ACCESSIBILITY.md,COMPONENT_REUSE.md}` | posicionar o reuso no `ui/Button` | sim |
| Primitiva compartilhada | `front-end/src/ui/Button/**` | criar novo variant reutilizável | sim |
| Consumidor atual | `front-end/src/pages/Main/Reports/**` | aplicar o novo variant no CTA `Baixar` | sim |

## Orçamento de contexto

- baixo
- estrategia: limitar a mudança ao `Button` e à rota `Reports`, sem tocar outras páginas

## Criterios de conclusao

- [x] existe um variant reutilizável de botão para ações informativas baseado no azul do design system
- [x] o CTA `Baixar` usa esse variant, sem skin local de cor improvisada
- [x] a rota `/relatorios` continua funcional

## Dependencias

- Task 315 - done

## Resultado da execucao

- o componente global `Button` passou a expor o variant `info`, baseado na paleta azul `Confianca` (`#2978BB`)
- o CTA `Baixar` da tabela de relatórios foi migrado para o variant global, removendo a estilização local improvisada
- a coluna `Ações` permaneceu alinhada com o cabeçalho sem regressão funcional na rota `/relatorios`

## Contexto utilizado

### Mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/011-relatorios-evolucao.md`
- `.agents/state/handoffs/TASK-315.md`

### Sob demanda

- `design-system/front/Design_System_Evolente_Desktop.md`
- `front-end/docs/ai/AGENTS.md`
- `front-end/docs/ai/ARCHITECTURE.md`
- `front-end/docs/ai/ACCESSIBILITY.md`
- `front-end/docs/ai/COMPONENT_REUSE.md`
- `front-end/src/ui/Button/index.tsx`
- `front-end/src/ui/Button/styles.module.css`
- `front-end/src/pages/Main/Reports/index.tsx`
- `front-end/src/pages/Main/Reports/styles.module.css`

### Contexto evitado

- `backend/`, porque o ajuste é exclusivamente visual e estrutural no front-end
- `contracts/openapi.yaml`, porque não há alteração de API

## Handoff

- `.agents/state/handoffs/TASK-316.md`

## Arquivos alterados

- `front-end/src/ui/Button/index.tsx`
- `front-end/src/ui/Button/styles.module.css`
- `front-end/src/pages/Main/Reports/index.tsx`
- `front-end/src/pages/Main/Reports/styles.module.css`
- `tasks/change-requests/316-extrair-variant-info-do-botao-e-aplicar-no-baixar-relatorios.md`
- `tasks/slices/011-relatorios-evolucao.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-316.md`

## Validacoes executadas

- `cd front-end && npx eslint src/ui/Button/index.tsx src/pages/Main/Reports/index.tsx`
- `cd front-end && npm run build`

## Pendencias pos-task

- nenhuma

## Status final

done

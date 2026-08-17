# Task 351 - Refinar botões e resumo da semana na trilha web

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

nao se aplica

## Modo de execucao

single-stack

## Referencia de design system

### Stack de referencia visual

front-end

### Tipo de referencia visual

ajuste visual orientado por referência enviada no chat

### Fonte primaria visual

- `design-system/front/Design_System_Evolente_Desktop.md`

### Regra de aderencia visual

- preservar a estrutura da tela da trilha e reforçar apenas a hierarquia dos CTAs secundários e do resumo da semana

## Contexto de negocio

### Por que

Os botões superiores e de navegação semanal da trilha ainda estavam com aparência neutra, enquanto o resumo textual da semana tinha baixa hierarquia visual.

### O que

Aplicar o azul pedido pelo usuário aos botões `Voltar`, `Perfil do paciente`, `Semana anterior` e `Próxima semana`, além de melhorar o design do bloco que apresenta o período da semana.

### Comportamento esperado

- botão `Voltar` da trilha usa azul sólido
- botão `Perfil do paciente` da trilha usa azul sólido
- botões de mudança de semana usam azul sólido
- o período da semana aparece destacado visualmente em badge, com texto de apoio mais claro

### Fora de escopo

- mudanças na lógica de datas
- alterações nas ações de salvar, sugerir ou inativar trilha
- redesign de outras páginas fora da trilha do paciente

## Slice vertical

### Identificador do slice

Slice 017 - Redesign interface interna web

### Arquivo do slice

- `tasks/slices/017-redesign-interface-interna-web.md`

## Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/017-redesign-interface-interna-web.md`
- `.agents/state/handoffs/TASK-349.md`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| UI web | `front-end/docs/ai/ACCESSIBILITY.md`, `CODE_STYLE.md` | preservar contraste, foco e semântica dos botões | sim |
| Trilha do paciente | `front-end/src/pages/Main/Plans/PatientTrail/index.tsx` | aplicar novos estilos e melhorar o resumo da semana | sim |
| Estilos locais | `front-end/src/pages/Main/Plans/styles.module.css` | criar variações visuais específicas da trilha | sim |
| Teste focado | `front-end/src/pages/Main/Plans/PatientTrail/index.test.tsx` | validar que a tela continua estável | sim |

## Orçamento de contexto

- baixo
- estrategia de reducao: limitar a mudança ao header e ao card da semana da trilha, sem reabrir outras rotas de planejamentos

## Criterios de conclusao

- [x] botões `Voltar` e `Perfil do paciente` da trilha usam azul sólido
- [x] botões `Semana anterior` e `Próxima semana` usam azul sólido
- [x] o resumo do período da semana ganhou destaque visual e copy de apoio mais clara
- [x] teste focado da trilha passa

## Dependencias

- Task 349

## Resultado da execucao

- a trilha passou a usar um CTA azul sólido para retorno, acesso ao perfil do paciente e navegação entre semanas
- o cabeçalho do card da semana ganhou um badge visual para o intervalo exibido
- a descrição do comportamento de normalização da data ficou mais limpa e legível

## Contexto utilizado

### Mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`
- `tasks/000-index.md`, esta task, `tasks/slices/017-redesign-interface-interna-web.md`
- `.agents/state/handoffs/TASK-349.md`

### Sob demanda

- `front-end/docs/ai/ACCESSIBILITY.md`
- `front-end/docs/ai/CODE_STYLE.md`
- `front-end/src/pages/Main/Plans/PatientTrail/index.tsx`
- `front-end/src/pages/Main/Plans/styles.module.css`
- `front-end/src/pages/Main/Plans/PatientTrail/index.test.tsx`

### Contexto evitado

- `contracts/openapi.yaml` por nao haver alteração de contrato
- `backend/` por nao haver alteração de API
- outras páginas de pacientes e planejamentos por nao participarem deste ajuste

## Handoff

- `.agents/state/handoffs/TASK-351.md`

## Arquivos alterados

- `front-end/src/pages/Main/Plans/PatientTrail/index.tsx`
- `front-end/src/pages/Main/Plans/styles.module.css`
- `tasks/change-requests/351-refinar-botoes-e-resumo-da-semana-na-trilha-web.md`
- `tasks/slices/017-redesign-interface-interna-web.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-351.md`

## Validacoes executadas

- `cd front-end && npm test -- --run src/pages/Main/Plans/PatientTrail/index.test.tsx` - ok
- `cd front-end && npx eslint src/pages/Main/Plans/PatientTrail/index.tsx src/pages/Main/Plans/PatientTrail/index.test.tsx` - ok
- `cd front-end && npx eslint src/pages/Main/Plans/styles.module.css` - aviso esperado; arquivo CSS ignorado pela configuração atual do ESLint

## Pendencias pos-task

- nenhuma

## Status final

done

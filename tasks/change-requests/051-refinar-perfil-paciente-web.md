# Task 051 - Refinar design da página de perfil do paciente web

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

- nao se aplica; preservar dados e integracoes existentes

## Modo de execucao

single-stack

## Slice vertical

- Slice 007 - Gestao de pacientes do profissional
- `tasks/slices/007-gestao-pacientes-profissional.md`

## Referencia de design system

### Stack de referencia visual

front-end

### Tipo de referencia visual

artefato de design system

### Fonte primaria visual

- `design-system/front/Design_System_Evolente_Desktop.md`

### Regra de aderencia visual

- manter base clara, acolhedora e clinica da area interna
- aumentar hierarquia visual do perfil sem alterar contrato, estados e acoes existentes

## Objetivo

Refinar a leitura da pagina de perfil do paciente com melhor hierarquia, resumo superior e separacao mais clara entre dados do paciente, vinculo e anamnese.

## Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/007-gestao-pacientes-profissional.md`
- `.agents/state/handoffs/TASK-046.md`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| UI web | `design-system/front/Design_System_Evolente_Desktop.md` | definir direcao visual do refino | sim |
| Front-end | `front-end/docs/ai/ARCHITECTURE.md`, `CODE_STYLE.md`, `ACCESSIBILITY.md` | implementar pagina React/Vite com acessibilidade | sim |
| Implementacao atual | `front-end/src/pages/Main/Patients/PatientProfile/index.tsx` e `front-end/src/pages/Main/Patients/styles.module.css` | aplicar o refino no menor escopo possivel | sim |
| Componentes base | `front-end/src/ui/Card/**` | validar encaixe visual e semantico do layout | sim |

## Orçamento de contexto

- baixo
- estrategia: limitar a mudanca ao perfil do paciente e ao CSS compartilhado do modulo Patients

## Criterios de conclusao

- [x] perfil com hierarquia visual mais clara e leitura mais rapida
- [x] dados, vinculo e anamnese reorganizados sem mudar fluxo funcional
- [x] acessibilidade, lint e build validados

## Dependencias

- Task 046 - done

## Resultado da execucao

- a pagina ganhou um hero superior com status, codigo e indicadores rapidos
- o conteudo foi reorganizado em area principal e painel lateral de vinculo
- dados do paciente e anamnese passaram a usar grids e paineis de leitura mais densos, preservando edicao, inativacao e montagem de trilha
- o toggle de status passou a refletir estado de carregamento durante a requisicao
- refinamento incremental posterior: botao de editar dados ganhou icone e mais area clicavel; hero e cards superiores receberam mais respiro; callout de proximo passo foi afastado do bloco `Inativado em`
- refinamento incremental posterior: hero passou a combinar notas clinicas, radar de dificuldade e estatisticas em composicao mais editorial; o botao de editar foi movido para o cabecalho do card e a anamnese ganhou um resumo clinico destacado

## Contexto utilizado

### Mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`
- `tasks/000-index.md`, esta task, `tasks/slices/007-gestao-pacientes-profissional.md`
- `.agents/state/handoffs/TASK-046.md`

### Sob demanda

- `design-system/front/Design_System_Evolente_Desktop.md`
- `front-end/docs/ai/ARCHITECTURE.md`, `CODE_STYLE.md`, `ACCESSIBILITY.md`
- `front-end/src/pages/Main/Patients/PatientProfile/index.tsx`
- `front-end/src/pages/Main/Patients/styles.module.css`
- `front-end/src/ui/Card/index.tsx`, `front-end/src/ui/Card/styles.module.css`
- `front-end/src/types/{patient.ts,guardian.ts}`
- `front-end/src/utils/{age.ts,formatDateTime.ts,formatCpf.ts}`

### Contexto evitado

- `contracts/openapi.yaml` por nao haver mudanca de integracao
- backend, mobile e outras paginas do shell por nao fazerem parte deste refino

## Handoff

- `.agents/state/handoffs/TASK-051.md`

## Arquivos alterados

- `front-end/src/pages/Main/Patients/PatientProfile/index.tsx`
- `front-end/src/pages/Main/Patients/styles.module.css`
- `tasks/change-requests/051-refinar-perfil-paciente-web.md`
- `tasks/slices/007-gestao-pacientes-profissional.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-051.md`

## Validacoes executadas

- `cd front-end && npm run lint` - ok
- `cd front-end && npm run build` - ok

## Pendencias pos-task

- nenhuma

## Status final

done

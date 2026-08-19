# Task 571 - Alinhar perfil do filho ao perfil de paciente

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

- `GET /guardians/me/children/{childId}`

## Modo de execucao

single-stack

## Slice vertical

- Slice 050 — `tasks/slices/050-area-web-responsavel-multiplos-filhos.md`

## Referencia de design system

- Stack: front-end; fonte: perfil de paciente em `front-end/src/pages/Main/Patients/PatientProfile/` e perfil de filho atual.
- Regra: reutilizar composição visual e cards do perfil profissional; não expor ações clínicas do profissional.

## Origem da solicitacao

Pedido humano: abrir o perfil da criança com design parecido ao perfil do profissional.

## Comportamento esperado

- Perfil do filho adota hierarquia visual, cabeçalho e cards semelhantes ao perfil do paciente.
- Mantém somente informações permitidas ao responsável.

## Fora de escopo

- Alterar dados, APIs, trilhas ou permissões.

## Criterios de aceite

- [ ] Perfil visualmente alinhado ao perfil profissional.
- [ ] Sem CTAs ou dados clínicos exclusivos do profissional.
- [ ] Lint focado passa.

## Contexto mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`, índice, esta task, Slice 050 e handoff Task 570.

## Contexto sob demanda

| Gatilho | Fonte | Decisão | Obrigatório? |
|---|---|---|---|
| Layout referência | `PatientProfile/**` | reutilizar composição segura | sim |
| Página afetada | `Guardian/ChildProfile/**` | aplicar somente dados do responsável | sim |
| UI | `front-end/docs/ai/ACCESSIBILITY.md` | headings e ações | sim |

## Orçamento de contexto

- médio; limitar aos dois perfis e seus estilos.

## Dependencias

- Task 570 (done)

## Resultado da execucao

Perfil do filho recebeu composição visual alinhada ao perfil de paciente: hero com avatar, código, identificação, cartões de leitura rápida e detalhes organizados; a anamnese ganhou cabeçalho contextual. Foram preservados dados e ações somente de leitura do responsável.

## Contexto utilizado

- Governança, Slice 050, handoff Task 570, ambos os perfis, estilos locais e acessibilidade.

## Handoff

`.agents/state/handoffs/TASK-571.md`

## Arquivos alterados

- `front-end/src/pages/Main/Guardian/ChildProfile/index.tsx`
- `front-end/src/pages/Main/Guardian/styles.module.css`
- task, Slice 050, índice e handoff.

## Validacoes executadas

- prettier e eslint focados: ok.
- `git diff --check`: ok (avisos CRLF preexistentes).

## Pendencias pos-task

- Nenhuma.

## Status final

done

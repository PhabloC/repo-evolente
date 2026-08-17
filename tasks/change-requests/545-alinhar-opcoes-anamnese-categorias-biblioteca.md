# Task 545 - Alinhar opções da anamnese (tópico 6) às categorias da biblioteca

## Status

done

## Tipo

shared

## Stacks envolvidos

- front-end
- backend

## Perfil do projeto

- stack web escolhida: front-end (React/Vite)
- mobile: sim

## Contrato

nao se aplica (valores internos do enum permanecem; só rótulos e opções visíveis)

## Modo de execucao

cross-stack

## Referencia de design system

### Stack de referencia visual

front-end

### Tipo de referencia visual

ajuste funcional orientado por feedback no chat

### Fonte primaria visual

- categorias da biblioteca em `front-end/src/constants/contentOptions.ts` (`CONTENT_CATEGORY_FORM_OPTIONS`)
- Task 403 (precedente de alinhamento de labels)

### Regra de aderencia visual

- a pergunta 6 da anamnese deve exibir as mesmas categorias da biblioteca
- preservar valores internos já aceitos pela API (`linguagem`, `articulatorio`, etc.)

## Contexto de negocio

### Por que

As opções da pergunta 6 da anamnese ainda usam a taxonomia antiga (Linguagem, Fala, Memória, etc.), divergente das categorias oficiais da biblioteca.

### O que

Trocar as opções selecionáveis e os rótulos de exibição da pergunta 6 para as categorias da biblioteca: Articulação, Cognição, Atenção, Vocabulário, Leitura e Escrita, Frases, Socioemocionais, Fluência e Diálogo.

### Comportamento esperado

- no cadastro do responsável, a pergunta 6 lista apenas as 9 categorias da biblioteca
- no perfil do paciente, áreas e sugestões de trilha usam os mesmos rótulos
- relatórios PDF usam os mesmos rótulos de categoria
- valores legados (`memoria`, `matematica`) continuam legíveis como Cognição quando já persistidos

### Fora de escopo

- remodelar o enum OpenAPI / persistência
- alterar mobile (sem UI de anamnese)

## Slice vertical

### Identificador do slice

Slice 004 - Onboarding responsavel, crianca e anamnese

### Arquivo do slice

- `tasks/slices/004-onboarding-responsavel-anamnese.md`

## Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- este arquivo
- `tasks/slices/004-onboarding-responsavel-anamnese.md`

## Contexto sob demanda

| Gatilho | Fonte | Decisão |
|---|---|---|
| Labels da biblioteca | `front-end/src/constants/contentOptions.ts` | espelhar opções |
| Opções atuais da anamnese | `front-end/src/constants/guardianOptions.ts` | substituir |
| Exibição no perfil | `front-end/src/pages/Main/Patients/PatientProfile/index.tsx` | rótulos |
| Labels em relatório | `backend/src/modules/reports/reports.service.ts` | rótulos |

## Orçamento de contexto

- baixo
- estratégia: só constantes de label + pontos de exibição; sem redesign

## Criterios de aceite

- [x] pergunta 6 mostra as 9 categorias da biblioteca com os mesmos rótulos
- [x] perfil do paciente e sugestões de trilha usam os mesmos rótulos
- [x] backend de relatório formata categorias com os mesmos rótulos
- [x] valores internos do enum não mudam

## Dependencias

- Task 403 (labels da biblioteca)

## Resultado da execucao

Opções da pergunta 6 da anamnese alinhadas a `CONTENT_CATEGORY_FORM_OPTIONS` da biblioteca. Exibição no perfil do paciente e labels de relatório atualizados.

## Contexto utilizado

- `front-end/src/constants/contentOptions.ts`
- `front-end/src/constants/guardianOptions.ts`
- `front-end/src/pages/Auth/RegisterGuardian/*`
- `front-end/src/pages/Main/Patients/PatientProfile/index.tsx`
- `backend/src/modules/reports/reports.service.ts`

## Handoff

`.agents/state/handoffs/TASK-545.md`

## Arquivos alterados

- `front-end/src/constants/guardianOptions.ts`
- `front-end/src/pages/Auth/RegisterGuardian/schemas.ts`
- `front-end/src/pages/Main/Patients/PatientProfile/index.tsx`
- `backend/src/modules/reports/reports.service.ts`
- `tasks/000-index.md`
- `tasks/change-requests/545-alinhar-opcoes-anamnese-categorias-biblioteca.md`

## Validacoes executadas

- lints nos arquivos front alterados: sem erros

## Pendencias pos-task

- nenhuma

## Status final

done

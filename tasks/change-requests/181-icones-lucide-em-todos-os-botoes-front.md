# Task 181 - Icones Lucide em todos os botoes do front-end

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

- nao se aplica

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

- Usar prop `icon` do `Button` com Lucide; manter variantes e labels existentes.

## Contexto de negocio

### Por que

Padronizar CTAs textuais com ícone para coerência visual em todo o site web.

### O que

Adicionar ícones Lucide em todos os `<Button>` sem `icon` (auth + área logada + modais).

### Comportamento esperado

- Cada botão textual do componente `Button` exibe ícone à esquerda
- Mapa fixo: Cancelar/Fechar=X, Salvar=Save, Confirmar=Check, Voltar=ArrowLeft, Continuar=ArrowRight, Entrar=LogIn, etc.
- Não alterar botões nativos de overlay/paginação/toggle

### Fora de escopo

- mobile
- mudanças de API do Button
- redesenho de layout além do ícone

## Slice vertical

### Identificador do slice

Slice 017 - Redesign da interface interna web

### Arquivo do slice

- `tasks/slices/017-redesign-interface-interna-web.md`

## Contexto mínimo

- `AGENTS.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/017-redesign-interface-interna-web.md`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| Button API | `front-end/src/ui/Button/` | prop icon | sim |
| páginas | arquivos listados no plano | implementação | sim |

## Orçamento de contexto

- Risco medio
- Estrategia: alterar apenas prop `icon` e imports Lucide por arquivo

## Criterios de conclusao

- Buttons textuais sem `icon` cobertos
- lint e build ok

## Dependencias

- nenhuma

## Resultado da execucao

- Ícones Lucide adicionados via prop `icon` em auth e área logada/modais
- Único `Button` restante sem prop `icon` é o fechar do Modal (já renderiza `<X>` como children, conforme plano)

## Contexto utilizado

- task 181, slice 017, `Button` UI, páginas Auth e Main listadas no plano

## Handoff

- `.agents/state/handoffs/TASK-181.md`

## Arquivos alterados

### Auth
- `front-end/src/pages/Auth/Login/index.tsx`
- `front-end/src/pages/Auth/PasswordRecovery/index.tsx`
- `front-end/src/pages/Auth/PasswordReset/index.tsx`
- `front-end/src/pages/Auth/RegisterProfessional/index.tsx`
- `front-end/src/pages/Auth/RegisterGuardian/index.tsx`
- `front-end/src/pages/Auth/SubscriptionGate/index.tsx`

### Main
- `front-end/src/pages/Main/ShellHome/index.tsx`
- `front-end/src/pages/Main/Forbidden/index.tsx`
- `front-end/src/pages/Main/Library/index.tsx`
- `front-end/src/pages/Main/Patients/index.tsx`
- `front-end/src/pages/Main/Patients/LinkPatientModal.tsx`
- `front-end/src/pages/Main/Patients/PatientProfile/index.tsx`
- `front-end/src/pages/Main/Plans/PatientTrail/index.tsx`
- `front-end/src/pages/Main/Plans/AddCatalogContentModal.tsx`
- `front-end/src/pages/Main/Reports/index.tsx`
- `front-end/src/pages/Main/AdminUsers/index.tsx`
- `front-end/src/pages/Main/AdminUsers/CreateMasterUserModal.tsx`
- `front-end/src/pages/Main/Admin/useAdminWorkspace.tsx`

### Governanca
- `tasks/change-requests/181-icones-lucide-em-todos-os-botoes-front.md`
- `tasks/slices/017-redesign-interface-interna-web.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-181.md`

## Validacoes executadas

- grep: só Modal close sem prop `icon` (children X justificado)
- `npm run lint` — ok
- `npm run build` — ok

## Pendencias pos-task

- nenhuma

## Status final

done

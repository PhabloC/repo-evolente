# Task 567 - Balão de download do app na sidebar do responsável

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

Não se aplica. A chamada leva à página web já existente de download do app.

## Modo de execucao

single-stack

## Slice vertical

### Identificador do slice

Slice 050 - Área web do responsável e cadastro de filhos

### Arquivo do slice

- `tasks/slices/050-area-web-responsavel-multiplos-filhos.md`

## Referencia de design system

- Stack de referência visual: front-end.
- Tipo: solicitação visual com imagem fornecida no chat.
- Fonte: balão de fala branco com borda preta arredondada e ponta inferior, reproduzido em CSS na sidebar existente.
- Lacuna: a imagem não existe como arquivo local; a geometria do balão governa a chamada, enquanto cores/tipografia seguem os tokens do projeto.

## Origem da solicitacao

Pedido humano: acima do nome do usuário na sidebar do responsável, colocar um balão similar à referência, convidando a baixar o aplicativo com ícones Apple Store e Google Play.

## Comportamento esperado

- O balão aparece somente para o responsável, acima do bloco de perfil da sidebar.
- Exibe convite breve, ícones Apple e Google Play com nomes acessíveis e abre a página de download existente.
- Não altera a sidebar de master ou profissional, nem é exibido no layout mobile onde a sidebar não está presente.

## Fora de escopo

- Criar links externos de lojas, QR code ou fluxo de instalação.
- Alterar navegação principal ou sidebar mobile.

## Criterios de aceite

- [ ] Responsável vê balão de download acima de seu perfil.
- [ ] Apple e Google Play são controles acessíveis e levam à página de download.
- [ ] Outros papéis não veem o balão.
- [ ] Lint focado passa.

## Contexto mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`, `tasks/000-index.md`
- esta task, Slice 050 e `.agents/state/handoffs/TASK-566.md`

## Contexto sob demanda

| Gatilho | Fonte | Decisão | Obrigatório? |
|---|---|---|---|
| Sidebar | `front-end/src/layout/Sidebar/**` e teste | inserir condição por papel e posição do balão | sim |
| Download | rotas e página `GuardianAppGate` | reutilizar destino existente | sim |
| Ícones | `lucide-react` já utilizado no front | representar lojas sem novo asset | sim |
| UI | `front-end/docs/ai/ACCESSIBILITY.md` | nomes, foco e contraste | sim |

## Orçamento de contexto

- baixo
- estratégia de redução: abrir apenas sidebar, rota/página de download, teste e acessibilidade; não carregar dashboard, serviços, backend ou mobile.

## Dependencias

- Task 559 - Área web do responsável: shell, dashboard, relatórios e configuração (done)

## Resultado da execucao

A sidebar recebe o papel autenticado pelo `MainLayout`. Para `responsavel`, um balão branco com borda escura, cantos arredondados e ponta inferior aparece acima do perfil, convidando a baixar o aplicativo. Os controles App Store e Google Play usam logos locais, possuem nomes acessíveis e levam à página existente `/baixar-app`. Master e profissional não veem o balão.

## Contexto utilizado

- Contexto mínimo: governança raiz, índice, esta task, Slice 050, handoff Task 566 e acessibilidade.
- Sob demanda: Sidebar, MainLayout, teste da Sidebar, rotas, GuardianAppGate e logos locais das lojas.

## Handoff

`.agents/state/handoffs/TASK-567.md`

## Arquivos alterados

- `front-end/src/layout/Sidebar/index.tsx`
- `front-end/src/layout/Sidebar/styles.module.css`
- `front-end/src/layout/Sidebar/index.test.tsx`
- `front-end/src/layout/MainLayout/index.tsx`
- esta task, Slice 050, índice e handoff da Task 567

## Validacoes executadas

- prettier nos arquivos alterados: ok.
- eslint focado: ok.
- `git diff --check`: ok (somente avisos CRLF preexistentes).
- Vitest focado não executou: workers do ambiente permanecem indisponíveis, condição registrada nas tasks anteriores.

## Pendencias pos-task

- Os links externos oficiais das lojas continuam fora de escopo; os dois controles levam à página web de download já existente.

## Status final

done

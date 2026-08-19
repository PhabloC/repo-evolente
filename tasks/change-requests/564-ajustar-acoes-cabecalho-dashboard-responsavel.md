# Task 564 - Ajustar CTA e notificações no cabeçalho do dashboard do responsável

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

Não se aplica: correção de interface e navegação local.

## Modo de execucao

single-stack

## Slice vertical

### Identificador do slice

Slice 052 - Dashboard analítico web do responsável

### Arquivo do slice

- `tasks/slices/052-dashboard-analitico-responsavel-web.md`

## Referencia de design system

- Stack de referência visual: front-end.
- Tipo: artefato de design system + captura fornecida pelo usuário na conversa.
- Fonte primária: `design-system/front/Design_System_Evolente_Desktop.md` e o header atual em `front-end/src/layout/MainLayout/`.
- Lacuna: a captura não está disponível como arquivo no repositório; ela governa a correção observável do CTA e dos ícones de busca/notificações, sem inferir alterações fora do header.

## Origem da solicitacao

Pedido humano com captura: corrigir os botões “Cadastrar filho” e o sino quebrado no dashboard do responsável.

## Comportamento esperado

- O botão “Cadastrar filho” permanece legível, alinhado e direciona para o cadastro autenticado de filho.
- O sino usa ícone e área clicável corretos, sem estado visual quebrado, e sua ação é acessível.
- As demais ações do header não regressam.

## Fora de escopo

- Criar central de notificações ou novos endpoints.
- Alterar o dashboard mobile ou os gráficos.

## Criterios de aceite

- [ ] CTA “Cadastrar filho” possui tamanho/alinhamento adequados e navega para o fluxo correto.
- [ ] Sino é renderizado corretamente, possui nome acessível e executa a ação disponível sem erro.
- [ ] Teste ou validação focada do header/dashboard e lint dos arquivos tocados passam.

## Contexto mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`, `tasks/000-index.md`
- esta task e `tasks/slices/052-dashboard-analitico-responsavel-web.md`
- `.agents/state/handoffs/TASK-563.md`

## Contexto sob demanda

| Gatilho | Fonte | Decisão | Obrigatório? |
|---|---|---|---|
| Ações do header | `front-end/src/layout/MainLayout/**`, `PageActionButton` e rotas | corrigir estilo e interação do CTA/sino | sim |
| Dashboard | `front-end/src/pages/Main/Guardian/Dashboard/index.tsx` | confirmar integração do CTA na página afetada | sim |
| UI web | `front-end/docs/ai/ACCESSIBILITY.md` | nomes acessíveis, foco e teclado | sim |

## Orçamento de contexto

- baixo
- estratégia de redução: limitar a investigação ao header, CTA, rotas e dashboard; não abrir serviços, OpenAPI, backend ou mobile.

## Dependencias

- Task 563 - Remover cards de filhos duplicados do dashboard web do responsável (done)

## Resultado da execucao

O CTA reutilizável `PageActionButton` passou a ter largura mínima e texto sem quebra, mantendo “Cadastrar filho” legível em uma única linha no header. O sino agora tem ação: ao clicar, revela uma mensagem acessível informando que as notificações são enviadas pelo aplicativo Evolente; antes ele não tinha nenhum manipulador de clique.

## Contexto utilizado

- Contexto mínimo: `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`, índice, esta task, Slice 052 e handoff da Task 563.
- Sob demanda: Header, `PageActionButton`, dashboard do responsável, rotas e diretriz de acessibilidade do front-end.

## Handoff

`.agents/state/handoffs/TASK-564.md`

## Arquivos alterados

- `front-end/src/layout/Header/index.tsx`
- `front-end/src/layout/Header/styles.module.css`
- `front-end/src/layout/Header/index.test.tsx`
- `front-end/src/components/PageActionButton/styles.module.css`
- esta task, Slice 052, índice e handoff da Task 564

## Validacoes executadas

- eslint focado nos componentes/teste TypeScript alterados: ok.
- `git diff --check`: ok (somente avisos de normalização CRLF em arquivos preexistentes).
- Vitest focado não foi repetido: o ambiente segue sem iniciar o worker, conforme a validação anterior da Task 563.

## Pendencias pos-task

- Nenhuma funcional. Uma central de notificações web permanece fora de escopo; o header agora informa corretamente que elas estão no app.

## Status final

done

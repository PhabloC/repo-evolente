# Task 810 - Limite de três filhos por responsável

## Status

done

## Tipo

shared

## Stacks envolvidos

- backend
- front-end
- mobile

## Perfil do projeto

- stack web escolhida: front-end (React/Vite)
- mobile: sim

## Contrato

- `contracts/openapi.yaml#/paths/~1guardians~1me~1children`
- `POST /guardians/me/children`
- `GET /guardians/me/children`

## Modo de execucao

cross-stack

## Slice vertical

- Slice 074 - Limite de três filhos por responsável
- `tasks/slices/074-limite-tres-filhos-responsavel.md`

## Objetivo

Impedir que o responsável cadastre mais de três filhos, na API, na web e no aplicativo.

## Escopo

- Rejeitar a criação do quarto filho em `createMyChild`.
- Na web, ocultar o atalho de cadastro e explicar o teto na lista e na rota de cadastro.
- No app, ocultar o atalho de novo filho e explicar o teto no seletor e na tela de cadastro.
- Documentar o teto no contrato.

## Fora de escopo

- Apagar filhos excedentes.
- Alterar preço da assinatura.
- Mudar o cadastro público do responsável, que continua sem filho.

## Referencia de design system

### Stack de referencia visual

multiplas stacks

### Tipo de referencia visual

artefato de design system

### Fonte primaria visual

- Web: `design-system/front/Design_System_Evolente_Desktop.md` apenas se o estado novo exigir componente que a lista de filhos ainda não usa.
- Mobile: `design-system/mobile/Design_System_Evolente_App_Mobile.md` apenas se o aviso exigir componente novo.

### Regra de aderencia visual

- Não há print deste estado. Reutilizar texto de status, botão e cards já usados no cadastro de filho.
- Web e mobile não copiam layout uma da outra; cada uma esconde o próprio atalho e mostra a mesma regra em texto.

## Origem da solicitacao

Pedido direto: colocar limite de até três filhos na web e no mobile.

## Comportamento esperado

- Com 0, 1 ou 2 filhos, o cadastro continua disponível.
- Com 3 ou mais, a API responde 400 e os clientes não abrem um novo cadastro.
- A mensagem é: "Cada responsável pode cadastrar no máximo 3 filhos."
- Contas que já passaram de três filhos antes desta regra mantêm os cadastros atuais.

## Critérios de aceite

- [x] O quarto `POST /guardians/me/children` da mesma conta falha.
- [x] Três filhos da mesma conta continuam sendo aceitos.
- [x] A página Filhos e a rota de cadastro na web não seguem o fluxo quando o teto foi atingido.
- [x] O seletor e a tela de cadastro no app não seguem o fluxo quando o teto foi atingido.
- [x] Testes do serviço, da página web e do estado do seletor cobrem o teto.

## Dependências

- Task 557 — done (criação autenticada de filhos)
- Task 560 — done (cadastro web)
- Task 621 — done (cadastro mobile)

## Contexto mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`, `tasks/000-index.md`
- esta task e o Slice 074

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| API | `contracts/openapi.yaml` path `/guardians/me/children` e `guardians.service.ts` | ao aplicar o teto no servidor | sim |
| UI web | páginas `Guardian/Children` e `Guardian/ChildRegister`, `ACCESSIBILITY.md` | ao esconder o atalho | sim |
| UI mobile | `SelectChildScreen`, `CreateChildScreen`, `resolveSelectChildViewState` | ao esconder o atalho | sim |
| Design system | arquivos declarados acima | somente se faltar um padrão de status já usado na tela | nao |

## Orçamento de contexto

- Fontes obrigatórias estimadas: 8
- Fontes sob demanda estimadas: 6
- Risco de contexto excessivo: baixo
- Estratégia para reduzir contexto: não abrir trilha, pagamento, dashboard analítico nem o wizard inteiro além do ponto de bloqueio.

## Instrucoes de implementacao

- O teto vale na criação pelo responsável. Não contar filhos de outra conta.
- Não remover filhos já gravados.
- A mesma frase de limite aparece na API e nos dois clientes.

## Validacao esperada

- Teste do `GuardiansService` com o quarto filho.
- Teste da página de filhos na web com três itens.
- Teste do estado do seletor mobile com três itens.

## Entregaveis esperados

- Contrato, API, web e mobile alinhados no teto de três.

## Riscos ou ambiguidades

- Conta antiga com mais de três filhos: permanece como está e não cadastra outro.

## Resultado da execucao

- Backend: `createMyChild` recusa o quarto filho com 400 e a frase do teto. Três filhos seguem válidos. Filhos já gravados não são apagados.
- Web: a lista esconde "Cadastrar filho" e a rota de cadastro troca o formulário pelo aviso quando já existem três filhos.
- Mobile: o seletor esconde "Cadastrar outro filho" e a tela de cadastro mostra o aviso. O modo demo também recusa o quarto filho.
- Contrato: a descrição de `POST /guardians/me/children` registra o máximo de 3.
- Acessibilidade: aviso em texto com `role="status"` na web e `accessibilityLiveRegion` no app. O botão some, então o teclado não encontra uma ação que não pode concluir.
- Visual: sem print deste estado. Reutilizado o texto de status e os botões já existentes. Web e mobile não copiaram layout entre si.

## Contexto utilizado

- Mínimo: AGENTS, GUIDE, context-map, índice, Task 810 e Slice 074.
- Sob demanda: path `/guardians/me/children` do contrato, `guardians.service.ts`, páginas Filhos e Cadastrar filho, `SelectChildScreen`, `CreateChildScreen`, `resolveSelectChildViewState`, `front-end/docs/ai/ACCESSIBILITY.md`.
- Não carregado: design system completo, trilha, pagamento, dashboard analítico e `requirements/`.

## Handoff

- `.agents/state/handoffs/TASK-810.md`

## Arquivos alterados

- `contracts/openapi.yaml`
- `backend/src/modules/guardians/guardian-children-limit.ts`
- `backend/src/modules/guardians/guardians.service.ts`
- `backend/src/modules/guardians/guardians.service.spec.ts`
- `front-end/src/constants/guardianChildrenLimit.ts`
- `front-end/src/pages/Main/Guardian/Children/index.tsx`
- `front-end/src/pages/Main/Guardian/Children/index.test.tsx`
- `front-end/src/pages/Main/Guardian/ChildRegister/index.tsx`
- `front-end/src/pages/Main/Guardian/ChildRegister/index.test.tsx`
- `mobile/src/features/children/constants/guardianChildrenLimit.ts`
- `mobile/src/features/children/screens/CreateChildScreen.tsx`
- `mobile/src/features/children/screens/SelectChildScreen.tsx`
- `mobile/src/features/children/services/childrenService.ts`
- `mobile/src/features/children/utils/resolveSelectChildViewState.ts`
- `mobile/src/features/children/utils/resolveSelectChildViewState.test.ts`
- `tasks/slices/049-cadastro-responsavel-sem-filho.md`
- `tasks/slices/050-area-web-responsavel-multiplos-filhos.md`
- `tasks/slices/074-limite-tres-filhos-responsavel.md`
- `tasks/000-index.md`

## Validacoes executadas

- `guardians.service.spec.ts`: 18 testes, incluindo a recusa do quarto filho.
- Vitest das páginas Filhos e Cadastrar filho: 7 testes, incluindo o teto.
- `resolveSelectChildViewState.test.ts`: 4 testes, incluindo três filhos sem novo cadastro.
- ESLint dos arquivos alterados nas três stacks, sem avisos.

## Pendencias pos-task

- O fluxo logado no navegador, com uma conta que já tenha três filhos, não foi percorrido nesta execução.
- Contas que já tinham mais de três filhos continuam com eles e só ficam impedidas de cadastrar outro.

## Status final

done

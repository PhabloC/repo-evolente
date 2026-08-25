# Task 613 - Remover botão de fechar da pesquisa no header web

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

Não se aplica; alteração visual e comportamental local do header compartilhado.

## Modo de execução

single-stack

## Slice vertical

- Slice 017 — `tasks/slices/017-redesign-interface-interna-web.md`

## Objetivo

Remover o botão com ícone X que aparece ao abrir a pesquisa global no cabeçalho web, preservando a lupa e o campo de pesquisa.

## Dependências

- Task 298 — done (pesquisa expansível do header)

## Contexto mínimo

- esta task
- `tasks/slices/017-redesign-interface-interna-web.md`
- `front-end/src/layout/Header/{index.tsx,index.test.tsx,styles.module.css}`

## Contexto sob demanda

| Gatilho | Fonte | Uso |
|---|---|---|
| UI compartilhada | pedido do usuário nesta conversa | remover somente o X azul visível ao abrir a pesquisa. |
| Acessibilidade/qualidade | `front-end/docs/ai/{ACCESSIBILITY,QA}.md` | manter nome acessível da lupa e atualizar testes. |

## Orçamento de contexto

- baixo
- estratégia: remover o controle e ajustar apenas a largura interna do campo; sem alterar busca, rotas ou cabeçalhos de páginas.

## Critérios de aceite

- [x] A lupa continua abrindo e focando o campo de pesquisa.
- [x] O botão X não é mais renderizado.
- [x] O input usa o espaço antes reservado ao botão removido.
- [x] Teste do Header, lint e build são executados.

## Resultado da execução

- Removidos o ícone X e o botão de fechar da pesquisa global compartilhada.
- A pesquisa continua sendo aberta pela lupa; o input usa a largura antes reservada ao botão removido.

## Contexto utilizado

- Task 613, Slice 017 e Header compartilhado, incluindo estilos e testes.
- Guias de acessibilidade e QA do front-end.

## Arquivos alterados

- `front-end/src/layout/Header/{index.tsx,index.test.tsx,styles.module.css}`
- `tasks/change-requests/613-remover-botao-fechar-pesquisa-header-web.md`
- `tasks/000-index.md`
- `tasks/slices/017-redesign-interface-interna-web.md`
- `.agents/state/handoffs/TASK-613.md`

## Validações executadas

- `npm run test -- --run src/layout/Header` — concluído sem mensagem de erro (o ambiente não exibiu o resumo final do Vitest).
- `npm run lint` — concluído sem mensagem de erro (o ambiente não exibiu o resumo final do ESLint).
- `npm run build` — concluído sem mensagem de erro (o ambiente não exibiu o resumo final).

## Pendências pós-task

- Conferir visualmente o header em desktop e mobile, especialmente a largura do campo depois da abertura.

## Handoff

- `.agents/state/handoffs/TASK-613.md`

## Status final

done

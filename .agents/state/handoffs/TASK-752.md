# TASK-752

## Slice

Slice 063 — diretório de profissionais para o responsável (web)

## Status

done

## Decisões preservadas

- Botão **Encontrar profissionais** no cabeçalho de Filhos, ao lado de Cadastrar filho.
- Rota `/profissionais` só para `responsavel`.
- Consome `GET /professionals` com busca debounced.
- Sem CTA de vínculo no diretório; hint aponta código da criança.

## Contexto usado

- Handoff TASK-751
- `front-end/src/pages/Main/Guardian/**`
- `front-end/docs/ai/ACCESSIBILITY.md`

## Arquivos alterados

- rotas, service, hook, página Professionals, botão em Children, estilos

## Validações

- Vitest Children + Professionals — ok
- ReadLints — ok

## Pendências

- Nenhuma no slice 063

## Próximo contexto recomendado

- Não necessário; slice concluído.
- Se evoluir vínculo a partir do diretório, criar nova task (não reabrir 063 sem CR).

# Handoff - Task 092

## Task

- identificador: 092
- título: Ajustar execucao web do Expo mobile
- tipo: mobile
- modo de execução: single-stack
- status final: done

## Slice vertical

- identificador: Slice 001 - Fundacao e contrato base
- objetivo de negócio: manter o shell mobile executavel tambem no alvo web local
- entrega verificável: `npm run web` sobe em porta dedicada e responde HTTP 200
- status do slice: done

## Decisões preservadas

- decisão: usar a porta `19006` no script `npm run web`
- motivo: evitar colisao com a porta padrao `8081` usada por Metro/outros fluxos Expo
- impacto: execucao web previsivel sem prompt interativo por troca de porta

- decisão: documentar a URL local e o cuidado com `EXPO_PUBLIC_API_URL`
- motivo: no navegador a API precisa ser acessivel pelo browser, nao apenas por device/emulador
- impacto: README operacional reduz ambiguidade para testes web

## Contexto utilizado

### Contexto mínimo lido

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`
- `tasks/000-index.md`, `tasks/change-requests/092-ajustar-execucao-web-expo-mobile.md`
- `tasks/slices/001-fundacao-contrato-base.md`
- `.agents/state/handoffs/TASK-004.md`

### Contexto sob demanda carregado

| Fonte | Gatilho | Uso |
|---|---|---|
| `mobile/AGENTS.md` + `mobile/docs/ai/AGENTS.md` | stack mobile | validar regra local |
| `mobile/package.json` | falha do comando web | ajustar script |
| `mobile/README.md` | operacao local | alinhar documentacao |

### Contexto evitado

| Fonte | Motivo |
|---|---|
| design system mobile | sem ajuste de UI |
| contrato OpenAPI | sem alteracao de integracao |

## Resultado por stack

- mobile: done

## Arquivos alterados

- `mobile/package.json`
- `mobile/README.md`
- `tasks/change-requests/092-ajustar-execucao-web-expo-mobile.md`
- `tasks/slices/001-fundacao-contrato-base.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-092.md`

## Validações executadas

- `npm run lint`: ok
- `npm run typecheck`: ok
- `npm run web`: ok em `http://localhost:19006`

## Pendências ou bloqueios

- conferir `EXPO_PUBLIC_API_URL` por ambiente quando o alvo web precisar usar backend local no navegador

## Próxima ação sugerida

- se houver falha funcional restante na web, inspecionar agora o fluxo de autenticação/API já com o bootstrap operacional estabilizado

## Próximo contexto recomendado

- `mobile/src/shared/network/apiClient.ts`
- `.env` do mobile
- backend local apenas se o problema restante for de integração navegador/API

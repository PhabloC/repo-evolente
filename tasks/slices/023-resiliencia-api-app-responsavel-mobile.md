# Slice 023 - Resiliencia da API no app do responsavel

## Status

done

## Objetivo de negocio

Garantir que o app do responsavel use dados reais por padrao nas telas principais e exponha falhas reais de conectividade quando o modo demo estiver desligado.

## Entrega verificavel

Atividades, perfil e avisos usam API real por padrao quando o modo demo estiver desligado, sem fallback automatico para mock em falha de rede.

## Fora de escopo

- Sincronizacao offline bidirecional
- Cache persistente
- Alteracoes em auth, tab bar ou shell

## Perfil do projeto

- stack web escolhida: front-end (React/Vite)
- mobile: sim

## Stacks envolvidas

- mobile

## Contrato

- `contracts/openapi.yaml#/paths/~1guardians~1me`
- `contracts/openapi.yaml#/paths/~1guardians~1me~1children`
- `contracts/openapi.yaml#/paths/~1notifications`
- `contracts/openapi.yaml#/paths/~1patients~1{patientId}~1trails`
- `contracts/openapi.yaml#/paths/~1patients~1{patientId}~1progress`

## Referencia visual por stack

### Web

- tipo: `nao se aplica`
- fonte primaria: `nao se aplica`

### Mobile

- tipo: continuidade de interface existente
- fonte primaria: `design-system/mobile/prints/home-responsavel-referencia.png`

## Permissoes e atores

- Responsavel autenticado

## Casos de erro e borda

- API indisponivel no ambiente local/mobile
- Timeout de requests do responsavel
- Responsavel sem criancas vinculadas

## Decisoes humanas confirmadas

- Dados reais prevalecem nas telas do responsavel quando demo estiver desligado
- Nao mascarar falhas de leitura ou mutacao com mock automatico

## Premissas adotadas

- Dados demo so podem aparecer por opt-in explicito de ambiente
- Erros de rede, timeout ou configuracao devem permanecer visiveis para facilitar diagnostico

## Tasks relacionadas

- `tasks/024-app-responsavel-home-perfil-notificacoes.md` - Home/perfil/notificacoes — **done**
- `tasks/change-requests/120-corrigir-login-mobile-api-local.md` - Login mobile com API local — **done**
- `tasks/change-requests/124-linguagem-visual-print-demais-telas-mobile.md` - Linguagem visual nas telas mobile — **done**
- `tasks/change-requests/125-resiliencia-api-telas-responsavel-mobile.md` - Hardening de atividades, perfil e avisos — **done**
- `tasks/change-requests/126-exigir-dados-reais-telas-responsavel-mobile.md` - Exigir dados reais nas telas do responsavel — **done**

## Dependencias do slice

- Slices 002, 008, 010 e 022

## Contexto minimo recomendado

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- este slice

## Contexto sob demanda recomendado

| Gatilho | Fonte | Quando carregar | Obrigatorio? |
|---|---|---|---|
| API mobile | `contracts/openapi.yaml` | validar rotas de leitura do responsavel | sim |
| Mobile | `mobile/docs/ai/ARCHITECTURE.md`, `CODE_STYLE.md`, `QA.md` | implementacao e teste | sim |
| Handoff recente | `.agents/state/handoffs/TASK-120.md`, `.agents/state/handoffs/TASK-124.md` | reaproveitar decisoes de API local e telas | sim |

## Risco de contexto

- baixo
- estrategia: restringir a `services/`, rede compartilhada e telas do responsavel; sem tocar backend

## Observacoes de rastreabilidade

- Fallback automatico por `network`/`timeout` foi removido das leituras do responsavel na Task 126.
- Dados demo permanecem apenas por opt-in de `EXPO_PUBLIC_USE_DEMO_DATA=true`.

## Status final

done

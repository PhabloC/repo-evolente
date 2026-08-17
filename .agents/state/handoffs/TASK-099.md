# Handoff - Task 099

## Task

- identificador: 099
- título: Corrigir camada da menina atras da nuvem no login mobile
- tipo: mobile
- status final: done

## Slice vertical

- Slice 002 - Autenticacao — done

## Decisões preservadas

- menina em camada absoluta (`zIndex: 1`), fora do hero
- painel nuvem+form (`zIndex: 2`) cobre o corpo
- hero/texto (`zIndex: 3`) nao eleva a menina
- SVG novo: `mobile/assets/nuvem_login_onda.svg`

## Arquivos alterados

- nuvem_login_onda.svg, SignInCloud*, SignInScreen, styles, task/index/slice/handoff 099

## Validacoes

- lint/typecheck ok

## Proxima acao

- Validar visualmente no Expo web

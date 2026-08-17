# Handoff - Task 386

## Task

- identificador: 386
- título: Corrigir contagem e espaçamento do hero da trilha mobile
- tipo: mobile
- modo de execução: single-stack
- status final: done

## Slice vertical

- identificador: Slice 008 - Trilhas semanais e evolução

## Decisões preservadas

- o hero da trilha agora usa a contagem total da rotina semanal da criança, não apenas as atividades do dia atual
- o layout do hero passou a usar `justifyContent: 'flex-start'`
- o CTA `Abrir próxima` usa `marginTop: 'auto'` para manter o alinhamento inferior sem criar vazio no bloco textual

## Contexto utilizado

- `mobile/src/features/trail/screens/TrailTodayScreen.tsx`
- `mobile/src/features/trail/screens/styles.ts`

## Arquivos alterados

- tela, estilos, task, slice, índice e handoff

## Validações executadas

- `cd mobile && npm run typecheck` — iniciou sem novos diagnósticos, mas o shell ficou preso após o `tsc --noEmit` e os processos foram encerrados manualmente

## Pendências ou bloqueios

- se necessário, repetir a validação em terminal local fora do backend de execução

## Próximo contexto recomendado

- `mobile/src/features/trail/screens/TrailTodayScreen.tsx`

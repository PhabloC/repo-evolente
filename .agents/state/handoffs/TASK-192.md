# Handoff - Task 192

## Task

- identificador: 192
- título: Colunas de vínculo profissional-paciente na página de usuários
- status final: done

## Decisões preservadas

- contagens a partir de `/admin/professionals-tree`
- profissionais: coluna `Pacientes` (`N paciente(s)`)
- pacientes: coluna `Profissional` (`Vinculado` + nome ou `Sem vínculo`)

## Arquivos alterados

- `front-end/src/pages/Main/AdminUsers/index.tsx`
- `front-end/src/pages/Main/AdminUsers/styles.module.css`
- `front-end/src/pages/Main/AdminUsers/index.test.tsx`

## Validações executadas

- lint ok
- AdminUsers tests ok

## Pendências

- listagem de pacientes sem vínculo depende de endpoint admin dedicado (fora desta entrega)

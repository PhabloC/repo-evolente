# Handoff - Task 443

- task: `443`
- título: Exibir foto do paciente na tabela de relatórios web
- slice: `tasks/slices/011-relatorios-evolucao.md`
- status final: done

## Decisões preservadas

- coluna Paciente com `PatientAvatar` + nome + código
- pacientes carregados sem filtro de status para resolver foto no histórico
- select de geração usa apenas pacientes ativos

## Arquivos alterados

- `front-end/src/pages/Main/Reports/index.tsx`
- `front-end/src/pages/Main/Reports/styles.module.css`

## Pendências

- nenhuma

# Handoff - Task 496

## Task

- TASK-496 - Estabilizar elevação do login e baixar um pouco o form
- status final: done

## Decisões

- Debounce 200ms no `keyboardDidHide` para não colapsar ao trocar e-mail↔senha
- `onFieldFocus` cancela hide pendente e mantém lift aberto
- `paddingTop: 56` no form elevado para não colar no topo

## Próxima ação

- Validar: e-mail e senha com mesma altura; restore só ao fechar teclado

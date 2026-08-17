# Handoff - Task 494

## Task

- TASK-494 - Corrigir overshoot do login com Samsung Pass / pan
- status final: done

## Decisões

- Com `softwareKeyboardLayoutMode: pan`, não ancorar o form no topo absoluto
- Só recolher hero + menina; form fica com `marginTop: auto`
- O pan (e o Samsung Pass) ajustam a janela sem segundo deslocamento nosso

## Arquivos

- `SignInScreen.tsx`, `styles.ts`

## Próxima ação

- Testar foco em e-mail/senha com Samsung Pass aberto e com teclado normal

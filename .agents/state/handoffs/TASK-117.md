# Handoff - Task 117

## Task

- 117 - Elevar recuperacao de senha mobile ao abrir teclado
- status final: done

## Decisões

- A recuperacao de senha passou a usar a mesma lógica de recolhimento do topo e subida do bloco inferior já usada no login
- O foco do campo de e-mail dispara a animacao imediatamente
- O ajuste foi restrito ao fluxo recovery mobile

## Validacoes

- `npm run lint` ok
- `npm run typecheck` ok
- `npm run test` ok

# Handoff - Task 120

## Task

- 120 - Corrigir acesso da API no login mobile em ambiente local
- status final: done

## Decisões

- `EXPO_PUBLIC_API_URL` pode continuar em `http://localhost:3000/api` no desenvolvimento
- No app nativo, `localhost` passa a ser resolvido para o host do Metro quando disponível
- No Android Emulator, fallback explícito para `http://10.0.2.2:3000/api`
- A mensagem de erro de rede agora indica indisponibilidade de servidor/acesso da URL

## Validações

- `npm run lint` ok
- `npm run typecheck` ok
- `npm run test -- --runInBand` ok

# Handoff Tasks 706 e 707

- Slice: 060 OneSignal / 008 trilhas semanais
- Status final: done
- Decisões: push é best-effort após persistência in-app; timeout OneSignal configurável com padrão de 10s; seleção de trilha exige igualdade com o início da semana.
- Arquivos: adapter OneSignal, NotificationsService, DailyTrailReminderService, ajustes.md e tasks 706/707.
- Validações: Prettier e lint passaram; typecheck tem falhas preexistentes em specs; testes executados sem diagnóstico adicional.
- Pendências: outbox/retry persistente é melhoria futura, se necessária.

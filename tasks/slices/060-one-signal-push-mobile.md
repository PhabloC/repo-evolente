# Slice 060 - Push OneSignal no mobile

## Objetivo de negócio

Permitir que usuários autenticados do app responsável recebam notificações push por meio do OneSignal, preservando a central in-app existente.

## Entrega verificável

- SDK OneSignal configurado no Expo/EAS.
- Inicialização controlada por App ID de ambiente.
- Usuário autenticado associado ao `externalId`.
- Eventos de recebimento e clique preparados para integração com as telas existentes.
- Backend preparado para substituir o adapter noop por envio OneSignal.

## Fora de escopo

- Campanhas e segmentações definitivas.
- Migração de notificações in-app.
- Credenciais APNs/FCM ou chaves secretas versionadas.

## Tasks relacionadas

- `tasks/change-requests/703-integrar-onesignal-push-mobile.md`

## Status

done

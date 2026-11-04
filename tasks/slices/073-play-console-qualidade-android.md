# Slice 073 - Qualidade Android na Play Console

## Objetivo de negócio

Eliminar ou reduzir avisos de qualidade da Google Play que afetam ofuscação DEX e APIs edge-to-edge no app Evolente.

## Entrega verificável

Build de produção Android com R8 (minify/shrink/optimize) habilitado e configuração edge-to-edge alinhada ao Expo SDK 57; próximo AAB deve reportar ofuscação ≥ 25% quando analisado na Play Console.

## Fora de escopo

- Publicar o AAB nas lojas nesta execução
- Alterar fluxos de produto ou UI além do necessário para system bars/modais
- Corrigir avisos originados exclusivamente em código interno do React Native/Expo sem patch upstream disponível

## Tasks relacionadas

- Task 807 — corrigir avisos Play Console (DEX + edge-to-edge)

## Contexto mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`, `tasks/000-index.md`
- esta slice

## Contexto sob demanda

- `mobile/app.json`, `mobile/eas.json`
- `expo-build-properties`
- docs Expo/Play sobre R8 e edge-to-edge

## Risco de contexto

Baixo: escopo nativo Android de build, sem API nem redesign.

## Status

done

# Handoff — Task 437

## Identificador

- Task: 437 — Diálogos em Ação: catálogo, prévia e runtime
- Slice: `tasks/slices/046-dialogos-em-acao.md`
- Status final: done

## Decisões preservadas

- `gameType: dialogue`, categoria `socializacao` (Diálogo)
- Só partida jogável; sem menu/níveis/conquistas/mic/dica
- 10 stages com situação + opções de fala + feedback
- Capas: usuário coloca em `dialogos_em_acao/` (`capa-jogo-dialogos-acao.webp`, `capa-modal-jogo-dialogos-acao.webp`) e sobe com `upload-dialogue-assets.mjs`

## Contexto usado

- print `design-system/front/prints/dialogos-em-acao.png`
- padrão emotions
- openapi + bootstrap

## Arquivos principais

- `backend/.../dialogue-game-assets.ts`
- `front-end/.../DialoguePreviewModal.tsx`
- `mobile/.../DialogueGameRenderer/`
- `dialogos_em_acao/stages/*.webp`

## Validações

- bootstrap spec PASS (16 jogos)
- upload 10 stages S3 + catalog `stages_with_image: 10`

## Pendências

- Capas: aguardar arquivos na pasta local e rodar upload

## Próximo contexto

- Capas: `dialogos_em_acao/` + script upload
- Não recarregar outros slices

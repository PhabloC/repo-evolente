# Handoff - Task 784

## Task

- identificador: 784
- título: Upload áudios Animais/difícil do Descubra a palavra
- status final: done

## Slice vertical

- Slice 043 — `tasks/slices/043-complete-a-palavra.md`

## Decisões preservadas

- IDs das palavras permanecem `gato_preto`, `pato_branco`, `peixe_azul` (Task 731)
- Novos MP3 sobrescrevem as mesmas chaves S3 / `audioUrl`
- Match por label do arquivo → label da palavra

## Mapeamento arquivo → texto

| Arquivo local | Texto na atividade | Chave S3 |
|---|---|---|
| `mulher-2026-10-12-10-40-[excited]Gato-laranja.mp3` | GATO LARANJA | `dev/games/complete_a_palavra/audio/words/animais/dificil/gato_preto.mp3` |
| `mulher-2026-10-12-10-39-[excited]Pato-amarelo.mp3` | PATO AMARELO | `dev/games/complete_a_palavra/audio/words/animais/dificil/pato_branco.mp3` |
| `mulher-2026-10-12-10-40-[excited]Peixe-laranja.mp3` | PEIXE LARANJA | `dev/games/complete_a_palavra/audio/words/animais/dificil/peixe_azul.mp3` |

## Arquivos alterados

- `backend/scripts/_word-spell-catalog.json`
- task / index / handoff

## Validações

- upload script: 120 matched, 0 unmatched

## Pendências

- nenhuma

## Próximo contexto recomendado

- smoke no botão Ouvir de Animais/difícil (web ou mobile)

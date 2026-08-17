# Handoff — Task 539

## Identificador

TASK-539

## Título

Prévia web Diálogos: falar prompt ao iniciar situação

## Slice vertical

`tasks/slices/046-dialogos-em-acao.md`

## Status final

done

## Decisões preservadas

- Mesma regra do mobile: `/fazer/i` no prompt → `promptAudioUrls.fazer`, senão `falar`
- Delay ~400ms ao entrar na situação
- URLs já no catálogo (Task 537)

## Arquivos alterados

- `DialoguePreviewModal.tsx`, `dialogueGame.ts`, `content.ts` (tipos)

## Validações

- Lint OK; DB com prompts presentes

## Próxima ação sugerida

- Abrir Diálogos em Ação na biblioteca, clicar Jogar e confirmar o áudio do prompt

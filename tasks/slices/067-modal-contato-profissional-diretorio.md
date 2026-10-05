# Slice 067 - Modal de contato do profissional no diretório

## Status

done

## Objetivo de negócio

Permitir que o responsável clique em um profissional no diretório, veja os detalhes e abra o WhatsApp em nova aba para contato.

## Entrega verificável

- Clique no card abre modal com dados públicos do profissional.
- Modal mostra botão/link WhatsApp que abre `wa.me` em nova aba.
- Telefone de contato disponível no item do diretório (sem e-mail).

## Fora de escopo

- Chat interno
- App mobile
- Vinculação a partir do modal

## Decisões confirmadas

- Contato WhatsApp usa o telefone do usuário profissional; em clínica, prioriza `clinicPhone` se existir, senão o telefone pessoal.
- Link: `https://wa.me/55...` em `target="_blank"` com `rel="noopener noreferrer"`.

## Perfil do projeto

- stack web: front-end (React/Vite)
- mobile: sim (fora deste slice)

## Stacks envolvidas

- contracts
- backend
- front-end

## Contrato

- `ProfessionalDirectoryItem.phone` / `contactPhone`

## Tasks relacionadas

- `tasks/change-requests/760-api-telefone-contato-diretorio-profissionais.md`
- `tasks/change-requests/761-modal-contato-whatsapp-diretorio-web.md`
- `tasks/change-requests/770-refinar-layout-modal-contato-diretorio.md`

## Progresso

- Task 760 — done
- Task 761 — done
- Task 770 — done (layout do modal)

## Risco de contexto

baixo

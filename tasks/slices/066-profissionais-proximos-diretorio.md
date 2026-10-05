# Slice 066 - Profissionais próximos no diretório do responsável

## Status

done

## Objetivo de negócio

Na página de profissionais do responsável, separar quem está perto (mesmo CEP/cidade do responsável) de quem está mais longe.

## Entrega verificável

- `GET /professionals` devolve listas `nearby` e `others` com base no endereço do responsável autenticado.
- Profissional próximo: mesma cidade (normalizada) **ou** mesmo CEP / prefixo de 5 dígitos.
- UI web com duas seções: **Próximos** e **Outros profissionais**.
- Se o responsável não tiver endereço, todos aparecem em “Outros” com aviso.

## Fora de escopo

- Geocoding / distância em km / mapa
- App mobile
- Filtro manual por cidade na UI
- Expor rua completa do profissional no diretório

## Decisões confirmadas

- Comparação server-side usando endereço do responsável autenticado.
- Item do diretório pode expor `city` (pública) para contexto visual.
- Busca por nome/especialidade continua aplicando às duas listas.

## Perfil do projeto

- stack web: front-end (React/Vite)
- mobile: sim (fora deste slice)

## Stacks envolvidas

- contracts
- backend
- front-end

## Contrato

- `GET /professionals` (`ProfessionalDirectoryListResponse`)

## Tasks relacionadas

- `tasks/change-requests/758-api-profissionais-proximos-diretorio.md`
- `tasks/change-requests/759-ui-profissionais-proximos-diretorio-web.md`

## Progresso

- Task 758 — done
- Task 759 — done

## Risco de contexto

médio — contrato + serviço de diretório + página web

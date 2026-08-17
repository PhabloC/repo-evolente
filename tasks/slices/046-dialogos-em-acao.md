# Slice 046 - Diálogos em Ação

## Status

done

## Objetivo de negocio

Incluir o jogo Diálogos em Ação no catálogo master, na categoria Diálogo (`socializacao`), para a criança praticar escolhas de fala em situações sociais.

## Entrega verificavel

- Conteúdo `dialogue` no catálogo (`category: socializacao` / Diálogo)
- Pool de 10 etapas com situação, ilustração e opções de fala
- Prévia web e runtime mobile
- Sem menu, níveis, conquistas, microfone ou dica

## Fora de escopo

- Menu JOGAR / HISTÓRIA / CONQUISTAS / PERSONAGENS / LOJA
- Níveis e progresso com estrelas
- Microfone / conversa livre / STT
- Botão DICA
- Capas no S3 até o usuário colocar arte em `dialogos_em_acao/`

## Contexto mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`
- `tasks/000-index.md`
- este slice
- task relacionada

## Contexto sob demanda

- print `design-system/front/prints/dialogos-em-acao.png`
- padrão `emotions` (escolha + feedback + shuffle)
- `contracts/openapi.yaml` (ContentGameType + DialogueGameConfig)

## Orçamento de contexto

- risco: medio — novo gameType + UI de diálogo + 10 artes

## Tasks relacionadas

- Task 437 — done

## Decisões humanas confirmadas

1. Só partida jogável
2. Sem microfone
3. 10 etapas
4. Categoria Diálogo (`socializacao`)
5. Sem botão DICA
6. Imagens personalizadas das etapas
7. Pasta local só para capas (usuário coloca; agente sobe S3)

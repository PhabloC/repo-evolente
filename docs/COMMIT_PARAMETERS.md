# Parâmetros de Commit para IA

Este documento define como a IA deve realizar commits neste repositório quando o usuário solicitar explicitamente.

## Regras obrigatórias

1. Nunca realizar commit sem pedido explícito do usuário.
2. Todas as mensagens de commit devem estar em português.
3. Os commits devem ser feitos um por um, sempre por arquivo.
4. Se houver 12 arquivos alterados para subir, devem ser feitos 12 commits separados.
5. Cada commit deve conter apenas 1 arquivo (`1 commit = 1 arquivo`).
6. Não agrupar múltiplos arquivos no mesmo commit.
7. Antes de cada commit, revisar a ortografia e a acentuação da mensagem.
8. A mensagem deve descrever de forma objetiva a alteração do arquivo commitado.

## Fluxo obrigatório

1. Listar os arquivos alterados.
2. Para cada arquivo, nesta ordem:
   - Adicionar apenas o arquivo atual ao stage.
   - Criar mensagem em português referente somente a esse arquivo.
   - Executar o commit desse único arquivo.
3. Repetir até finalizar todos os arquivos.

## Padrão de mensagem

Formato recomendado:

`<tipo>: <descrição curta em português>`

Exemplos de tipo:

- `feat`
- `fix`
- `refactor`
- `style`
- `test`
- `docs`
- `chore`

Exemplos válidos:

- `feat: adiciona validação de período no formulário de turma`
- `fix: corrige renderização da aba de período do curso`
- `docs: atualiza instruções de commit para agentes`

## Reforço operacional

- Quando o usuário pedir para "subir" alterações, interpretar como necessidade de commitar seguindo este padrão.
- Se a alteração depender de backend, avisar explicitamente antes de finalizar o trabalho de frontend.
- Não reescrever histórico (`rebase`, `amend`, `reset --hard`) sem pedido explícito.

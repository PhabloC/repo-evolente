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

## Título e descrição do pull request

Ao terminar os commits, entregar no mesmo retorno um título e uma descrição prontos para colar no pull request. Fazer um par por repositório que recebeu commits (`front-end`, `mobile`, `backend` ou raiz).

Regras:

1. Escrever em português, com ortografia e acentuação revisadas.
2. O título é uma linha curta que resume a alteração do pull request.
3. A descrição é um único parágrafo em texto corrido, sem lista, sem tópicos e sem copiar as mensagens de commit.
4. O parágrafo deve dizer o que mudou e qual efeito isso tem para quem usa a tela, o jogo ou a API.
5. Se o mesmo repositório tiver mais de um assunto, o título e o parágrafo cobrem todos.
6. Descrever só o que foi commitado. Não inventar escopo, testes ou telas que não entraram nos commits.
7. Atualização de ponteiro de submódulo não entra no título nem na descrição, salvo quando for a única alteração daquele repositório.

Exemplo de formato:

**Front**

**Título:** Adiciona a política de privacidade e usa só áudio gravado nas prévias

**Descrição:** A web passa a ter uma página pública de política de privacidade, com acesso aberto e link no login, nos cadastros e nas configurações. Nas prévias da biblioteca, a reprodução fica restrita aos áudios gravados da atividade e, se o arquivo não existir ou falhar, a prévia permanece em silêncio.

## Reforço operacional

- Quando o usuário pedir para "subir" alterações, interpretar como necessidade de commitar seguindo este padrão.
- Se a alteração depender de backend, avisar explicitamente antes de finalizar o trabalho de frontend.
- Não reescrever histórico (`rebase`, `amend`, `reset --hard`) sem pedido explícito.

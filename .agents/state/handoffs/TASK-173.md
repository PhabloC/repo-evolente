# Handoff - Task 173

## Task

- identificador: 173
- título: Alfabeto completo no jogo de escrita de letras
- status final: done

## Decisões preservadas

- decisão: templates A–Z no web e mobile; bootstrap default A–Z
- motivo: pedido explícito para sair das vogais
- impacto: o jogo padrão passa a sortear qualquer letra do alfabeto

- decisão: bootstrap atualiza “Escreva a letra” existente se `letters.length < 26`
- motivo: banco local já tinha só vogais
- impacto: reinício do backend aplica a expansão sem recriar o conteúdo

## Validações

- bootstrap, web e mobile writing tests — ok

## Pendências

- garantir reload do backend para sincronizar o catálogo local
- calibração fina de consoantes após uso real

## Próxima ação sugerida

- abrir o preview e confirmar que aparecem letras além de A/E/I/O/U

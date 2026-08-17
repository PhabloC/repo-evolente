# Slice 018 - Fidelidade visual dashboard e pacientes web

## Status

done

## Objetivo de negocio

Aproximar a area autenticada da composicao visual aprovada pelo usuario, com maior densidade informacional, acolhimento e aparencia profissional.

## Entrega verificavel

- Shell claro, busca superior, perfil compacto, cards de indicadores e paineis seguem os prints fornecidos.
- Dashboard e pacientes usam dados existentes ou estados honestos, sem inventar metricas de API.
- Demais paginas herdam a fundacao visual compartilhada refinada.

## Fora de escopo

- Novos endpoints, notificacoes reais, agenda real, fotos de usuarios ou dados ficticios apresentados como reais.
- Mobile e auth.

## Tasks relacionadas

- Task 040 - refinamento visual por prints internos
- `tasks/change-requests/066-refinar-tabela-pacientes-referencia-visual.md` - novo refino local da tabela de pacientes por referência de chat
- `tasks/change-requests/067-adicionar-barra-progresso-tabela-pacientes.md` - completar a coluna visual de progresso na tabela de pacientes
- `tasks/change-requests/294-integrar-progresso-real-na-tabela-de-pacientes-web.md` - trocar o placeholder da coluna por percentual real baseado nas trilhas ativas
- `tasks/change-requests/296-icones-no-dropdown-de-acoes-da-tabela-de-pacientes.md` - adicionar ícones às ações do menu da tabela de pacientes
- `tasks/change-requests/068-acoes-dropdown-tabela-pacientes.md` - simplificação das ações da tabela de pacientes com menu local
- `tasks/change-requests/069-desacoplar-dropdown-tabela-pacientes.md` - correção do dropdown para abrir fora do overflow da tabela

## Contexto mínimo

- fontes globais, Task 040, handoff 039 e este slice

## Contexto sob demanda

- dois prints concretos em `design-system/front/prints/`
- shell, dashboard, pacientes e componentes compartilhados diretamente afetados

## Risco de contexto

- Medio; limitado a uma task front e às telas governadas pelos dois prints.

## Resultado

- Shell, dashboard e pacientes refinados conforme os prints, sem introduzir dados clinicos ficticios.
- Task 066 aproximou especificamente a tabela de pacientes de uma nova referência de chat, usando somente dados reais atuais e avatar textual sem foto.
- Task 067 completou a composição visual com a barra de progresso em estado neutro enquanto o dado real ainda nao existe no payload.
- Task 294 substituiu o placeholder da coluna por percentual real calculado a partir das trilhas e conclusoes ja disponiveis no front.
- Task 296 adicionou ícones às ações `Perfil` e `Inativar/Reativar` no dropdown da tabela de pacientes.
- Task 068 simplificou a tabela removendo o vínculo e agrupando as ações em dropdown nos três pontinhos.
- Task 069 moveu o dropdown para portal, evitando que o menu fosse cortado ou deformasse a tabela.
